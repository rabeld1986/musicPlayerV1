'''
Created on Sep 8, 2020

@author: rabel
'''
import tkinter
from MusicList import music_list
from tkinter import messagebox
from functools import partial
import sys

#create a window
root = tkinter.Tk()
#window size
root.geometry("300x400")
canvas = tkinter.Canvas(root, width = 500, height = 100)
canvas.pack()
root.wm_title("Music Player")

##function
global count 
count = 0.7
def vol_control_up(event = None):
    global count
    count += 0.1
    if count >= 1:
        count = 1
    mus_playlist.volume_up(count)
    print(count)
def vol_control_down(event = None):
    global count
    count -= 0.1
    if count <= 0:
        count = 0
    mus_playlist.volume_down(count)    
    print(count)
##music object

mus_playlist = music_list()
#path and song where the your music is
mus_playlist.add_song("stairway to heaven - led zeppelin", "C:\\Users\\rabel\\Pictures\\Camera Roll\\MyMusic")


##photos
note = tkinter.PhotoImage(file = "music_note.png")
canvas.create_image(150,70, image=note)

p_pic = tkinter.PhotoImage(file = "play-button.png")
canvas.create_image(135, 300, image = p_pic)

back_pic = tkinter.PhotoImage(file = "back_buttom.png")
canvas.create_image(60, 300, image = back_pic)

ff_pic = tkinter.PhotoImage(file = "ff_buttom.png")
canvas.create_image(190, 300, image = ff_pic)
###main buttoms

play_b = tkinter.Button(root, text = "Play", image = p_pic, command = mus_playlist.start)
play_b.pack()
play_b.place(x = 125, y = 300)

ff_b = tkinter.Button(root, text = "ff", image = ff_pic)
ff_b.pack()
ff_b.place(x = 190, y = 300)

back_b = tkinter.Button(root, text = "back", image = back_pic)
back_b.pack()
back_b.place(x = 60, y = 300)

scrollbar = tkinter.Scrollbar(root)
scrollbar.pack( side = tkinter.RIGHT, fill = tkinter.Y )
scrollbar.pack()
scrollbar.place(x = 70, y = 150)

song_list = tkinter.Listbox(root, height = 5, yscrollcommand = scrollbar.set)
song_list.insert(0,mus_playlist.get_name())
song_list.pack()
song_list.place(x = 90, y = 150)

scrollbar.config(command = song_list.yview)

vol_up = tkinter.Button(root, text = "+", command = vol_control_up)
vol_up.pack()
vol_up.place(x = 200, y = 360)

vol_down = tkinter.Button(root, text = "-", command = vol_control_down)
vol_down.pack()
vol_down.place(x = 170, y = 360)

##volume control

##label showing the song info
song_info = tkinter.Label(root, text = mus_playlist.get_name() + " - " +mus_playlist.get_artist(), font='Helvetica 9 bold')
song_info.pack()
song_info.place(x = 50,y = 270)

vol_label = tkinter.Label(root,text = "Volume ", font = 'TimesNewRoman 8 bold')
vol_label.pack()
vol_label.place(x = 110, y = 365 )
##asks whether you want to exit the window

def ask_exit():
    if tkinter.messagebox.askyesno(title = "Exit", message = "Are You Sure?"):
        root.destroy()
        stop_thread = True
    return stop_thread
        
root.protocol('WM_DELETE_WINDOW', ask_exit)


root.mainloop()
mus_playlist.join()



