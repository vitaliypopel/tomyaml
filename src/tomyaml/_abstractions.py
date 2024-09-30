from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Literal, Optional, Union

from .formats import (
    Format,
    JSONFormat,
    YAMLFormat,
    TOMLFormat,
    INIFormat,
)


class FormatAbstraction(ABC):
    __file_format: str
    __load_func: Callable[[Union[str, bytes]], Dict[str, Any]]
    __dump_func: Callable[[Dict[str, Any]], Union[str, bytes]]

    __dictionary: Optional[Dict[str, Any]]
    __string: Optional[str]

    def __init__(
            self,
            file_format: Literal['json', 'yaml', 'toml', 'ini'],
            load_func: Callable[[Union[str, bytes]], Dict[str, Any]],
            dump_func: Callable[[Dict[str, Any]], Union[str, bytes]],
    ):
        self.__file_format = file_format
        self.__load_func = load_func
        self.__dump_func = dump_func

        self.__dictionary = None
        self.__string = None

    @property
    def file_format(self) -> str:
        return self.__file_format

    @property
    def load_func(self) -> Callable[[Union[str, bytes]], Dict[str, Any]]:
        return self.__load_func

    @property
    def dump_func(self) -> Callable[[Dict[str, Any]], Union[str, bytes]]:
        return self.__dump_func

    @property
    def dictionary(self) -> Dict[str, Any]:
        return self.__dictionary

    @property
    def string(self) -> str:
        return self.__string

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


class SerializerAbstraction(ABC):
    __file_format: Format

    def __init__(
            self,
            file_format: Literal['json', 'yaml', 'toml', 'ini'],
    ):
        file_format = file_format.lower()

        if file_format == 'json':
            self.__file_format = JSONFormat()
        elif file_format == 'yaml':
            self.__file_format = YAMLFormat()
        elif file_format == 'toml':
            self.__file_format = TOMLFormat()
        elif file_format == 'ini':
            self.__file_format = INIFormat()
        else:
            raise ValueError(
                'Expected "json", "yaml", "toml" or "ini" file format, '
                'instead got "%s"' % file_format.lower()
            )

    @property
    def file_format(self) -> Format:
        return self.__file_format

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
