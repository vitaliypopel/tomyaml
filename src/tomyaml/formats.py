from typing import Any, Dict, Hashable, Optional, Union

import json
import yaml
import toml

from ._abstractions import FormatAbstraction


class Format(FormatAbstraction):
    def load(self, string: Union[str, bytes]) -> Optional[Dict[Hashable, Any]]:
        if isinstance(string, bytes):
            string = string.decode('utf-8')

        if not string and self.file_format == 'json':
            string = '{}'

        self.__string = string
        self.__dictionary = self.load_func(self.__string)

        if not self.__dictionary:
            self.__dictionary = {}

        return self.__dictionary

    def dump(self, dictionary: Dict[Hashable, Any]) -> Optional[str]:
        string = self.dump_func(dictionary)

        if isinstance(self.string, bytes):
            self.__string = string.decode('utf-8')

        return self.__string

    def to_dict(self) -> Dict[Hashable, Any]:
        return self.__dictionary

    def __str__(self) -> str:
        return self.__string

    def __repr__(self) -> str:
        return str(self)
