from operator import xor

from jinja2 import Environment, Template, filters
from markupsafe import soft_str

from ..custom_jinja.custom_jinja_filters import CustomJinjaFilters
from ..custom_jinja.custom_jinja_functions import CustomJinjaFunctions
from ..custom_jinja.custom_jinja_tests import CustomJinjaTests
from .ruamel_yaml_wrapper import RuamelYAMLWrapper


class JinjaEnvironmentWrapper(Environment):
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
        self.filters['postfix'] = CustomJinjaFilters.do_postfix
        self.filters['prefix'] = CustomJinjaFilters.do_prefix
        self.filters['rejectattr_ifkey'] = CustomJinjaFilters.do_rejectattr_ifkey
        self.filters['rejectkey'] = CustomJinjaFilters.do_rejectkey
        self.filters['selectattr_ifkey'] = CustomJinjaFilters.do_selectattr_ifkey
        self.filters['selectkey'] = CustomJinjaFilters.do_selectkey
        self.filters['toyaml'] = yaml.dump_str


    def __load_custom_functions(self, yaml: RuamelYAMLWrapper):
        """
        Loads all the custom functions into the Jinja environment.

        Parameters:
            yaml (RuamelYAMLWrapper): Instance of the YAML parser.
        """
        self.globals.update(hasprop=CustomJinjaFunctions.do_hasprop)
        self.globals.update(soft_str=soft_str)
        self.globals.update(toyaml=yaml.dump_str)
        self.globals.update(xor=xor)


    def __load_custom_tests(self):
        """
        Loads all the custom tests into the Jinja environment.
        """
        self.tests['contains'] = CustomJinjaTests.do_contains
        self.tests['containsgttimes'] = CustomJinjaTests.do_contains_gttimes
        self.tests['containstimes'] = CustomJinjaTests.do_contains_times
        self.tests['endswith'] = CustomJinjaTests.do_endswith
        self.tests['notcontains'] = CustomJinjaTests.do_not_contains
        self.tests['notendswith'] = CustomJinjaTests.do_not_endswith
        self.tests['notregexmatch'] = CustomJinjaTests.do_not_regexmatch
        self.tests['notstartswith'] = CustomJinjaTests.do_not_startswith
        self.tests['regexmatch'] = CustomJinjaTests.do_regexmatch
        self.tests['startswith'] = CustomJinjaTests.do_startswith


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
