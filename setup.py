from distutils.core import setup
import py2exe

setup(
    windows=[{"script": "main.py"}],
    options={"py2exe": {"includes": ["sys", "PyQt5.QtCore", "PyQt5.QtGui", "PyQt5.QtWidgets"]}}, requires=['pywinauto',
                                                                                                           'PyQt5']
)


__author__ = 'Администратор'
