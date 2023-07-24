from tkinter import *
dict={"Authentic":['Accurate','it is an adjective,& comes from Latin roots ad curare'],"Brittle":["Breakable","It is a verb"],"Classic":["Simple","simple is an adjective"],"Glut":["Stuff","You can use it to refer to things such as substance, events, or ideas etc"]}


#**********************Choices******************
def mainScreen():
    global screen
    screen=Tk()
    screen.geometry("800x600")
    screen.title("Dictionary")

    Label(text="Dictionary",width="300" ,height="2" ,fg="white",bg="black", font=("times new roman",25,"bold")).pack()
    Label(text="").pack()
    Label(text="").pack()
    
    Button(text="Admin", width="20",height="2",font=("serif",15,"bold"),command=screenlogin).pack()
    Label(text="").pack()
    
    Button(text="User",width="20",height="2",font=("serif",15,"bold"),command=screenuser).pack()

    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    
    
    Label(text="",bg="black",width="500",height="1").pack()
        
    screen.mainloop()

def screenlogin():
    global loginScreen
    global username
    global password
    
    loginScreen=Toplevel(screen)
    loginScreen.geometry("800x600")
    loginScreen.title("Login for Admin")

    username=StringVar()
    password=StringVar()

    Label(loginScreen,text="Dictionary",width="300" ,height="2" ,fg="white",bg="black", font=("times new roman",25,"bold")).pack()
    Label(loginScreen,text="").pack()
    Label(loginScreen,text="Admin",width="100",height="2",font=("calibri",22,"bold")).pack()
    
    Label(loginScreen,text="Username *",width="80",height="2",font=("serif",13)).pack()
    Entry(loginScreen,textvariable=username).pack()

    Label(loginScreen,text="Password *",width="80",height="2",font=("serif",13)).pack()
    Entry(loginScreen,textvariable=password).pack()

    Label(loginScreen,text="").pack()
    Button(loginScreen,text="Login",width="18",height="1",font=("serif",15),command=login_admin).pack()
    
#**********************login operation***************
def login_admin():
    name = username.get()
    pas = password.get()
    if name=="admin" and pas=="admin":
        welcomeadmin()

    else :
        error()

def error():
    print()


#****************After admin login**************
def welcomeadmin():

    global homeadmin
    
    homeadmin=Toplevel(loginScreen)
    homeadmin.title("Admin")
    homeadmin.geometry("800x600")

    Label(homeadmin,text="Dictionary",width="300" ,height="2" ,fg="white",bg="black", font=("times new roman",25,"bold")).pack()
   
    Label(homeadmin,text="").pack()
    Label(homeadmin,text="").pack()
    Button(homeadmin,text="Add word",width="19",height="2",bd="5",command=addWord,font=("serif",15,"bold")).pack()

    Label(homeadmin,text="").pack()
    Button(homeadmin,text="Modify word",width="19",height="2",bd="5",command=modifyWord,font=("serif",15,"bold")).pack()
    
    Label(homeadmin,text="").pack()
    Button(homeadmin,text="Delete word",width="19",height="2",bd="5",command=deleteWord,font=("serif",15,"bold")).pack()

    Label(homeadmin,text="").pack()
    Button(homeadmin,text="Show all words",width="19",height="2",bd="5",command=showWord,font=("serif",15,"bold")).pack()

    Label(homeadmin,text="").pack()
    Button(homeadmin,text="search word",width="19",height="2",bd="5",command=screenuser,font=("serif",15,"bold")).pack()

#**************Add word UI******************

def addWord():

    global word
    global mean
    global info
    global addword

    word=StringVar()
    mean=StringVar()
    info=StringVar()
    
    addword=Toplevel(homeadmin)
    addword.geometry("800x600")
    addword.title("Add words..")

    Label(addword,text="Dictionary",width="300" ,height="2" ,fg="white",bg="black", font=("times new roman",25,"bold")).pack()
    Label(addword,text="").pack()
    Label(addword,text="").pack()

    Label(addword,text="Add words to dictionary.",fg="black",font=("serif",20,"bold")).pack()

    Label(addword,text="").pack()
    Label(addword,text="").pack()
    
    l1=Label(addword,text="Enter word :",font=("serif",15)).pack()

    e1=Entry(addword,textvariable=word,width="50").pack()

    Label(addword,text="").pack()
    l2=Label(addword,text="Enter meaning : ",font=("serif",15)).pack()

    Entry(addword,textvariable=mean,width="50").pack()

    Label(addword,text="").pack()
    l3=Label(addword,text="Enter information : ",font=("serif",15)).pack()

    Entry(addword,textvariable=info,width="50").pack()

    Label(addword,text="").pack()
    Button(addword,text="Add",width="19",height="2",font=("serif",15,"bold"),bd="2",command=add).pack()


#******************************Add word operation*********************

def add():
    global lst
    lst=StringVar()
    
    k=word.get()
    m=mean.get()
    i=info.get()
    lst=[]
    lst.append(m)
    lst.append(i)


    if k!=" " and m!=" " and i!= " " and k not in dict:
        dict[k]=lst
        Label(addword,text="word is added to dictionary...!",width="50",height="1",font=15).pack()
    elif k in dict:
        Label(addword,text="This word is already present in dictionary...!",width="50",height="1",font=15).pack()
        
    else:
        Label(addword,text="All the fields are necessary",width="50",height="1",font=15).pack()

#*************************Modify word Ui*******************************        
    
