from ruamel.yaml.composer import Composer
from ruamel.yaml.constructor import RoundTripConstructor
from ruamel.yaml.loader import RoundTripLoader
from ruamel.yaml.parser import RoundTripParser
from ruamel.yaml.reader import Reader
from ruamel.yaml.resolver import VersionedResolver
from ruamel.yaml.scanner import RoundTripScanner

from yaml_docs_constructor import YAMLDocsConstructor


class YAMLDocsLoader(RoundTripLoader):
    """

    """

    def __init__(self, stream, version=None, preserve_quotes=None):
        """

        """
        Reader.__init__(self, stream, loader=self)
        RoundTripScanner.__init__(self, loader=self)
        RoundTripParser.__init__(self, loader=self)
        Composer.__init__(self, loader=self)
        YAMLDocsConstructor.__init__(self, preserve_quotes=preserve_quotes, loader=self)
        VersionedResolver.__init__(self, version, loader=self)