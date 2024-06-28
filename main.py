from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
import requests
from PyQt5.QtGui import QFont, QFontDatabase
import json
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("My First PyQt App")
main_window.resize(300, 200)

master_layout = QVBoxLayout()
QFontDatabase.addApplicationFont("Poppins-Regular.ttf")
poppins = QFont("Poppins")
# Functions
def truth():
    reponse = requests.get("https://api.truthordarebot.xyz/v1/truth")
    r = reponse.json()
    question = r['question']
    text1.setText(f"Truth : {question}")
    text2.setText("")
    text3.setText("")
  
def dare():
    reponse = requests.get("https://api.truthordarebot.xyz/v1/dare")
    r = reponse.json()
    question = r['question']
    text1.setText(f"Dare : {question}")
    text2.setText("")
    text3.setText("")    
#------------------
# Rows
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
# ---------
title = QLabel(text="Truth Or Dare")
title_font = QFont()
title_font.setPointSize(20)
title_font.setFamily("Poppins")
title_font.setWeight(QFont.Bold)
title.setFont(title_font)

# Buttons
button1 = QPushButton("Truth")
button2 = QPushButton("Dare")
# ---------

# Texts

text1 = QLabel("")
text2 = QLabel("")
text3 = QLabel("")
# ---------

# Calls
button1.clicked.connect(truth)
button2.clicked.connect(dare)
# ---------

# Add Wid
row1.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)
row3.addWidget(button1)
row3.addWidget(button2)

# ---------

# Add Layout
master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)
main_window.setLayout(master_layout)
# -----------

dark_style_sheet = """
    QWidget {
        background-color: #2e2e2e;
        color: #ffffff;
    }
    QLabel {
        color: #ffffff;
        font-family: "Poppins";
    }
    QPushButton {
        background-color: #444444;
        color: #ffffff;
        border: 1px solid #555555;
        padding: 5px;
        border-radius: 10px;
        font-family: "Poppins";
    }
    QPushButton:hover {
        background-color: #121212;
        
    }
"""

main_window.setStyleSheet(dark_style_sheet)
main_window.show()
app.exec_()
