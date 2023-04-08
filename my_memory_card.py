from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

app = QApplication([])#создание оконного приложения
main_win = QWidget()#основное окно
main_win.current_question = -1

#class
class Question():
    def __init__(self,question,right_answer,answer1,answer2,answer3):
        self.question = question
        self.right_answer = right_answer
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3

#list Question
question_list = [Question('какое число делится на 5?','5','11','17','19'),Question('какое число не делится на 5?','11','5','20','110')]


#виджеты
rGroup = QButtonGroup()
answord1 = QRadioButton("Португальский")#кнопка выбора
answord2 = QRadioButton("Испанский")#кнопка выбора
answord3 = QRadioButton("Итальянский")#кнопка выбора
answord4 = QRadioButton("Бразильский")#кнопка выбора
answer = [answord1, answord2, answord3, answord4]
rGroup.addButton(answord1)
rGroup.addButton(answord2)
rGroup.addButton(answord3)
rGroup.addButton(answord4)
answer_push = QPushButton("Ответить")#кнопка ответа
box = QGroupBox("Варианты ответов")#бокс
question = QLabel("Государственный язык Бразилии")#надпись в боксе
box_ans_str = QLabel("Правильно/неправильно")#хрень в боксе
box_answer = QGroupBox("Результат теста")
box_answer_layout = QVBoxLayout()
box_answer.setLayout(box_answer_layout)

#лайны
layout_main = QVBoxLayout()#главная вертикальная линия main_win
question_layout = QHBoxLayout()#гор. линия для вопроса
answord12 = QVBoxLayout()#гор. линия для вариантов ответа
answord34 = QVBoxLayout()#гор. линия для вариантов ответа
layout_box_main = QHBoxLayout()#линиия на main_win для бокса
layout_box = QHBoxLayout()#линия в боксе для answord12 и 34
answord_layout = QHBoxLayout()#линия для кнопки ответить
layout_box_answer = QVBoxLayout()



#крепление лайнов и виджетов на лайны
question_layout.addWidget(question)#question на question_layout
answord12.addWidget(answord1)#answord1 на линию answord12
answord12.addWidget(answord2)#answord2 на линию answord12
answord34.addWidget(answord3)#answord3 на линию answord34
answord34.addWidget(answord4)#answord4 на линию answord34
box_answer_layout.addWidget(box_ans_str)
answord_layout.addWidget(answer_push)#PushButton на линию answord_layout
box.setLayout(layout_box)#вставка layout_box в box
layout_box.addLayout(answord12)#answord12 в box
layout_box.addLayout(answord34)#answord34 в box
layout_box_main.addWidget(box)#box на layout_box_main
layout_box_main.addWidget(box_answer)
box_answer.hide()


#крепление лайнов на основной лайн

layout_main.addLayout(question_layout)#question_layout на layout_main
layout_main.addLayout(layout_box_main)#layout_box_main на layout_main
layout_main.addLayout(answord_layout)#answord_layout на layout_main

def show_result():
    box.hide()
    box_answer.show()
    answer_push.setText("Следующий вопрос")

#Мифически неонятная хрень
def ask(q):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.answer1)
    answer[2].setText(q.answer2)
    answer[3].setText(q.answer3)
    question.setText(q.question)
    show_question()

def check_answer():
    if answer[0].isChecked():
       show_correct(True)
    else:
        show_correct(False)

def next_question():
    main_win.current_question += 1
    if main_win.current_question > len(question_list):
        main_win.current_question = 0
    ask(question_list[main_win.current_question])

def show_correct(res):
    box_ans_str.setText(str(res))
    show_result()

def show_question():
    box.show()
    box_answer.hide()
    answer_push.setText("Ответить")
    rGroup.setExclusive(False)
    answord1.setChecked(False)
    answord2.setChecked(False)
    answord3.setChecked(False)
    answord4.setChecked(False)
    rGroup.setExclusive(True)

def click_ok():
    if answer_push.text() == 'Ответить':
        check_answer()
    else:
        next_question()


    
#Мифически понятная хрень

answer_push.clicked.connect(click_ok)
#конец
main_win.setLayout(layout_main)#прикрепление главной линии на экран приложения
main_win.show()#показать экран приложения
app.exec_()#не закрывать приложение, пока не нажат крестик