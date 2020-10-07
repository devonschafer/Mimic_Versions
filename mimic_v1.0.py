from guizero import *
import random
import time
import keyboard
import mouse
import os
import pyautogui

#colors
black = 0, 0, 0
light_grey = 130, 130, 130
medium_grey = 100, 100, 100
medium_grey_1 = 70, 70, 70
medium_grey_2 = 60, 60, 60
dark_grey = 40, 40, 40
off_white = 255, 255, 240
green = 0, 200, 0
blue = 50, 115, 255
red = 255, 0, 0

#properties
appwidth = 780
appheight = 340
windowwidth = 780
windowheight = 340
textsize = 14
textcolor = blue
font = 'Helvetica'
buttonwidth = 10
buttonheight = 1
userinputwidth = 200
userinputheight = 306
textboxwidth = 50
textboxheight = 20
editlinewidth = 10

side = []
xx = []
yy = []
mm = []

def openreadme():
    openFile = open('in_game_readme.txt', 'r')
    readme.value = openFile.read()
    openFile.close()

def keep_time():
    if record.text == 'Stop Recording':
        mili_seconds.value = int(mili_seconds.value) + 1
        if mili_seconds.value == str(1000):
            mili_seconds.value = 0
            seconds.value = int(seconds.value) + 1
            if seconds.value == str(300):
                seconds.value = 0

def start_record():
    if record.text == 'Record':
        record.text = 'Stop Recording'
        record.bg = red
    elif record.text == 'Stop Recording':
        record.text = 'Record'
        mili_seconds.value = 0
        record.bg = dark_grey

def delete_one():
    selected = user_entry.value
    user_entry.remove(selected)
    entry_box.remove(selected)

def clear_all():
    user_entry.clear()
    side.clear()
    xx.clear()
    yy.clear()
    mm.clear()
    entry_box.clear()

def edit():
    edit_window.show()

def edit_selected():
    selected = entry_box.value
    a = entry_box.items
    line = a.index(selected)
    edit_side.value = side[line]
    edit_xx.value = xx[line]
    edit_yy.value = yy[line]
    edit_mm.value = mm[line]

def refresh():
    selected = entry_box.value
    a = entry_box.items
    line = a.index(selected)
    side.pop(line)
    xx.pop(line)
    yy.pop(line)
    mm.pop(line)
    side.insert(line, edit_side.value)
    xx.insert(line, int(edit_xx.value))
    yy.insert(line, int(edit_yy.value))
    mm.insert(line, float(edit_mm.value))
    entry_box.clear()
    for a in range(len(side)):
        entry_box.append('c:%s x:%s y:%s t:%s' % (side[a], xx[a], yy[a], mm[a]))
    
def done_edit():
    selected = entry_box.value
    a = entry_box.items
    line = a.index(selected)
    side.pop(line)
    xx.pop(line)
    yy.pop(line)
    mm.pop(line)
    side.insert(line, edit_side.value)
    xx.insert(line, int(edit_xx.value))
    yy.insert(line, int(edit_yy.value))
    mm.insert(line, float(edit_mm.value))
    user_entry.clear()
    entry_box.clear()
    for a in range(len(side)):
        user_entry.append('c:%s x:%s y:%s t:%s' % (side[a], xx[a], yy[a], mm[a]))
        entry_box.append('c:%s x:%s y:%s t:%s' % (side[a], xx[a], yy[a], mm[a]))
    edit_window.hide()
    
def mimic_record():
    m = mili_seconds.value
    s = seconds.value
    if record.text == 'Stop Recording':
        if mouse.is_pressed('left') == True:
            x, y = pyautogui.position()
            l = 'left'
            user_entry.append('c:%s x:%s y:%s t:%s.%s' % (l, x, y, s, m))
            entry_box.append('c:%s x:%s y:%s t:%s.%s' % (l, x, y, s, m))
            mili_seconds.value = 0
            seconds.value = 0
            side.append(l)
            xx.append(x)
            yy.append(y)
            mm.append('%s.%s' % (s, m))
        elif mouse.is_pressed('right') == True:
            x, y = pyautogui.position()
            r = 'right'
            user_entry.append('c:%s x:%s y:%s t:%s.%s' % (r, x, y, s, m))
            entry_box.append('c:%s x:%s y:%s t:%s.%s' % (r, x, y, s, m))
            mili_seconds.value = 0
            seconds.value = 0
            side.append(r)
            xx.append(x)
            yy.append(y)
            mm.append('%s.%s' % (s, m))
        elif keyboard.is_pressed('e'):
            mili_seconds.value = 0
            record.text = 'Record'
            record.bg = dark_grey
    else:
        None

def start_mimic():
    if start_stop.text == 'Start':
        start_stop.text = 'Stop Mimic'
        start_stop.bg = green
    elif start_stop.text == 'Stop Mimic':
        start_stop.text = 'Start'
        start_stop.bg = dark_grey

