from typing import Any, Dict, Optional, Union

from ._abstractions import SerializerAbstraction


class Serializer(SerializerAbstraction):
    def load(self, string: Union[str, bytes]) -> Optional[Dict[str, Any]]:
        return self.file_format.load(string)

    def dump(self, dictionary: Dict[str, Any]) -> Optional[str]:
        return self.file_format.dump(dictionary)

    def to_dict(self) -> Dict[str, Any]:
        return self.file_format.dictionary or {}

    def __str__(self) -> str:
        return self.file_format.string or ''

    def __repr__(self) -> str:
        return str(self)
