from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2


class Student :
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        ################################ Create Text Variables  ##################
        self.var_dep = StringVar()
        self.var_Year = StringVar()
        self.var_Semester = StringVar()
        self.var_Std_name = StringVar()
        self.var_Std_id = StringVar()
        self.var_Roll = StringVar()
        self.var_Phone = StringVar()
        self.var_Address = StringVar()
        self.var_Photosample = StringVar()

    #ImageLabel
        image = Image.open(r"images\FR3.jpg")
        image = image.resize((1530,710),Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(image)
        label = Label(self.root,image=self.image)
        label.place(x=0,y=130,width=1530,height=710)


    #MainFrame
    

        main_Frame = Frame(label,bd=2,bg="white")
        main_Frame.place(x=8,y=55,width=1530,height=600)

        #left labelFrame

        Left_frame = LabelFrame(main_Frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x =10,y = 10,width=750,height=580 )

        #Right labelFrame

        Right_frame = LabelFrame(main_Frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x =770,y = 10,width=750,height=580 )
        #CurrentCourse Frame
        Course = LabelFrame(main_Frame,bd=2,relief=RIDGE,text="Course",font=("times new roman",12,"bold"))
        Course.place(x =10,y = 50,width=750,height=120)
        
        #Department Combox
        depLabel = Label(Course,text='Department :',font=("times new roman",11,"bold"))
        depLabel.grid(row=0,column=0)
        dep_combo =ttk.Combobox(Course,textvariable = self.var_dep,state="readonly")
        dep_combo["values"] = ("Select Department","Computer Science","BBA","BCA","BSW")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx = 10,pady = 10)

        #Semester ComboBox 
        
        Semester = Label(Course,text='Semester :',font=("times new roman",11,"bold"))
        Semester.grid(row=0,column=3)

        Sem_combo =ttk.Combobox(Course,textvariable = self.var_Semester,state="readonly")
        Sem_combo["values"] = ("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        Sem_combo.current(0)
        Sem_combo.grid(row=0,column=5,padx = 10,pady = 10)

        #Batch 

        BatchLabel = Label(Course,text='Batch(Year) :',font=("times new roman",11,"bold"))
        BatchLabel.grid(row=2,column=0)
        b_combo =ttk.Combobox(Course,textvariable = self.var_Year,state="readonly")
        b_combo["values"] = ("Select Batch","2074","2075","2076","2077","2078")
        b_combo.current(0)
        b_combo.grid(row=2,column=1,padx = 0,pady = 10)

        #Student's Personal Details Frame

        P_info = LabelFrame(Left_frame,bd=2,relief =RIDGE,text = "Personal Details of Students",font=("times new roman",12,"bold"))
        P_info.place(x=5,y=150,width=730,height=320)

        #Student Id

        IdLabel = Label(P_info,text="Student's ID :",font=("times new roman",11,"bold"))
        IdLabel.grid(row=0,column=0)
        Id_entry =ttk.Entry(P_info,textvariable = self.var_Std_id,width=20)
        Id_entry.grid(row=0,column=1,padx = 0,pady = 10)

        #Sudents Name

        NLabel = Label(P_info,text="Student's Name :",font=("times new roman",11,"bold"))
        NLabel.grid(row=3,column=0)
        N_entry =ttk.Entry(P_info,textvariable = self.var_Std_name,width=20)
        N_entry.grid(row=3,column=1,padx = 0,pady = 10)


        #Roll number

        RLabel = Label(P_info,text="Roll Number :",font=("times new roman",11,"bold"))
        RLabel.grid(row=6,column=0)
        R_entry =ttk.Entry(P_info,textvariable = self.var_Roll,width=20)
        R_entry.grid(row=6,column=1,padx = 10,pady = 10)

        #Phone number

        PLabel = Label(P_info,text="Contact Number :",font=("times new roman",11,"bold"))
        PLabel.grid(row=9,column=0)
        P_entry =ttk.Entry(P_info,textvariable = self.var_Phone,width=20)
        P_entry.grid(row=9,column=1,padx = 0,pady = 10)


        #Address

        ALabel = Label(P_info,text="Permanent Address :",font=("times new roman",11,"bold"))
        ALabel.grid(row=12,column=0)
        A_entry =ttk.Entry(P_info,textvariable = self.var_Address,width=20)
        A_entry.grid(row=12,column=1,padx = 0,pady = 10)

        #radio_button
        self.var_radio1 = StringVar()
        radiobutton1 = ttk.Radiobutton(P_info,variable = self.var_radio1,text = "Take Photo Sample",value="Yes")
        radiobutton1.grid(row = 16,column =0)
        self.var_radio2 = StringVar()
        radiobutton2 = ttk.Radiobutton(P_info,variable = self.var_radio1,text = "No Photo Sample",value="No")
        radiobutton2.grid(row = 16,column =3)

        #Buttons

        btn_frame = Frame(Left_frame,bg="white")
        btn_frame.place(x=20,y=500,width =720,height = 50)

        save_btn = Button(btn_frame,text = "SAVE",command = self.Add_Data,font=("times new roman",11,"bold"))
        save_btn.grid(row=0,column=1)

        U_btn = Button(btn_frame,text = "UPDATE",command=self.update_data,font=("times new roman",11,"bold"))
        U_btn.grid(row=0,column=5)

        D_btn = Button(btn_frame,text = "DELETE",command=self.delete_data,font=("times new roman",11,"bold"))
        D_btn.grid(row=0,column=10)

        R_btn = Button(btn_frame,text = "RESET",command=self.reset_data,font=("times new roman",11,"bold"))
        R_btn.grid(row=0,column=15)

        TakePhoto = Button(btn_frame,text = "Take Photo",command=self.generate_dataset,font=("times new roman",11,"bold"))
        TakePhoto.grid(row=0,column=20)

        UpdatePhoto = Button(btn_frame,text = "Update Photo",font=("times new roman",11,"bold"))
        UpdatePhoto.grid(row=0,column=25)

        ############ Search ########################

        Search_frame = LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search by Details",font=("times new roman",12,"bold"))
        Search_frame.place(x = 5,y = 50,width=700,height=150 )

        Search_Label = Label(Search_frame,text="Search By :",font=("times new roman",11,"bold"))
        Search_Label.grid(row=0,column=0)
        Search_combo =ttk.Combobox(Search_frame,state="readonly")
        Search_combo["values"] = ("Select","Student's Id","Student's Name","Phone Number")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx = 0,pady = 10)

        search_entry =ttk.Entry(Search_frame,width=22 )
        search_entry.grid(row=0,column=3,padx = 10,pady = 10)

        Search_button = Button(Search_frame,text = "Search",font=("times new roman",11,"bold"))
        Search_button.grid(row=2,column=0)

        ShowAll_btn = Button(Search_frame,text = "Show All",font=("times new roman",11,"bold"))
        ShowAll_btn.grid(row=2,column=1) 

        ###################table##############################

        Table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x = 5,y = 150,width=710,height=300 )

        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.Table = ttk.Treeview(Table_frame,column=("dep","Year","Semester","Std_name","Std_id","Roll","Phone","Address","Photosample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Table.xview)
        scroll_y.config(command=self.Table.yview)

        self.Table.heading("dep",text="Department")
        self.Table.heading("Year",text="Year")
        self.Table.heading("Semester",text="Semester")
        self.Table.heading("Std_name",text="Student's Name")
        self.Table.heading("Std_id",text="Student's ID")
        self.Table.heading("Roll",text="Roll_no.")
        self.Table.heading("Phone",text="Contact No.")
        self.Table.heading("Address",text="Address")
        self.Table.heading("Photosample",text="Photosample")
        self.Table["show"] = "headings"
        self.Table.pack(fill = BOTH,expand =1)
        self.Table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    ############### Function Declaration  ###################

    def Add_Data(self):
        if self.var_dep.get() == "Select Department" or self.var_Std_name.get() == "" or self.var_Std_id.get() == "":
            messagebox.showerror("Error","All fields are required to be filled",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="12345",database="facerecognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                    self.var_dep.get(),
                                                                    self.var_Year.get(),
                                                                    self.var_Semester.get(),
                                                                    self.var_Std_name.get(),
                                                                    self.var_Std_id.get(),
                                                                    self.var_Roll.get(),
                                                                    self.var_Phone.get(),
                                                                    self.var_Address.get(),
                                                                    self.var_radio1.get()


                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                print("Connection successful")
                messagebox.showinfo("Student details has been added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f'Due to {str(es)}',parent = self.root)


                ################ Fetch Data ###########################
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="12345",database="facerecognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select *from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.Table.delete(*self.Table.get_children())
            for i in data:
                self.Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    ##################get cursor ##################

    def get_cursor(self,event=""):
        cursor_focus = self.Table.focus()
        content = self.Table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_Year.set(data[1]),
        self.var_Semester.set(data[2]),
        self.var_Std_name.set(data[3]),
        self.var_Std_id.set(data[4]),
        self.var_Roll.set(data[5]),
        self.var_Phone.set(data[6]),
        self.var_Address.set(data[7]),
        self.var_radio1.set(data[8])

    ######### Update Function ########
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_Std_name.get() == "" or self.var_Std_id.get() == "":
            messagebox.showerror("Error","All fields are required to be filled",parent = self.root)
        else :
            try:
                Update = messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost",user="root",password="12345",database="facerecognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set `dep` = %s,`Year`=%s,`Semester`=%s,`Std_name`=%s,`Roll-no`=%s,`Phone`=%s,`Address`=%s,`Photosample`=%s where `Std_id`=%s",(
                                                                    self.var_dep.get(),
                                                                    self.var_Year.get(),
                                                                    self.var_Semester.get(),
                                                                    self.var_Std_name.get(),
                                                                    self.var_Roll.get(),
                                                                    self.var_Phone.get(),
                                                                    self.var_Address.get(),
                                                                    self.var_radio1.get(),
                                                                    self.var_Std_id.get()
                                                                    

                 
                    
                    
                    
                    
                    
                    
                    
                    
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


        ########### Delete Function ########## 

    def delete_data(self):  
        if self.var_Std_id.get() =="":
            messagebox.showerror("Error","Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete warnig","Do you want to delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",user="root",password="12345",database="facerecognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Std_id=%s"
                    val=(self.var_Std_id.get(),)
                    my_cursor.execute(sql,val)
                else :
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Successfully deleted the students details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    ######################### Reset Function ##############

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_Year.set("Select Year")
        self.var_Semester.set("Select Semester")
        self.var_Std_name.set("")
        self.var_Std_id.set("")
        self.var_Roll.set("")
        self.var_Phone.set("")
        self.var_Address.set("")
        self.var_radio1.set("")

        ################## Generate data set and Take photo samples########

    def generate_dataset(self):
            if self.var_dep.get() == "Select Department" or self.var_Std_name.get() == "" or self.var_Std_id.get() == "":
                messagebox.showerror("Error","All fields are required to be filled",parent = self.root)
            else :
                try:
                
                    conn = mysql.connector.connect(host="localhost",user="root",password="12345",database="facerecognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                        id+=1
                    my_cursor.execute("update student set `dep` = %s,`Year`=%s,`Semester`=%s,`Std_name`=%s,`Roll-no`=%s,`Phone`=%s,`Address`=%s,`Photosample`=%s where `Std_id`=%s",(
                                                                    self.var_dep.get(),
                                                                    self.var_Year.get(),
                                                                    self.var_Semester.get(),
                                                                    self.var_Std_name.get(),
                                                                    self.var_Roll.get(),
                                                                    self.var_Phone.get(),
                                                                    self.var_Address.get(),
                                                                    self.var_radio1.get(),
                                                                    self.var_Std_id.get() == id+1
                    ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    ############ Load predefined data on face frontals from opencv #######
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray,1.3,5)
                        # Scaling Factor = 1.3
                        #Minimum Neighour = 5

                        for(x,y,w,h) in faces:
                            face_cropped = img[y:y+h,x:x+w]
                            return face_cropped
                    cap = cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,myframe=cap.read()
                        if face_cropped(myframe) is not None :
                            img_id+=1
                        face = cv2.resize(face_cropped(myframe),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating dataset completed")
                except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

        





            




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
