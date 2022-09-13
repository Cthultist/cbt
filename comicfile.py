from zipfile import ZipFile
from PIL import Image
from io import BytesIO
import filetype
import rarfile

class ComicFile():

    def __init__(self, container_file):

        self.pages = []
        self.current_page = None
        if self.file_type_check(container_file) == 'zip':
            
            container_file = ZipFile(container_file)

            for file in container_file.infolist():
                print(file.filename)
                self.pages.append(Image.open(BytesIO(container_file.read(file.filename)))) # is there a better way of doing this

            # print(self.pages)
        elif self.file_type_check(container_file) == 'rar':
        
            container_file = rarfile.RarFile(container_file)

            for file in container_file.infolist():
                print(file.filename)
                self.pages.append(Image.open(BytesIO(container_file.read(file.filename))))
        
        self.current_page = 0
            
    def get_next_page(self):
        if self.current_page + 1 < len(self.pages):
            self.current_page += 1
            return self.pages[self.current_page]

    def get_previous_page(self):
        if self.current_page - 1 >= 0:
            self.current_page -= 1
            return self.pages[self.current_page]
        
    def file_type_check(self, type_input):
        type_check = filetype.guess(type_input)
        print(type_check)
        if type_check.extension == 'zip':
            print(type_check.extension)
            return 'zip'
        elif type_check.extension == 'rar':
            print(type_check.extension)
            return "rar"
        # elif type_check.is_7zip():
        #     return "7zip"
        # elif type_check.is_tar():
        #     return "tar"
                
        else:
            print("type error")
            return
            
            