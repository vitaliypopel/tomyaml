from typing import Any, Dict, Optional, Union

import json
import yaml
import toml
from . import ini

from ._abstractions import FormatAbstraction


class Format(FormatAbstraction):
    def load(self, string: Union[str, bytes]) -> Optional[Dict[str, Any]]:
        if isinstance(string, bytes):
            string = string.decode('utf-8')

        if not string and self.file_format == 'json':
            string = '{}'

        self._string = string
        self._dictionary = self.load_func(self._string)

        if not self._dictionary:
            self._dictionary = {}

        return self._dictionary

    def dump(self, dictionary: Dict[str, Any]) -> Optional[str]:
        string = self.dump_func(dictionary)

        if isinstance(self.string, bytes):
            self._string = string.decode('utf-8')

        return self._string

    def to_dict(self) -> Dict[str, Any]:
        return self._dictionary

    def __str__(self) -> str:
        return self._string

    def __repr__(self) -> str:
        return str(self)


class JSONFormat(Format):
    def __init__(self):
        super().__init__(
            file_format='json',
            load_func=json.loads,
            dump_func=json.dumps,
        )


class YAMLFormat(Format):
    def __init__(self):
        super().__init__(
            file_format='yaml',
            load_func=yaml.safe_load,
            dump_func=yaml.safe_dump,
        )


class TOMLFormat(Format):
    def __init__(self):
        super().__init__(
            file_format='toml',
            load_func=toml.loads,
            dump_func=toml.dumps,
        )


class INIFormat(Format):
    def __init__(self):
        super().__init__(
            file_format='ini',
            load_func=ini.loads,
            dump_func=ini.dumps,
        )


formats = {
    'json': JSONFormat,
    'yaml': YAMLFormat,
    'toml': TOMLFormat,
    'ini': INIFormat,
}
