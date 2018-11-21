import os
import sys
import tkinter as tk

class Question_w_options(tk.Frame):
    def __init__(self, quest = 0, master = None):
        super().__init__()
        self.pack(fill = "both", expand = True)                    
        self.master.attributes("-fullscreen", True)
        self.master.attributes('-topmost',True)
        self.height, self.width = self.master.winfo_screenheight(), self.master.winfo_screenwidth()
        self.cnv = tk.Canvas(self, width = self.width, height = self.height, bg = "#E8E8E8")
        self.cnv.pack()
        self.master.focus_force()
        self.items = self.get_items(quest, os.path.dirname(sys.argv[0]))
        self.cnv.create_text(self.width/2, 20, width = self.width - 100, text = "".join(self.items.pop(0)), anchor = tk.N, font = ("Verdana", 14), justify = "center", tags = "instruction")
        self.bind_all("<Escape>", self._quit)
        self.data = []
        self.start = False
        self.it = self.cnv.create_text(self.width/2, self.height/2, width = self.width - 100, text = "".join(self.items.pop(0)), anchor = tk.CENTER, font = ("Verdana", 14), justify = "center", tags = "it")
        self.bind_all("<Key>", self.handle)
        
    def get_items(self, filename, path):
        test = open(filename, "r")
        lines = test.readlines()
        items = []
        item = []
        for line in lines:
            if line != "\n":
                item.append(line)
            else:
                items.append((item))
                item = []
        return items

    def _quit(self, event):
        self.master.destroy()
        
    def show_item(self):
        self.it = self.cnv.create_text(self.width/2, self.height/2, width = self.width - 100, text = "".join(self.items.pop(0)), anchor = tk.CENTER, font = ("Verdana", 14), justify = "center", tags = "it")
        self.bind_all("<Key>", self.handle)
            
    def handle(self, event):
        try:        
            if event.keysym == "Return" and self.start == False:
                self.cnv.delete(self.it)
                self.show_item()
                self.start = True
            if n_options == 4 and self.start == True and event.keysym in "aAbBcCdD1234":
                if event.keysym in "aA1":
                    p = "0"
                elif event.keysym in "bB2":
                    p = "1"
                elif event.keysym in "cC3":
                    p = "2"
                elif event.keysym in "dD4":
                    p = "3"
                self.data.append(p)
                self.cnv.delete(self.it)
                self.show_item()            
            elif n_options == 2 and self.start == True and event.keysym in "aAbBcCdD1234":
                if event.keysym in "aA1":
                    p = "0"
                elif event.keysym in "bB2":
                    p = "1"
                self.data.append(p)
                self.cnv.delete(self.it)
                self.show_item()
            elif self.start == True and event:
                pass
        except IndexError:
            self.master.destroy()
                    
class Question_w_entry(tk.Frame):
    def __init__(self, master = None, quest = 0):
        super().__init__()
        self.pack(fill = "both", expand = True)                    
        self.master.attributes("-fullscreen", True)
        self.master.attributes('-topmost',True)
        self.height, self.width = self.master.winfo_screenheight(), self.master.winfo_screenwidth()
        self.master.focus_force()
        self.items = self.get_items(quest, os.path.dirname(sys.argv[0]))
        self.bind_all("<Escape>", self.close)
        self.trn = 0
        self.q = 0            
        self.data = []
        self.instructions = "".join(self.items.pop(0))
        self.instruct()
    
    def get_items(self, filename, path):
        test = open(filename, "r")
        lines = test.readlines()
        items = []
        item = []
        for line in lines:
            if line != "\n":
                item.append(line)
            else:
                items.append(item)
                item = []
        return items
        
    def instruct(self, event = 0):
        if self.trn != 0:
            self.ins_label.destroy()
        self.ins_label = tk.Label(self, text = self.instructions, font = ("Verdana", 18), justify = "center")
        self.ins_label.pack(side = "top")            
        self.trn += 1
        self.ins_label2 = tk.Label(self, text = "Presione Enter para comenzar", font = ("Verdana", 18), justify = "center")
        self.ins_label2.pack()
        self.bind_all("<Return>", self.question)

    def close(self, event):
        self.master.destroy()
        
    def get_(self, event = 0):
        self.a = self.box.get()
        self.box.delete(0, tk.END)
        self.it.destroy()            
        self.data.append(self.a)
        if len(self.items) > 0:
            self.question(self)
        else:
            self.master.destroy()
        
    def question(self, event = 0):
        if self.q == 0:
            self.ins_label2.destroy()
            self.box = tk.Entry(self, font = "Helvetica 30")
            self.box.pack(side = "bottom")                            
        self.i = "".join(self.items.pop(0))
        self.q += 1
        self.it = tk.Label(self, text = str(self.i), font = ("Verdana", 20), justify = "center")
        self.it.pack(expand = True)
        self.bind_all("<Return>", self.get_)
        self.box.focus_set()


"""
w = tk.Tk()
ques = 'STAIa.txt'
b = Question_w_options(master = w, quest = ques)
b.mainloop()
b.data
"""