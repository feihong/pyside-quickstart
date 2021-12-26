import sys
import hanzi
from PySide6 import QtCore, QtWidgets, QtGui
from MainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)
    self.button.clicked.connect(self.on_click)

  @QtCore.Slot()
  def on_click(self):
    only_common = self.onlyCommon.checkState() == QtCore.Qt.Checked
    gen_func = hanzi.random_common if only_common else hanzi.random
    text = gen_func(self.count.value())
    self.output.setText(text)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
