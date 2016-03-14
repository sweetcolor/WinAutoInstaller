import os
import glob
import re

PATH_VIEW = os.path.join('app', 'view')


def ui_compiler():
    curr_path = os.getcwd()
    os.chdir(PATH_VIEW)
    file_extension = '.qrc'
    _compiler('pyrcc5', file_extension, '_rc')
    file_extension = '.ui'
    _compiler('pyuic5', file_extension)
    os.chdir(curr_path)


def _compiler(compiler, file_extension, compiled_end_file_name=''):
    for file_ in glob.glob('*%s' % file_extension):
        file_name = file_[:-len(file_extension)]
        compiled_file_name = file_name + compiled_end_file_name + '.py'
        os.system('%s %s > %s' % (compiler, file_, compiled_file_name))
        if file_extension == '.ui':
            compiled_file_lines = open(compiled_file_name).readlines()
            for idx, line in enumerate(compiled_file_lines):
                f_word = 'import '
                if re.match('%s[a-zA-Z0-9]+_rc' % f_word, line):
                    len_f_word = len(f_word)
                    compiled_file_lines[idx] = '{0}{1}.{2}'.format(line[:len_f_word], PATH_VIEW.replace(os.path.sep, '.'),
                                                                   line[len_f_word:])
            compiled_file = open(compiled_file_name, 'w')
            compiled_file.writelines(compiled_file_lines)
