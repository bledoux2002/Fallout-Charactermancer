from tkinter import *
from tkinter import ttk
import os

class Charactermancer:
    
    def __init__(self, root):
        self.root = root
        self.recent_files = ['file1', 'file2', 'file3']
        
        self.root.title('Fallout 2d20 Charactermancer')
        
        self.root.option_add('*tearOff', FALSE)

        self.__setupMenu()

        # mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        # mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        # self.root.columnconfigure(0, weight=1)
        # self.root.rowconfigure(0, weight=1)

    def __setupMenu(self):
        # Menubar
        self.menubar = Menu(self.root)
        self.root['menu'] = self.menubar

        # Menus
        self.menu_file = Menu(self.menubar)
        self.menu_edit = Menu(self.menubar)
        self.menu_view = Menu(self.menubar)
        self.menu_help = Menu(self.menubar)
        
        self.menubar.add_cascade(menu=self.menu_file, label='File')
        self.menubar.add_cascade(menu=self.menu_edit, label='Edit')
        self.menubar.add_cascade(menu=self.menu_view, label='View')
        self.menubar.add_cascade(menu=self.menu_help, label='Help')

        # Menu Items
        self.menu_file.add_command(label='New', command=self.newFile)
        self.menu_file.add_command(label='Open', command=self.openFile)
        self.menu_recent = Menu(self.menu_file)
        self.menu_file.add_cascade(menu=self.menu_recent, label='Open Recent') #disable?
        for f in self.recent_files:
            self.menu_recent.add_command(label=os.path.basename(f), command=lambda f=f: self.openFile(f))
        self.menu_file.add_separator()
        self.menu_file.add_command(label='Save', command=self.saveFile)
        self.menu_file.add_command(label='Save As', command=self.saveAs)
        self.menu_file.add_command(label='Make Copy', command=self.makeCopy)
        self.menu_file.add_separator()
        self.menu_file.add_command(label='Rename', command=self.renameFile)
        self.menu_file.add_command(label='Delete', command=self.deleteFile)
        self.menu_file.add_separator()
        self.menu_file.add_command(label='Close', command=self.closeFile)
        
        self.menu_edit.add_command(label='Undo', command=self.undo) #disable when stack empty
        self.menu_edit.entryconfigure('Undo', state=DISABLED)
        self.menu_edit.add_command(label='Redo', command=self.redo) #disable when stack empty (shold empty after new action)
        self.menu_edit.entryconfigure('Redo', state=DISABLED)
        self.menu_edit.add_separator()
        self.menu_edit.add_command(label='Cut', command=self.cut)
        self.menu_edit.add_command(label='Copy', command=self.copy)
        self.menu_edit.add_command(label='Paste', command=self.paste) #disable when nothing in clipboard
        self.menu_edit.entryconfigure('Paste', state=DISABLED)
        self.menu_edit.add_separator()
        self.menu_edit.add_command(label='Select All', command=self.selectAll)
        self.menu_edit.add_command(label='Delete', command=self.delete)
        self.menu_edit.add_separator()
        self.menu_edit.add_command(label='Options', command=self.options)

        self.menu_view.add_command(label='Zoom In', command=self.zoom) #disable when max font
        self.menu_view.add_command(label='Zoom Out', command=lambda: self.zoom(-1)) #disable when min font

    def newFile(self):
        print('newFile')
    
    def openFile(self, file=None):
        print('openFile')
        if file:
            print(file)
    
    def closeFile(self):
        print('POP UP WARNING IF FILE NOT SAVED')
        # quit()
    
    def saveFile(self):
        print('saveFile')
    
    def saveAs(self):
        print('saveAs')
    
    def makeCopy(self):
        print('makeCopy')
    
    def renameFile(self):
        print('renameFile')
    
    def deleteFile(self):
        print('deleteFile')


    def undo(self):
        print('undo')
    
    def redo(self):
        print('redo')
    
    def cut(self):
        print('cut')
    
    def copy(self):
        print('copy')
    
    def paste(self):
        print('paste')
    
    def selectAll(self):
        print('selectAll')
    
    def delete(self):
        print('delete')
    
    def options(self):
        print('options')


    def zoom(self, amt=1):
        # Increase font size by amt (zoom out decreases size)
        print(f'zoom {amt}')

def main():
    root = Tk()
    Charactermancer(root)
    root.mainloop()

if __name__ == "__main__":
    main()