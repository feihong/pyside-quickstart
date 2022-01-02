"""
Hello World implemented in QtQuick
"""
import sys
import random

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtCore import QObject, Slot

QML_IMPORT_NAME = 'hello.signals.greeter'
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class Greeter(QObject):
  messages = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир", "你好世界"]

  @Slot(result=str)
  def random(self):
    return random.choice(self.messages)

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('hello.qml')
if not engine.rootObjects():
  sys.exit(-1)

sys.exit(app.exec())
