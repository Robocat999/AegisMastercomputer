from PySide6 import QtCore, QtWidgets, QtGui
import sys

class WidgetMain(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self._create_menus()
        self.setWindowTitle("Aegis Mastercomputer")

    def _create_menus(self):
        """
        Creates gui elements and adds them to the layout
        :return:
        """
        self.text = QtWidgets.QLabel("Intial Text", alignment=QtCore.Qt.AlignLeft)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        return

    @QtCore.Slot()
    def magic(self):
        self.text.setText("Test Text")
        return


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = WidgetMain()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())