def modifyWord():
    global modify
    global se

    se=StringVar()
    
    modify=Toplevel(homeadmin)
    modify.title("Modify Word..!")
    modify.geometry("800x600")

    Label(modify,text="Dictionary",width="300" ,height="2" ,fg="white",bg="black", font=("times new roman",25,"bold")).pack()
    Label(modify,text="").pack()
    Label(modify,text="").pack()

    Label(modify,text="Enter word to modify : ",width="50",height="3",font=("serif",15,"bold")).pack()
    Entry(modify,textvariable=se).pack()

    Label(modify,text="").pack()
    Button(modify,text="Search",width="18",height="1",font=("serif",15),bd=5,command=modifyOperation).pack()

def modifyOperation():
    global info1
    global mean1
    global w
    global operation

    mean1=StringVar()
    info1=StringVar()
    w=se.get()

    if w=="":
        Label(modify,text="Please enter text..!",width="50",height="3",font=("serif",15),fg="red").pack()

    elif w in dict:

        operation=Toplevel(modify)
        operation.title("Modify Word..!")
        operation.geometry("800x600")

        Label(operation,text="Dictionary",width="300" ,height="2" ,fg="white",bg="black", font=("times new roman",25,"bold")).pack()
        Label(operation,text="").pack()
        Label(operation,text="").pack()
        

        s="%s : %s \n Information : %s"%(w,dict[w][0],dict[w][1])
        
        Label(operation,text=s,width="100",height="3",font=("serif",15),fg="blue").pack()
        Label(operation,text="").pack()
        
        Label(operation,text="").pack()
        l2=Label(operation,text="Enter meaning : ",font=("serif",15,"bold")).pack()

        Entry(operation,textvariable=mean1,width="50").pack()

        Label(operation,text="").pack()
        l3=Label(operation,text="Enter information : ",font=("serif",15)).pack()
        Entry(operation,textvariable=info1,width="50").pack()
        Label(operation,text="").pack()
    
        Button(operation,text="Modify",width=18,height=1,font=("serif",15),bd=5,command=modifyO).pack()

    else:
        Label(modify,text="This word is not present in dictionary..!",width="50",height="3",font=("serif",15),fg="red").pack()

def modifyO():
    m1=mean1.get()
    i1=info1.get()

    lst1=[]
    lst1.append(m1)
    lst1.append(i1)

    if m1==" " and i1==" ":
        Label(operation,text="Please fill all the fields..",width="40",height="1",font=("serif",15)).pack()
       
    else:
        dict[w]=lst1
        Label(operation,text="Word is modified..!",width="40",height="1",font=("serif",15)).pack()    

        
#***************************Delete UI*********************
    
def deleteWord():

    global de
    global delete

    de=StringVar()
    
    delete=Toplevel(homeadmin)
    delete.title("English to English Dictonary..")
    delete.geometry("800x600")

    Label(delete,text="Dictionary",width="300" ,height="2" ,fg="white",bg="black", font=("times new roman",25,"bold")).pack()
    Label(delete,text="").pack()
    Label(delete,text="").pack()
    
    Label(delete,text="Delete word ",width="20",height="2",font=("serif",15,"bold")).pack()
    Entry(delete,textvariable=de,width="15").pack()

    Label(delete,text="").pack()

    Button(delete,text="Delete",width="18",height="1",font=("serif",15),command=deleteW,bd=5).pack()

   
#**********************delete operation******************
   
    
def deleteW():

    w=de.get()

    if w in dict:
        del dict[w]
        Label(delete,text="word is deleted",width="18",height="2",font=("serif",13)).pack()
    else :
        Label(delete,text="word is deleted",width="18",height="2",font=("serif",13)).pack()

#*************************show word *********************
    

def showWord():
    global s
    showword=Toplevel(homeadmin)
    showword.geometry("800x600")
    showword.title("Show words..")

    
    Label(showword,text="Dictionary",width="300",height="2" ,fg="white",bg="black", font=("times new roman",25,"bold")).pack()
    Label(showword,text="").pack()
    Label(showword,text="").pack()

    for i in dict:
        #f=i.join(" : ")
        #s=f.join(dict[i][0])
        #t=s.join(dict[i][1])

        s="%s : %s \n Information : %s"%(i,dict[i][0],dict[i][1])
        
        Label(showword,text=s,width="100",height="3",font=("serif",15),fg="blue").pack()
        Label(showword,text="").pack()


#*************************User screen i.e search*********************

def screenuser():
    global user
    global se

    se=StringVar()
    
    user=Toplevel(screen)
    user.title("English to English Dictonary..")
    user.geometry("800x600")

    Label(user,text="Dictionary",width="300" ,height="2" ,fg="white",bg="black", font=("times new roman",25,"bold")).pack()
    Label(user,text="").pack()
    Label(user,text="").pack()
    Label(user,text="Search your word ",width="20",height="2",font=("serif",15,"bold")).pack()
    Entry(user,textvariable=se,width="15").pack()
    Label(user,text="").pack()

    Button(user,text="Search",width="18",height="1",font=("serif",15),command=search,bd=5).pack()

   
    Label(user,text="").pack()
    Label(user,text="").pack()
    Label(user,text="").pack()

  
def search():
    w=se.get()
    
    if w in dict:
        s="%s : %s \n Information : %s"%(w,dict[w][0],dict[w][1])

        Label(user,text=s,width="100",height="2",font=("serif",15,"bold"),fg="green").pack()

mainScreen()

