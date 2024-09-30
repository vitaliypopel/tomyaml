from abc import ABC, abstractmethod
from typing import Any, Dict, Literal, Optional, Union

from ..formats import (
    Format,
    JSONFormat,
    YAMLFormat,
    TOMLFormat,
    INIFormat,
)


class SerializerAbstraction(ABC):
    _file_format: Format

    def __init__(
            self,
            file_format: Literal['json', 'yaml', 'toml', 'ini'],
    ):
        file_format = file_format.lower()

        if file_format == 'json':
            self._file_format = JSONFormat()
        elif file_format == 'yaml':
            self._file_format = YAMLFormat()
        elif file_format == 'toml':
            self._file_format = TOMLFormat()
        elif file_format == 'ini':
            self._file_format = INIFormat()
        else:
            raise ValueError(
                'Expected "json", "yaml", "toml" or "ini" file format, '
                'instead got "%s"' % file_format.lower()
            )

    @property
    def file_format(self) -> Format:
        return self._file_format

    @abstractmethod
    def load(self, string: Union[str, bytes]) -> Optional[Dict[str, Any]]:
        '''Loads a string or bytes into a dictionary'''
        pass

    @abstractmethod
    def dump(self, dictionary: Dict[str, Any]) -> Optional[str]:
        '''Dumps a dictionary into a string'''
        pass

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        '''Converts the current object to a dictionary'''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''String representation of the object'''
        pass

    @abstractmethod
    def __repr__(self) -> str:
        '''Representation of the object for debugging'''
        pass
