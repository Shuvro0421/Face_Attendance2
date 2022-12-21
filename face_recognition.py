from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1580x790+0+0")
        self.root.title("Face recognition")

        #face detection backgroung
        face_recognition_img = Image.open(r"images\face_recognition_bg_img.png")
        face_recognition_img = face_recognition_img.resize((1580,790) , Image.ANTIALIAS)
        self.photo_face_recognition = ImageTk.PhotoImage(face_recognition_img)
        face_frame_img = Label(self.root,image =self.photo_face_recognition)
        face_frame_img.place(x = 0,y = 0,width=1580,height=800)

        #face detection frame
        face_recognition_frame = Frame(face_frame_img,bd=2,relief=RIDGE , bg="pink")
        face_recognition_frame.place(x=500,y=250,width=200,height=45)

        #click to detect faces button
        title_btn=Button(face_recognition_frame,text="Recognize Faces",command=self.face_recog,width=16,font=("Comic Sans MS",15,"bold"),bg="red",fg="white")
        title_btn.grid(row=0,column=0)
        
    #attendance
    def mark_attendance(self,i,n,c):
        with open("attendance_report/Attendance.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list) and (n not in name_list) and (c not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                datestring=now.strftime("%H:%M:%S")
                
                f.writelines(f"\n{i},{n},{c},{datestring},{d1},Present")

                



    #face recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scalefactor,min_neighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,min_neighbour)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="SHUVROshuvro123@",database="face_attendancesql1")
                my_cursor=conn.cursor()

                #student id 
                my_cursor.execute("select Registation from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                #st name
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                #st dep
                my_cursor.execute("select Course from student where Student_id="+str(id))
                c=my_cursor.fetchone()
                c="+".join(c)


                #putting face frame
                if confidence>75:
                    cv2.putText(img,f"ID:{i}",(x,y-90),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),3)
                    cv2.putText(img,f"Name:{n}",(x,y-70),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),3)
                    cv2.putText(img,f"Department:{c}",(x,y-40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),3)
                    self.mark_attendance(i,n,c)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),3)
                coord=[x,y,w,h]
            return coord

        #recognizing
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,0,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__=='__main__':
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()