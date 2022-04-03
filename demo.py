import tkinter as tk
import subprocess
import os

class App(tk.Tk):
   def __init__(self):
      tk.Tk.__init__(self)
      self.title("Canvas2PDF")
      self.line_start = None
      self.canvas = tk.Canvas(self, width=300, height=300, bg="white")
      self.canvas.bind("<Button-1>", lambda e: self.draw(e.x, e.y))
      self.button = tk.Button(self, text="Generate PDF",command=self.generate_pdf)
      self.canvas.pack()
      self.button.pack(pady=10)

def draw(self, x, y):
    if self.line_start:
        x_origin, y_origin = self.line_start
        self.canvas.create_line(x_origin, y_origin, x, y)
        self.line_start = None
    else:
        self.line_start = (x, y)

def generate_pdf(self):
    self.canvas.postscript(file="tmp.ps", colormode='color')
    process = subprocess.Popen(["ps2pdf", "tmp.ps", "result.pdf"], shell=True)
    process.wait()
    os.remove("tmp.ps")
    self.destroy()
app = App()
app.mainloop()