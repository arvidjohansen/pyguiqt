from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg

from pprint import pprint as p 


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #title
        self.setWindowTitle('Tittel Yo')
        
        #set vertical layout
        self.setLayout(qtw.QVBoxLayout())
        
        #create label
        label1 = qtw.QLabel('Hei test')
        #label font size
        label1.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(label1)

        #create entry box
        entry1 = qtw.QLineEdit()
        entry1.setObjectName('name_field')
        entry1.setText('')
        self.layout().addWidget(entry1)

        #create button
        button = qtw.QPushButton(
            'Trykk her',
            clicked = lambda: press_it()
        )
        self.layout().addWidget(button)

        
        self.show()
        def press_it():
            #add name to label
            label1.setText(f'Hei {entry1.text()}')
            #clear entry box
            entry1.setText('')



app = qtw.QApplication([])

mw = MainWindow()

app.exec_()
