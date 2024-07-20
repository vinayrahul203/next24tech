# Importing necessary libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json
import requests

def extract_song_lyrics():
	global artist, song
	artist_name = str(artist.get()).lower()
	song_name = str(song.get()).lower() 
	link = "https://api.lyrics.ovh/v1/"+artist_name.replace(' ', '%20')+'/'+song_name.replace(' ', '%20')

	req = requests.get(link)
	json_data = json.loads(req.content)

	try:
		lyrics = json_data["lyrics"]
		print(lyrics)
		messagebox.showinfo("Success", "The lyrics to {} have been extracted and is visible in the terminal".format(song_name.upper()))

	except:
		messagebox.showerror("Error","The song you are looking for has not been found.Please ensure that your have given the Song Name and Artist Name correctly.")

#Window Intialization
window = Tk()
window.title("Lyric Extractor")
window.geometry("700x200")
window.resizable(0, 0)
window.configure(bg="black")

# Creating Labels and Entries
heading_label=tk.Label(window, text="Lyric Extractor", font=("Algerian", 18, "bold"), bg="Cyan")
heading_label.pack(side=TOP,fill=X)

song_name_label=tk.Label(window, text="Song Name: ", font=("Comic Sans", 14), bg="cyan",fg="black")
song_name_label.place(x=60, y=50)
song = StringVar()
song_name_Entry=tk.Entry(window, width=40, textvariable=song, font=("Courier", 14, "italic"))
song_name_Entry.place(x=200, y=50)

artist_name_label=tk.Label(window, text="Artist Name: ", font=("Comic Sans", 14), bg="cyan",fg="black")
artist_name_label.place(x=60, y=100)
artist = StringVar()
artist_name_entry=tk.Entry(window, width=40, textvariable=artist, font=("Courier", 14, "italic"))
artist_name_entry.place(x=200, y=100)

Extract_Button=tk.Button(window, text='Extract lyrics', font=("Courier", 15, "bold"), width=15, command=extract_song_lyrics)
Extract_Button.place(x=250, y=150)

window.mainloop()