import tkinter as tk
 
calc = tk.Tk()
calc.title("Calculator")
calc.geometry("300x300")
 
def func(event):
    result = eval(tk.Entry.get(display))
    display.delete(0,tk.END)  # 내용 삭제
    display.insert(0,result)  # 새 값 입력
 
display = tk.Entry(calc, width=20)
display.pack()
 
calc.bind('<Return>', func)
 
calc.mainloop()
