from pathlib import Path

from ruamel.yaml import YAML, yaml_object


@yaml_object(YAML())
class FileDetails(object):
    """
    Model for storing the file details so that they can be used in the
    Jinja2 template.

    Properties:
        name (str): Name of the file.
        name_without_suffix (str): Name of the file, excluding the file
            extension.
        parent (str): The parent folder of the file.
        extension (str): The file extension for the file.
        full_name (str): The full path to the file.
        rel_parent (str): The relative parent path to the file, uses the repository
            root to calculate.
        rel_full_name (str): The relative full path to the file, uses the repository
            root to calculate.
    """


    def __init__(
        self,
        file: str,
        root: str = None
    ):
        """
        Constructor for initializing the model with the relevant properties.
        """

        path = Path(file)

        self.name = path.name
        self.name_without_suffix = path.name.replace(path.suffix, '')
        self.parent = str(path.parent)
        self.extension = path.suffix
        self.full_name = str(path)

        if root:
            self.rel_parent = self.parent.replace(root, '')
            self.rel_full_name = self.full_name.replace(root, '')
