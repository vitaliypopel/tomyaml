from typing import Any


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
