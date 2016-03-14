import sys


if __name__ == '__main__':
    from framework.ui_compiller import ui_compiler
    ui_compiler()
    from app.run import run
    run(sys.argv)


__author__ = 'Администратор'
