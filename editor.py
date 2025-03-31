from tkinter import *
from tkinter import ttk
import os

# Color Chart: https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html

class Charactermancer:
    
    def __init__(self, root):
        self.root = root
        root.configure(bg="light sky blue")
        self.recent_files = []
        
        self.root.title("Fallout 2d20 Charactermancer")
        
        self.root.option_add("*tearOff", FALSE)

        self.__setupMenu()

        mainframeStyle = ttk.Style()
        mainframeStyle.configure('mf.TFrame', background="white smoke")
        mainframe = ttk.Frame(self.root, padding="12 12 12 12", style='mf.TFrame')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        topStyle = ttk.Style()
        topStyle.configure('top.TFrame', background="AntiqueWhite3")
        top = ttk.Frame(mainframe, padding="12 12 12 12", borderwidth=2, relief="raised", style='top.TFrame')
        top.grid(column=0, row=0, sticky=(N, W, E))
        nameEntry = ttk.Entry(top)
        nameEntry.insert(0, "Name")
        nameEntry.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=(N, W))
        levelLabel = ttk.Label(top, text="Level: 1")
        levelLabel.grid(column=2, row=1, sticky=(E))
        originStyle = ttk.Style()
        originStyle.configure('origin.TFrame')
        origin = ttk.Frame(top, padding="0 6 0 6", borderwidth=2, style='origin.TFrame')
        origin.grid(column=0, row=2, sticky=(W))
        originLabel = ttk.Label(origin, text="Origin: ")
        originLabel.grid(column=0, row=0)
        originEntry = ttk.Entry(origin)
        originEntry.insert(0, "Origin")
        originEntry.grid(column=1, row=0)
        ap = ttk.Frame(top, padding="0 6 0 6", borderwidth=2, relief="raised")
        ap.grid(column=1, row=2)
        apLabel = ttk.Label(ap, text="Action Points", padding="6 0 6 0")
        apLabel.grid(column=0, row=0)
        apEntry = ttk.Entry(ap, width=4, justify="right")
        apEntry.insert(0, 0)
        apEntry.grid(column=1, row=0)
        apMax = ttk.Label(ap, text=" / 6", padding="0 0 6 0")
        apMax.grid(column=2, row=0)
        xp = ttk.Frame(top, padding="0 6 0 6", borderwidth=2, relief="raised")
        xp.grid(column=2, row=2)
        xpLabel = ttk.Label(xp, text="Experience Points", padding="6 0 0 0")
        xpLabel.grid(column=0, row=0)
        xpEntry = ttk.Entry(xp, width=12, justify="right")
        xpEntry.insert(0, 0)
        xpEntry.grid(column=1, row=0, padx=6)
        
        # SPECIAL
        specialStyle = ttk.Style()
        specialStyle.configure('special.TFrame', background="ghost white")
        special = ttk.Frame(top, padding="12 12 12 12", borderwidth=2, style='special.TFrame')
        special.grid(column=0, row=3, columnspan=9, rowspan=2)

        # Change to colors from character sheet        
        sEnt = ttk.Entry(special, width=4, justify="center") # bg="DarkSeaGreen4"
        sEnt.insert(0, 0)
        sEnt.grid(column=0, row=0)
        sLbl = ttk.Label(special, width=12, text="Strength", anchor="center", padding="3 0 3 0") # bg="dark sea green"
        sLbl.grid(column=0, row=1)
        pEnt = ttk.Entry(special, width=4, justify="center")
        pEnt.insert(0, 0)
        pEnt.grid(column=1, row=0)
        pLbl = ttk.Label(special, width=12, text="Perception", anchor="center", padding="3 0 3 0")
        pLbl.grid(column=1, row=1)
        eEnt = ttk.Entry(special, width=4, justify="center")
        eEnt.insert(0, 0)
        eEnt.grid(column=2, row=0)
        eLbl = ttk.Label(special, width=12, text="Endurance", anchor="center", padding="3 0 3 0")
        eLbl.grid(column=2, row=1)
        cEnt = ttk.Entry(special, width=4, justify="center")
        cEnt.insert(0, 0)
        cEnt.grid(column=3, row=0)
        cLbl = ttk.Label(special, width=12, text="Charisma", anchor="center", padding="3 0 3 0")
        cLbl.grid(column=3, row=1)
        iEnt = ttk.Entry(special, width=4, justify="center")
        iEnt.insert(0, 0)
        iEnt.grid(column=4, row=0)
        iLbl = ttk.Label(special, width=12, text="Intelligence", anchor="center", padding="3 0 3 0")
        iLbl.grid(column=4, row=1)
        aEnt = ttk.Entry(special, width=4, justify="center")
        aEnt.insert(0, 0)
        aEnt.grid(column=5, row=0)
        aLbl = ttk.Label(special, width=12, text="Agility", anchor="center", padding="3 0 3 0")
        aLbl.grid(column=5, row=1)
        lEnt = ttk.Entry(special, width=4, justify="center")
        lEnt.insert(0, 0)
        lEnt.grid(column=6, row=0)
        lLbl = ttk.Label(special, width=12, text="Luck", anchor="center", padding="3 0 3 0")
        lLbl.grid(column=6, row=1)
        
        # Luck Points
        luckPoints = ttk.Frame(special, padding="3 0 0 0")
        luckPoints.grid(column=7, row=0, rowspan=2, sticky=(E))
        lpEnt = ttk.Entry(luckPoints, width=4, justify="center")
        lpEnt.insert(0, 0)
        lpEnt.grid(column=0, row=0, sticky=(E))
        lpMax =ttk.Label(luckPoints, text=" / 0")
        lpMax.grid(column=1, row=0, sticky=(W))
        lpLbl = ttk.Label(luckPoints, width=12, text="Luck Points", anchor="center", padding="3 0 3 0")
        lpLbl.grid(column=0, row=1, columnspan=2)
        
        core = ttk.Frame(mainframe, padding="12 12 12 12")
        core.grid(column=0, row=1)
        
        # perks = ttk.Frame(mainframe, padding="3 3 12 12")
        # perks.grid(column=0, row=1, sticky=(W, E, S))
        
        # gear = ttk.Frame(mainframe, padding="3 3 12 12")
        # gear.grid(column=0, row=1, sticky=(W, E, S))
        

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