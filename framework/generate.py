import sys
import os
import time
import re


def migration(name):
    converted_name = ''
    while name != '':
        find = re.search('([A-Z])', name)
        if find:
            converted_name += name[find.pos:find.end()-1] + '_' + name[find.end()-1].lower()
            name = name[find.end():]
        else:
            converted_name += name
            name = ''
    migration_name = str(int(round(time.time() * 1000))) + '_' + converted_name + '.sql'
    open(os.path.join('db', migration_name), 'w')

arg_dict = {
    'migration': migration,
}

for i in range(1, 1 + len(sys.argv[1:]), 2):
    arg_dict[sys.argv[i]](sys.argv[i + 1])

