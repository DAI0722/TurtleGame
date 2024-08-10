from tkinter import *
import random
import time

root = Tk()
root.title("Tuto Game")

block_image = PhotoImage(file="./block.png")
green_tuto_image = PhotoImage(file="./tudo_green.png")

views = [[Label(root, image=block_image), Label(root, image=block_image), Label(root, image=block_image)],
         [Label(root, image=block_image), Label(root, image=block_image), Label(root, image=block_image)],
         [Label(root, image=block_image), Label(root, image=block_image), Label(root, image=block_image)]]

class Tuto(object):
    def __init__(self, colour=''):
        self.colour = colour
        self.up = None
        self.down = None
        self.left = None
        self.right = None
    
    def display_colour(self):
        if self.colour != None:
            return self.colour
        else:
            return "空"
    
    def set_colour(self, colour):
        self.colour = colour

tuto_dic = {'红色':green_tuto_image, 
            '橘色':green_tuto_image,
            '黄色':green_tuto_image,
            '绿色':green_tuto_image,
            '青色':green_tuto_image,
            '蓝色':green_tuto_image,
            '紫色':green_tuto_image,
            '粉色':green_tuto_image,
            '玫红':green_tuto_image,
            '咖色':green_tuto_image,
            '':block_image}

colours = ['红色', '橘色', '黄色', '绿色', '青色', '蓝色', '紫色', '粉色', '玫红', '咖色']

def view_set_colour(row:int, col:int, colour:str):
    views[row][col].destroy()
    
    tuto_img = tuto_dic[colour]
    views[row][col] = Label(root, image=tuto_img)
    views[row][col].grid(row=row, column=col)

def game(draw:int, colour_chosen:int):
    
    blocks = [[Tuto(), Tuto(), Tuto()], 
              [Tuto(), Tuto(), Tuto()], 
              [Tuto(), Tuto(), Tuto()]]

    draws = draw
    drawed = 0
    colour_want = ''
    if colour_chosen == 1:
        colour_want = '红色'
    elif colour_chosen == 2:
        colour_want = '橘色'
    elif colour_chosen == 3:
        colour_want = '黄色'
    elif colour_chosen == 4:
        colour_want = '绿色'
    elif colour_chosen == 5:
        colour_want = '青色'
    elif colour_chosen == 6:
        colour_want = '蓝色'
    elif colour_chosen == 7:
        colour_want = '紫色'
    elif colour_chosen == 8:
        colour_want = '粉色'
    elif colour_chosen == 9:
        colour_want = '玫红'
    elif colour_chosen == 10:
        colour_want = '咖色'
        
    while True:
        if draws <= 0:
            break
        print("draws: " + str(draws))
        full = False
        done = False
        for i in range(3):
            for j in range(3):
                if blocks[i][j].colour == '':
                    new_colour = random.choice(colours)
                    blocks[i][j].set_colour(new_colour)
                    view_set_colour(i, j, new_colour)
                    if new_colour == colour_want:
                        draw += 1
                        print("叮叮！抽到心仪颜色加拆一个")
                    done = True
                    draws -= 1
                    drawed += 1
                    break
            if done:
                break
        if not done:
            full = True
            
        for i in range(3):
            print(blocks[i][0].display_colour() + "\t" + blocks[i][1].display_colour() + "\t" + blocks[i][2].display_colour())
        print("\n")
        time.sleep(0.5)
        
        if full or draws == 0:
            print("full\n")
            row_to_clear = list()
            col_to_clear = list()
            for i in range(3):
                if (blocks[i][0].colour == blocks[i][1].colour and blocks[i][1].colour == blocks[i][2].colour and blocks[i][0].colour != ''):
                    row_to_clear.append(i)
                    draws += 5
                    print("叮叮叮！连成一行加五个！")
            for i in range(3):
                if (blocks[0][i].colour == blocks[1][i].colour and blocks[1][i].colour == blocks[2][i].colour and blocks[0][i].colour != ''):
                    col_to_clear.append(i)
                    draws += 5
                    print("叮叮叮！连成一列加五个！")
            if (blocks[0][0].colour == blocks[1][1].colour and blocks[1][1].colour == blocks[2][2].colour and blocks[0][0].colour != ''):
                draws += 5
                print("叮叮叮！连成斜线加五个！")
                blocks[0][0].set_colour('')
                blocks[1][1].set_colour('')
                blocks[2][2].set_colour('')
                view_set_colour(0, 0, '')
                view_set_colour(1, 1, '')
                view_set_colour(2, 2, '')
                
            if (blocks[0][2].colour == blocks[1][1].colour and blocks[1][1].colour == blocks[2][0].colour and blocks[0][2].colour != ''):
                draws += 5
                print("叮叮叮！连成斜线加五个！")
                blocks[0][2].set_colour('')
                blocks[1][1].set_colour('')
                blocks[2][0].set_colour('')
                view_set_colour(0, 2, '')
                view_set_colour(1, 1, '')
                view_set_colour(2, 0, '')
            for i in row_to_clear:
                blocks[i][0].set_colour('')
                blocks[i][1].set_colour('')
                blocks[i][2].set_colour('')
                view_set_colour(i, 0, '')
                view_set_colour(i, 1, '')
                view_set_colour(i, 2, '')
            for j in col_to_clear:
                blocks[0][j].set_colour('')
                blocks[1][j].set_colour('')
                blocks[2][j].set_colour('')
                view_set_colour(0, j, '')
                view_set_colour(1, j, '')
                view_set_colour(2, j, '')
            counts = dict()
            for c in colours:
                counts[c] = int(0)
            
            for i in range(3):
                for j in range(3):
                    colour = str(blocks[i][j].colour)
                    if colour != '':
                        counts[colour] +=1
            
            all_different = True
            for colour, count in counts.items():
                pairs = count//2
                pairs = int(pairs)
                if pairs >= 1:
                    print(colour + str(pairs) + '碰！')
                    all_different = False
                    to_remove = int(pairs*2)
                    for i in range(3):
                        done = False
                        for j in range(3):
                            if blocks[i][j].colour == colour:
                                blocks[i][j].set_colour('')
                                view_set_colour(i, j, '')
                                to_remove = to_remove - 1
                                if to_remove == 0:
                                    done = True
                                    break
            if all_different:
                print("全家福!加拆5个!")
                draws += 5
                extra_tuto = Tuto(random.choice(colours))
                drawed += 1
                for i in range(3):
                    done = False
                    for j in range(3):
                        if blocks[i][j].colour == extra_tuto.colour:
                            blocks[i][j].set_colour('')
                            view_set_colour(i, j, '')
                            print(extra_tuto.colour + '碰！')
                            draws += 1
                
            
        input("continue") 
        
        if draws == 0:
            break

