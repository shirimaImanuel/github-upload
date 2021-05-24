import tkinter as tk
from tkinter import  ttk
from PIL import Image, ImageTk, ImageFile
import face_recognition
import numpy as np
import cv2



def Confirm(click):
    if click == "Register":
        print("Register Button clicked")
        register = tk.Tk()
        register.title("Registration mode")
        register.config(bg = "lightgreen")
        register.geometry("400x500")
        register.resizable(0,0)
        
        
        
        text = tk.Label(register, text = "Registration Form", bg = "lightgreen", fg = "black", font = "Times 19 italic bold")
        text.pack(fill=tk.X, pady=20)
        
        
        l1 = tk.Label(register, text = "Enter your first name", bg = "lightgreen", fg = "black", font = "Harvetica 9")
        name = tk.Entry(register, bg = "azure", fg = "black")
        l1.place(x=10,y=100)
        name.place(x=170, y=100,width=200)
        
        
        l2= tk.Label(register, text = "Enter your middle name", bg = "lightgreen", fg = "black", font = "Harvetica 9")
        name = tk.Entry(register, bg = "azure", fg = "black")      
        l2.place(x=10,y=150)
        name.place(x=170, y=150,width=200)
        
        
        
        l3= tk.Label(register, text = "Enter your Last name", bg = "lightgreen", fg = "black", font = "Harvetica 9")
        name = tk.Entry(register, bg = "azure", fg = "black")      
        l3.place(x=10,y=200)
        name.place(x=170, y=200,width=200)
        
        
        l4= tk.Label(register, text = "Course", bg = "lightgreen", fg = "black", font = "Harvetica 9")
        name = tk.Entry(register, bg = "azure", fg = "black")      
        l4.place(x=10,y=250)
        name.place(x=170, y=250,width=200)
        
        
        l5= tk.Label(register, text = "Your course", bg = "lightgreen", fg = "black", font = "Harvetica 9")
        course = ttk.Combobox(register,font="Harvetica 10",state="readonly")
        course['values']=('--select--',"Computer Science","IT","Civil", "Biomedical ", "Electrical","Lab")
        l5.place(x=10,y=250)
        course.place(x=170, y=250,width=200)
        course.current(0)
        
        #camera function button
        
        def PhoCam(camera):
                       
            if camera == "Face":
                print("Face Registration button Clickied")
                cam = cv2.VideoCapture(0)
               
            
                while True:
                    success, picha = cam.read()
                    cv2.imshow("Face Detection Mode", picha)
                    if cv2.waitKey(100) & 0xFF == ord('s'):
                        cv2.resize(picha, (400,500,))
                        cv2.imwrite("Photo.png", picha)
                        break
                cam.release()
        cv2.destroyAllWindows()
                
        btn = tk.Button(register, text = "Face registration")
        btn.config(command = lambda:PhoCam("Face"))
        btn.place(x=10, y=350)  


        def btnconfirm(send):
            if send == "Confirm":
                datquery = 'insert into users (fname, mname, lname) values ('
                
                
                #sign attendance function
    elif click == "Sign":
        print("Sign Button is clicked")
        cam = cv2.VideoCapture(0)
               
        while True:
            success, picha = cam.read()
            cv2.imshow("Face Recognition", picha)
            if cv2.waitKey(100) & 0xFF == ord('s'):
                cv2.imwrite("Recogniton.png", picha)
                break
                cam.release()
        cv2.destroyAllWindows()
            
        
        #view attendance function
    elif click == "View":
        print("View Button is clicked")
   
        


gui = tk.Tk()



gui.title("Face recognition and finger print attendance system")
gui.config(bg = "azure")
gui.geometry("630x670")
gui.resizable(0,0)



#load = Image.open("/home/shirima/AttendenceAI/cascade/Photo.png")
#phot = tk.PhotoImage(file = load)
#img=tk.Label(gui, bg=phot)
#img.pack()







text = tk.Label(gui, text="Arusha Technical College\n Information and Communication Technology", bg = "azure", fg = "black",  font = "Courier 18 bold")
#text.place(x=200,y=60)
text.pack(fill = tk.X)


neno = tk.Label(gui, text="\n\n\nWelcome to ATC Biometrick Attendance System", bg = "azure", fg = "black",  font = "Courier 18 bold")
#neno.place(x=200,y=120)
neno.pack(fill = tk.Y)


button1 = tk.Button(gui,  text = "Register", bg = "lightgreen", fg = "black")
button1.pack(side=tk.LEFT, fill = tk.X)
button1.config(command = lambda:Confirm("Register"))


button2 = tk.Button(gui,  text = "Sign Attendance", bg = "lightgreen", fg = "black")
button2.pack(side = tk.LEFT, pady=240, padx = 150)
button2.config(command = lambda:Confirm("Sign"))


button3 = tk.Button(gui,  text = "View Attendance", bg = "lightgreen", fg = "black")
button3.pack(side=tk.RIGHT, fill = tk.X)
button3.config(command = lambda:Confirm("View"))









gui.mainloop()
