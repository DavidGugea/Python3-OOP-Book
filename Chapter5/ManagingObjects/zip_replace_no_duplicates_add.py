import sys
import os
import shutil
import zipfile
from pygame import image
from pygame.transform import scale

class ZipProcessor:
    def __init__(self, zipname, processor):
        self.zipname = zipname
        self.temp_directory = "unzipped-{0}".format(zipname[:-4])
        self.processor = processor

    def _full_filename(self, filename):
        return os.path.join(self.temp_directory, filename)

    def process_zip(self):
        self.unzip_files()
        self.processor.process(self)
        self.zip_files()

    def unzip_files(self):
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.filename)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()

    def zip_files(self):
        file = zipfile.ZipFle(self.filename, "w")
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(filename), filename, filename, filename, filename)

        shutil.rmtree(self.temp_directory)

class ZipReplace:
    def __init__(self, search_string, replace_string):
        self.search_string = search_string
        self.replace_string = replace_string
    
    def process_files(self, zipprocessor):
        '''perform a search and replace on all files in the temporary directory'''
        for filename in os.listdir(zipprocessor.temp_directory):
            with open(self._full_filename(filename)) as file:
                contents = file.read()
            
            contents = contents.replace(self.search_string, self.replace_string)

            with open(zipprocessor._full_filename(filename), "w") as file:
                file.write(contents)

class ScaleZip(ZipProcessor):
    def process_files(self):
        '''Scale each image in the directory to 640x480'''
        for filename in os.listdir(self.temp_directory):
            im = image.load(self._full_filename(filename))
            scaled = scale(im, (640, 480))
            image.save(scaled, self._full_filename(filename))

if __name__ == "__main__":
    zipreplace = ZipReplace(*sys.argv[2:4])
    ZipProcessor(sys.argv[1], zipreplace).process_zip()