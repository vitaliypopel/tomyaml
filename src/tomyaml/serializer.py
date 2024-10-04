from typing import Any, Dict, Optional, Union

from ._abstractions.serializer import SerializerAbstraction


class Serializer(SerializerAbstraction):
    def load(self, string: Union[str, bytes]) -> Optional[Dict[str, Any]]:
        return self._file_format.load(string)

    def dump(self, dictionary: Dict[str, Any]) -> Optional[str]:
        return self._file_format.dump(dictionary)

    def __str__(self) -> str:
        return 'Serializer(file_format="%s")' % self._file_format.file_format

    def __repr__(self) -> str:
        return str(self)
