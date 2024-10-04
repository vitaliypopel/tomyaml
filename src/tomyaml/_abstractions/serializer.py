from abc import ABC, abstractmethod
from typing import Any, Dict, Literal, Optional, Union

from ..formats import (
    Format,
    formats,
)


class SerializerAbstraction(ABC):
    _file_format: Format

    def __init__(
            self,
            file_format: Literal['json', 'yaml', 'toml', 'ini'],
    ):
        FormatClass = formats.get(file_format.lower(), None)

        if not FormatClass:
            raise ValueError(
                'Expected "json", "yaml", "toml" or "ini" file format, '
                'instead got "%s"' % file_format.lower()
            )

        self._file_format = FormatClass()

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
    def __str__(self) -> str:
        '''String representation of the object'''
        pass

    @abstractmethod
    def __repr__(self) -> str:
        '''Representation of the object for debugging'''
        pass
