from jinja2 import Environment, Template

from ..extensions.jinja_filters import JinjaFilters
from ..extensions.jinja_tests import JinjaTests


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

        self.filters['rejectattr_ifkey'] = JinjaFilters.rejectattr_ifkey
        self.filters['rejectkey'] = JinjaFilters.rejectkey
        self.filters['selectattr_ifkey'] = JinjaFilters.selectattr_ifkey
        self.filters['selectkey'] = JinjaFilters.selectkey

        self.globals.update(contains_gttimes=JinjaTests.contains_gttimes)

        self.tests['contains'] = JinjaTests.contains
        self.tests['contains_gttimes'] = JinjaTests.contains_gttimes
        self.tests['contains_times'] = JinjaTests.contains_times
        self.tests['endswith'] = JinjaTests.endswith
        self.tests['not_endswith'] = JinjaTests.not_endswith
        self.tests['not_startswith'] = JinjaTests.not_startswith
        self.tests['regex_match'] = JinjaTests.regex_match
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
