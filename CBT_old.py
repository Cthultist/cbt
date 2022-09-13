#TODO create program to open a cbr file and display the first image.
from guizero import App, Text, PushButton, Box, Picture
import zipfile
from unrar import rarfile



def get_file():

    issue = []

    filename = app.select_file()
    # display_image(filename.value)
    if rarfile.is_rarfile(filename):
        rf = rarfile.RarFile(filename)
        for f in rf.infolist():
            print(f.filename)
            # issue.append(rf.extract(member=f.filename)) # needs to be rf.read but .read produces a IOBytes
            open(rf.read(member=f.filename))
            print("appended file to issue")
            # issue.append(rarfile.RarFile.open(rf, member=f.filename))
        print(issue)
        print(f"first item in list is {issue[0]}")
        display_image(issue[0])
        
                
def display_image(file):
    picture.image = file
    
app = App(title="ComicBookTorture", height=1000, width=800, bg="#7d8e87")
text = Text(app, text="Please put your comicbooks into the vise")
box = Box(app, border=1)
picture = Picture(box, image="Baphomet.png", height=600, width=600)

button = PushButton(app, text="Open File", padx=5, pady=10, command=get_file, align="bottom")
# filename = Text(app)

app.display()