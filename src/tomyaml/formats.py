from typing import Any, Dict, Optional, Union

import json
import yaml
import toml
from . import ini

from ._abstractions.format import FormatAbstraction


class Format(FormatAbstraction):
    def load(self, string: Union[str, bytes]) -> Optional[Dict[str, Any]]:
        if isinstance(string, bytes):
            string = string.decode('utf-8')

        if not string and self.file_format == 'json':
            string = '{}'

        dictionary = self.load_func(string)

        if not dictionary:
            dictionary = {}

        return dictionary

    def dump(self, dictionary: Dict[str, Any]) -> Optional[str]:
        string = self.dump_func(dictionary)

        if isinstance(string, bytes):
            string = string.decode('utf-8')

        return string

    def __str__(self) -> str:
        return 'Format("%s")' % self._file_format

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
