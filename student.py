from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1580x790+0+0")
        self.root.title("Student Details")

        #Variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_section=StringVar()
        self.var_student_id=StringVar()
        self.var_student_name=StringVar()
        self.var_reg=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()


        #Student background image
        img2 = Image.open(r"images\st_bg_image.jpg")
        img2 = img2.resize((1536,910) , Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img = Label(self.root,image =self.photoimg2)
        bg_img.place(x = 0,y = 0,width=1536,height=910)

        #Student Frame
        main_frame = Frame(bg_img,bd=2,bg="light green")
        main_frame.place(x = 20,y=30,width=1480,height=630)

        #Left label Frame
        left_frame = LabelFrame(main_frame,bd=2,bg="light green",relief=RIDGE,text="Information",
        font=("Comic Sans MS",15,"bold"),fg="green")
        left_frame.place(x=10,y=10,width=740,height=610)

        #current course
        current_course_frame = LabelFrame(left_frame,bd=2,bg="light green",relief=RIDGE,text="Current Course",
        font=("Comic Sans MS",15,"bold"),fg="green")
        current_course_frame.place(x=5,y=50,width=725,height=150)

        #Department
        dep_label = Label(current_course_frame,text="Department",font=("Comic Sans MS",15,"bold"),bg="light green")
        dep_label.grid(row=0,column=0)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Comic Sans MS",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department ","Computer","Civil","Electrical","Information & Communication",
        "Business & Studies","Law","Mechanical","English")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label = Label(current_course_frame,text="Course",font=("Comic Sans MS",15,"bold"),bg="light green")
        course_label.grid(row=0,column=2)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Comic Sans MS",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","CSE","CE","EEE","ICE","BBA","LLB","ME","English")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        
        #Year
        year_label = Label(current_course_frame,text="Year",font=("Comic Sans MS",15,"bold"),bg="light green")
        year_label.grid(row=50,column=2)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Comic Sans MS",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","1st Year","2nd Year","3rd Year","4th Year")
        year_combo.current(0)
        year_combo.grid(row=50,column=3,padx=10,pady=10,sticky=W)

        #Semester
        sem_label = Label(current_course_frame,text="Semester",font=("Comic Sans MS",15,"bold"),bg="light green")
        sem_label.grid(row=50,column=0)
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Comic Sans MS",12,"bold"),width=17,state="readonly")
        sem_combo["values"]=("Select Semester","1st Semester","2nd Semester")
        sem_combo.current(0)
        sem_combo.grid(row=50,column=1,padx=10,pady=10,sticky=W)

        #Class Student information
        class_student_frame = LabelFrame(left_frame,bd=2,bg="light green",relief=RIDGE,text="Student Class Information",
        font=("Comic Sans MS",15,"bold"),fg="green")
        class_student_frame.place(x=5,y=200,width=720,height=370)

        #Student Serial entry
        studentid_label = Label(class_student_frame,text="Serial No",font=("Comic Sans MS",15,"bold"),bg="light green")
        studentid_label.grid(row=0,column=0)
        studentid_entry = Entry(class_student_frame,textvariable=self.var_student_id,width=20,font=("Comic Sans MS",15,"bold"),bg="light green")
        studentid_entry.grid(row=0,column=1)

        #Student name entry
        studentname_label = Label(class_student_frame,text="Name",font=("Comic Sans MS",15,"bold"),bg="light green")
        studentname_label.grid(row=0,column=250)
        studentname_entry = Entry(class_student_frame,textvariable=self.var_student_name,width=20,font=("Comic Sans MS",15,"bold"),bg="light green")
        studentname_entry.grid(row=0,column=300)

        #Student section
        studentsection_label = Label(class_student_frame,text="Section",font=("Comic Sans MS",15,"bold"),bg="light green")
        studentsection_label.grid(row=50,column=0)
        section_combo=ttk.Combobox(class_student_frame,textvariable=self.var_section,font=("Comic Sans MS",12,"bold"),width=17,state="readonly")
        section_combo["values"]=("Select Section","A","B","C","D","None")
        section_combo.current(0)
        section_combo.grid(row=50,column=1,padx=10,pady=10,sticky=W)

        #Student ID
        studentreg_label = Label(class_student_frame,text="ID No",font=("Comic Sans MS",15,"bold"),bg="light green")
        studentreg_label.grid(row=50,column=250)
        studentreg_entry =Entry(class_student_frame,textvariable=self.var_reg,width=20,font=("Comic Sans MS",15,"bold"),bg="light green")
        studentreg_entry.grid(row=50,column=300)

        #Student gender
        studentgender_label = Label(class_student_frame,text="Gender",font=("Comic Sans MS",15,"bold"),bg="light green")
        studentgender_label.grid(row=100,column=0)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Comic Sans MS",12,"bold"),width=17,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=100,column=1,padx=10,pady=10,sticky=W)

        #Student Email
        studentemail_label = Label(class_student_frame,text="E-mail",font=("Comic Sans MS",15,"bold"),bg="light green")
        studentemail_label.grid(row=150,column=0)
        studentemail_entry =Entry(class_student_frame,textvariable=self.var_email,width=20,font=("Comic Sans MS",15,"bold"),bg="light green")
        studentemail_entry.grid(row=150,column=1,sticky=W)

        #Student address
        studentaddress_label = Label(class_student_frame,text="Address",font=("Comic Sans MS",15,"bold"),bg="light green")
        studentaddress_label.grid(row=200,column=0)
        studentaddress_entry =Entry(class_student_frame,textvariable=self.var_address,width=20,font=("Comic Sans MS",15,"bold"),bg="light green")
        studentaddress_entry.grid(row=200,column=1,sticky=W)

        #Student Date of birth
        studentdob_label = Label(class_student_frame,text="Date Of Birth",font=("Comic Sans MS",15,"bold"),bg="light green")
        studentdob_label.grid(row=100,column=250)
        studentdob_entry =Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("Comic Sans MS",15,"bold"),bg="light green")
        studentdob_entry.grid(row=100,column=300,sticky=W)

        #Student Number
        studentno_label = Label(class_student_frame,text="Phone No.",font=("Comic Sans MS",15,"bold"),bg="light green")
        studentno_label.grid(row=150,column=250)
        studentno_entry =Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("Comic Sans MS",15,"bold"),bg="light green")
        studentno_entry.grid(row=150,column=300,sticky=W)

        #Teacher Name
        teachername_label = Label(class_student_frame,text="Teacher Name",font=("Comic Sans MS",15,"bold"),bg="light green")
        teachername_label.grid(row=200,column=250)
        teachername_entry =Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("Comic Sans MS",15,"bold"),bg="light green")
        teachername_entry.grid(row=200,column=300,sticky=W)

        #Radio Button
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=250,column=0) 
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=250,column=1)

        #button frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE , bg="pink")
        btn_frame.place(x=5,y=220,width=705,height=57)

        #button frame2
        btn_frame2 = Frame(class_student_frame,bd=2,relief=RIDGE , bg="pink")
        btn_frame2.place(x=5,y=270,width=705,height=57)

        #Save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("Comic Sans MS",15,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        #Update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=13,font=("Comic Sans MS",15,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)

        #Delete button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("Comic Sans MS",15,"bold"),bg="green",fg="white")
        delete_btn.grid(row=0,column=2)

        #Reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("Comic Sans MS",15,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)

        #Add photo sample button
        add_photo_sample_btn=Button(btn_frame2,command=self.generate_dataset,text="Add Photo Sample",width=58,font=("Comic Sans MS",15,"bold"),bg="green",fg="white")
        add_photo_sample_btn.grid(row=0,column=0)


        #Right label Frame
        right_frame = LabelFrame(main_frame,bd=2,bg="light green",relief=RIDGE,text="Details",
        font=("Comic Sans MS",15,"bold"),fg="green")
        right_frame.place(x=750,y=10,width=720,height=610)


        #Table frame
        table_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,
        font=("Comic Sans MS",15,"bold"),fg="green")
        table_frame.place(x=1,y=60,width=712,height=510)

        #scrollbar table frame
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,column=("Dep","Crs","Sem",
        "Yr","ID","Nm","Sec","Reg","Gen","DOB","mail","Phn",
        "Add","Tchr","Pht"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Crs",text="Course")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Yr",text="Year")
        self.student_table.heading("ID",text="Serial No.")
        self.student_table.heading("Nm",text="Name")
        self.student_table.heading("Sec",text="Section")
        self.student_table.heading("Reg",text="ID")
        self.student_table.heading("Gen",text="Gender")
        self.student_table.heading("DOB",text="Date Of Birth")
        self.student_table.heading("mail",text="E-mail")
        self.student_table.heading("Phn",text="Phone No.")
        self.student_table.heading("Add",text="Address")
        self.student_table.heading("Tchr",text="Teacher Name")
        self.student_table.heading("Pht",text="Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Crs",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Yr",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Nm",width=100)
        self.student_table.column("Sec",width=100)
        self.student_table.column("Reg",width=100)
        self.student_table.column("Gen",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("mail",width=100)
        self.student_table.column("Phn",width=100)
        self.student_table.column("Add",width=100)
        self.student_table.column("Tchr",width=100)
        self.student_table.column("Pht",width=100)

        self.student_table.pack(fill = BOTH ,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #function declearation
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="SHUVROshuvro123@",database="face_attendancesql1")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                            self.var_dep.get(), 
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_student_id.get(),
                                                                                                            self.var_student_name.get(),
                                                                                                            self.var_section.get(),
                                                                                                            self.var_reg.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucsess", "Student details has ben added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}",parent=self.root)

    #fetch data 
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="SHUVROshuvro123@",database="face_attendancesql1")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #get cursour
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]), 
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_student_id.set(data[4]),
        self.var_student_name.set(data[5]),
        self.var_section.set(data[6]),
        self.var_reg.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="SHUVROshuvro123@",database="face_attendancesql1")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Registation=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",
                    (
                                        self.var_dep.get(), 
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_student_name.get(),
                                        self.var_section.get(),
                                        self.var_reg.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        self.var_student_id.get()
                                        
                                        ))

                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success", "Student Details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_student_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)

        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student data?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="SHUVROshuvro123@",database="face_attendancesql1")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_student_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfullly deleted student details",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
    #reset funtion
    def reset_data(self):
        self.var_dep.set("Select Department"), 
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_student_id.set(""),
        self.var_student_name.set(""),
        self.var_section.set("Select Section"),
        self.var_reg.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
    
    #generate dataset or take a photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="SHUVROshuvro123@",database="face_attendancesql1")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Registation=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",
                    (
                                        self.var_dep.get(), 
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_student_name.get(),
                                        self.var_section.get(),
                                        self.var_reg.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        self.var_student_id.get()==id+1
                                        
                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predefined data on face frontal from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                #face crop
                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.1,6)
                    #scaling factor=1.3
                    #minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_crop(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_crop(my_frame),(600,600))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),2)
                        cv2.imshow("Front face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Genereating data set completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 
                
    #search data  #not working          
    def search_data(self):
        if self.var_dep.get()=="Select Department" or self.var_student_id.get()=="":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="SHUVROshuvro123@",database="face_attendancesql1")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_dep())+" LIKE '%"+str(self.var_student_id.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
             

if __name__=='__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()










