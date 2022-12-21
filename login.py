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
from main import Face_Attendance
import mysql.connector


def main():
    win=Tk()
    apps=Login(win)
    win.mainloop()

class Login:
    def __init__(self,root):
        self.root = root
        self.root.geometry("400x500+600+200")
        self.root.title("Log In")

        #bg image
        img = Image.open(r"images\login_bg.png")
        img = img.resize((400,500) , Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root,image =self.photoimg)
        f_lbl.place(x = 0,y = 0,width=400,height=500)

        #usernameLabel
        username_lbl=Label(f_lbl,text="Email",font=("Comic Sans MS",15,"bold"),fg="white",bg="purple")
        username_lbl.place(x=30,y=200)
        

        #ussername etry
        self.txtuser=Entry(f_lbl,font=("Comic Sans MS",15,"bold"),bg="white",fg="black")
        self.txtuser.place(x=30,y=240,width=300)

        #passwordLabel
        password_lbl=Label(f_lbl,text="Password",font=("Comic Sans MS",15,"bold"),fg="white",bg="purple")
        password_lbl.place(x=30,y=290)
        

        #password entry
        self.txtpass=Entry(f_lbl,font=("Comic Sans MS",15,"bold"),bg="white",fg="black")
        self.txtpass.place(x=30,y=330,width=300)

        #log in button
        login_btn=Button(f_lbl,text="Log in",command=self.login,width=14,font=("Comic Sans MS",10,"bold"),bg="red",fg="white",activebackground="red",activeforeground="white")
        login_btn.place(x=30,y=370,width=150,height=40)

        #sign up button
        signup_btn=Button(f_lbl,text="Sign Up",command=self.register_window,width=14,font=("Comic Sans MS",8,"bold"),bg="purple",fg="white",borderwidth=0,activebackground="pink",activeforeground="white")
        signup_btn.place(x=30,y=440,width=80,height=30)

        #fogot pass up button
        forgotpass_btn=Button(f_lbl,text="Forgot Password??",command=self.forgot_password_window,width=14,font=("Comic Sans MS",8,"bold"),bg="purple",fg="white",borderwidth=0,activebackground="red",activeforeground="white")
        forgotpass_btn.place(x=160,y=440,width=120,height=30)

    #signup
    def register_window(self):
        self.window=Toplevel(self.root)
        self.app=Register(self.window)

    #Null entry function also log into anthoer class 
    def login(self):
        if self.txtuser.get()=="" or self.txtpass=="":
            messagebox.showerror("Error","Cannot be empty")
        elif self.txtuser.get()=="User" and self.txtpass.get()=="User":
            messagebox.showinfo("Success","Welcome")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="SHUVROshuvro123@",database="face_attendancesql1")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(self.txtuser.get(),self.txtpass.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("Yes or No","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Attendance(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
    
    #forget password
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="Adib",password="SHUVROshuvro123@",database="face_attendancesql1")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter valid email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("400x500+600+200") 

                forgot_pass_frame = LabelFrame(self.root2,bd=10,bg="light green",text="Forgot Password",relief=RIDGE,
                font=("Comic Sans MS",15,"bold"),fg="red")
                forgot_pass_frame.place(x=0,y=0,width=400,height=500,relwidth=0) 

                #select security question label
                Security_question_select_lbl=Label(forgot_pass_frame,text="Select Security Question",font=("Comic Sans MS",15,"bold"),fg="green",bg="light green")
                Security_question_select_lbl.place(x=20,y=30)    

                #combo box s q
                self.security_question_select_entry=ttk.Combobox(forgot_pass_frame,font=("Comic Sans MS",15,"bold"),state="readonly")
                self.security_question_select_entry["values"]=("Select","Your birth place","Your home town","Which food you like most",)
                self.security_question_select_entry.place(x=20,y=70,width=200)
                self.security_question_select_entry.current([0])

                #security answer label
                security_answer_lbl=Label(forgot_pass_frame,text="Security Answer",font=("Comic Sans MS",15,"bold"),fg="green",bg="light green")
                security_answer_lbl.place(x=20,y=130)

                #security answer enrty
                self.security_answer_entry=Entry(forgot_pass_frame,font=("Comic Sans MS",15,"bold"),bg="white",fg="black")
                self.security_answer_entry.place(x=20,y=170,width=200)

                #new password  label
                new_pass_lbl=Label(forgot_pass_frame,text="New Password",font=("Comic Sans MS",15,"bold"),fg="green",bg="light green")
                new_pass_lbl.place(x=20,y=230)

                #new password  enrty
                self.new_pass_entry=Entry(forgot_pass_frame,font=("Comic Sans MS",15,"bold"),bg="white",fg="black")
                self.new_pass_entry.place(x=20,y=270,width=200)

                #reset button
                rst_buton=Button(forgot_pass_frame,text="Reset",command=self.reset_pass,font=("Comic Sans MS",15,"bold"),bg="red",fg="white")
                rst_buton.place(x=10,y=400,width=200)

    #reset password
    def reset_pass(self):
        if self.security_question_select_entry.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.security_answer_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.new_pass_entry.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)

        else:
            conn=mysql.connector.connect(host="localhost",username="Adib",password="SHUVROshuvro123@",database="face_attendancesql1")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.security_question_select_entry.get(),self.security_answer_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.new_pass_entry.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been changed",parent=self.root2)

        




