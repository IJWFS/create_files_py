from tkinter import *
import os
from tkinter import filedialog

class Interface(Tk):
    def __init__(self, model):
        super().__init__()
        self.title("create_files")
        self.geometry('400x200')
        # self.resizable(width=False, height=False)
        self.model = model
        self.model.set_view(self)
        self.select_dir = Button(self, text='выберите папку', command=model.select_directory)
        self.select_dir.grid(column=0, row=0, sticky=W)
        self.lb_select_dir = Label(text='выбрана директория:')
        self.lb_select_dir.grid(column=0, row=1, sticky=W)
        self.lb_path = Label(text='None')
        self.lb_path.grid(column=1, row=1)
        self.count_files = Label(text='кол-во файлов')
        self.count_files.grid(column=0, row=2, sticky=W)
        self.count1 = Entry()
        self.count1.grid(column=1, row=2, sticky=W)
        self.count1.configure(width=10)
        self.count2 = Entry()
        self.count2.grid(column=2, row=2, sticky=W)
        self.count2.configure(width=10)
        self.lb_name_files = Label(text='имя файла')
        self.lb_name_files.grid(column=0, row=3, sticky=W)
        self.name_folder = Entry()
        self.name_folder.grid(column=1, row=3, sticky=W)
        self.name_folder.configure(width=10)
        self.create_folder = Button(self, text='создать в директории ПАПКУ', command=self.model.create_folder)
        self.create_folder.grid(column=0, row=5, sticky=W)
        self.create_files = Button(self, text='создать в директории ФАЙЛ', command=self.model.create_files)
        self.create_files.grid(column=0, row=6, sticky=W)
        self.lb_file_extension = Label(text='расширение файла')
        self.lb_file_extension.grid(column=0, row=4, sticky=W)
        self.file_extension = Entry()
        self.file_extension.grid(column=1, row=4, sticky=W)
        self.file_extension.configure(width=10)

    # def clear_textbox(self):
    #     self.count1.insert(0, '')
    #     self.count2.insert(0, '')
    #     self.name_folder.insert(0, '')


class open_model():
    def __init__(self):
        self.path = ''
        self.view = None
        self.count1 = ''
        self.count2 = ''
        self.name = ''
        self.file_extension = ''

    def set_view(self, view):
        self.view = view

    def select_directory(self):
        self.path = filedialog.askdirectory()
        self.view.lb_path.configure(text=self.path)

    def create_folder(self):
        self.count1 = self.view.count1.get()
        self.count2 = self.view.count2.get()
        self.name = self.view.name_folder.get()
        if self.count2 == '':
            for i in range(int(self.count1)):
                os.mkdir(self.path + '\\' + self.name + str(i + 1))
        else:
            try:
                for i in range(int(self.count1)):
                    for j in range(int(self.count2)):
                        os.mkdir(self.path + '\\' + self.name + str(i + 1) + '\\' + str(j + 1))
            except FileNotFoundError:
                for i in range(int(self.count1)):
                    os.mkdir(self.path + '\\' + self.name + str(i + 1))
                    for j in range(int(self.count2)):
                        os.mkdir(self.path + '\\' + self.name + str(i + 1) + '\\' + str(j + 1))

        # self.path = ''
        # self.count1 = 0
        # self.count2 = 0
        # self.view.clear_textbox()

    def create_files(self):
        self.count1 = self.view.count1.get()
        self.count2 = self.view.count2.get()
        self.name = self.view.name_folder.get()
        self.file_extension = self.view.file_extension.get()
        if self.count2 == '':
            for i in range(int(self.count1)):
                my_file = open(self.path + '\\' + self.name + str(i + 1) + '.' + self.file_extension, "a+")
        else:
            try:
                for i in range(int(self.count1)):
                    for j in range(int(self.count2)):
                        my_file = open(self.path + '\\' + self.name + str(i + 1) + '\\' + str(j + 1) + '.' + self.file_extension, "a+")
            except FileNotFoundError:
                for i in range(int(self.count1)):
                    os.mkdir(self.path + '\\' + self.name + str(i + 1))
                    for j in range(int(self.count2)):
                        my_file = open(self.path + '\\' + self.name + str(i + 1) + '\\' + str(j + 1) + '.' + self.file_extension, "a+")

model1 = open_model()
view1 = Interface(model1)
view1.mainloop()
