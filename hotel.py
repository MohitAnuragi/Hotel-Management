from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_win
from room import Roombooking
from detail import DetailsRoom

class HotelManagementSystem:
    def __init__(self, root):  # Constructor call
        self.root = root  # Initialization of root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        
        # First Image
        img1 = Image.open(r"C:\Users\anura\Downloads\Content\hotel1.jpeg")
        img1 = img1.resize((1600, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lbl_img1.place(x=0, y=0, width=1600, height=200)
        
        # Second Image Logo
        img2 = Image.open(r"C:\Users\anura\Downloads\Content\HotelLogo.jpg")
        img2 = img2.resize((300, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbl_img2.place(x=0, y=0, width=300, height=200)

        # Title
        lbl_title = Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=200,width=1600,height=50)

        # Main Frame
        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=250,width=1600,height=600)
        # MENU
        lbl_menu = Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="white",fg="black",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=300)
        # Btn Frame
        btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=30,width=300,height=200)
        # Buttons
        cust_btn = Button(btn_frame,text="CUSTOMERS",command=self.cust_details,width=26,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame,text="ROOMS",command=self.roombooking,width=26,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn = Button(btn_frame,text="DETAILS",command=self.details_room,width=26,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn = Button(btn_frame,text="REPORT",width=26,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn = Button(btn_frame,text="LOGOUT",command=self.logout,width=26,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        #  Right Side Image
        img3 = Image.open(r"C:\Users\anura\Downloads\Content\view.jpeg")
        img3 = img3.resize((1360, 524), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lbl_img3.place(x=300, y=0, width=1360, height=524)
       # Down Images
        img4 = Image.open(r"C:\Users\anura\Downloads\Content\hotel.jpg")
        img4 = img4.resize((300, 160), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lbl_img4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lbl_img4.place(x=0, y=220, width=300, height=160)

        img5 = Image.open(r"C:\Users\anura\Downloads\Content\food.WEBP")
        img5 = img5.resize((300, 160), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lbl_img5 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lbl_img5.place(x=0, y=370, width=300, height=160)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_win(self.new_window)
    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)
    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)
    def logout(self):
        self.root.destroy()







if __name__ == "__main__":  # Object call
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
