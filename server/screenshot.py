#!/usr/bin/python3

from sys import argv
from base64 import b64encode

from PyQt4.QtGui import QPixmap, QApplication
from PyQt4.Qt import QBuffer, QIODevice

__all__ = [
    'size',
    'get_data_uri'
]

app = QApplication(argv)
size = QApplication.desktop().size()
size = (size.width(), size.height())

def get_data_uri():
    buffer = QBuffer()
    buffer.open(QIODevice.ReadWrite)

    QPixmap.grabWindow(QApplication.desktop().winId()).save(buffer, 'jpg', 10)
    
    return 'data:image/jpeg;base64,' + str(b64encode(buffer.data().data()), 'ascii')

if __name__ == '__main__':
    print(size)
    uri = get_data_uri()
    print(len(uri))