from tkinter import *
import time
MBTI = [["E", "I"], ["S", "N"],
        ["T", "F"], ["J", "P"]]


def windowSetting():
    window.title("MBTI 검사기")
    window.geometry("400x400+100+100")
    window.resizable(width=True, height=True)


def start_menu():
    start = Label(window, text="MBTI 검사를 시작합니다.")
    b_start = Button(window, text="시작!",
                     command = (lambda: b_start.pack_forget(), lambda: problem_building(0, question[0], answer[0])))

    start.pack()
    b_start.pack()


def problem_building(i, question, answer):
    problem_number = Label(window, text="{}번째 문항".format(i))
    problem = Label(window, text=question)
    select_1 = Button(window, text=answer[0])
    select_2 = Button(window, text=answer[1])

    problem_number.pack()
    problem.pack()
    select_1.pack()
    select_2.pack()


def buildGUI():
    global question, answer
    question = ['q1' for _ in range(12)]
    answer = [('a1', 'a2') for _ in range(12)]
    start_menu()


window = Tk()
windowSetting()
buildGUI()
window.mainloop()


"""
tkinter를 이용한 MBTI test 윈도우 프로그래밍
과제는 2회에 걸쳐서 내면 될듯
"""
