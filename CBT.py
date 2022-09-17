#TODO create program to open a cbr file and display the first image.
from guizero import App, Text, PushButton, Box, Picture
from zipfile import ZipFile
from PIL import Image

from io import BytesIO
import filetype
from comicfile import ComicFile

#TODO: make GUI play nicer with various resolutions and scales
#TODO: make buttons look nicer and be visible on gui
#TODO: change the bottom button color to something nicer = #2B083B
page = 0

pages = []

def get_file():

    # get shit from zip into memory

    app.comicfile = ComicFile(app.select_file())
    
    picture.image = app.comicfile.pages[0]

def image_forward():
    picture.image = app.comicfile.get_next_page()

def image_back():
    picture.image = app.comicfile.get_previous_page()
    
app = App(title="CBT", height=1000, width=800, bg="#010814")
text = Text(app, bg="#010814", color="#005eff")
box = Box(app, border=1)
box.bg = "#010814"
box.color ="#005eff"
# picture = Picture(box, image="Baphomet.png", height=600, width=600)
b_box = Box(box, align="bottom", border=1,  height=45, width=177, layout="grid", visible="yes")
b_box.bg = "#2B083B"
b_box.text_color = "#005eff"
picture = Picture(box, image="Baphomet.png")
picture.resize(app.width, app.height)

OF_button = PushButton(b_box, text="Open File", padx=5, pady=10, command=get_file, align="bottom", grid=[1,0])
BACK_button = PushButton(b_box, text="Back", padx=5, pady=10, command=image_back, align="bottom", grid=[0,0])
FORWARD_button = PushButton(b_box, text="Forward", padx=5, pady=10, command=image_forward, align="bottom", grid=[2,0])

app.display()