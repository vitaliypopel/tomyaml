import configparser
from io import StringIO

from typing import Any, Dict, Union


def loads(string: Union[str, bytes]) -> Dict[str, Any]:
    '''
    Loads a string or bytes of .ini format into a dictionary
    :param string: Union[str, bytes]
    :return: Dict[Hashable, Any]
    '''
    if isinstance(string, bytes):
        string = string.decode('utf-8')

    config = configparser.ConfigParser()
    config.read_string(string)

    return {
        section: dict(config.items(section))
        for section in config.sections()
    }


def dumps(dictionary: Dict[str, Any]) -> str:
    '''
    Dumps a dictionary into a .ini format string
    :param dictionary: Dict[str, Any]
    :return: str
    '''
    config = configparser.ConfigParser()
    for section, params in dictionary.items():
        config[section] = params

    with StringIO() as ini_out:
        config.write(ini_out)
        return ini_out.getvalue()
