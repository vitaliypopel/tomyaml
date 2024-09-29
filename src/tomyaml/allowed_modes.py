MODES_HELPER = \
    '+---------------------------+---------------+------------------------------------------+\n' \ 
    '|    HUMAN READABLE MODE    |      MODE     |   ACCESS                                 |\n' \
    '+---------------------------+---------------+------------------------------------------+\n' \
    '|          read             |       r       |   only for reading file                  |\n' \
    '|          write            |       w       |   only for writing into file             |\n' \
    '|          append           |       a       |   only for appending data into file      |\n' \
    '|          binary           |       b       |   only for reading binary file           |\n' \
    '|          read_write       |       r+      |   first reading file and then writing    |\n' \
    '|          write_read       |       w+      |   first writing file and then reading    |\n' \
    '|          append_read      |       a+      |   first append file and then reading     |\n' \
    '+---------------------------+---------------+------------------------------------------+\n'

ALLOWED_MODES = {
    'read':         'r',
    'write':        'w',
    'append':       'a',
    'binary':       'b',
    'read_write':   'r+',
    'write_read':   'w+',
    'append_read':  'a+',
}
