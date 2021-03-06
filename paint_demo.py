from Tkinter import *

b1 = "up"
xold, yold = None, None
color = 'black'
size = 2

def main():
    root = Tk()
    colors = ['black', 'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'white']
    for i in range(len(colors)):
        btn = Button(root, command=lambda c=colors[i]:changeColor(c), width=2,
                     bg=colors[i], activebackground=colors[i])
        btn.grid(row=i/4, column=96+i%4, sticky=E+W)
    for i in range(4):
        Button(root,command=lambda s=i*2:changeSize(s),width=2).grid(row=3, column=96+i%4, sticky=E+W)
    drawing_area = Canvas(root, width=400, height=300, bg='white')
    drawing_area.grid(row=2, column=0, columnspan=100);
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)
    root.mainloop()

def changeColor(c):
    global color
    color = c

def changeSize(s):
    global size
    size = s

def b1down(event):
    global b1
    b1 = "down"

def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None
    yold = None

def motion(event):
    if b1 == "down":
        global xold, yold
        if xold is not None and yold is not None:
            event.widget.create_line(xold, yold-size/2, event.x, event.y-size/2, fill=color, width=size, smooth=TRUE)
        xold = event.x
        yold = event.y

if __name__ == "__main__":
    main()
