import os
import glob
import re

PATH_VIEW_UI = os.path.join('app', 'view_ui')
PATH_VIEW_PY = os.path.join('app', 'view_py')


def ui_compiler():
    default_path = os.getcwd()
    file_extension = '.qrc'
    _compiler('pyrcc5', file_extension, '_rc')
    file_extension = '.ui'
    _compiler('pyuic5', file_extension)
    os.chdir(default_path)


def _compiler(compiler, file_extension, compiled_end_file_name=''):
    for file_ in glob.glob(os.path.join(PATH_VIEW_UI, '*%s' % file_extension)):
        file_name = os.path.basename(file_[:-len(file_extension)])
        compiled_file_name = os.path.join(PATH_VIEW_PY, file_name + compiled_end_file_name + '.py')
        os.system('%s %s > %s' % (compiler, file_, compiled_file_name))
        if file_extension == '.ui':
            compiled_file_lines = open(compiled_file_name).readlines()
            for idx, line in enumerate(compiled_file_lines):
                f_word = 'import '
                if re.match('%s[a-zA-Z0-9]+_rc' % f_word, line):
                    len_f_word = len(f_word)
                    compiled_file_lines[idx] = '{0}{1}.{2}'.format(line[:len_f_word], PATH_VIEW_PY.replace(os.path.sep, '.'),
                                                                   line[len_f_word:])
            compiled_file = open(compiled_file_name, 'w')
            compiled_file.writelines(compiled_file_lines)
