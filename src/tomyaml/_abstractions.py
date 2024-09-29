from abc import ABC, abstractmethod
from typing import Any, Callable, Hashable, Optional, Union


class FormatAbstraction(ABC):
    __file_format: str
    __load_func: Callable[[Union[str, bytes]], dict[Hashable, Any]]
    __dump_func: Callable[[dict[Hashable, Any]], Union[str, bytes]]

    __dictionary: Optional[dict[Hashable, Any]]
    __string: Optional[str]

    def __init__(
            self,
            file_format: str,
            load_func: Callable[[Union[str, bytes]], dict[Hashable, Any]],
            dump_func: Callable[[dict[Hashable, Any]], Union[str, bytes]],
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
    def load_func(self) -> Callable[[Union[str, bytes]], dict[Hashable, Any]]:
        return self.__load_func

    @property
    def dump_func(self) -> Callable[[dict[Hashable, Any]], Union[str, bytes]]:
        return self.__dump_func

    @property
    def dictionary(self) -> dict[Hashable, Any]:
        return self.__dictionary

    @property
    def string(self) -> str:
        return self.__string

    @abstractmethod
    def load(self, string: Union[str, bytes]) -> Optional[dict[Hashable, Any]]:
        '''Loads a string or bytes into a dictionary'''
        pass

    @abstractmethod
    def dump(self, dictionary: dict[Hashable, Any]) -> Optional[str]:
        '''Dumps a dictionary into a string'''
        pass

    @abstractmethod
    def to_dict(self) -> dict[Hashable, Any]:
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
