from typing import Any, Dict, Optional, Union

from ._abstractions.serializer import SerializerAbstraction


class Serializer(SerializerAbstraction):
    def load(self, string: Union[str, bytes]) -> Optional[Dict[str, Any]]:
        return self._file_format.load(string)

    def dump(self, dictionary: Dict[str, Any]) -> Optional[str]:
        return self._file_format.dump(dictionary)

    def to_dict(self) -> Dict[str, Any]:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...
