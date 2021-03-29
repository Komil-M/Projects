"""

@Author Komil Mamasaliev

Description : A music player, it is what it is.

"""
from tkinter import *
import playsound
import threading
import time
import pygame

pygame.init()
pygame.mixer.init()


variable = "NULL"


def song_selection(value):
    global variable
    variable = value

    if variable == 0:
        song_shower.set("Selected: Migos - T-shirt")

    if variable == 1:
        song_shower.set("Selected: Saint Jhn")


def stop_song():
    pygame.mixer.music.stop()
    song_shower.set("Music Stopped")

def pause_song():
    pygame.mixer.music.pause()
    song_shower.set("Music Paused")

def unpause_song():
    pygame.mixer.music.unpause()
    song_shower.set("Music Un-paused")


def song():  # The songs

    song_list = [r"C:\Users\Komil\Desktop\Project for December\Migos - T-Shirt (Culture).mp3",
                 r"C:\Users\Komil\Desktop\Project for December\SAINt JHN - TRAP (Quarantine Live).mp3",
                 r"C:\Users\Komil\Desktop\Project for December\Alone.mp3"]


    try:
        if variable == "NULL":
            song_shower.set("Song not selected")

        if variable == 0:
            song_shower.set("Playing: Migos - T-shirt")

        if variable == 1:
            song_shower.set("Playing: Saint Jhn")
        music_choice = int(variable)
        selected_music = song_list[music_choice]

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(selected_music)
        pygame.mixer.music.play()
    except:
        print("Variable error most likely xd")


"""
def counter():  # Counter for the songs
    x = 1
    while x != 250:
        time.sleep(1)
        print(x)
        x = x + 1
"""

# def main():  # Threading to play the song and the counter.
    # threading.Thread(target=song, args=("1")).start()
    # threading.Thread(target=song, args=("2")).start()
    # threading.Thread(target=counter, args=()).start()


root = Tk()

""" Geometry of the window """
root.geometry("500x200")
root.resizable(0, 0)  # Fix the size
root.pack_propagate(0)  # Setting the size to not move after packing
root.title("Music player")

""" Declaring the variables """
song_shower = StringVar()
PLAY = StringVar()
song0 = StringVar()
song1 = StringVar()

""" Setting the variables """
song_shower.set("Please select a song")
PLAY.set("PLAY")
song0.set("Migos")
song1.set("Saint")


""" Creating the stuFF """
label1 = Label(root, width=30, font=("Arial", 20), textvariable=song_shower)
label1.pack()


Button_song_play = Button(root, width=8,height=1, font=("Arial", 10), text='PLAY', command=song, background="green")
Button_song_play.pack()

Button_song_stop = Button(root, width=8,height=1, font=("Arial", 10), text='STOP', command=stop_song, background="green")
Button_song_stop.pack()

Button_song_play = Button(root, width=8,height=1, font=("Arial", 10), text='PAUSE', command=pause_song, background="green")
Button_song_play.pack()

Button_song_stop = Button(root, width=8,height=1, font=("Arial", 10), text='UNPAUSE', command=unpause_song, background="green")
Button_song_stop.pack()

Button_song_migos = Button(root, width=4,height=1, font=("Arial", ), text='Migos', command=lambda *args: song_selection(0), background="green")
Button_song_migos.place(x=100, y=100)

Button_song_saint = Button(root, width=4,height=1, font=("Arial", ), text='saint', command=lambda *args: song_selection(1), background="green")
Button_song_saint.place(x=150, y=100)


root.mainloop()
