"""
Random Hanzi implemented using QtQuick
"""
import sys
import random

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtCore import QObject, Slot

import hanzi

QML_IMPORT_NAME = 'random_hanzi.signals.hanzi'
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class Hanzi(QObject):
  @Slot(int, bool, result=str)
  def random(self, count, is_common):
    if is_common:
      return hanzi.random_common(count)
    else:
      return hanzi.random(count)

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('random_hanzi.qml')
if not engine.rootObjects():
  sys.exit(-1)

sys.exit(app.exec())
