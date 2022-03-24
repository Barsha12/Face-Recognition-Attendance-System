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

class Attendance :
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















if __name__ == "__main__":
    root = Tk()
    object = Attendance(root)
    root.mainloop()