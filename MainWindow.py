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
        # Master layout
        master_layout = QtWidgets.QHBoxLayout(self)

        # Input column
        input_label_layout = QtWidgets.QVBoxLayout()
        input_label = QtWidgets.QLabel("Inputs", alignment=QtCore.Qt.AlignCenter)
        input_label_layout.addWidget(input_label)

        roll_label = QtWidgets.QLabel("Roll", alignment=QtCore.Qt.AlignLeft)
        roll_input = QtWidgets.QLineEdit("")
        roll_button = QtWidgets.QPushButton("Calculate")

        pitch_label = QtWidgets.QLabel("Pitch", alignment=QtCore.Qt.AlignLeft)
        pitch_input = QtWidgets.QLineEdit("")
        pitch_button = QtWidgets.QPushButton("Calculate")

        yaw_label = QtWidgets.QLabel("Yaw", alignment=QtCore.Qt.AlignLeft)
        yaw_input = QtWidgets.QLineEdit("")
        yaw_button = QtWidgets.QPushButton("Calculate")

        first_line_layout = QtWidgets.QHBoxLayout()
        first_line_layout.addWidget(roll_label)
        first_line_layout.addWidget(roll_input)
        first_line_layout.addWidget(roll_button)

        second_line_layout = QtWidgets.QHBoxLayout()
        second_line_layout.addWidget(pitch_label)
        second_line_layout.addWidget(pitch_input)
        second_line_layout.addWidget(pitch_button)

        third_line_layout = QtWidgets.QHBoxLayout()
        third_line_layout.addWidget(yaw_label)
        third_line_layout.addWidget(yaw_input)
        third_line_layout.addWidget(yaw_button)

        input_vertical_layout = QtWidgets.QVBoxLayout()
        input_vertical_layout.addLayout(input_label_layout)
        input_vertical_layout.addLayout(first_line_layout)
        input_vertical_layout.addLayout(second_line_layout)
        input_vertical_layout.addLayout(third_line_layout)
        master_layout.addLayout(input_vertical_layout)

        # Result Column
        output_label = QtWidgets.QLabel("Results", alignment=QtCore.Qt.AlignCenter)

        roll_layout = QtWidgets.QHBoxLayout()
        roll_output_label = QtWidgets.QLabel("Roll", alignment=QtCore.Qt.AlignLeft)
        roll_outcome = QtWidgets.QLabel("0", alignment=QtCore.Qt.AlignRight)
        roll_layout.addWidget(roll_output_label)
        roll_layout.addWidget(roll_outcome)

        pitch_layout = QtWidgets.QHBoxLayout()
        pitch_output_label = QtWidgets.QLabel("Pitch", alignment=QtCore.Qt.AlignLeft)
        pitch_outcome = QtWidgets.QLabel("0", alignment=QtCore.Qt.AlignRight)
        pitch_layout.addWidget(pitch_output_label)
        pitch_layout.addWidget(pitch_outcome)

        heading_layout = QtWidgets.QHBoxLayout()
        heading_output_label = QtWidgets.QLabel("Heading", alignment=QtCore.Qt.AlignLeft)
        heading_outcome = QtWidgets.QLabel("0", alignment=QtCore.Qt.AlignRight)
        heading_layout.addWidget(heading_output_label)
        heading_layout.addWidget(heading_outcome)

        input_label_layout = QtWidgets.QVBoxLayout()
        input_label_layout.addWidget(output_label)
        input_label_layout.addLayout(roll_layout)
        input_label_layout.addLayout(pitch_layout)
        input_label_layout.addLayout(heading_layout)

        master_layout.addLayout(input_label_layout)


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