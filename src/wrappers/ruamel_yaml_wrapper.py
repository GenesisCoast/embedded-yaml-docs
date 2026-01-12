from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO


class RuamelYAMLWrapper(YAML):
    """
    Custom implementation of the ruamel library.
    """

    def __init__(self):
        """Initialize the wrapper with both full and safe parsers."""
        super().__init__()
        self._safe_yaml = YAML(typ='safe', pure=True)


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

        super().dump(data, stream, **kwargs)

        output_str = stream.getvalue()

        stream.close()

        return output_str


    def load_from_file(self, file: str) -> any:
        """
        Loads a YAML document from a file, includes any metadata, comments etc...

        Parameters:
            file (str): The file path to load the YAML from.

        Returns:
            The parsed YAML document.
        """
        return super().load(open(file).read())


    def safe_load(self, stream: any) -> any:
        """
        Safely loads the YAML document, excluding any metadata.

        Parameters:
            stream (any): The YAML stream to parse.

        Returns:
            The parsed YAML document.
        """
        return self._safe_yaml.load(stream)
