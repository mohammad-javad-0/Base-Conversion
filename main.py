from PyQt6.QtWidgets import QTextBrowser, QTextEdit, QApplication, QComboBox, QWidget, QLabel, QPushButton, QMessageBox
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # window setting
        self.setWindowTitle("Base Conversion")
        self.setWindowIcon(QIcon("image/heading-icon.png"))
        self.setFixedSize(650, 600)
        self.setStyleSheet("background-color:green")

        # create label heading
        lbl_heading = QLabel("BASE CONVERSION", self)
        lbl_heading.setFont(QFont("arial", 15))
        lbl_heading.setStyleSheet("background-color:black;color:yellow")
        lbl_heading.setIndent(230)
        lbl_heading.setGeometry(0, 20, 650, 40)

        # create input base
        lbl_input_base = QLabel("Choice input base: ", self)
        lbl_input_base.setFont(QFont("arial", 15))
        lbl_input_base.setGeometry(20, 80, 200, 30)

        self.combo_input_base = QComboBox(self)
        self.combo_input_base.addItem("2 (bin)", 2)
        self.combo_input_base.addItem("8 (oct)", 8)
        self.combo_input_base.addItem("10 (dec)", 10)
        self.combo_input_base.addItem("16 (hex)", 16)
        self.combo_input_base.setStyleSheet("background-color:white; color: black")
        self.combo_input_base.setFont(QFont("arial", 13))
        self.combo_input_base.setGeometry(200, 85, 100, 20)

        # create output base
        lbl_output_base = QLabel("Choice output base: ", self)
        lbl_output_base.setFont(QFont("arial", 15))
        lbl_output_base.setGeometry(320, 80, 200, 30)

        self.combo_output_base = QComboBox(self)
        self.combo_output_base.addItem("10 (dec)", 10)
        self.combo_output_base.addItem("2 (bin)", 2)
        self.combo_output_base.addItem("8 (oct)", 8)
        self.combo_output_base.addItem("16 (hex)", 16)
        self.combo_output_base.setStyleSheet("background-color:white; color: black")
        self.combo_output_base.setFont(QFont("arial", 13))
        self.combo_output_base.setGeometry(510, 85, 100, 20)

        # create input number
        lbl_input = QLabel("input: ", self)
        lbl_input.setFont(QFont("arial", 20))
        lbl_input.setGeometry(20, 200, 100, 30)

        self.txt_input = QTextEdit(self)
        self.txt_input.setStyleSheet("background-color:white; color: black")
        self.txt_input.setFont(QFont("arial", 15))
        self.txt_input.setGeometry(110, 140, 500, 150)

        # create output number
        lbl_output = QLabel("output: ", self)
        lbl_output.setFont(QFont("arial", 20))
        lbl_output.setGeometry(20, 390, 100, 30)

        self.txt_output = QTextBrowser(self)
        self.txt_output.setStyleSheet("background-color:white; color:black")
        self.txt_output.setFont(QFont("arial", 15))
        self.txt_output.setGeometry(110, 330, 500, 150)

        # create convert button
        btn_convert = QPushButton("CONVERT", self)
        btn_convert.setFont(QFont("arial", 25))
        btn_convert.setStyleSheet("background-color:red")
        btn_convert.setGeometry(225, 520, 200, 50)
        btn_convert.clicked.connect(self.convert)

        self.show()


    def convert(self):
        try:
            result = str()
            assert self.txt_input.toPlainText() != "", "Input cannot be empty"
            number = int(self.txt_input.toPlainText(), base=self.combo_input_base.currentData())
        except Exception as err:
            msgbox = QMessageBox()
            msgbox.setWindowTitle(["Empty Input", "Invalid Input"][err.__class__.__name__ == "ValueError"])
            msgbox.setText(f"{err}")
            msgbox.setStyleSheet("""
                QMessageBox {
                    background-color: grey;
                    font-family: Arial;
                    font-size: 15pt;
                }
            """)
            msgbox.exec()
        else:
            base = self.combo_output_base.currentData()
            
            if base == 2:
                result = bin(number)[2:]
            elif base == 8:
                result = oct(number)[2:]
            elif base == 10:
                result = str(number)
            elif base == 16:
                result = hex(number)[2:]
        finally:
            self.txt_output.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = Window()

    sys.exit(app.exec())