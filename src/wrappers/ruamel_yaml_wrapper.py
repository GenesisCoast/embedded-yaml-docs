from ruamel.yaml import YAML, safe_load
from ruamel.yaml.compat import StringIO


class RuamelYAMLWrapper():
    """
    Custom implementation of the ruamel library.
    """


    def __init__(self, yaml: YAML):
        """

        """
        self.yaml = yaml


    def dump_str(self, data: any, **kwargs) -> str:
        """
        Return the YAML object as a string.

        Properties:
            data<any>: The YAML object.
            **kwargs: Options for the YAML dump.

        Returns:
            The YAML object as a string.
        """
        stream = StringIO()

        self.yaml.dump(data, stream, **kwargs)

        output_str = stream.getvalue()

        stream.close()

        return output_str


    def load(self, stream) -> any:
        """

        """
        return self.yaml.load(stream)


    def load_from_file(self, path: str) -> any:
        """

        """
        return self.load(open(path).read())


    def safe_loader(self, stream) -> any:
        """

        """
        return safe_load(stream)
