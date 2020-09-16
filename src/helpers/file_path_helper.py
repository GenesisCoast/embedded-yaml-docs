import os
from .string_helper import StringHelper

class FilePathHelper:
    """

    """


    @staticmethod
    def join(path: str, *paths: list) -> str:
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