def mimic_begin():
    if start_stop.text == 'Stop Mimic':
        record.text = 'Record'
        record.bg = dark_grey
        pt = int(pixel_input.value)
        tt = float(time_input.value)
        for a in range(len(user_entry.items)):
            rando_pixel = random.randint(0, pt)
            rando_time = random.uniform(0.000, tt)
            wait = mm[a]
            wait_f = float(wait)
            wait_random = wait_f + rando_time
            xcoord = int(xx[a]) + rando_pixel
            ycoord = int(yy[a]) - rando_pixel
            LorR = side[a]
            pyautogui.moveTo(xcoord, ycoord)
            pyautogui.click(button=LorR)
            time.sleep(wait_random)
            if keyboard.is_pressed('r'):
                start_stop.text = 'Start'
                start_stop.bg = dark_grey
    else:
        None

main = App(title='Mimic V 1.0', width=appwidth, height=appheight, layout='grid', bg=black)

#second window stuff------------------------------------------------------------------------------------------
edit_window = Window(main, title='Edit Line', width=windowwidth, height=windowheight, layout='grid', bg=black)
edit_window.hide()

edit_box0 = Box(edit_window, layout='grid', grid=[0,0], border=10, align='top')
edit_box1 = Box(edit_window, layout='grid', grid=[1,0], border=10, align='top')
edit_box2 = Box(edit_window, layout='grid', grid=[2,0], border=10, align='top')

edit_button = PushButton(edit_box0, text='Edit', command=edit_selected, width=buttonwidth, height=buttonheight, grid=[0,0])
edit_button.bg = dark_grey
edit_button.text_color = off_white

refresh_button = PushButton(edit_box0, text='Refresh', command=refresh, width=buttonwidth, height=buttonheight, grid=[0,1])
refresh_button.bg = dark_grey
refresh_button.text_color = off_white

done_button = PushButton(edit_box0, text='Done', command=done_edit, width=buttonwidth, height=buttonheight, grid=[0,2])
done_button.bg = dark_grey
done_button.text_color = off_white

pixel_tolerance = Text(edit_box0, text='Pixel Tolerance', font=font, color=textcolor, grid=[0,3])

pixel_input = TextBox(edit_box0, text='5', command=None, width=editlinewidth, grid=[0,4])
pixel_input.bg = off_white

time_tolerance = Text(edit_box0, text='Time Tolerance', font=font, color=textcolor, grid=[0,5])

time_input = TextBox(edit_box0, text='.010', command=None, width=editlinewidth, grid=[0,6])
time_input.bg = off_white

entry_box = ListBox(edit_box1, items=[], command=None, width=userinputwidth, height=userinputheight, grid=[0,0])
entry_box.bg = off_white

edit_side = TextBox(edit_box2, text='', command=None, width=editlinewidth, grid=[0,0])
edit_side.bg = off_white

edit_xx = TextBox(edit_box2, text='', command=None, width=editlinewidth, grid=[1,0])
edit_xx.bg = off_white

edit_yy = TextBox(edit_box2, text='', command=None, width=editlinewidth, grid=[2,0])
edit_yy.bg = off_white

edit_mm = TextBox(edit_box2, text='', command=None, width=editlinewidth, grid=[3,0])
edit_mm.bg = off_white

#-------------------------------------------------------------------------------------------------------------

box0 = Box(main, layout='grid', grid=[0,0], border=10, align='top')
box01 = Box(box0, layout='grid', grid=[0,1], border=10, align='top')
box1 = Box(box0, layout='grid', grid=[0,2], border=10, align='top')
box2 = Box(main, layout='grid', grid=[1,0], border=10, align='top')
box3 = Box(main, layout='grid', grid=[2,0], border=10, align='top')

help_banner = Text(box0, text='Welcome to Mimic', size=textsize, color=textcolor, font=font, grid=[0,0])
help_banner.repeat(100, mimic_record)
help_banner.repeat(100, mimic_begin)

seconds = Text(box01, text='0', size=textsize, color=red, font=font, grid=[0,0], align='top')

mili_seconds = Text(box01, text='0', size=textsize, color=red, font=font, grid=[1,0], align='top')
mili_seconds.repeat(1, keep_time)

edit_line = PushButton(box1, text='Edit', command=edit, width=buttonwidth, height=buttonheight, grid=[0,2])
edit_line.bg = dark_grey
edit_line.text_color = off_white

delete = PushButton(box1, text='Delete One', command=delete_one, width=buttonwidth, height=buttonheight, grid=[0,3])
delete.bg = dark_grey
delete.text_color = off_white

clear = PushButton(box1, text='Clear All', command=clear_all, width=buttonwidth, height=buttonheight, grid=[0,4])
clear.bg = dark_grey
clear.text_color = off_white

record = PushButton(box1, text='Record', command=start_record, width=buttonwidth, height=buttonheight, grid=[0,5])
record.bg = dark_grey
record.text_color = off_white

start_stop = PushButton(box1, text='Start', command=start_mimic, width=buttonwidth, height=buttonheight, grid=[0,6])
start_stop.bg = dark_grey
start_stop.text_color = off_white

user_entry = ListBox(box2, items=[], command=None, width=userinputwidth, height=userinputheight, grid=[0,0])
user_entry.bg = off_white

readme = TextBox(box3, text='', command=None, multiline=True, scrollbar=True, width=textboxwidth, height=textboxheight, grid=[0,0])
readme.bg = off_white
readme.after(100, openreadme)



main.display()
