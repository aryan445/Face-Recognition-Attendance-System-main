from tkinter import*
root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def userText(event):
    user.delete(0,END)
    usercheck=True
def passText(event):
    code.delete(0, END)
    passcheck=True
    
def signin():
    username=user.get()
    password=code.get()
    
    if username=='admin' and password=='****':
        import subprocess
        cmd = 'python E:\\Face-Recognition-Attendance-System-main\\AMS_Run.py'
        p = subprocess.Popen(cmd, shell=True)
        out, err = p.communicate()
    else:
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")
        
        Label(screen,text='Incorrect Details!',bg='#fff',font=('calibri(Body)',50,'bold')).pack(expand=True)   
        
        # from subprocess import call
        # def open_py_file():
        #     call(["Python3",'app.py'])
            
        # open_py_file()
        # class CallPy(object):
        #     def __init__(self, path='E:\\FacialRealProject\\F_A_S\\app.py'):
        #         self.path = path
        #     def call_python_file(self):
        #         call(["Python3","{}".format(self.path)])
        #     if __name__=="__main":
        #         c = CallPy()
        #         c.call_python_file()
        # screen=Toplevel(root)
        # screen.title("App")
        # screen.geometry('925x500+300+200')
        # screen.config(bg="white")
        
        # Label(screen,text='Hello Everyone!',bg='#ff',font=('calibri(Body)',50,'bold')).pack(expand=True)
        
        # screen.mainloop()

img = PhotoImage(file="E:\\FacialRealProject\\F_A_S\\login.png")
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)


heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)
#############################---------------------
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind("<Button>",userText)
Frame(frame,width=295,bg='black').place(x=25,y=107)

##############################---------------------
code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind("<Button>",passText)
Frame(frame,width=295,bg='black').place(x=25,y=177)
###############################
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=215,y=270)


root.mainloop()