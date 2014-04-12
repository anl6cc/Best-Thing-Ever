from Tkinter import *

b1 = "up"
xold, yold = None, None
color = 'black'

def main():
    root = Tk()
#    Label(bg='#234').grid(row=1,column=1)
    btn = Button(root,text="     ",command=black,bg='black',activebackground='black').grid(row=1,column=1)
 #   btn.configure(bg='blue')
    Button(root,text="Red",command=red).grid(row=1,column=2)
    Button(root,text="Blue",command=blue).grid(row=1,column=3)
    Button(root,text="Green",command=green).grid(row=1,column=4)
    Button(root,text="Yellow",command=yellow).grid(row=2,column=1)
    Button(root,text="Orange",command=orange).grid(row=2,column=2)
    Button(root,text="Purple",command=purple).grid(row=2,column=3)
    Button(root,text="Eraser",command=white).grid(row=2,column=4)
    drawing_area = Canvas(root)
    drawing_area.grid(row=3,column=1,columnspan=4,rowspan=4);
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)
    root.mainloop()

def black():
    global color
    color = 'black'

def red():
    global color
    color = 'red'

def blue():
    global color
    color = 'blue'

def green():
    global color
    color = 'green'

def yellow():
    global color
    color = 'yellow'

def orange():
    global color
    color = 'orange'

def purple():
    global color
    color = 'purple'

def white():
    global color
    color = 'white'

def changeColor(c):
    global color
    print(c);
    color = c
    print(color);

def b1down(event):
    global b1
    b1 = "down"           # you only want to draw when the button is down
                          # because "Motion" events happen -all the time-

def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None           # reset the line when you let go of the button
    yold = None

def motion(event):
    if b1 == "down":
        global xold, yold
        if xold is not None and yold is not None:
            event.widget.create_line(xold,yold,event.x,event.y,fill=color,smooth=TRUE)
                          # here's where you draw it. smooth. neat.
        xold = event.x
        yold = event.y

if __name__ == "__main__":
    main()
