from tkinter import *

def f_convert_CtoF():
    input_data = float(Entry.get(e_input_C))
    convert = (((input_data)* 9) / 5) + 32
    convert = convert * 100 // 1 / 100
    
    e_input_F.delete(0, END)    
    e_input_F.insert(0, convert)
    
def f_convert_FtoC():
    input_data = float(Entry.get(e_input_F))
    convert = ((input_data) -32) * 5 / 9
    convert = convert * 100 // 1 / 100
    
    e_input_C.delete(0, END)
    e_input_C.insert(0, convert)
     
def f_init():
    e_input_F.delete(0, END)
    e_input_C.delete(0, END)

def windowSetting():
    window.resizable(width = True, height = True)

def buildGUI():
    global e_input_F
    global e_input_C
    
    t_hwasi   = Label(window, text = "화씨")
    e_input_F = Entry(window, width = 10, bg = "light blue")
    t_subsi   = Label(window, text = "섭씨")
    e_input_C = Entry(window, width = 10, bg = "light blue")

    b_convert_FtoC = Button(window,
                            text = "화씨 -> 섭씨",
                            command = f_convert_FtoC)
    b_convert_CtoF = Button(window,
                            text = "섭씨 -> 화씨",
                            command = f_convert_CtoF)
    b_init = Button(window,
                    text = "초기화",
                    command = f_init )
    b_quit = Button(window,
                    text = "종료",
                    command = quit) 

    t_hwasi.pack()
    e_input_F.pack()
    t_subsi.pack()
    e_input_C.pack()
    b_convert_FtoC.pack()
    b_convert_CtoF.pack()
    b_init.pack()
    b_quit.pack()

window = Tk()
windowSetting()
buildGUI()
window.mainloop()
