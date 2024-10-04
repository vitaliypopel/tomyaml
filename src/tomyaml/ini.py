import configparser
from io import StringIO

from typing import Any, Dict, Union


def _convert_to_python(value: str) -> Any:
    '''
    Converting values from .ini string to Python type
    :param value: str
    :return: Any
    '''

    if value == 'true':
        value = True
    elif value == 'false':
        value = False
    elif ',' in value:
        value = value.split(',')
    else:
        try:
            if '.' in value:
                value = float(value)
            value = int(value)
        except ValueError:
            pass

    return value


def _convert_to_ini(value: Any) -> str:
    '''
    Converts from Python type to .ini string
    :param value: Any
    :return: str
    '''

    if isinstance(value, bool):
        value = str(value).lower()
    elif isinstance(value, list):
        value = ','.join(value)

    return str(value)


def loads(string: Union[str, bytes]) -> Dict[str, Any]:
    '''
    Loads a string or bytes of .ini format into a dictionary
    :param string: Union[str, bytes]
    :return: Dict[str, Any]
    '''
    if isinstance(string, bytes):
        string = string.decode('utf-8')

    config = configparser.ConfigParser()
    config.read_string(string)

    dictionary = {}

    if config.sections():
        for section in config.sections():
            dictionary[section] = {}

            for key, value in config.items(section):
                dictionary[section][key] = _convert_to_python(value)
    else:
        dictionary = dict(config.defaults())

        for key, value in dictionary.items():
            dictionary[key] = _convert_to_python(value)

    return dictionary


def dumps(dictionary: Dict[str, Any]) -> str:
    '''
    Dumps a dictionary into a .ini format string
    :param dictionary: Dict[str, Any]
    :return: str
    '''
    config = configparser.ConfigParser()

    for section, params in dictionary.items():
        if isinstance(params, dict):
            config[section] = {}

            for key, value in params.items():
                config[section][key] = _convert_to_ini(value)

        else:
            key, value = section, params

            config['DEFAULT'][key] = _convert_to_ini(value)

    with StringIO() as ini_out:
        config.write(ini_out)
        return ini_out.getvalue()
