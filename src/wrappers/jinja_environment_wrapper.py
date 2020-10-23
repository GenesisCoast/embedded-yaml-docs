from jinja2 import Environment, Template, filters

from operator import xor

from ..extensions.jinja_filters import JinjaFilters
from ..extensions.jinja_functions import JinjaFunctions
from ..extensions.jinja_tests import JinjaTests
from .ruamel_yaml_wrapper import RuamelYAMLWrapper

from markupsafe import soft_str

class JinjaEnvironmentWrapper(Environment):
    """
    Custom implementation for the Jinja2 environment.
    """


    def __init__(self, **kwargs):
        """
        Initialize the environment, and adds the custom Tests and Filters.

        Parameters:
            **kwargs: Additional configuration for the environment.
        """
        super().__init__(**kwargs)

        yaml = RuamelYAMLWrapper()

        self.filters['rejectattr_ifkey'] = JinjaFilters.rejectattr_ifkey
        self.filters['rejectkey'] = JinjaFilters.rejectkey
        self.filters['selectattr_ifkey'] = JinjaFilters.selectattr_ifkey
        self.filters['selectkey'] = JinjaFilters.selectkey

        self.globals.update(hasprop=JinjaFunctions.hasprop)
        self.globals.update(soft_str=soft_str)
        self.globals.update(xor=xor)
        self.filters['prefix'] = JinjaFilters.prefix
        self.filters['postfix'] = JinjaFilters.postfix
        self.filters['toyaml'] = yaml.dump_str

        self.tests['contains'] = JinjaTests.contains
        self.tests['notcontains'] = JinjaTests.not_contains
        self.tests['containsgttimes'] = JinjaTests.contains_gttimes
        self.tests['containstimes'] = JinjaTests.contains_times
        self.tests['endswith'] = JinjaTests.endswith
        self.tests['notendswith'] = JinjaTests.not_endswith
        self.tests['notstartswith'] = JinjaTests.not_startswith
        self.tests['regexmatch'] = JinjaTests.regex_match
        self.tests['startswith'] = JinjaTests.startswith


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
