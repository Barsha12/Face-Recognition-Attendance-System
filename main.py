from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from student import Student
from tkinter import messagebox
import os
import mysql.connector
import numpy as np
import cv2
from time import strftime
from datetime import datetime

class FaceRecog :
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")
        #BackgroundImage
        Bimg = Image.open(r"images\FR3.jpg")
        Bimg = Bimg.resize((1530,750),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(Bimg)

        bLabel = Label(self.root,image = self.photoimg)
        bLabel.place(x=0,y=0,width=1530,height=790)

        #StudentDeatails_button
        bnImg1 = Image.open(r"images\FR.png")
        bnImg1 = bnImg1.resize((250,300),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(bnImg1)
        b1 = Button(self.root,image = self.photoimg1,cursor="hand2")
        b1.place(x=200,y=80,width = 250,height=260)

        b1_1 = Button(text ="Student Details",command = self.StudentDetails,cursor = "hand2" )
        b1_1.place(x=200,y=360,width=250,height=40)

        #FaceDetector_button
        bnImg2 = Image.open(r"images\FR1.jpg")
        bnImg2 = bnImg2.resize((250,300),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(bnImg2)
        b2 = Button(self.root,image = self.photoimg1,cursor="hand2")
        b2.place(x=600,y=80,width = 250,height=260)

        b2_2 = Button(text ="Face Recognition",cursor = "hand2",command=self.recognition )
        b2_2.place(x=600,y=360,width=250,height=40)

        #Attendance_button
        bnImg3 = Image.open(r"images\FR.png")
        bnImg3 = bnImg3.resize((250,300),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(bnImg3)
        b3 = Button(self.root,image = self.photoimg1,cursor="hand2")
        b3.place(x=1000,y=80,width = 250,height=260)

        b3_3 = Button(text ="Attendance",cursor = "hand2" )
        b3_3.place(x=1000,y=360,width=250,height=40)

        #TrainData_button
        bnImg4 = Image.open(r"images\FR1.jpg")
        bnImg4 = bnImg4.resize((250,300),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(bnImg4)
        b4 = Button(self.root,image = self.photoimg1,cursor="hand2")
        b4.place(x=200,y=440,width = 250,height=260)

        b4_4 = Button(text ="Train Data",cursor = "hand2",command=self.train_classifier )
        b4_4.place(x=200,y=720,width=250,height=40)

        #Photos_button

        bnImg5 = Image.open(r"images\FR.png")
        bnImg5 = bnImg5.resize((300,300),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(bnImg5)
        b5 = Button(self.root,image = self.photoimg1,cursor="hand2")
        b5.place(x=600,y=440,width = 250,height=260)

        b5_5 = Button(text ="Photos",cursor = "hand2",command=self.open_img )
        b5_5.place(x=600,y=720,width=250,height=40)

        #########  Function buttons ################

    def open_img(self): 
        os.startfile("data") ############data samples


    def StudentDetails(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join (data_dir,file)for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')## coverting to grayscale
            imageArray = np.array(img,'uint8') #grid images
            id=int(os.path.split(image)[1].split('.')[1]) #obtaining ids of images
            faces.append(imageArray)
            ids.append(id)
            cv2.imshow("Training",imageArray)
            cv2.waitKey(1)==13

        ids = np.array(ids)

################### training through LBPH   ########

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces,ids)
        recognizer.write("recognizer.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Training datasets completed !!")


###################   Attendance   ######################

    def mark_attendance(self,sid,n,d,c):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((sid not in name_list)) and ((n not in name_list)) and ((d not in name_list)) and ((c not in name_list)) :
                now=datetime.now()
                date1=now.strftime("%d/%m/%Y")
                time1 = now.strftime("%H:%M:%S")
                f.writelines(f"\n{sid},{n},{d},{c},{date1},{time1},Present")






#########################face recognition ########################

    def recognition(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,recognizer):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

            coord = [] #coordinates for rectangle

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=recognizer.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",user="root",password="12345",database="facerecognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Std_name from student where Std_id="+str(id))
                n = my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select dep from student where Std_id="+str(id))
                d = my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Semester from student where Std_id="+str(id))
                c = my_cursor.fetchone()
                c="+".join(c)

                my_cursor.execute("select Std_id from student where Std_id="+str(id))
                sid = my_cursor.fetchone()
                sid="+".join((sid))



                if confidence > 77:
                    cv2.putText(img,f"Id:{(sid)}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
                    cv2.putText(img,f"Faculty:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
                    cv2.putText(img,f"Semester:{c}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
                    self.mark_attendance(sid,n,d,c)
                else :
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Face not recognized",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                coord = [x,y,w,h]
            return coord

        def recognise(img,recognizer,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"face",recognizer)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        recognizer=cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("recognizer.xml")

        videoCap=cv2.VideoCapture(0)
        while True:
            ret,img = videoCap.read()
            img = recognise(img,recognizer,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1) == 13:
                break
                videoCap.release()
                cv2.destroyAllWindows()

        


























if __name__ == "__main__":
    root = Tk()
    object = FaceRecog(root)
    root.mainloop()

