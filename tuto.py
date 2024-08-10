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
    
    def display_colour(self):
        if self.colour != None:
            return self.colour
        else:
            return "空"
    
    def set_colour(self, colour):
        self.colour = colour
        
colours = ['红色', '橘色', '黄色', '绿色', '青色', '蓝色', '紫色', '粉色', '玫红', '咖色']
    
def main():
    
    blocks = [[Tuto(), Tuto(), Tuto()], 
              [Tuto(), Tuto(), Tuto()], 
              [Tuto(), Tuto(), Tuto()]]

    draws = input("今天要抽多少个呀~")
    draws = int(draws)
    drawed = 0
    colour_want = input("选个颜色吧\n1.红色\n2.橘色\n3.黄色\n4.绿色\n5.青色\n6.蓝色\n7.紫色\n8.粉色\n9.玫红\n10.咖色")
    if colour_want == 1:
        colour_want = '红色'
    elif colour_want == 2:
        colour_want = '橘色'
    elif colour_want == 3:
        colour_want = '黄色'
    elif colour_want == 4:
        colour_want = '绿色'
    elif colour_want == 5:
        colour_want = '青色'
    elif colour_want == 6:
        colour_want = '蓝色'
    elif colour_want == 7:
        colour_want = '紫色'
    elif colour_want == 8:
        colour_want = '粉色'
    elif colour_want == 9:
        colour_want = '玫红'
    elif colour_want == 10:
        colour_want = '咖色'
    
    game = True
    while game:
        print("draws: " + str(draws))
        full = False
        done = False
        for i in range(3):
            for j in range(3):
                if blocks[i][j].colour == '':
                    new_colour = random.choice(colours)
                    blocks[i][j].set_colour(new_colour)
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
            if (blocks[0][2].colour == blocks[1][1].colour and blocks[1][1].colour == blocks[2][0].colour and blocks[0][2].colour != ''):
                draws += 5
                print("叮叮叮！连成斜线加五个！")
                blocks[0][2].set_colour('')
                blocks[1][1].set_colour('')
                blocks[2][0].set_colour('')
            for i in row_to_clear:
                blocks[i][0].set_colour('')
                blocks[i][1].set_colour('')
                blocks[i][2].set_colour('')
            for j in col_to_clear:
                blocks[0][j].set_colour('')
                blocks[1][j].set_colour('')
                blocks[2][j].set_colour('')
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
                            print(extra_tuto.colour + '碰！')
                            draws += 1
                
            
        input("continue") 
        
        if draws == 0:
            break
        
main()