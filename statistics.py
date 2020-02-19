from Tix import Tk, Entry, Button, StringVar

from _tkinter import *
screen = Tk()

screen.title('ESHUN STATISTICS CALCULATOR')
screen.geometry('360x490')
def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

tex = StringVar()
operator=''

def AC():
    global operator
    operator= ''
    tex.set(operator)

def equal():
    global operator
    result = eval(operator)
    operator= str(result)
    tex.set(result)
    ###### work for all
def on_enter(e):
    btn7.configure(bg='red')
def on_leave(e):
    btn7.configure(bg='white')







def on_entryenter(e):
    btn7.configure(bg='red')
def on_entryleave(e):
    btn7.configure(bg='white')







entry1 = Entry(screen, bg='green', font=('yellow', 20, 'italic bold'),bd='20',justify='left',textvariable=tex)
entry1.grid(row=0, columnspan=4)


btn7 = Button(screen,text=' 7',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(7),
              activebackground='pink',activeforeground='blue',bg='powder blue' )
btn7.grid(row=1,column=0)
btn7.bind('<Enter>',on_enter)
btn7.bind('<Leave>',on_leave)

btn8=Button(screen, text='8', font=('yellow', 15, 'italic bold'), bd=8, padx=15, pady=15, command=lambda:click(8) )
btn8.grid(row=1,column=1)

btn9=Button(screen,text=' 9',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(9))
btn9.grid(row=1,column=2)

btnadd=Button(screen,text='+',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click('+'))
btnadd.grid(row=1,column=3)

btn4 = Button(screen,text='4',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(4))
btn4.grid(row=2,column=0)

btn5=Button(screen,text='5',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(5))
btn5.grid(row=2,column=1)

btn6=Button(screen,text='6',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(6))
btn6.grid(row=2,column=2)

btnsub=Button(screen,text='-',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click('-'))
btnsub.grid(row=2,column=3)


btn1 = Button(screen,text='1',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(1))
btn1.grid(row=3,column=0)

btn2=Button(screen,text='2',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(2))
btn2.grid(row=3,column=1)

btn3=Button(screen,text='3',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(3))
btn3.grid(row=3,column=2)

btnmul=Button(screen,text='x',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click('*'))
btnmul.grid(row=3,column=3)


btn0 = Button(screen,text='0',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(0))
btn0.grid(row=4,column=0)

btnAC=Button(screen,text='AC',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=AC)
btnAC.grid(row=4,column=1)

btnequal=Button(screen,text='=',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=equal)
btnequal.grid(row=4,column=2)

btndiv=Button(screen,text='/',font=('yellow',15,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click('/'))
btndiv.grid(row=4,column=3)



screen.mainloop()
###################################### work for all
entry1.bind('<Enter>',on_entryenter)
entry1.bind('<Enter>',on_entryleave)

btn7.bind('<Enter>',on_enter)
btn7.bind('<Enter>',on_leave)
## others here