import os
from pathlib import Path


class FileDetails:
    """

    """

    def __init__(self, path: Path, output_path: str, root: str):
        """

        """
        self.name = path.name
        self.name_without_suffix = path.name.replace(path.suffix, '')
        self.parent = str(path.parent)
        self.extension = path.suffix
        self.full_name = str(path)
        self.rel_parent = self.parent.replace(root, '')
        self.rel_full_name = self.full_name.replace(root, '')