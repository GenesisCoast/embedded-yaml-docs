from operator import xor

from jinja2 import Environment, Template, filters
from markupsafe import soft_str

from .jinja2_custom_filters import Jinja2CustomFilters
from .jinja2_custom_functions import Jinja2CustomFunctions
from .jinja2_custom_tests import Jinja2CustomTests
from ..wrappers.ruamel_yaml_wrapper import RuamelYAMLWrapper


class Jinja2Environment(Environment):
    """
    Custom implementation for the Jinja2 environment.
    """


    def __init__(self, **kwargs):
        """
        Initialize the environment, and loads any custom Filters, Functions and Tests.

        Parameters:
            **kwargs: Additional configuration for the environment.
        """
        super().__init__(**kwargs)
        yaml = RuamelYAMLWrapper()
        self.__load_custom_filters(yaml)
        self.__load_custom_functions(yaml)
        self.__load_custom_tests()


    def __load_custom_filters(self, yaml: RuamelYAMLWrapper):
        """
        Loads all the custom filters into the Jinja environment.

        Parameters:
            yaml (RuamelYAMLWrapper): Instance of the YAML parser.
        """
        self.filters['postfix'] = Jinja2CustomFilters.do_postfix
        self.filters['prefix'] = Jinja2CustomFilters.do_prefix
        self.filters['rejectattr_ifkey'] = Jinja2CustomFilters.do_rejectattr_ifkey
        self.filters['rejectkey'] = Jinja2CustomFilters.do_rejectkey
        self.filters['selectattr_ifkey'] = Jinja2CustomFilters.do_selectattr_ifkey
        self.filters['selectkey'] = Jinja2CustomFilters.do_selectkey
        self.filters['toyaml'] = yaml.dump_str


    def __load_custom_functions(self, yaml: RuamelYAMLWrapper):
        """
        Loads all the custom functions into the Jinja environment.

        Parameters:
            yaml (RuamelYAMLWrapper): Instance of the YAML parser.
        """
        self.globals.update(hasprop=Jinja2CustomFunctions.do_hasprop)
        self.globals.update(soft_str=soft_str)
        self.globals.update(toyaml=yaml.dump_str)
        self.globals.update(xor=xor)


    def __load_custom_tests(self):
        """
        Loads all the custom tests into the Jinja environment.
        """
        self.tests['contains'] = Jinja2CustomTests.do_contains
        self.tests['containsgttimes'] = Jinja2CustomTests.do_contains_gttimes
        self.tests['containstimes'] = Jinja2CustomTests.do_contains_times
        self.tests['endswith'] = Jinja2CustomTests.do_endswith
        self.tests['notcontains'] = Jinja2CustomTests.do_not_contains
        self.tests['notendswith'] = Jinja2CustomTests.do_not_endswith
        self.tests['notregexmatch'] = Jinja2CustomTests.do_not_regexmatch
        self.tests['notstartswith'] = Jinja2CustomTests.do_not_startswith
        self.tests['regexmatch'] = Jinja2CustomTests.do_regexmatch
        self.tests['startswith'] = Jinja2CustomTests.do_startswith


    def from_file(self, file: str) -> Template:
        """
        Load a Jinja2 template from file.

        Parameters:
            file (str): The file path to load the template from.

        Returns:
            Returns the loaded template.
        """
        with open(file, mode='r') as f:
            return super().from_string(f.read())
