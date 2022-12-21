from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
import os
from time import strftime
from datetime import datetime
from tkinter import messagebox

class Face_Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1580x790+0+0")
        self.root.title("Face Attendance")

        #Background image
        img2 = Image.open(r"images\bg_img.jpg")
        img2 = img2.resize((1580,900) , Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img = Label(self.root,image =self.photoimg2)
        bg_img.place(x = 0,y = 0,width=1536,height=900)


        #clock
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)


        lbl= Label(self.root,font=("Comic Sans MS",9,"bold"),background="light green",foreground="navy blue")
        lbl.place(x=0,y=2,width=90,height=50)
        time()

        #Student button
        img3 = Image.open(r"images\st_button.png")
        img3 = img3.resize((220,220) , Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_img,image = self.photoimg3,command=self.student_details,cursor="hand2")
        b1.place(x=400,y=200,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Comic Sans MS",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=400,y=410,width=220,height=30)

        #Recognize face button
        img4 = Image.open(r"images\face_detection.png")
        img4 = img4.resize((220,220) , Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img,image = self.photoimg4,cursor="hand2",command=self.face_recognition_data)
        b1.place(x=700,y=200,width=220,height=220)
        b1_1 = Button(bg_img,text="Face Recognition",cursor="hand2",command=self.face_recognition_data,font=("Comic Sans MS",15,"bold"),bg="white",fg="grey")
        b1_1.place(x=700,y=410,width=220,height=30)

        #Attendance button
        img5 = Image.open(r"images\Attendance_img.jpg")
        img5 = img5.resize((220,220) , Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img,image = self.photoimg5,cursor="hand2",command=self.Attendance_management)
        b1.place(x=1000,y=200,width=220,height=220)
        b1_1 = Button(bg_img,text="Attendance",cursor="hand2",command=self.Attendance_management,font=("Comic Sans MS",15,"bold"),bg="white",fg="orange")
        b1_1.place(x=1000,y=410,width=220,height=30)

        #Train face button
        img7 = Image.open(r"images\train_faces.jpg")
        img7 = img7.resize((220,220) , Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img,image = self.photoimg7,cursor="hand2",command=self.train_data)
        b1.place(x=400,y=500,width=220,height=220)
        b1_1 = Button(bg_img,text="Train Faces",cursor="hand2",command=self.train_data,font=("Comic Sans MS",15,"bold"),bg="white",fg="purple")
        b1_1.place(x=400,y=710,width=220,height=30)

        #photos button
        img8 = Image.open(r"images\photos_image.jpg")
        img8 = img8.resize((220,220) , Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img,image = self.photoimg8,command=self.open_image,cursor="hand2")
        b1.place(x=700,y=500,width=220,height=220)
        b1_1 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_image,font=("Comic Sans MS",15,"bold"),bg="white",fg="green")
        b1_1.place(x=700,y=710,width=220,height=30)


        #Exit button
        img10 = Image.open(r"images\Exit_image.jpg")
        img10 = img10.resize((220,220) , Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img,image = self.photoimg10,cursor="hand2",command=self.exit)
        b1.place(x=1000,y=500,width=220,height=220)
        b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("Comic Sans MS",15,"bold"),bg="white",fg="red")
        b1_1.place(x=1000,y=710,width=220,height=30)

    #image directory
    def open_image(self):
        os.startfile("data")

    #=====function buttons=====
    #student details
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    #train data    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    #Face recognition    
    def face_recognition_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window) 


    #Attendance management system
    def Attendance_management(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


    #Exit
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Attendance","Exit this project??",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return


if __name__=='__main__':
    root = Tk()
    obj = Face_Attendance(root)
    root.mainloop()

    