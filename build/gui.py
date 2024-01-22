
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pytube import YouTube
from pathlib import Path
import threading

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\henri\OneDrive\Documentos\Vscode\YouTube-Downloader\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.resizable(False,False)
window.title("Youtube Downloader")
window.geometry("585x326")
window.configure(bg = "#FFFFFF")

def download_audio():
    """
    The function `download_audio` downloads the audio from a YouTube video given a link.
    """
    try:
        link = entry_1.get()
        yt = YouTube(link)
        yt.register_on_complete_callback(on_download_complete)
        stream = yt.streams.filter(only_audio=True).first()
        canvas.itemconfig(text_id, text="Downloading...")
        stream.download()
    except Exception as e:
        print(e)
    finally:
        print("Done")

def download_audio_thread(): 
    """
    The function `download_audio_thread` creates a new thread and starts the `download_audio` function
    in that thread.
    """
    threading.Thread(target=download_audio).start()


def on_download_complete(stream, filepath):
    print("Download completed")
    canvas.itemconfig(text_id, text="Download completed")
    window.after(2000, lambda: canvas.itemconfig(text_id, text="Downloaded"))
    window.after(4000, lambda: canvas.itemconfig(text_id, text="Video URL"))

def download_video():
    try:
        link = entry_1.get()
        yt = YouTube(link)
        yt.register_on_complete_callback(on_download_complete)
        stream = yt.streams.first()
        canvas.itemconfig(text_id, text="Downloading...")
        stream.download()
    except Exception as e:
        print(e)
    finally:
        print("Done")


def download_video_thread():
   threading.Thread(target=download_video).start()




canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 326,
    width = 585,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    219.0,
    404.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    169.0,
    390.0,
    fill="#3C3C3C",
    outline="")

canvas.create_rectangle(
    211.0,
    173.0,
    516.0,
    216.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    363.5,
    192.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=232.0,
    y=177.0,
    width=263.0,
    height=28.0
)

canvas.create_text(
    236.0,
    17.0,
    anchor="nw",
    text="Youtube Downloader",
    fill="#000000",
    font=("LexendDeca Bold", 24 * -1)
)

canvas.create_text(
    242.0,
    54.0,
    anchor="nw",
    text="Download all your videos\n with this tool! Just provide the video link and voalah!",
    fill="#000000",
    font=("LexendDeca ExtraLight", 13 * -1)
)

text_id = canvas.create_text(233.0, 143.0, anchor="nw", text="Video URL", fill="#000000", font=("LexendDeca ExtraLight", 16 * -1))
canvas.itemconfig(text_id, fill="#ff0000")  # Change the color of the text to red

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=download_audio_thread,
    relief="flat"
)
button_1.place(
    x=427.0,
    y=216.0,
    width=98.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=download_video_thread,
    relief="flat"
)
button_2.place(
    x=203.0,
    y=216.0,
    width=98.0,
    height=40.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    109.0,
    90.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
