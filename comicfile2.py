from zipfile import ZipFile
from PIL import Image
from io import BytesIO

class ComicFile():

    def __init__(self, zip_file):

        self.pages = []
        self.current_page = None

        zip_file = ZipFile(zip_file)

        for file in zip_file.infolist():
            print(file.filename)
            self.pages.append(Image.open(BytesIO(zip_file.read(file.filename)))) # is there a better way of doing this

        # print(self.pages)

        self.current_page = 0

    def get_next_page(self):
        if self.current_page + 1 < len(self.pages):
            self.current_page += 1
            return self.pages[self.current_page]

    def get_previous_page(self):
        if self.current_page - 1 >= 0:
            self.current_page -= 1
            return self.pages[self.current_page]
        
    def file_type_check(self):
        if self.testzip():
            if self.is_zipfile():
                return "zip"
            elif self.is_rarfile():
                return "rar"
            elif self.is_7zip():
                return "7zip"
            elif self.is_tar():
                return "tar"
                
        else:
            print("File is corrupted!")
            return
            
            