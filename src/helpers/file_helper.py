import contextlib
import os
import re
from pathlib import Path
from typing import List

from .string_helper import StringHelper


class FileHelper:
    """

    """


    @staticmethod
    def get_files(path, pattern, recursive=False):
        """

        """
        if os.path.isfile(path):
            files = ''.join(path)
        else:
            folder = Path(path)

            if recursive:
                files = list(folder.rglob(pattern))
            else:
                files = list(folder.glob(pattern))

        return files


    @staticmethod
    @contextlib.contextmanager
    def open_makedirs(file: str, mode: str):
        """

        """
        # Make sure that the files directory exists.
        os.makedirs(
            FileHelper.get_file_parent(file),
            exist_ok=True
        )

        # Open the file.
        s = open(file, mode)

        # Yield the file stream.
        yield s

        # Close the stream once it is finished.
        s.close()


    @staticmethod
    def get_file_parent(file: str):
        """

        """
        return Path(file).parent


    @staticmethod
    def join_paths(path: str, *paths: list) -> str:
        """

        """
        path = StringHelper.remove_postfix(path, '/')
        path = StringHelper.remove_postfix(path, '\\')

        if not isinstance(paths, list):
            paths = list(paths)

        for index in range(0, len(paths)):
            paths[index] = StringHelper.remove_prefix(paths[index], '/')
            paths[index] = StringHelper.remove_prefix(paths[index], '\\')
            paths[index] = StringHelper.remove_postfix(paths[index], '/')
            paths[index] = StringHelper.remove_postfix(paths[index], '\\')

        return os.path.join(path, *paths)
