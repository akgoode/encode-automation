import os

class File_System:
    def __init__(self):
        print("hi from fs")

    def list_dir(self):
        return os.listdir(".")