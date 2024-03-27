from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
        
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        ''' окно, в котором проводится опрос '''
        super().__init__()
        self.exp = exp
        # создаём и настраиваем графические элелементы:
        self.initUI()
        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        # старт:
        self.show()
       

    def initUI(self):
        ''' создает графические элементы '''
        self.workh_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)         
        self.setLayout(self.layout_line)

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def results(self):
        self.index = (4 * (self.exp.p1 + self.exp.p2 + self.exp.p3) - 200) / 10
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index >= 11:
                return txt_res2
            elif self.index >= 6:
                return txt_res3
            elif self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5
        elif self.exp.age >= 13:
            if self.index >= 16.5:
                return txt_res1
            elif self.index >= 12.5:
                return txt_res2
            elif self.index >= 7.5:
                return txt_res3
            elif self.index >= 2:
                return txt_res4
            else:
                return txt_res5
        elif self.exp.age >= 11:
            if self.index >= 18:
                return txt_res1
            elif self.index >= 14:
                return txt_res2
            elif self.index >= 9:
                return txt_res3
            elif self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        elif self.exp.age >= 9:
            if self.index >= 19.5:
                return txt_res1
            elif self.index >= 15.5:
                return txt_res2
            elif self.index >= 10.5:
                return txt_res3
            elif self.index >= 5:
                return txt_res4
            else:
                return txt_res5
        else:
            if self.index >= 21:
                return txt_res1
            elif self.index >= 17:
                return txt_res2
            elif self.index >= 12:
                return txt_res3
            elif self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
