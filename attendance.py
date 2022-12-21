from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1580x790+0+0")
        self.root.title("Attendance Management System")

        #text variables
        self.variable_atten_id=StringVar()
        self.variable_atten_name=StringVar()
        self.variable_atten_dep=StringVar()
        self.variable_atten_time=StringVar()
        self.variable_atten_date=StringVar()
        self.variable_atten_attendance=StringVar()



        #Attendance bg
        attendance_bg_img = Image.open(r"images\Attendance_bg.png")
        attendance_bg_img = attendance_bg_img.resize((1580,790) , Image.ANTIALIAS)
        self.photo_attendance = ImageTk.PhotoImage(attendance_bg_img)
        attendance_frame_img = Label(self.root,image =self.photo_attendance)
        attendance_frame_img.place(x = 0,y = 0,width=1537,height=800)

        #left label frame
        left_frame = LabelFrame(self.root,bd=2,bg="light green",relief=RIDGE,text="Student Attendance Details",
        font=("Comic Sans MS",15,"bold"),fg="green")
        left_frame.place(x=10,y=170,width=740,height=625)


        #id
        studentID_label = Label(left_frame,text="ID",font=("Comic Sans MS",15,"bold"),bg="light green")
        studentID_label.grid(row=2,column=0)
        studentID_entry = Entry(left_frame,width=20,textvariable=self.variable_atten_id,font=("Comic Sans MS",15,"bold"),bg="light green")
        studentID_entry.grid(row=2,column=1)

        #Name
        studentname_label = Label(left_frame,text="Name",font=("Comic Sans MS",15,"bold"),bg="light green")
        studentname_label.grid(row=3,column=0)
        studentname_entry = Entry(left_frame,width=20,textvariable=self.variable_atten_name,font=("Comic Sans MS",15,"bold"),bg="light green")
        studentname_entry.grid(row=3,column=1)

        #department
        studentdep_label = Label(left_frame,text="Department",font=("Comic Sans MS",15,"bold"),bg="light green")
        studentdep_label.grid(row=4,column=0)
        studentdep_entry = Entry(left_frame,width=20,textvariable=self.variable_atten_dep,font=("Comic Sans MS",15,"bold"),bg="light green")
        studentdep_entry.grid(row=4,column=1)

        #time
        studenttime_label = Label(left_frame,text="Time",font=("Comic Sans MS",15,"bold"),bg="light green")
        studenttime_label.grid(row=5,column=0)
        studenttime_entry = Entry(left_frame,width=20,textvariable=self.variable_atten_time,font=("Comic Sans MS",15,"bold"),bg="light green")
        studenttime_entry.grid(row=5,column=1)


        #date
        studentdate_label = Label(left_frame,text="Date",font=("Comic Sans MS",15,"bold"),bg="light green")
        studentdate_label.grid(row=6,column=0)
        studentdate_entry = Entry(left_frame,width=20,textvariable=self.variable_atten_date,font=("Comic Sans MS",15,"bold"),bg="light green")
        studentdate_entry.grid(row=6,column=1)

        #Attendance Status
        attstatus_label = Label(left_frame,text="Attendance status",font=("Comic Sans MS",15,"bold"),bg="light green")
        attstatus_label.grid(row=7,column=0)
        attstatus_combo=ttk.Combobox(left_frame,font=("Comic Sans MS",12,"bold"),width=17,textvariable=self.variable_atten_attendance,state="readonly")
        attstatus_combo["values"]=("Attendance Status","Present","Absent")
        attstatus_combo.current(0)
        attstatus_combo.grid(row=7,column=1,padx=10,pady=10,sticky=W)

        #button frame
        btn_frame = Frame(left_frame,bd=2,relief=RIDGE , bg="pink")
        btn_frame.place(x=5,y=400,width=705,height=57)

        #import button
        save_btn=Button(btn_frame,text="Import csv",command=self.ImportCsv,width=19,font=("Comic Sans MS",15,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        #export button
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=18,font=("Comic Sans MS",15,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)


        #Reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("Comic Sans MS",15,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)

        #right label frame
        right_frame = LabelFrame(self.root,bd=2,bg="light green",relief=RIDGE,text="Attendance Details",
        font=("Comic Sans MS",15,"bold"),fg="green")
        right_frame.place(x=755,y=170,width=775,height=625)

        table_frame = LabelFrame(right_frame,bd=2,bg="light green",relief=RIDGE,
        font=("Comic Sans MS",15,"bold"),fg="green")
        table_frame.place(x=4,y=0,width=760,height=590)

        #Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.Attendancereporttable=ttk.Treeview(table_frame,column=("ID","Name","Dep","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Attendancereporttable.xview)
        scroll_y.config(command=self.Attendancereporttable.yview)

        self.Attendancereporttable.heading("ID",text="ID")
        self.Attendancereporttable.heading("Name",text="Name")
        self.Attendancereporttable.heading("Dep",text="Department")
        self.Attendancereporttable.heading("Time",text="Time")
        self.Attendancereporttable.heading("Date",text="Date")
        self.Attendancereporttable.heading("Attendance",text="Attendance")

        self.Attendancereporttable["show"]="headings"

        self.Attendancereporttable.column("ID",width=100)
        self.Attendancereporttable.column("Name",width=100)
        self.Attendancereporttable.column("Dep",width=100)
        self.Attendancereporttable.column("Time",width=100)
        self.Attendancereporttable.column("Date",width=100)
        self.Attendancereporttable.column("Attendance",width=100)
 

        self.Attendancereporttable.pack(fill=BOTH,expand=1)
        
        self.Attendancereporttable.bind("<ButtonRelease>",self.get_cursor)

    #face data
    def facedata(self,rows):
        self.Attendancereporttable.delete(*self.Attendancereporttable.get_children())

        for i in rows:
            self.Attendancereporttable.insert("",END,values=i)

    #import csv
    def ImportCsv(self):
        global mydata
        mydata.clear()
        flname=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALl File","*.*")),parent=self.root)
        with open(flname) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.facedata(mydata)

    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data To Export",parent=self.root)
                return False
            flname=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALl File","*.*")),parent=self.root)
            with open(flname,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","You data exported to "+os.path.basename(flname)+" successfully!")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.Attendancereporttable.focus()
        content=self.Attendancereporttable.item(cursor_row)
        rows=content['values']
        self.variable_atten_id.set(rows[0])
        self.variable_atten_name.set(rows[1])
        self.variable_atten_dep.set(rows[2])
        self.variable_atten_time.set(rows[3])
        self.variable_atten_date.set(rows[4])
        self.variable_atten_attendance.set(rows[5])

    #reset att data
    def reset_data(self):
        self.variable_atten_id.set("")
        self.variable_atten_name.set("")
        self.variable_atten_dep.set("")
        self.variable_atten_time.set("")
        self.variable_atten_date.set("")
        self.variable_atten_attendance.set("")





if __name__=='__main__':
    root = Tk()
    obj = Attendance(root)
    root.mainloop()