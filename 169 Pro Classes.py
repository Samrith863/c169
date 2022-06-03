from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.title("Classes")
root.geometry("900x700")
list1=["Label","Button","Dropdown"]
dropdown=ttk.Combobox(root,state="readonly",values=list1)
dropdown.pack()

class createElements():
    
    def __init__(self):
        print("This class is used to create elements dynamically")
    
    def createLabel(self):
        label1=Label(root,text="A New Label Is Created Using This class! ",fg="red")
        label1.pack()
        
    def createBtn(self):
        btn=Button(root,text="Button",command=self.message)
        btn.pack(padx=20,pady=10)
        
    def createDropdown(self):
        value=[1,2,3,4]
        dropdown2=ttk.Combobox(root,state="readonly",values=value)
        dropdown2.pack()
    
    def message(self):
        messagebox.showinfo("ShowInfo","this button is created using class")
    
    
    def choose(self):
        global dropdown
        get_value=dropdown.get()
        if(get_value=="Label"):
            self.createLabel()
        elif(get_value=="Button"):
            self.createBtn()
        elif(get_value=="Dropdown"):
            self.createDropdown()

object1=createElements()

btn_show=Button(root,text="Show Element",command=object1.choose)
btn_show.pack()
root.mainloop()
