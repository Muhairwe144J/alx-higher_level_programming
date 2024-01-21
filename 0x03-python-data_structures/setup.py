from distutils.core import setup, Extension

module = Extension('libPyList', sources=['100-print_python_list_info.c'])

setup(name='libPyList',
      version='1.0',
      description='Python List Info',
      ext_modules=[module])
