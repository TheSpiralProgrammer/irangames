import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

url = 'https://raw.githubusercontent.com/TheSpiralProgrammer/irangames/main/irangames.py'
r = requests.get(url, allow_redirects=True)

open('irangames.py', 'wb').write(r.content)




    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(800,800)
    w.setWindowTitle("Iran Games")
    w.show()
    
    
    #btn = QPushButton(w)
    #btn.setText('...')
    #btn.move(110,150)
    #btn.show()
    #btn.clicked.connect(download1)
    
    label = QLabel(w)
    label.setText("وقتی برنامه را ری استارت میکنید آپدیت می شود!")
    label.move(250,0)
    label.show()
    
    label2 = QLabel(w)
    label2.setText("تست")
    label2.move(300,250)
    label2.show()
    
    qp = QPalette()
    qp.setColor(QPalette.ButtonText, Qt.black)
    qp.setColor(QPalette.Window, Qt.gray)
    qp.setColor(QPalette.Button, Qt.gray)
    app.setPalette(qp)

    
    
    sys.exit(app.exec_())