def decide_draws():
    title_pic.grid_forget()
    title.grid_forget()
    start_btn.grid_forget()
    

    number_prompt.pack(pady=10)
    number_input.pack(padx=10, pady=10)
    next_btn.pack(pady=10)

def pick_colour():
    draws = int(number_input.get())
    number_prompt.pack_forget()
    number_input.pack_forget()
    next_btn.pack_forget()
    button1 = Button(root, image=green_tuto_image, text='1', command=lambda:start_game(button1))
    button2 = Button(root, image=green_tuto_image, text='2', command=lambda:start_game(button2))
    button3 = Button(root, image=green_tuto_image, text='3', command=lambda:start_game(button3))
    button4 = Button(root, image=green_tuto_image, text='4', command=lambda:start_game(button4))
    button5 = Button(root, image=green_tuto_image, text='5', command=lambda:start_game(button5))
    button6 = Button(root, image=green_tuto_image, text='6', command=lambda:start_game(button6))
    button7 = Button(root, image=green_tuto_image, text='7', command=lambda:start_game(button7))
    button8 = Button(root, image=green_tuto_image, text='8', command=lambda:start_game(button8))
    button9 = Button(root, image=green_tuto_image, text='9', command=lambda:start_game(button9))
    button0 = Button(root, image=green_tuto_image, text='0', command=lambda:start_game(button0))
    
    button1.grid(row=0, column=0, padx=5, pady=5)
    button2.grid(row=0, column=1, padx=5, pady=5)
    button3.grid(row=0, column=2, padx=5, pady=5)
    button4.grid(row=0, column=3, padx=5, pady=5)
    button5.grid(row=0, column=4, padx=5, pady=5)
    button6.grid(row=1, column=0, padx=5, pady=5)
    button7.grid(row=1, column=1, padx=5, pady=5)
    button8.grid(row=1, column=2, padx=5, pady=5)
    button9.grid(row=1, column=3, padx=5, pady=5)
    button0.grid(row=1, column=4, padx=5, pady=5)

def start_game(tuto_chosen):
    colour = tuto_chosen['text']
    for element in root.winfo_children():
        element.grid_forget()
    for i in range(3):
        for j in range(3):
            views[i][j].grid(row=i, column=j)
    print("starting game with " + str(int(number_input.get())) + " draws and " + str(colour) + "chosen")
    game(int(number_input.get()), colour)


title_pic = Label(root, image=green_tuto_image, padx=20, pady=20)
title = Label(root, text="Tuto Game!", padx=20)
start_btn = Button(root, text="Start!", padx=30, command=decide_draws)

number_prompt = Label(root, text="今天要抽几个呀~")
number_input = Entry(root)
next_btn = Button(root, text="确定", command=pick_colour)

title_pic.grid(row=0, column=0)
title.grid(row=1, column=0)
start_btn.grid(row=2, column=0)


root.mainloop()