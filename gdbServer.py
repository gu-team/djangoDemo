#!/usr/bin/env python
import gdb
import sys
import os
sys.path.append(r'~/Desktop/')

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoDemo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
		    raise ImportError(
				    "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(['gdbEntry.py', 'runserver'])

class GdbDemo():
    fileName = 'demo.c'
    def start(self):
        gdb.execute('file ' + self.fileName)
        ret = gdb.execute('start', to_string=True)
        return 'it is start return: ' + ret
