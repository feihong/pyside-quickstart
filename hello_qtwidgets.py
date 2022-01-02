"""
Hello World using QtWidgets.

Show how to add shortcut and change font size of label.
"""
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

messages = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир", "你好世界"]

class MyWidget(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle('Hello Qt')

    self.button = QtWidgets.QPushButton("Click me!")
    self.label = QtWidgets.QLabel("Hello World",
                                  alignment=QtCore.Qt.AlignCenter)
    self.label.setFont(QtGui.QFont(self.font().family(), 40))

    self.layout = QtWidgets.QVBoxLayout(self)
    self.layout.addWidget(self.label)
    self.layout.addWidget(self.button)

    self.button.clicked.connect(self.on_click)

    QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)

  @QtCore.Slot()
  def on_click(self):
    self.label.setText(random.choice(messages))

if __name__ == "__main__":
  app = QtWidgets.QApplication([])

  widget = MyWidget()
  widget.resize(800, 600)
  widget.show()

  sys.exit(app.exec())
