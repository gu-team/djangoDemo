import gdb

class GdbDemo():
    fileName = 'demo.c'
    def start(self):
        gdb.execute('file ' + self.fileName)
        ret = gdb.execute('start', to_string=True)
        return 'it is start return: ' + ret