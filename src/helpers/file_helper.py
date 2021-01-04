import contextlib
import os
import re
from pathlib import Path
from typing import List

from .string_helper import StringHelper


class FileHelper:
    """
    Collection of methods to help with files.
    """


    @staticmethod
    def get_files(path: str, pattern: str, recursive: bool = False) -> list:
        """
        Get a file or list of files using a path and search pattern.

        Parameters:
            path (str): The path to search for files in.
            pattern (str): The search pattern to use when searching for
                files within a directory.
            recursive (bool): Flag if the method should search for files in
                sub-folders or just the root folder.

        Returns:
            list: A list of files for the path.
        """
        if os.path.isfile(path):
            files = [Path(path)]
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
        Opens the file and double checks that its directory path actually exists.
        If it doesn't then the relevant directories are created. Useful for creating
        a new file in a directory(ies) that doe not already exist.

        Parameters:
            file (str): Filepath to open.
            mode (str): The mode to open the file using.
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
    def get_file_parent(file: str) -> str:
        """
        Gets the parent folder of the specified file path.

        Parameters:
            file (str): Path to get the parent for.

        Returns:
            str: The parent of the specified path.
        """
        return Path(file).parent


    @staticmethod
    def join_paths(path: str, *paths: list) -> str:
        """
        Joins a collection of paths together. That have been formatted.

        Parameters:
            path (str): The first path to join.
            paths (list): Collection of paths to join together.

        Returns:
            str: The paths combined together.
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