class Register:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1589x790+0+20")
        self.root.title("Register")

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_question_select_entry=StringVar()
        self.var_security_answer=StringVar()
        self.var_password=StringVar()
        self.var_confirm_password=StringVar()
        self.var_chkbtn=IntVar()

        #bg image
        self.bg = ImageTk.PhotoImage(file=r"images/st_bg_image.jpg")

        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,width=1589,height=810)

        #bg frame
        bg_frame = LabelFrame(self.root,bd=10,bg="light green",text="Register",relief=RIDGE,
        font=("Comic Sans MS",15,"bold"),fg="green")
        bg_frame.place(x=100,y=100,width=1200,height=610)

        # ==========================Labels and Entry========================
        #first name label
        fname_lbl=Label(bg_frame,text="First Name",font=("Comic Sans MS",15,"bold"),fg="green",bg="light green")
        fname_lbl.place(x=30,y=40)

        #first name entry
        self.fname_entry=Entry(bg_frame,textvariable=self.var_fname,font=("Comic Sans MS",15,"bold"),bg="white",fg="black")
        self.fname_entry.place(x=30,y=80,width=300)

        #last name label
        lname_lbl=Label(bg_frame,text="Last Name",font=("Comic Sans MS",15,"bold"),fg="green",bg="light green")
        lname_lbl.place(x=400,y=40)

        #last name entry
        self.lname_entry=Entry(bg_frame,textvariable=self.var_lname,font=("Comic Sans MS",15,"bold"),bg="white",fg="black")
        self.lname_entry.place(x=400,y=80,width=300)

        #conact label
        contact_lbl=Label(bg_frame,text="Contact",font=("Comic Sans MS",15,"bold"),fg="green",bg="light green")
        contact_lbl.place(x=30,y=130)

        #contact entry
        self.contact_entry=Entry(bg_frame,textvariable=self.var_contact,font=("Comic Sans MS",15,"bold"),bg="white",fg="black")
        self.contact_entry.place(x=30,y=170,width=300)

        #email name label
        email_lbl=Label(bg_frame,text="Email",font=("Comic Sans MS",15,"bold"),fg="green",bg="light green")
        email_lbl.place(x=400,y=130)

        #email name entry
        self.email_entry=Entry(bg_frame,textvariable=self.var_email,font=("Comic Sans MS",15,"bold"),bg="white",fg="black")
        self.email_entry.place(x=400,y=170,width=300)

        #select security question label
        Security_question_select_lbl=Label(bg_frame,text="Select Security Question",font=("Comic Sans MS",15,"bold"),fg="green",bg="light green")
        Security_question_select_lbl.place(x=30,y=220)    

        #combo box s q
        self.security_question_select_entry=ttk.Combobox(bg_frame,textvariable=self.var_security_question_select_entry,font=("Comic Sans MS",15,"bold"),state="readonly")
        self.security_question_select_entry["values"]=("Select","Your birth place","Your home town","Which food you like most",)
        self.security_question_select_entry.place(x=30,y=260,width=300)
        self.security_question_select_entry.current([0])

        #security answer label
        security_answer_lbl=Label(bg_frame,text="Security Answer",font=("Comic Sans MS",15,"bold"),fg="green",bg="light green")
        security_answer_lbl.place(x=400,y=220)

        #security answer enrty
        self.security_answer_entry=Entry(bg_frame,textvariable=self.var_security_answer,font=("Comic Sans MS",15,"bold"),bg="white",fg="black")
        self.security_answer_entry.place(x=400,y=260,width=300)

        #password label
        password_lbl=Label(bg_frame,text="Password",font=("Comic Sans MS",15,"bold"),fg="green",bg="light green")
        password_lbl.place(x=30,y=320)

        #password entry
        self.password_entry=Entry(bg_frame,textvariable=self.var_password,font=("Comic Sans MS",15,"bold"),bg="white",fg="black")
        self.password_entry.place(x=30,y=360,width=300)

        #confirm password label
        password_lbl=Label(bg_frame,text="Confirm Password",font=("Comic Sans MS",15,"bold"),fg="green",bg="light green")
        password_lbl.place(x=400,y=320)

        #confirm password entry
        self.password_entry=Entry(bg_frame,textvariable=self.var_confirm_password,font=("Comic Sans MS",15,"bold"),bg="white",fg="black")
        self.password_entry.place(x=400,y=360,width=300)

        #chcek button
        chkbutton=Checkbutton(bg_frame,variable=self.var_chkbtn,text="I Agree  to the terms and condtions",font=("Comic Sans MS",10,"bold"),bg="light green",onvalue=1,offvalue=0)
        chkbutton.place(x=30,y=400)

        #register button
        self.register1=Button(bg_frame,text="Register",command=self.register_data,width=17,font=("Comic Sans MS",10,"bold"),bg="light green",fg="red",activebackground="green",activeforeground="white")
        self.register1.place(x=30,y=440,width=250,height=40)


    #function declrearation for register data

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email=="" or self.var_security_question_select_entry.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        elif self.var_password.get()!=self.var_confirm_password.get():
            messagebox.showerror("Error","Both password must be same",parent=self.root)
        elif self.var_chkbtn.get() == 0:
            messagebox.showerror("Error","Please agree our terms and condition",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="Adib",password="SHUVROshuvro123@",database="face_attendancesql1")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User already exists,try another email")
            else:
                my_cursor.execute("insert into register value(%s,%s,%s,%s,%s,%s,%s)",(

                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_security_question_select_entry.get(),
                                                                                        self.var_security_answer.get(),
                                                                                        self.var_password.get()
                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered successfully!",parent=self.root)


if __name__=='__main__':
    main()