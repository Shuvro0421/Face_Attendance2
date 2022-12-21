from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1580x790+0+0")
        self.root.title("Student Details")

        #title backgroung
        title_bg_img = Image.open(r"images\train_bg_image.png")
        title_bg_img = title_bg_img.resize((1580,790) , Image.ANTIALIAS)
        self.photo_title_img = ImageTk.PhotoImage(title_bg_img)
        title_img = Label(self.root,image =self.photo_title_img)
        title_img.place(x = 0,y = 0,width=1580,height=800)

        #title frame
        title_frame = Frame(title_img,bd=2,relief=RIDGE , bg="pink")
        title_frame.place(x=900,y=380,width=96,height=96)

        #click to train button title button
        title_btn=Button(title_frame,text="Train",command=self.train_classifier,width=7,height=3,font=("Comic Sans MS",14,"bold"),bg="red",fg="white")
        title_btn.grid(row=0,column=0)
    
    #train images
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # to grayscale convert
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")





if __name__=='__main__':
    root = Tk()
    obj = Train(root)
    root.mainloop()
