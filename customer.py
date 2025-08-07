from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class Cust_win:
    def __init__(self, root):  # Constructor call
        self.root = root  # Initialization of root
        self.root.title("Hotel Management System")
        self.root.geometry("1240x525+304+280")
        # ++++ Variables +++
        self.var_ref = StringVar()
        x = random.randint(1000,99999)
        self.var_ref.set(str(x))

        self.var_cus_name = StringVar()
        self.var_mother_name = StringVar()
        self.var_cus_gender = StringVar()
        self.var_cus_post = StringVar()
        self.var_cus_mobile = StringVar()
        self.var_cus_email = StringVar()
        self.var_cus_nationality = StringVar()
        self.var_cus_idproof = StringVar()
        self.var_cus_idnumber = StringVar()
        self.var_cus_address = StringVar()
      

         # Title
        lbl_title = Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1240,height=40)
 
        # Second Image Logo
        img2 = Image.open(r"C:\Users\anura\Downloads\Content\HotelLogo.jpg")
        img2 = img2.resize((80, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbl_img2.place(x=2, y=0, width=80, height=40)

       # Label Frame In Left
        labelFrameLeft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",14,"bold"),bg="white",fg="black")
        labelFrameLeft.place(x=5,y=40,width=360,height=460)

        # Labels and Entrys
        # Curt Ref
        label_cust_ref = Label(labelFrameLeft,text="Customer Ref",font=("arial",10,"bold"),padx=4,pady=6)
        label_cust_ref.grid(row=0,column=0,sticky=W)
        
        entry_ref = ttk.Entry(labelFrameLeft,textvariable=self.var_ref,font=("arial",9,"bold"),width = 29,state="readonly")
        entry_ref.grid(row=0,column=1)
        # Cust Name
        cname = Label(labelFrameLeft,text="Customer Name",font=("arial",10,"bold"),padx=4,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        
        cname_ref = ttk.Entry(labelFrameLeft,textvariable=self.var_cus_name,font=("arial",9,"bold"),width=29)
        cname_ref.grid(row=1,column=1)
        #mother name
        mname = Label(labelFrameLeft,text="Mother Name",font=("arial",10,"bold"),padx=4,pady=6)
        mname.grid(row=2,column=0,sticky=W)
        
        mname_ref = ttk.Entry(labelFrameLeft,textvariable=self.var_mother_name,font=("arial",9,"bold"),width=29)
        mname_ref.grid(row=2,column=1)
       
       # postcode
        pcode = Label(labelFrameLeft,text="PostCode",font=("arial",10,"bold"),padx=4,pady=6)
        pcode.grid(row=4,column=0,sticky=W)
        
        pcode_ref = ttk.Entry(labelFrameLeft,textvariable=self.var_cus_post,font=("arial",9,"bold"),width = 29)
        pcode_ref.grid(row=4,column=1)
        # Mobile Number
        mnumber = Label(labelFrameLeft,text="Mobile No.",font=("arial",10,"bold"),padx=4,pady=6)
        mnumber.grid(row=5,column=0,sticky=W)
        
        mnumber_ref = ttk.Entry(labelFrameLeft,textvariable=self.var_cus_mobile,font=("arial",9,"bold"),width=29)
        mnumber_ref.grid(row=5,column=1)
        #email
        email = Label(labelFrameLeft,text="Email",font=("arial",10,"bold"),padx=4,pady=6)
        email.grid(row=6,column=0,sticky=W)
        
        email_ref = ttk.Entry(labelFrameLeft,textvariable=self.var_cus_email,font=("arial",9,"bold"),width=29)
        email_ref.grid(row=6,column=1)
        # Gender
        gender = Label(labelFrameLeft,text="Gender",font=("arial",10,"bold"),padx=4,pady=6)
        gender.grid(row=3,column=0,sticky=W)
        gCombo = ttk.Combobox(labelFrameLeft,textvariable=self.var_cus_gender,font=("arial",9,"bold"),width=27,state="readonly")
        gCombo["value"] = ("Male","Female","Other")
        gCombo.current(0)
        gCombo.grid(row=3,column=1)
        # Nationality
        nationality = Label(labelFrameLeft,text="Nationality",font=("arial",10,"bold"),padx=4,pady=6)
        nationality.grid(row=7,column=0,sticky=W)
        nationatlity_ref = ttk.Combobox(labelFrameLeft,textvariable=self.var_cus_nationality,font=("arial",9,"bold"),width=27,state="readonly")
        nationatlity_ref["value"] = ("Indian","American","Britist","Chinese")
        nationatlity_ref.current(0)
        nationatlity_ref.grid(row=7,column=1)
        # ID Proof
        idProofe = Label(labelFrameLeft,text="ID Proof Type",font=("arial",10,"bold"),padx=4,pady=6)
        idProofe.grid(row=9,column=0,sticky=W)
        idProofe_ref = ttk.Combobox(labelFrameLeft,textvariable=self.var_cus_idproof,font=("arial",9,"bold"),width=27,state="readonly")
        idProofe_ref["value"] = ("AdharCard","DrivingLicence","Passport")
        idProofe_ref.current(0)
        idProofe_ref.grid(row=9,column=1)
        
         # Id Number
        idNumber = Label(labelFrameLeft,text="ID Number",font=("arial",10,"bold"),padx=4,pady=6)
        idNumber.grid(row=10,column=0,sticky=W)
        
        idNumber_ref = ttk.Entry(labelFrameLeft,textvariable=self.var_cus_idnumber,font=("arial",9,"bold"),width = 29)
        idNumber_ref.grid(row=10,column=1)
        # Cust Address
        address = Label(labelFrameLeft,text="Address",font=("arial",10,"bold"),padx=4,pady=6)
        address.grid(row=8,column=0,sticky=W)
        
        address_ref = ttk.Entry(labelFrameLeft,textvariable=self.var_cus_address,font=("arial",9,"bold"),width=29)
        address_ref.grid(row=8,column=1)

       # Buttons 
        btn_frame = Frame(labelFrameLeft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=360,width=360,height=40)

        btnAdd = Button(btn_frame,text="Add",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=2)

        btnupdate = Button(btn_frame,text="Update",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=2)

        btndelete = Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btndelete.grid(row=0,column=2,padx=2)

        btnreset = Button(btn_frame,text="Reset",command=self.reset,font=("arial",10,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=2)

       # Table Frame
        table_frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",14,"bold"),bg="white",fg="black")
        table_frame.place(x=360,y=40,width=860,height=460)
       # Text
        searchBy = Label(table_frame,text="Search By:",bg="red",fg="white",font=("arial",10,"bold"),padx=4,pady=6)
        searchBy.grid(row=0,column=0,sticky=W,padx=2)
       # Combo Box
        self.search_var = StringVar()
        searchBy_ref = ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",9,"bold"),width=24,state="readonly")
        searchBy_ref["value"] = ("Mobile","Ref")
        searchBy_ref.current(0)
        searchBy_ref.grid(row=0,column=1,padx=2)
         #input field
        self.txt_search = StringVar()
        txtSearch = ttk.Entry(table_frame,textvariable=self.txt_search,font=("arial",10,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)
        #buttons
        btnsearch = Button(table_frame,text="Search",command=self.search,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnsearch.grid(row=0,column=3,padx=2)

        btnshowAll = Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",10,"bold"),bg="black",fg="gold",width=9)
        btnshowAll.grid(row=0,column=4,padx=2)

      #  Show Data Table
        details_frame = Frame(table_frame,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=50,width=855,height=350)

         # Scrollable Table
        scroll_x = ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.Cust_Details_table = ttk.Treeview(details_frame,columns=("ref","name","mother","postcode","mobile","email","gender","nationality","address","idproof","idnumber"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_table.xview)
        scroll_y.config(command=self.Cust_Details_table.yview)

       # table Making
        self.Cust_Details_table.heading("ref",text="Refer No")
        self.Cust_Details_table.heading("name",text="Name")
        self.Cust_Details_table.heading("mother",text="Mother Name")
        self.Cust_Details_table.heading("gender",text="Gender")
        self.Cust_Details_table.heading("postcode",text="PostCode")
        self.Cust_Details_table.heading("mobile",text="Mobile No.")
        self.Cust_Details_table.heading("email",text="Email")
        self.Cust_Details_table.heading("nationality",text="Nationality")
        self.Cust_Details_table.heading("address",text="Address")
        self.Cust_Details_table.heading("idproof",text="ID Proof")
        self.Cust_Details_table.heading("idnumber",text="Id Number")


       # table Customization
        self.Cust_Details_table["show"] = "headings"
        self.Cust_Details_table.column("ref",width=100)
        self.Cust_Details_table.column("name",width=100)
        self.Cust_Details_table.column("mother",width=100)
        self.Cust_Details_table.column("gender",width=100)
        self.Cust_Details_table.column("postcode",width=100)
        self.Cust_Details_table.column("mobile",width=100)
        self.Cust_Details_table.column("email",width=100)
        self.Cust_Details_table.column("nationality",width=100)
        self.Cust_Details_table.column("address",width=100)
        self.Cust_Details_table.column("idproof",width=100)
        self.Cust_Details_table.column("idnumber",width=100)

        


        self.Cust_Details_table.pack(fill=BOTH,expand=1)
        self.Cust_Details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_cus_mobile.get()=="" or self.var_cus_idproof.get()=="":
            messagebox.showerror("Error","Please Fill all the Details",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Mohit@468",database = "hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customerd values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                      self.var_ref.get(),
                      self.var_cus_name.get(),
                      self.var_mother_name.get(),
                      self.var_cus_gender.get(),
                      self.var_cus_post.get(),
                      self.var_cus_mobile.get(),
                      self.var_cus_email.get(),
                      self.var_cus_nationality.get(),
                      self.var_cus_address.get(),
                      self.var_cus_idnumber.get(),
                      self.var_cus_idproof.get()
                      
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "customer has been added",parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning",f"Something went wrong!:{str(e)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Mohit@468",database = "hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customerd")
        rows = my_cursor.fetchall()
        for child in self.Cust_Details_table.get_children():
           self.Cust_Details_table.delete(child)
        if rows:
            for i in rows:
                self.Cust_Details_table.insert("",END,values=i)
        conn.commit()
        conn.close()



    # show data in table when i click any entry
    def get_cursor(self, event=""):
     cursor_row = self.Cust_Details_table.focus() 
     content = self.Cust_Details_table.item(cursor_row)  
     row = content["values"] 
     if row:  
        self.var_ref.set(row[0]), 
        self.var_cus_name.set(row[1]), 
        self.var_mother_name.set(row[2]), 
        self.var_cus_gender.set(row[3]),
        self.var_cus_post.set(row[4]),
        self.var_cus_mobile.set(row[5]), 
        self.var_cus_email.set(row[6]),
        self.var_cus_nationality.set(row[7]),  
        self.var_cus_address.set(row[8]),  
        self.var_cus_idproof.set(row[9]), 
        self.var_cus_idnumber.set(row[10]), 



    # Updating the data
    def update(self):
     if self.var_cus_mobile.get() == "" or self.var_cus_idproof.get() == "" or self.var_cus_idnumber.get() == "":
        messagebox.showerror("Error", "Please fill all the details", parent=self.root)
     else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mohit@468", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "UPDATE customerd SET Name=%s, Mother=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Nationality=%s, Address=%s, IDProof=%s, IdNumber=%s WHERE Ref=%s",
                (
                    self.var_cus_name.get(),
                    self.var_mother_name.get(),
                    self.var_cus_gender.get(),
                    self.var_cus_post.get(),
                    self.var_cus_mobile.get(),
                    self.var_cus_email.get(),
                    self.var_cus_nationality.get(),
                    self.var_cus_address.get(),
                    self.var_cus_idproof.get(),
                    self.var_cus_idnumber.get(),
                    self.var_ref.get()
                )
            )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details have been updated successfully", parent=self.root)
        except Exception as e:
            messagebox.showwarning("Warning", f"Something went wrong: {str(e)}", parent=self.root)
    #Delete the data
    def mDelete(self):
       mDelete = messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent = self.root)
       if mDelete>0:
          conn = mysql.connector.connect(host="localhost", username="root", password="Mohit@468", database="hotel")
          my_cursor = conn.cursor()
          query="delete from customerd where Ref=%s"
          value = (self.var_ref.get(),)
          my_cursor.execute(query,value)
       else:
          if not mDelete:
             return
       conn.commit()
       self.fetch_data()
       conn.close()
          
    def reset(self):
        #self.var_ref.set(""),
        self.var_cus_name.set(""), 
        self.var_mother_name.set(""), 
        # self.var_cus_gender.set(""), 
        self.var_cus_post.set(""), 
        self.var_cus_mobile.set(""),  
        self.var_cus_email.set(""), 
        # self.var_cus_nationality.set(""),  
        self.var_cus_address.set(""),  
        # self.var_cus_idproof.set(""), 
        self.var_cus_idnumber.set(r"")
        x = random.randint(1000,99999)
        self.var_ref.set(str(x))
    def search(self):  
     if not self.txt_search.get():
        messagebox.showerror("Error", "Please enter a search term.", parent=self.root)
        return

     try:
        conn = mysql.connector.connect(host="localhost", username="root", password="Mohit@468", database="hotel")
        my_cursor = conn.cursor()

        # Use parameterized queries to prevent SQL injection
        query = "SELECT * FROM customerd WHERE {} LIKE %s".format(self.search_var.get())
        value = ("%{}%".format(self.txt_search.get()),)
        my_cursor.execute(query, value)

        rows = my_cursor.fetchall()
        self.Cust_Details_table.delete(*self.Cust_Details_table.get_children())  # Clear existing rows
        
        if rows:
            for row in rows:
                self.Cust_Details_table.insert("", END, values=row)
        else:
            messagebox.showinfo("No Results", "No matching records found.", parent=self.root)
        
        conn.commit()
        conn.close()
     except Exception as e:
        messagebox.showwarning("Warning", f"Something went wrong: {str(e)}", parent=self.root)






if __name__ == "__main__":
    root = Tk()
    obj = Cust_win(root)
    root.mainloop()