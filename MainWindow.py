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
        text = QtWidgets.QLabel("Intial Text", alignment=QtCore.Qt.AlignLeft)
        roll_input = QtWidgets.QLineEdit("Roll")
        pitch_input = QtWidgets.QLineEdit("Pitch")
        yaw_input = QtWidgets.QLineEdit("Yaw")
        confirm_button = QtWidgets.QPushButton("Calculate")


        first_line_layout = QtWidgets.QHBoxLayout()
        first_line_layout.addWidget(text)
        first_line_layout.addWidget(roll_input)
        first_line_layout.addWidget(confirm_button)

        second_line_layout = QtWidgets.QHBoxLayout()
        second_line_layout.addWidget(pitch_input)
        second_line_layout.addWidget(yaw_input)

        left_vertical_layout = QtWidgets.QVBoxLayout(self)
        left_vertical_layout.addLayout(first_line_layout)
        left_vertical_layout.addLayout(second_line_layout)

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