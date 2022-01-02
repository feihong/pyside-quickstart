"""
Random hanzi implemented using QtWidgets and loading directly from .ui file
"""
import sys
import hanzi
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

@QtCore.Slot()
def on_click():
  only_common = window.onlyCommon.checkState() == QtCore.Qt.Checked
  gen_func = hanzi.random_common if only_common else hanzi.random
  text = gen_func(window.count.value())
  window.output.setText(text)

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
window = loader.load("mainwindow.ui", None)
QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), window, window.close)
window.button.clicked.connect(on_click)
window.show()
app.exec()
