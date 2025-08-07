from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self, root):  # Constructor call
        self.root = root  # Initialization of root
        self.root.title("Hotel Management System")
        self.root.geometry("1240x525+304+280")

# variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

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
        labelFrameLeft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman",14,"bold"),bg="white",fg="black")
        labelFrameLeft.place(x=5,y=40,width=360,height=460)
#  Labels and entry 
# Customer Conatct
        label_cust_contact = Label(labelFrameLeft,text="Customer Contact: ",font=("arial",10,"bold"),padx=4,pady=6)
        label_cust_contact.grid(row=0,column=0,sticky=W)
        entry_contact = ttk.Entry(labelFrameLeft,textvariable=self.var_contact,font=("arial",9,"bold"),width = 20)
        entry_contact.grid(row=0,column=1,sticky=W)
# Fetch data button
        btnfetch_data = Button(labelFrameLeft,command=self.fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnfetch_data.place(x=280,y=4)
# check in date
        check_in_date = Label(labelFrameLeft,text="Check_in Date: ",font=("arial",10,"bold"),padx=4,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date = ttk.Entry(labelFrameLeft,textvariable=self.var_checkin,font=("arial",9,"bold"),width = 29)
        txtcheck_in_date.grid(row=1,column=1)
# check out date
        check_out_date = Label(labelFrameLeft,text="Check_out Date: ",font=("arial",10,"bold"),padx=4,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)
        txtcheck_out_date = ttk.Entry(labelFrameLeft,textvariable=self.var_checkout,font=("arial",9,"bold"),width = 29)
        txtcheck_out_date.grid(row=2,column=1)
# room type
        room_type = Label(labelFrameLeft,text="Room Type:",font=("arial",10,"bold"),padx=4,pady=6)
        room_type.grid(row=3,column=0,sticky=W)
        # Creating DataBase
        conn = mysql.connector.connect(host="localhost",username="root",password="Mohit@468",database = "hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        rType = my_cursor.fetchall()
        Combo_room_type = ttk.Combobox(labelFrameLeft,textvariable=self.var_roomtype,font=("arial",9,"bold"),width=27,state="readonly")
        Combo_room_type["value"] = rType
        Combo_room_type.current(0)
        Combo_room_type.grid(row=3,column=1)
#Available Room
        lblroom_available = Label(labelFrameLeft,text="Available Room: ",font=("arial",10,"bold"),padx=4,pady=6)
        lblroom_available.grid(row=4,column=0,sticky=W)
        # txtroom_available = ttk.Entry(labelFrameLeft,textvariable=self.var_roomavailable,font=("arial",9,"bold"),width = 29)
        # txtroom_available.grid(row=4,column=1)

# Creating DataBase
        conn = mysql.connector.connect(host="localhost",username="root",password="Mohit@468",database = "hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()
        Combo_RoomNo = ttk.Combobox(labelFrameLeft,textvariable=self.var_roomavailable,font=("arial",9,"bold"),width=27,state="readonly")
        Combo_RoomNo["value"] = rows
        Combo_RoomNo.current(0)
        Combo_RoomNo.grid(row=4,column=1)

# Meal
        meal = Label(labelFrameLeft,text="Meal: ",font=("arial",10,"bold"),padx=4,pady=6)
        meal.grid(row=5,column=0,sticky=W)
        txtmeal = ttk.Entry(labelFrameLeft,textvariable=self.var_meal,font=("arial",9,"bold"),width = 29)
        txtmeal.grid(row=5,column=1)

# number of days
        NoofDays = Label(labelFrameLeft,text="No of Days: ",font=("arial",10,"bold"),padx=4,pady=6)
        NoofDays.grid(row=6,column=0,sticky=W)
        txtNoofDays = ttk.Entry(labelFrameLeft,textvariable=self.var_noofdays,font=("arial",9,"bold"),width = 29)
        txtNoofDays.grid(row=6,column=1)

# Paid Tax
        paidTax = Label(labelFrameLeft,text="Paid tax: ",font=("arial",10,"bold"),padx=4,pady=6)
        paidTax.grid(row=7,column=0,sticky=W)
        txtpaidTax = ttk.Entry(labelFrameLeft,textvariable=self.var_paidtax,font=("arial",9,"bold"),width = 29)
        txtpaidTax.grid(row=7,column=1)

#Sub Total
        sub_total = Label(labelFrameLeft,text="Sub total: ",font=("arial",10,"bold"),padx=4,pady=6)
        sub_total.grid(row=8,column=0,sticky=W)
        txtsub_total = ttk.Entry(labelFrameLeft,textvariable=self.var_actualtotal,font=("arial",9,"bold"),width = 29)
        txtsub_total.grid(row=8,column=1)

# Total Cost
        TotalCost = Label(labelFrameLeft,text="Total Cost: ",font=("arial",10,"bold"),padx=4,pady=6)
        TotalCost.grid(row=9,column=0,sticky=W)
        txtTotalCost = ttk.Entry(labelFrameLeft,textvariable=self.var_total,font=("arial",9,"bold"),width = 29)
        txtTotalCost.grid(row=9,column=1)
# Bill button
        btnbillButton = Button(labelFrameLeft,text="Bill",command=self.Total_cost,font=("arial",10,"bold"),bg="black",fg="gold",width=8)
        btnbillButton.grid(row=10,column=0,padx=1)
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

# Right Side Image
        img3 = Image.open(r"C:\Users\anura\Downloads\Content\bed1.jpg")
        img3 = img3.resize((520, 260), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lbl_img3.place(x=710, y=40, width=520, height=260)

 # Table Frame and search system
        table_frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",14,"bold"),bg="white",fg="black")
        table_frame.place(x=360,y=240,width=860,height=260)
       # Text
        searchBy = Label(table_frame,text="Search By:",bg="red",fg="white",font=("arial",10,"bold"),padx=4,pady=6)
        searchBy.grid(row=0,column=0,sticky=W,padx=2)
       # Combo Box
        self.search_var = StringVar()
        searchBy_ref = ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",9,"bold"),width=24,state="readonly")
        searchBy_ref["value"] = ("Contact","Room")
        searchBy_ref.current(0)
        searchBy_ref.grid(row=0,column=1,padx=2)
         #input field
        self.txt_search = StringVar()
        txtSearch = ttk.Entry(table_frame,textvariable=self.txt_search,font=("arial",10,"bold"),width=30)
        txtSearch.grid(row=0,column=2,padx=2)
        #buttons
        btnsearch = Button(table_frame,text="Search",command=self.search,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnsearch.grid(row=0,column=3,padx=2)

        btnshowAll = Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnshowAll.grid(row=0,column=4,padx=2)

    #  Show Data Table
        details_frame = Frame(table_frame,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=50,width=855,height=180)

         # Scrollable Table
        scroll_x = ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.room_Details_table = ttk.Treeview(details_frame,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_Details_table.xview)
        scroll_y.config(command=self.room_Details_table.yview)

       # table Making
        self.room_Details_table.heading("contact",text="Contact")
        self.room_Details_table.heading("checkin",text="Check-In")
        self.room_Details_table.heading("checkout",text="Check-Out")
        self.room_Details_table.heading("roomtype",text="Room Type")
        self.room_Details_table.heading("roomavailable",text="Room No")
        self.room_Details_table.heading("meal",text="Meal")
        self.room_Details_table.heading("noOfdays",text="NoOfDays")

       # table Customization
        self.room_Details_table["show"] = "headings"
        self.room_Details_table.column("contact",width=100)
        self.room_Details_table.column("checkin",width=100)
        self.room_Details_table.column("checkout",width=100)
        self.room_Details_table.column("roomtype",width=100)
        self.room_Details_table.column("roomavailable",width=100)
        self.room_Details_table.column("meal",width=100)
        self.room_Details_table.column("noOfdays",width=100)

        self.room_Details_table.pack(fill=BOTH,expand=1)

        self.room_Details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
# Adding data
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","Please Fill all the Details",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Mohit@468",database = "hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                    
                        self.var_contact.get(),
                        self.var_checkin.get(),
                        self.var_checkout.get(),
                        self.var_roomtype.get(),
                        self.var_roomavailable.get(),
                        self.var_meal.get(),
                        self.var_noofdays.get()
                      
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Booked Successfully",parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning",f"Something went wrong!:{str(e)}",parent=self.root)
# Fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Mohit@468",database = "hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
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
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])
# Search System
    def search(self):  
     try:
        conn = mysql.connector.connect(host="localhost", username="root", password="Mohit@468", database="hotel")
        my_cursor = conn.cursor()
        query = "SELECT * FROM room WHERE {} LIKE %s".format(self.search_var.get())
        value = ("%{}%".format(self.txt_search.get()),)
        my_cursor.execute(query, value)

        rows = my_cursor.fetchall()
        self.room_Details_table.delete(*self.room_Details_table.get_children()) 
        if rows:
            for row in rows:
                self.room_Details_table.insert("", END, values=row)
        else:
            messagebox.showinfo("No Results", "No matching records found.", parent=self.root)       
        conn.commit()
        conn.close()
     except Exception as e:
        messagebox.showwarning("Warning", f"Something went wrong: {str(e)}", parent=self.root)

# Updating the data
    def update(self):
     if self.var_contact.get() == "" or self.var_checkin.get() == "" or self.var_checkout.get() == "":
        messagebox.showerror("Error", "Please fill all the details", parent=self.root)
     else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mohit@468", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "UPDATE room SET check_in=%s, check_out=%s, roomtype=%s, roomavailable=%s, meal=%s, noOfdays=%s WHERE Contact=%s",
                (
                       
                        self.var_checkin.get(),
                        self.var_checkout.get(),
                        self.var_roomtype.get(),
                        self.var_roomavailable.get(),
                        self.var_meal.get(),
                        self.var_noofdays.get(),
                        self.var_contact.get(),
                )
            )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details have been updated successfully", parent=self.root)
        except Exception as e:
            messagebox.showwarning("Warning", f"Something went wrong: {str(e)}", parent=self.root)


#Delete the data
    def mDelete(self):
       mDelete = messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent = self.root)
       if mDelete>0:
          conn = mysql.connector.connect(host="localhost", username="root", password="Mohit@468", database="hotel")
          my_cursor = conn.cursor()
          query="delete from room where Contact=%s"
          value = (self.var_contact.get(),)
          my_cursor.execute(query,value)
       else:
          if not mDelete:
             return
       conn.commit()
       self.fetch_data()
       conn.close()
# Reset button
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")



# Fetch all data
    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error","Please Enter Contact number!",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="Mohit@468",database = "hotel")
            my_cursor = conn.cursor()
            query = "select Name from customerd where Mobile=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                shoDataframe = Frame(self.root,bd=4,relief=RIDGE,padx=2)
                shoDataframe.place(x=370,y=40,width=360,height=200)
#name
                lblName = Label(shoDataframe,text="Name: ",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)
                lbl = Label(shoDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=80,y=0)
#Gender
                conn = mysql.connector.connect(host="localhost",username="root",password="Mohit@468",database = "hotel")
                my_cursor = conn.cursor()
                query = "select Gender from customerd where Mobile=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender = Label(shoDataframe,text="Gender: ",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)
                lbl2 = Label(shoDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=80,y=30)
#Email
                conn = mysql.connector.connect(host="localhost",username="root",password="Mohit@468",database = "hotel")
                my_cursor = conn.cursor()
                query = "select Email from customerd where Mobile=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblEmail = Label(shoDataframe,text="Email: ",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)
                lbl3 = Label(shoDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=80,y=60)

# Id proof
                conn = mysql.connector.connect(host="localhost",username="root",password="Mohit@468",database = "hotel")
                my_cursor = conn.cursor()
                query = "select IDProof from customerd where Mobile=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblIDProof = Label(shoDataframe,text="IDProof: ",font=("arial",12,"bold"))
                lblIDProof.place(x=0,y=90)
                lbl4 = Label(shoDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=80,y=90)
# Id Number
                conn = mysql.connector.connect(host="localhost",username="root",password="Mohit@468",database = "hotel")
                my_cursor = conn.cursor()
                query = "select IDNumber from customerd where Mobile=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblIDNumber = Label(shoDataframe,text="IDNumber: ",font=("arial",12,"bold"))
                lblIDNumber.place(x=0,y=120)
                lbl5 = Label(shoDataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)
#Nationality
                conn = mysql.connector.connect(host="localhost",username="root",password="Mohit@468",database = "hotel")
                my_cursor = conn.cursor()
                query = "select Nationality from customerd where Mobile=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality = Label(shoDataframe,text="Nationality: ",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=150)
                lbl6 = Label(shoDataframe,text=row,font=("arial",12,"bold"))
                lbl6.place(x=100,y=150)
    def Total_cost(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get() == "Laxary"):
            q1 = float(300)
            q2 = float(500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs. " +str("%.2f"%((q5)*0.2))
            St = "Rs. " +str("%.2f"%((q5)))
            TT = "Rs. " +str("%.2f"%(q5+((q5)*0.2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Launch" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs. " +str("%.2f"%((q5)*0.02))
            St = "Rs. " +str("%.2f"%((q5)))
            TT = "Rs. " +str("%.2f"%(q5+((q5)*0.02)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get() == "Laxary"):
            q1 = float(300)
            q2 = float(500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs. " +str("%.2f"%((q5)*0.4))
            St = "Rs. " +str("%.2f"%((q5)))
            TT = "Rs. " +str("%.2f"%(q5+((q5)*0.4)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get() == "Double"):
            q1 = float(300)
            q2 = float(500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs. " +str("%.2f"%((q5)*0.3))
            St = "Rs. " +str("%.2f"%((q5)))
            TT = "Rs. " +str("%.2f"%(q5+((q5)*0.3)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get() == "Double"):
            q1 = float(300)
            q2 = float(500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs. " +str("%.2f"%((q5)*0.2))
            St = "Rs. " +str("%.2f"%((q5)))
            TT = "Rs. " +str("%.2f"%(q5+((q5)*0.2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs. " +str("%.2f"%((q5)*0.2))
            St = "Rs. " +str("%.2f"%((q5)))
            TT = "Rs. " +str("%.2f"%(q5+((q5)*0.2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Launch" and self.var_roomtype.get() == "Duplex"):
            q1 = float(500)
            q2 = float(600)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs. " +str("%.2f"%((q5)*0.2))
            St = "Rs. " +str("%.2f"%((q5)))
            TT = "Rs. " +str("%.2f"%(q5+((q5)*0.2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get() == "Couple"):
            q1 = float(350)
            q2 = float(500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs. " +str("%.2f"%((q5)*0.2))
            St = "Rs. " +str("%.2f"%((q5)))
            TT = "Rs. " +str("%.2f"%(q5+((q5)*0.2)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(TT)





if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()