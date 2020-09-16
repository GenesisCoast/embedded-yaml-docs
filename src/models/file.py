from pathlib import Path


class File:
    """

    """

    def __init__(self, path: Path, output_path: str):
        """

        """
        self.name = path.name
        self.name_without_suffix = path.name.replace(path.suffix, '')
        self.parent = str(path.parent)
        self.extension = path.suffix
        self.full_name = str(path)