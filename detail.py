from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class DetailsRoom:
    def __init__(self, root):  # Constructor call
        self.root = root  # Initialization of root
        self.root.title("Hotel Management System")
        self.root.geometry("1240x525+304+280")

      # Title
        lbl_title = Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1240,height=40)
 
        # Second Image Logo
        img2 = Image.open(r"C:\Users\anura\Downloads\Content\HotelLogo.jpg")
        img2 = img2.resize((80, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbl_img2.place(x=2, y=0, width=80, height=40)
        # Label Frame In Left
        labelFrameLeft = LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",14,"bold"),bg="white",fg="black")
        labelFrameLeft.place(x=5,y=40,width=540,height=350)

# Floor
        label_floor= Label(labelFrameLeft,text="Floor: ",font=("arial",10,"bold"),padx=4,pady=6)
        label_floor.grid(row=0,column=0,sticky=W)
        self.var_floor = StringVar()
        entry_floor = ttk.Entry(labelFrameLeft,textvariable=self.var_floor,font=("arial",9,"bold"),width = 20)
        entry_floor.grid(row=0,column=1,sticky=W)
# Room Number
        label_RoomNo= Label(labelFrameLeft,text="Room No: ",font=("arial",10,"bold"),padx=4,pady=6)
        label_RoomNo.grid(row=1,column=0,sticky=W)
        self.var_roomno = StringVar()
        entry_RoomNo = ttk.Entry(labelFrameLeft,textvariable=self.var_roomno,font=("arial",9,"bold"),width = 20)
        entry_RoomNo.grid(row=1,column=1,sticky=W)
# Room type
        label_Roomtype= Label(labelFrameLeft,text="Room Type: ",font=("arial",10,"bold"),padx=4,pady=6)
        label_Roomtype.grid(row=2,column=0,sticky=W)
        self.var_roomtype = StringVar()
        entry_Roomtype = ttk.Entry(labelFrameLeft,textvariable=self.var_roomtype,font=("arial",9,"bold"),width = 20)
        entry_Roomtype.grid(row=2,column=1,sticky=W)

 # Buttons 
        btn_frame = Frame(labelFrameLeft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=360,height=40)

        btnAdd = Button(btn_frame,text="Add",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=2)

        btnupdate = Button(btn_frame,text="Update",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=2)

        btndelete = Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btndelete.grid(row=0,column=2,padx=2)

        btnreset = Button(btn_frame,text="Reset",command=self.reset,font=("arial",10,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=2)

 # Table Frame and search system
        table_frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",14,"bold"),bg="white",fg="black")
        table_frame.place(x=560,y=40,width=660,height=350)
       # Scrollable Table
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.room_Details_table = ttk.Treeview(table_frame,columns=("floor","roomno","roomType",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_Details_table.xview)
        scroll_y.config(command=self.room_Details_table.yview)
       # table Making
        self.room_Details_table.heading("floor",text="Floor")
        self.room_Details_table.heading("roomno",text="Room No")
        self.room_Details_table.heading("roomType",text="Room Type")


       # table Customization
        self.room_Details_table["show"] = "headings"
        self.room_Details_table.column("floor",width=100)
        self.room_Details_table.column("roomno",width=100)
        self.room_Details_table.column("roomType",width=100)

        self.room_Details_table.pack(fill=BOTH,expand=1)
        self.room_Details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

# Adding data
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomno.get()=="":
            messagebox.showerror("Error","Please Fill all the Details",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Mohit@468",database = "hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                    
                        self.var_floor.get(),
                        self.var_roomno.get(),
                        self.var_roomtype.get()
                       
                      
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "New Room Added Successfully",parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning",f"Something went wrong!:{str(e)}",parent=self.root)

# Fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Mohit@468",database = "hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        for child in self.room_Details_table.get_children():
           self.room_Details_table.delete(child)
        if rows:
            for i in rows:
                self.room_Details_table.insert("",END,values=i)
        conn.commit()
        conn.close()
    # show data in table when i click any entry
    def get_cursor(self, event=""):
     cursor_row = self.room_Details_table.focus() 
     content = self.room_Details_table.item(cursor_row)  
     row = content["values"] 
     if row:  
        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])
# Updating the data
    def update(self):
    #  if self.var_floor.get() == "" or self.var_roomno.get() == "":
    #     messagebox.showerror("Error", "Please fill All Details", parent=self.root)
    #  else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mohit@468", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "UPDATE details SET Floor=%s,RoomType=%s WHERE RoomNo=%s",
                (
                       
                        self.var_floor.get(),
                        self.var_roomtype.get(),
                        self.var_roomno.get(),
                )
            )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "New Room Details has been updated successfully", parent=self.root)
        except Exception as e:
            messagebox.showwarning("Warning", f"Something went wrong: {str(e)}", parent=self.root)


#Delete the data
    def mDelete(self):
       mDelete = messagebox.askyesno("Hotel Management System","Do you want to delete this Room Details?",parent = self.root)
       if mDelete>0:
          conn = mysql.connector.connect(host="localhost", username="root", password="Mohit@468", database="hotel")
          my_cursor = conn.cursor()
          query="delete from details where RoomNo=%s"
          value = (self.var_roomno.get(),)
          my_cursor.execute(query,value)
       else:
          if not mDelete:
             return
       conn.commit()
       self.fetch_data()
       conn.close()
# Reset button
    def reset(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("")











if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()