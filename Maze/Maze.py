from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import time


def back_end(my_dir):
    def check_wall(x, y):
        print('checking for path', x, y)
        pos = map[x][y]
        print('pos', pos)
        if pos is 0:
            return 1
        else:
            return 0

    # code for array i.e. Map for maze
    map = (
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        (0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1),
        (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1),
        (1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1),
        (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1),
        (1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1),
        (1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1),
        (1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1),
        (1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1),
        (1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1),
        (1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1),
        (1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1),
        (1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1),
        (1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    )  # key for this map 'dssdsdwddwawddssdssawaassawassdsddwddwdssd'
    print(map[0], [0])
    # correct for the destination
    ans_key = 'ds'#sds'
    global i, permission
    global your_path
    global old_dir
    global x, y
    global x1, y1
    print('Your chance no.: ', i)
    print('Your current position: ', x, y)
    print('Your Path: ' + your_path)
    print('Old dir: ' + old_dir)
    print(my_dir)
    dir = my_dir
    print(old_dir, x1, y1)
    if dir is 'd':
        path = check_wall(x, y + 1)
        if path == 1:
            if i == 1:
                y += 1
                x1 += 58
                canvas.create_image(x - 58 if old_dir == 'a' else x1 - 29, y1,
                                    image=white if old_dir == 'a' else red)
                canvas.update()
                time.sleep(0.5)
                canvas.create_image(x1 - 29 if old_dir == 'a' else x1, y1, image=white if old_dir == 'a' else red)
            else:
                y += 2
                x1 += 58
                canvas.create_image(x1 - 58 if old_dir == 'a' else x1 - 29, y1, image=white if old_dir == 'a' else red)
                canvas.update()
                time.sleep(0.5)
                canvas.create_image(x1 - 29 if old_dir == 'a' else x1, y1, image=white if old_dir == 'a' else red)
    if dir is 'w':
        path = check_wall(x - 1, y)
        if path == 1:
            x -= 2
            y1 -= 58
            canvas.create_image(x1, y1 + 58 if old_dir == 's' else y1 + 29, image=white if old_dir == 's' else red)
            canvas.update()
            time.sleep(0.5)
            canvas.create_image(x1, y1 + 29 if old_dir == 's' else y1, image=white if old_dir == 's' else red)
    if dir is 'a':
        path = check_wall(x, y - 1)
        if path == 1:
            y -= 2
            x1 -= 58
            canvas.create_image(x1 + 58 if old_dir == 'd' else x1 + 29, y1, image=white if old_dir == 'd' else red)
            canvas.update()
            time.sleep(0.5)
            canvas.create_image(x1 + 29 if old_dir == 'd' else x1, y1, image=white if old_dir == 'd' else red)
    if dir is 's':
        path = check_wall(x + 1, y)
        if path == 1:
            x += 2
            y1 += 58
            canvas.create_image(x1, y1 - 58 if old_dir == 'w' else y1 - 29, image=white if old_dir == 'w' else red)
            canvas.update()
            time.sleep(0.5)
            canvas.create_image(x1, y1 - 29 if old_dir == 'w' else y1, image=white if old_dir == 'w' else red)
    i += 1
    print('Value of path', path)
    if path == 0: i -= 1
    if (old_dir == 'w' and dir == 's') or (old_dir == 's' and dir == 'w') or (old_dir == 'a' and dir == 'd') or (
            old_dir == 'd' and dir == 'a'):
        your_path = your_path[:-1]
    else:
        if path == 1:
            your_path = your_path + dir
    print('length of your_path: ', len(your_path))
    if len(your_path) != 0: old_dir = your_path[len(your_path) - 1]
    if your_path == ans_key:
        permission = messagebox.askyesno("Python", "Congratulations!!! You Won.\nDo you want to play again?")
    if i > 52:
        permission = messagebox.askyesno("Python", "Sorry, You are out of chances.\nDo you want to try again?")
    if permission == True:
        #        new_canvas()
        # print('debug 1')
        # canvas.create_image(250, 150, anchor=NW, image=map_1)
        main1()
        print(permission)
    global flag
    flag ='N'
    print('Flag: '+flag)
    canvas.create_rectangle(60, 320, 190, 405, fill='white')
    canvas.create_text(125, 365, text=53 - i, font='Fixedsys 70', fill='#353535')


# def new_canvas():
#    global i,x,y,x1,y1,your_path,old_dir
#    i = 1
#    x, y = 1, 0
#    x1, y1 = 237, 193
#    your_path = ''
#    old_dir = ''
#    canvas.pack()
#    canvas.create_image(250, 150, anchor=NW, image=map)
#    canvas.create_image(236, 193, image=red)
#    canvas.create_text(145, 470, text='Chances \n Left', font='Courier 30 bold', fill='#00044C')
#    canvas.create_text(125, 365, text=52, font='Fixedsys 70', fill='#353535')
#    canvas.create_rectangle(60, 320, 190, 405, fill='white')

def main1():
    global root, i, x, y, x1, y1, your_path, old_dir, permission

    permission = False
    i = 1
    x, y = 1, 0
    x1, y1 = 237, 193
    your_path = ''
    old_dir = ''
    global red
    red = PhotoImage(file="red_dot.png")

def main():
    global root, i, x, y, x1, y1, your_path, old_dir, permission

    permission = False
    i = 1
    x, y = 1, 0
    x1, y1 = 237, 193
    your_path = ''
    old_dir = ''
    print('flag: '+flag)
    if flag=='Y':root = Tk()
    root.title('Maze')
    root.geometry('1000x1000')
    root.maxsize(1000, 1000)
    root.minsize(1000, 1000)
    root.iconbitmap('maze.ico')
    print('debug 2')
    global map_1
    if flag == 'Y':
        map_1 = Image.open('Map.PNG')
        map_1 = map_1.resize((500, 500), Image.ANTIALIAS)
        map_1 = ImageTk.PhotoImage(map_1)
    print('debug 3')
    global canvas
    canvas = Canvas(root, width=1000, height=1000)
    print('debug 4')
    canvas.pack()
    print('debug 5')
    canvas.create_image(250, 150, anchor=NW, image=map_1)
    global red
    red = PhotoImage(file="red_dot.png")

    global white
    white = PhotoImage(file="white_dot.png")
    canvas.create_rectangle(221, 183, 241, 203, fill='#40E0D0', outline='white')
    canvas.create_text(145, 470, text='Chances \n Left', font='Courier 30 bold', fill='#00044C')
    canvas.create_rectangle(60, 320, 190, 405, fill='white')
    canvas.create_text(125, 365, text=52, font='Fixedsys 70', fill='#353535')

    up_btn = Button(root, text="UP", command=lambda: back_end('w'))
    down_btn = Button(root, text="DOWN", command=lambda: back_end('s'))
    left_btn = Button(root, text="LEFT", command=lambda: back_end('a'))
    right_btn = Button(root, text="RIGHT", command=lambda: back_end('d'))

    up_btn.place(x=450, y=670, width=100, height=50)
    down_btn.place(x=450, y=760, width=100, height=50)
    right_btn.place(x=570, y=715, width=100, height=50)
    left_btn.place(x=330, y=715, width=100, height=50)
    if flag == 'Y': root.mainloop()

global flag
flag = 'Y'
main()
