from PyQt5.QtGui import QRegExpValidator, QRegularExpressionValidator, QValidator

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QPushButton, QSpinBox, QLineEdit, QCalendarWidget, QDateEdit, \
    QComboBox, QMessageBox


# check if the text field isnt empty

class EmailLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        validator = QRegularExpressionValidator(QtCore.QRegularExpression(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"), self)
        self.setValidator(validator)

    def focusOutEvent(self, event):
        print("focus out")
        input_text = self.text()
        if self.validator().validate(input_text, 0)[0] != QValidator.Acceptable:
            # make gui alert message
            QMessageBox.critical(self, "Error", "Invalid email address")
            self.setFocus()
        else:
            super().focusOutEvent(event)
