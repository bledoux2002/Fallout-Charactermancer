import os
from tkinter import *
from tkinter.ttk import *
from yt_dlp import YoutubeDL

class MusicBox:
    
    def __init__(self, root):
        self.ydl_opts = {
            'format': 'm4a/bestaudio/best',
            'windowsFilenames': True,
            'paths': {
                'home': './sound/files',
            },
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }]
        }
        
        # self.path = os.path.dirname(os.path.abspath(__file__))

        self.root = root
        # root.configure(bg="light sky blue")
        self.root.title("Adaptive Music Box")
        
        self.style_default = Style()
        self.style_name = "Outlined.TFrame"
        self.style_default.configure(self.style_name, borderwidth=2, relief="solid")
        
        self.root.columnconfigure(0, weight=1, minsize=500)
        self.root.rowconfigure(0, weight=1, minsize=150)
        
        self.frm_download = Frame(self.root, style=self.style_name)
        self.frm_download.grid(row=0, column=0, padx=50, pady=25, sticky='new')
        self.frm_download.columnconfigure(0, weight=0, minsize=10)
        self.frm_download.columnconfigure(1, weight=1)
        self.frm_download.columnconfigure(2, weight=0, minsize=50)
        self.frm_download.rowconfigure(0, weight=1, minsize=25)
        self.frm_download.rowconfigure(1, weight=1, minsize=25)
        
        self.lbl_url = Label(master=self.frm_download, text="URL:")
        self.ent_url = Entry(master=self.frm_download)
        self.btn_url = Button(master=self.frm_download, text="Download")
        self.status = StringVar(master=self.frm_download, value="Waiting for download...")
        self.lbl_status = Label(master=self.frm_download, textvariable=self.status)
        
        self.lbl_url.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.ent_url.grid(row=0, column=1, sticky='ew')
        self.btn_url.grid(row=0, column=2, padx=5, sticky='e')
        self.lbl_status.grid(row=1, column=1, pady=5, sticky="ew")
        
        self.btn_url.bind("<Button-1>", self.download)
    
    def download(self, event):
        # URLs = ['https://youtu.be/FcaHJDj6KEE']
        
        url = self.ent_url.get()
        #ADD TO JSON FOR LATER
        
        URLs = []
        URLs.append(url)
        
        try:
            with YoutubeDL(self.ydl_opts) as ydl:
                error_code = ydl.download(URLs)
                if error_code == 0:
                    self.status.set("Success!")
                else:
                    self.status.set(error_code)
        except Exception as e:
            self.status.set(f"Error: {e}")

def main():
    
    root = Tk()
    MusicBox(root)
    root.mainloop()

if __name__ == "__main__":
    main()