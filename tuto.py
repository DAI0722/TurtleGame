from tkinter import *
import random
import time


class Tuto(object):
    def __init__(self, colour=''):
        self.colour = colour
        self.up = None
        self.down = None
        self.left = None
        self.right = None
    
    def colour(self):
        if self.colour != None:
            return self.colour
        else:
            return "None"
    
    def set_colour(self, colour):
        self.colour = colour
        
colour = ['red', 'blue', 'yellow', 'green', 'purple', 'pink', 'orange', 'coffee', 'rose', 'cyan']
    
def main():
    
    blocks = [[Tuto(), Tuto(), Tuto()], 
              [Tuto(), Tuto(), Tuto()], 
              [Tuto(), Tuto(), Tuto()]]

    draws = int(input("今天要抽多少个呀~"))
    drawed = 0
    colour_want = input("选个颜色吧\n1.红色\n2.橘色\n3.黄色\n4.绿色\n5.青色\n6.蓝色\n7.紫色\n8.粉色\n9.玫红\n10.咖色")
    if colour_want == 1:
        colour_want = 'red'
    elif colour_want == 2:
        colour_want = 'orange'
    elif colour_want == 3:
        colour_want = 'yellow'
    elif colour_want == 4:
        colour_want = 'green'
    elif colour_want == 5:
        colour_want = 'cyan'
    elif colour_want == 6:
        colour_want = 'blue'
    elif colour_want == 7:
        colour_want = 'purple'
    elif colour_want == 8:
        colour_want = 'pink'
    elif colour_want == 9:
        colour_want = 'rose'
    elif colour_want == 10:
        colour_want = 'coffee'
    
    game = True
    while game:
        full = False
        for i in range(3):
            done = False
            for j in range(3):
                if blocks[i][j].colour == '':
                    new_colour = random.choice(colour)
                    blocks[i][j].set_colour(new_colour)
                    if new_colour == colour_want:
                        draw += 1
                        print("叮叮！加拆一个")
                    done = True
                    draws = draws - 1
                    drawed = drawed + 1
                    break
            if done:
                break
            else:
                full = True
            
        for i in range(3):
            print(blocks[i][0].colour + "\t" + blocks[i][1].colour + "\t" + blocks[i][2].colour)
        print("\n")
        time.sleep(0.5)
        
        if full or draws == 0:
            row_to_clear = list()
            col_to_clear = list()
            for i in range(3):
                if (blocks[i][0].colour == blocks[i][1].colour and blocks[i][1].colour == blocks[i][2].colour):
                    row_to_clear.append(i)
                    draws += 5
                    print("叮叮叮！加五个！")
            for i in range(3):
                if (blocks[0][i].colour == blocks[1][i].colour and blocks[1][i].colour == blocks[2][i].colour):
                    col_to_clear.append(i)
                    draws += 5
                    print("叮叮叮！加五个！")
            for i in row_to_clear:
                blocks[i][0].set_colour('')
                blocks[i][1].set_colour('')
                blocks[i][2].set_colour('')
            for j in col_to_clear:
                blocks[0][j].set_colour('')
                blocks[1][j].set_colour('')
                blocks[2][j].set_colour('')
                    
        
        if draws == 0:
            break
        
main()