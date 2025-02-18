import tkinter as tk
from math import pi
from tkinter import Frame, Label, Button
from number_entry import IntEntry

def main():
    """
    
    """
    root = tk.Tk()
    
    frm_main = Frame(root)
    frm_main.master.title("Circle Area")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    
    populate_main_window(frm_main)

    root.mainloop()
    
def populate_main_window(frm_main):
    """
    
    """
    lbl_radius = Label(frm_main, text="Raduis: ")
    ent_raduis = IntEntry(frm_main, width=4, lower_bound=0, upper_bound=200)
    lbl_result = Label(frm_main, width=6)
    btn_clear = Button(frm_main, text="Clear")
    
    lbl_radius.grid(      row=1, column=2, padx=6, pady=6)
    ent_raduis.grid(      row=1, column=3, padx=6, pady=6)
    lbl_result.grid(      row=2, column=3, padx=6, pady=6)
    btn_clear.grid(row=4, column=2, padx=3, pady=3, columnspan=4, sticky="w")

    def calculate(event):
      try:
        radius = ent_raduis.get()
        area = pi * radius ** 2
        lbl_result.config(text=f"{area:.0f}")

      except ValueError:
        print(ValueError)
        
    def clear():
        """This is clear all input and output"""
        btn_clear.focus()
        ent_raduis.clear()
        lbl_result.config(text="")
        print("Cleared")

    btn_clear.config(command=clear)
    ent_raduis.bind("<KeyRelease>", calculate)
    












    
    
    



    
    


if __name__ == "__main__":
  main()
  
  

