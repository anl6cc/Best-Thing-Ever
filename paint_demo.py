from Tkinter import *

b1 = "up"
xold, yold = None, None
color = 'blue'

def main():
    root = Tk()
    root.button = Button(root,text="Red",command=red)
    root.button.pack(side="top")
    root.button = Button(root,text="Black",command=black)
    root.button.pack(side="top")
    drawing_area = Canvas(root)
    drawing_area.pack()
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)
    root.mainloop()

def red():
    print("LOL")
    color = 'red'

def black():
    color = 'black'

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
