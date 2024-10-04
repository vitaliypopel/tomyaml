import configparser
from io import StringIO
from multiprocessing.managers import Value

from typing import Any, Dict, Union


def _convert_value(value: str) -> Any:
    '''
    Converting values to Python types
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
                dictionary[section][key] = _convert_value(value)
    else:
        dictionary = dict(config.defaults())

        for key, value in dictionary.items():
            dictionary[key] = _convert_value(value)

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
                if isinstance(value, list):
                    config[section][key] = ','.join(value)
                elif isinstance(value, bool):
                    config[section][key] = str(value).lower()
                else:
                    config[section][key] = str(value)

        else:
            key, value = section, params

            if isinstance(value, list):
                config['DEFAULT'][key] = ','.join(value)
            elif isinstance(value, bool):
                config['DEFAULT'][key] = str(value).lower()
            else:
                config['DEFAULT'][key] = str(value)

    with StringIO() as ini_out:
        config.write(ini_out)
        return ini_out.getvalue()
