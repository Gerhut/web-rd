#!/usr/bin/python3

from sys import argv

from PyQt4.QtCore import Qt, QCoreApplication, QEvent, QPoint
from PyQt4.QtGui import QMouseEvent, QApplication

__all__ = [
    'down',
    'move',
    'up'
]

app = QApplication(argv)
desktop = QApplication.desktop()

def down(x, y):
    event = QMouseEvent(
        QEvent.MouseButtonPress,
        QPoint(x, y),
        QPoint(x, y),
        Qt.LeftButton,
        Qt.LeftButton,
        Qt.NoModifier
    )
    QCoreApplication.postEvent(desktop, event)

def move(x, y):
    event = QMouseEvent(
        QEvent.MouseMove,
        QPoint(x, y),
        QPoint(x, y),
        Qt.NoButton,
        Qt.NoButton,
        Qt.NoModifier
    )
    QCoreApplication.sendEvent(desktop, event)
    QCoreApplication.processEvents()

def up(x, y):
    event = QMouseEvent(
        QEvent.MouseButtonRelease,
        QPoint(x, y),
        QPoint(x, y),
        Qt.LeftButton,
        Qt.LeftButton,
        Qt.NoModifier
    )
    QCoreApplication.postEvent(desktop, event)

if __name__ == '__main__':
    move(0, 0)