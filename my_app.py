import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


app = QApplication([])
window = QWidget()
window.resize(300, 300)
window.move(400, 300)

v = QVBoxLayout()
label1 = QLabel('')
label2 = QLabel('')
label1.setText('Добро пожаловать в программу по определеню состояния здоровья!')
message = """ Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.
Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца
при физической нагрузке.
У испытуемого, находящего в положении лежа на спине в течении 5 мин., определяют частоту пульса за 15 секунд;
затем в течении 45 секунд испытукмый выполняет 30 приседаний.
после окончания нагрузки испытуемый ложится, и у него внось подсчитывается число пульсаций за первые 15 секунд,
а потом - за последние 15 секунд первой минты периода восстановления.
Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в ушах,
сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.
"""
label2.setText(message)
button = QPushButton('Начать')
v.addWidget(label1, alignment=Qt.AlignCenter)
v.addWidget(label2, alignment=Qt.AlignLeft|Qt.AlignVCenter)
v.addWidget(button, alignment=Qt.AlignCenter)
window.setLayout(v)

window.show()
sys.exit(app.exec_())
