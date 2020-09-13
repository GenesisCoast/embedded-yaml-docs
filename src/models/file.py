from pathlib import Path

class File:
    """

    """

    def __init__(self, path: Path):
        """

        """
        self.name = path.name
        self.parent = str(path.parent)
        self.extension = path.suffix
        self.full_name = str(path)