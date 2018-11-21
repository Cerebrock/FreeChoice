import os
import tkinter as tk
from PIL import Image, ImageTk
import time
import random

class Rank(tk.Frame):
    def __init__(self, master = None, img_path = '', instr = ''):
        super().__init__()
        self.pack(fill = "both", expand = True)
        self.master.attributes("-fullscreen", True)
        self.master.attributes('-topmost',True)
        self.height, self.width = self.master.winfo_screenheight(), self.master.winfo_screenwidth()
        self.cnv = tk.Canvas(self, width = self.width, height = self.height, bg = "#E8E8E8")
        self.cnv.pack()
        self.master.focus_force()            
        self.trn = 0
        self.c = 1                
        self.path = img_path
        self.d = []      #PicId + Rated number + Time       
        self.mostradas = []
        self.maxms = 20000
        self.data = []     
        self.bind_all("<Escape>", self.close)
        self.instructions = instr
        self.instruct()
            
    def instruct(self, event = 0):
        self.cnv.delete("in")
        self.cnv.create_text(self.width/2, self.height/2, text = self.instructions[self.trn], font = ("Verdana", 18), justify = "center", tags = "in")
        self.trn += 1
        if self.trn < len(self.instructions):
            self.bind_all("<Return>", self.instruct)
        else:
            self.bind_all("<Return>", self.freeChoice)

    def freeChoice(self, event):
        self.cnv.delete("in")       
        self.trn = 0  
        self.bind_all("<Return>", self.nothing)
        self.load_images()  
        self.display_images()        

    def nothing(self, event):
        return "break"
        
    def load_images(self):
        self.imags = []
        for i in range(1, len([f for f in os.listdir(self.path)]) + 1):
            i = Image.open(os.path.join(self.path + "/" + str(i) + ".jpg"))             
            i.thumbnail((700, 700), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(i)
            self.imags.append(img)
        self.b = [i for i in range(1, len(self.imags) + 1)]
        self.images = [list(c) for c in zip(self.b, self.imags)]
        random.shuffle(self.images)
        #list of tuples
        
    def display_images(self):
        if self.trn != 0:
            self.cnv.delete("all")
        self.fixate()        
        try:
            self.imgn = self.images.pop()
            self.t0 = time.clock()      
            self.cnv.create_image(self.width/2, self.height/2, image = self.imgn[1])
            self.cnv.bind_all("<Key>", self.rate_img)
            self.trn += 1            
            self.a = self.cnv.after(self.maxms, self.rate_img) 
        except IndexError:
            self.cnv.delete("all")
            self.returndata()
            self.master.destroy()

    def close(self, event):
        self.returndata()            
        self.master.destroy()
        
    #Crea Fixation Point    
    def fixate(self):
        self.bind_all("<Key>", self.nothing)
        self.cnv.create_line((self.width/2)/self.c, ((self.height/2) + 20)/self.c, (self.width/2)/self.c, ((self.height/2) - 20)/self.c, width = 2, tag = "cross1")
        self.cnv.create_line(((self.width/2)-20)/self.c, (self.height/2)/self.c, ((self.width/2) + 20)/self.c, (self.height/2)/self.c, width = 2, tag = "cross2")
        self.update()
        time.sleep(2)
        
    #Rankea las imagenes y devuelve una lista de tuples con picID + rank + t
    def rate_img(self, event = 0):
        t1 = time.clock()
        t = t1 - self.t0        
        imgg = self.imgn[0]
        if event == 0:
            ratedn = "x" 
            rnk = (imgg, ratedn, self.maxms)
            self.d.append(rnk) 
            self.display_images()
        else:
            try:
                ratedn = int(event.char) 
            except ValueError:
                ratedn = "X"
            if ratedn != 0:
                rnk = (imgg, ratedn, round(t, 3)) 
            elif ratedn == 0:
                rnk = (imgg, "X", round(t, 3))
            self.d.append(rnk) 
            self.cnv.after_cancel(self.a)
            self.display_images()

    def returndata(self):
        self.d.sort()
        for t in self.d:
            self.data.append(str(t[1]))

def rank(img_path = '', instr = ''):
    m = tk.Tk()
    b = Rank(m, img_path = '', instr = '')
    b.mainloop()
    b.data