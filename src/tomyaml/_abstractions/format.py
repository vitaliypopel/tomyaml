from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Literal, Optional, Union


class FormatAbstraction(ABC):
    _file_format: str
    _load_func: Callable[[Union[str, bytes]], Dict[str, Any]]
    _dump_func: Callable[[Dict[str, Any]], Union[str, bytes]]

    _dictionary: Optional[Dict[str, Any]]
    _string: Optional[str]

    def __init__(
            self,
            file_format: Literal['json', 'yaml', 'toml', 'ini'],
            load_func: Callable[[Union[str, bytes]], Dict[str, Any]],
            dump_func: Callable[[Dict[str, Any]], Union[str, bytes]],
    ):
        self._file_format = file_format
        self._load_func = load_func
        self._dump_func = dump_func

        self._dictionary = None
        self._string = None

    @property
    def file_format(self) -> str:
        return self._file_format

    @property
    def load_func(self) -> Callable[[Union[str, bytes]], Dict[str, Any]]:
        return self._load_func

    @property
    def dump_func(self) -> Callable[[Dict[str, Any]], Union[str, bytes]]:
        return self._dump_func

    @property
    def dictionary(self) -> Dict[str, Any]:
        return self._dictionary

    @property
    def string(self) -> str:
        return self._string

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
