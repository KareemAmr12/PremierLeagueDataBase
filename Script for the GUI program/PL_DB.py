from ast import Lambda
from cProfile import label
from cgitb import enable
import email
from json.tool import main
from tkinter.font import BOLD
from turtle import bgcolor
from types import LambdaType
import mysql.connector
from tkinter import *
from tkinter import ttk
from datetime import datetime



#root window
root = Tk()
root.title('PremierLeague Database')
root.geometry("1600x800")


#Creating different tabs for different features 11 tabs

main_frame = Frame(root)
frame1= Frame(root)
frame1new = Frame(root)
frame2= Frame(root)
frame3= Frame(root)
frame4= Frame(root)
frame5= Frame(root)
frame6= Frame(root)
frame7= Frame(root)
frame8= Frame(root)
frame9= Frame(root)
frame10= Frame(root)
frame11= Frame(root)
login_frame= Frame(root)

main_frame.pack(fill='both',expand = 1)



main_label = Label(main_frame, text="Welcome to the primer league database",font= 15)
main_label.grid(row = 0, column = 0, columnspan=3, padx=10, pady=10)


# Defining Buttons for main window (main features)

# Button functions
def go1():
    frame1.pack(fill='both',expand=1)
    main_frame.forget()
    
def go2():
    frame2.pack(fill='both',expand=1)
    main_frame.forget()
    
def go3():
    frame3.pack(fill='both',expand=1)
    main_frame.forget()
    
def go4():
    frame4.pack(fill='both',expand=1)
    main_frame.forget()
    
def go5():
    frame5.pack(fill='both',expand=1)
    main_frame.forget()

def go6():
    frame6.pack(fill='both',expand=1)
    main_frame.forget()
    
def go7():
    frame7.pack(fill='both',expand=1)
    main_frame.forget()
    
def go8():
    frame8.pack(fill='both',expand=1)
    main_frame.forget()
    
def go9():
    frame9.pack(fill='both',expand=1)
    main_frame.forget()
    
def go10():
    frame10.pack(fill='both',expand=1)
    main_frame.forget()
    
def go11():
    frame11.pack(fill='both',expand=1)
    main_frame.forget()
    
def gologin():
    login_frame.pack(fill='both',expand=1)
    frame1.forget()
    
    
def ret1():
    main_frame.pack(fill='both',expand=1)
    frame1.forget()

def ret1new():
    main_frame.pack(fill='both',expand=1)
    frame1new.forget()
    
def ret2():
    main_frame.pack(fill='both',expand=1)
    frame2.forget()
    
def ret3():
    main_frame.pack(fill='both',expand=1)
    frame3.forget()
    
def ret4():
    main_frame.pack(fill='both',expand=1)
    frame4.forget()
    
def ret5():
    main_frame.pack(fill='both',expand=1)
    frame5.forget()
    
def ret6():
    main_frame.pack(fill='both',expand=1)
    frame6.forget()
    
def ret7():
    main_frame.pack(fill='both',expand=1)
    frame7.forget()
    
def ret8():
    main_frame.pack(fill='both',expand=1)
    frame8.forget()
    
def ret9():
    main_frame.pack(fill='both',expand=1)
    frame9.forget()
    
def ret10():
    main_frame.pack(fill='both',expand=1)
    frame10.forget()
    
def ret11():
    main_frame.pack(fill='both',expand=1)
    frame11.forget()
    
def retlogin():
    main_frame.pack(fill='both',expand=1)
    login_frame.forget()
    
    
def login():
    global email_entry
    global Password_entry
    global login_button_f1
    global error_label_flog
    mydb = mysql.connector.connect(
    host="db4free.net",
    user="sql11488194",
    password="I6pWKd1e91",
    database="sql11488194"
    )
    c = mydb.cursor(buffered=True)

    sql = """
    Select * FROM fan WHERE Email_address= %s
    """
    
    temp_email = (email_entry.get(),)
    temp_password = Password_entry.get()
    
    c.execute(sql, temp_email)
    
    result_login = c.fetchall()
    mydb.commit()
    print(result_login)
    if(result_login == []):
        error_label_flog.config(text="LOGIN ERROR! check your Email or password!")
    else:
        if(temp_password == result_login[0][1]):
            frame1new.pack(fill='both',expand=1)
            login_frame.forget()
        else:
            error_label_flog.config(text="LOGIN ERROR! check your Email or password!")
        
        


button_1 = Button(main_frame, text='Add a new user review', height= 3, width= 50, command=go1)
button_2 = Button(main_frame, text="View existing reviews", height= 3, width= 50, command=go2)
button_3 = Button(main_frame, text="Register as a user", height= 3, width= 50, command=go3)
button_4 = Button(main_frame, text="Query players by nationality", height= 3, width= 50, command=go4)
button_5 = Button(main_frame, text="Show top 10 teams", height= 3, width= 50, command=go5)
button_6 = Button(main_frame, text="Show teams who won the most games", height= 3, width= 50, command=go6)
button_7 = Button(main_frame, text="Query and view a given team", height= 3, width= 50, command= go7)
button_8 = Button(main_frame, text="Query and view a given player", height= 3, width= 50, command=go8)
button_9 = Button(main_frame, text="Query home team for a stadium", height= 3, width= 50, command=go9)
button_10 = Button(main_frame, text="Query players by position", height= 3, width= 50, command=go10)
button_11 = Button(main_frame, text="Identify all the teams in a given city in the UK", height= 3, width= 50, command=go11)

button_1.grid(row = 2, column=0)
button_2.grid(row = 3, column=0)
button_3.grid(row = 4, column=0)
button_4.grid(row = 5, column=0)
button_5.grid(row = 6, column=0)
button_6.grid(row = 7, column=0)
button_7.grid(row = 8, column=0)
button_8.grid(row = 9, column=0)
button_9.grid(row = 10, column=0)
button_10.grid(row = 11, column=0)
button_11.grid(row = 12, column=0)


#login frame



Password = Label(login_frame, text="Password: ")
Password.place(relx=0.45, rely=0.53, anchor=CENTER)

Password_entry = Entry(login_frame, width=30)
Password_entry.place(relx=0.57, rely=0.53, anchor=CENTER)

Email = Label(login_frame, text="Email: ")
Email.place(relx=0.45, rely=0.5, anchor=CENTER)

email_entry = Entry(login_frame, width=30)
email_entry.place(relx=0.57, rely=0.5, anchor=CENTER)

enter_button_flog = Button(login_frame, text="Enter", height=1, width=8, command=login, bg='green')
enter_button_flog.place(relx=0.55, rely= 0.57, anchor=CENTER)

ret_button_flog = Button(login_frame, text="Return", height=3, width=7, command=retlogin, bg='pink')
ret_button_flog.place(relx=1, rely=0, anchor=NE)

error_label_flog = Label(login_frame, fg='red', height=3, width=100, font=15) 
error_label_flog.place(relx=0.1, rely= 0.35)

#Frame for feature 1 (Add a new user review on a match) (login first)

login_button_f1 = Button(frame1, text="Login First!", height=5, width=10, command=gologin)
login_button_f1.place(relx=0.5, rely=0.5, anchor=CENTER)

ret_button_f1 = Button(frame1, text="Return", height=3, width=7, command=ret1, bg='pink')
ret_button_f1.place(relx=1, rely=0, anchor=NE)

#Frame for feature 1 (Add a new user review on a match)


osrch_label_f1n = Label(frame1new, text="Search for the match existance first.",font= 10, width=40, height= 3)
osrch_label_f1n.grid(row=0, column=0)

def review():
    
    global success_label_f1n
    mydb = mysql.connector.connect(
    host="db4free.net",
    user="sql11488194",
    password="I6pWKd1e91",
    database="sql11488194"
    )
    c = mydb.cursor(buffered=True)
    sql = """
    Insert INTO fan_review (Fan_EmailAddr, Match_Date, HomeTeam, AwayTeam, Rating, Text)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    val = (email_entry.get(), match_entry_f1n.get(), hometeam_entry_f1n.get(), awayteam_entry_f1n.get(), clicked.get(), text_entry_f1n.get())
    try:
        c.execute(sql, val)
        if(c.rowcount == 1):
            success_label_f1n.config(text="Review created successfully!", fg='green')
            mydb.commit()
    except mysql.connector.IntegrityError:
        success_label_f1n.config(text="Failed! (Review already exists? or Check the inputs above!)", fg='red')
        

success_label_f1n = Label(frame1new, fg='green', height=3, width=100, font=15) 
success_label_f1n.place(relx=0.4, rely= 0.7)



def srch_f1n():
    global output_text_f1n
    success_label_f1n.config(text="")
    for item in output_text_f1n.get_children():
          output_text_f1n.delete(item)
    mydb = mysql.connector.connect(
    host="db4free.net",
    user="sql11488194",
    password="I6pWKd1e91",
    database="sql11488194"
    )
    c = mydb.cursor(buffered=True)
    
    sql = """
    Select * FROM matches WHERE Date LIKE %s AND HomeTeam LIKE %s AND AwayTeam LIKE %s
    """
    temp = (match_entry_f1n.get(),hometeam_entry_f1n.get(),awayteam_entry_f1n.get())
    c.execute(sql, temp)
    result = c.fetchall()
    mydb.commit()
    i = 1
    if(result != []):
        for r_f1n in result:
            output_text_f1n.insert('', 'end', text=str(i), values=(r_f1n[0],r_f1n[1],r_f1n[2],r_f1n[3],r_f1n[4],r_f1n[5],r_f1n[6]))
            enter_review_f1n.config(state= NORMAL)
            i = i + 1
    else:
        enter_review_f1n.config(state= DISABLED)
        output_text_f1n.insert('', 'end', text=str(i), values=("No Record","No Record","No Record","No Record","No Record","No Record","No Record"))

output_text_f1n = ttk.Treeview(frame1new, column=("c1","c2","c3","c4", "c5", "c6","c7"), show='headings', height=10)
output_text_f1n.column("# 1", anchor=CENTER)
output_text_f1n.heading("# 1", text="Date")
output_text_f1n.column("# 2", anchor=CENTER)
output_text_f1n.heading("# 2", text="Stadium_Name")
output_text_f1n.column("# 3", anchor=CENTER)
output_text_f1n.heading("# 3", text="HT_Score")
output_text_f1n.column("# 4", anchor=CENTER)
output_text_f1n.heading("# 4", text="AT_Score")
output_text_f1n.column("# 5", anchor=CENTER)
output_text_f1n.heading("# 5", text="Season")
output_text_f1n.column("# 6", anchor=CENTER)
output_text_f1n.heading("# 6", text="HomeTeam")
output_text_f1n.column("# 7", anchor=CENTER)
output_text_f1n.heading("# 7", text="AwayTeam")
output_text_f1n.grid(row=1, column=0)

scroll_f1n = Scrollbar(frame1new ,command= output_text_f1n.yview).grid(row=1,column=1, sticky='nsew')
discard = Label(frame1new, height=4).grid(row=0)

srch_button_f1n = Button(frame1new, text="Search", height=1, width=5, command=srch_f1n, bg="cyan")
srch_button_f1n.place(relx=0.75, rely=-0.002, anchor='n')

match_label_f1n = Label(frame1new, text="Match date: ")
match_label_f1n.place(relx=0.1, rely=-0.005, anchor='n')

match_entry_f1n = Entry(frame1new, width=30)
match_entry_f1n.place(relx=0.2, rely= 0, anchor='n')
match_entry_f1n.insert(0, "Ex. Tue 19 Apr 2022")

hometeam_label_f1n = Label(frame1new, text="Hometeam: ")
hometeam_label_f1n.place(relx=0.3, rely=-0.005, anchor='n')

hometeam_entry_f1n = Entry(frame1new, width=30)
hometeam_entry_f1n.place(relx=0.4, rely= 0, anchor='n')
hometeam_entry_f1n.insert(0, "Ex. Liverpool")

awayteam_label_f1n = Label(frame1new, text="Awayteam: ")
awayteam_label_f1n.place(relx=0.5, rely=-0.005, anchor='n')

awayteam_entry_f1n = Entry(frame1new, width=30)
awayteam_entry_f1n.place(relx=0.6, rely= 0, anchor='n')
awayteam_entry_f1n.insert(0, "Ex. Manchester United")

rating_label_f1n = Label(frame1new, text="Rating: ", font=12)
rating_label_f1n.place(relx=0.12, rely=0.486, anchor='s')

clicked = IntVar()
ratings=[1,2,3,4,5,6,7,8,9,10]
clicked.set(5)
rating_entry_f1n = OptionMenu(frame1new, clicked, *ratings)
rating_entry_f1n.place(relx=0.17, rely= 0.49, anchor='s')


text_label_f1n = Label(frame1new, text="Review: ", font=12)
text_label_f1n.place(relx=0.26, rely=0.486, anchor='s')

text_entry_f1n = Entry(frame1new, width=50)
text_entry_f1n.place(relx=0.4, rely= 0.481, anchor='s')

enter_review_f1n= Button(frame1new, text="Enter", height=2, width=6, command=review, bg='green')
enter_review_f1n.place(relx=0.6, rely=0.5, anchor= 's')
enter_review_f1n.config(state= DISABLED)

ret_button_f1n = Button(frame1new, text="Return", height=3, width=7, command=ret1new, bg='pink')
ret_button_f1n.place(relx=1, rely=0, anchor=NE)

#Frame for feature 2 (View existing reviews on a given match)
match_label_f2 = Label(frame2, text="Match date: ")
match_label_f2.place(relx=0.1, rely=-0.005, anchor='n')

match_entry_f2 = Entry(frame2, width=30)
match_entry_f2.place(relx=0.2, rely= 0, anchor='n')
match_entry_f2.insert(0, "Ex. Tue 19 Apr 2022")

hometeam_label_f2 = Label(frame2, text="Hometeam: ")
hometeam_label_f2.place(relx=0.3, rely=-0.005, anchor='n')

hometeam_entry_f2 = Entry(frame2, width=30)
hometeam_entry_f2.place(relx=0.4, rely= 0, anchor='n')
hometeam_entry_f2.insert(0, "Ex. Liverpool")

awayteam_label_f2 = Label(frame2, text="Awayteam: ")
awayteam_label_f2.place(relx=0.5, rely=-0.005, anchor='n')

awayteam_entry_f2 = Entry(frame2, width=30)
awayteam_entry_f2.place(relx=0.6, rely= 0, anchor='n')
awayteam_entry_f2.insert(0, "Ex. Manchester United")

def srch_f2():
    global output_text_f2
    for item in output_text_f2.get_children():
          output_text_f2.delete(item)
    mydb = mysql.connector.connect(
    host="db4free.net",
    user="sql11488194",
    password="I6pWKd1e91",
    database="sql11488194"
    )
    c = mydb.cursor(buffered=True)

    sql = """
    Select * FROM fan_review WHERE Match_Date = %s AND HomeTeam = %s AND AwayTeam = %s
    """
    temp = (match_entry_f2.get(),hometeam_entry_f2.get(),awayteam_entry_f2.get())
    c.execute(sql, temp)
    result = c.fetchall()
    mydb.commit()
    i = 1
    if(result != []):
        for r_f2 in result:
            output_text_f2.insert('', 'end', text=str(i), values=(r_f2[0],r_f2[1],r_f2[2],r_f2[3],r_f2[4],r_f2[5]))
            i = i + 1
    else:
        output_text_f2.insert('', 'end', text=str(i), values=("No Record","No Record","No Record","No Record","No Record","No Record"))


    
output_text_f2 = ttk.Treeview(frame2, column=("c1","c2","c3","c4", "c5", "c6"), show='headings', height=30)
output_text_f2.column("# 1", anchor=CENTER)
output_text_f2.heading("# 1", text="Fan_EmailAddr")
output_text_f2.column("# 2", anchor=CENTER)
output_text_f2.heading("# 2", text="Match_Date")
output_text_f2.column("# 3", anchor=CENTER)
output_text_f2.heading("# 3", text="HomeTeam")
output_text_f2.column("# 4", anchor=CENTER)
output_text_f2.heading("# 4", text="AwayTeam")
output_text_f2.column("# 5", anchor=CENTER)
output_text_f2.heading("# 5", text="Rating")
output_text_f2.column("# 6", anchor=CENTER)
output_text_f2.heading("# 6", text="Text")
output_text_f2.grid(row=1, column=0)

scroll_f2 = Scrollbar(frame2 ,command= output_text_f2.yview).grid(row=1,column=1, sticky='nsew')
#scroll_f4 = Scrollbar(frame2,command= output_text_f2.xview).grid(row=2, sticky='nsew')

srch_button_f2 = Button(frame2, text="Search", height=1, width=5, command=srch_f2, bg="cyan")
srch_button_f2.place(relx=0.8, rely= -0.005, anchor='n')
discard = Label(frame2, height=3).grid(row=0, column=5)


ret_button_f2 = Button(frame2, text="Return", height=3, width=7, command=ret2, bg='pink')
ret_button_f2.place(relx=1, rely=0, anchor=NE)

#Frame for feature 3 (register a user)


def reg():
    mydb = mysql.connector.connect(
    host="db4free.net",
    user="sql11488194",
    password="I6pWKd1e91",
    database="sql11488194"
    )
    c = mydb.cursor(buffered=True)
    sql = """
    Insert INTO fan (Email_address, Password, Username, Birthdate, Gender, Age, Fav_Club)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
     
    try:
        bdate = datetime.strptime(Birthdate_entry_f3.get(), '%d/%m/%Y') 
        if((email_entry_f3.get().find('@') != -1) & (len(Password_entry_f3.get()) > 4) & (len(Gender_entry_f3.get()) == 1) & (len(Username_entry_f3.get()) > 4)):
            val = (email_entry_f3.get(), Password_entry_f3.get(), Username_entry_f3.get(), bdate, Gender_entry_f3.get()[0], 2022 - int(bdate.year) , FavClub_entry_f3.get())
            try:
                c.execute(sql, val)
                if(c.rowcount == 1):
                    success_label_f3.config(text="Account created successfully!",fg='green')
                else:
                    success_label_f3.config(text="Failed! please follow the specified format!", fg='red')
            except mysql.connector.IntegrityError:
                success_label_f3.config(text="Failed! Account already Exists!", fg='red')   
        else:
            success_label_f3.config(text="Failed! please follow the specified format!", fg='red')
    except ValueError:
        success_label_f3.config(text="Failed! please follow the specified format!", fg='red')
    
    
    mydb.commit()


success_label_f3 = Label(frame3, fg='green', height=3, width=100, font=15) 
success_label_f3.place(relx=0.1, rely= 0.32)

Email_f3 = Label(frame3, text="Email: ")
Email_f3.place(relx=0.45, rely=0.4, anchor=CENTER)

email_entry_f3 = Entry(frame3, width=30)
email_entry_f3.place(relx=0.57, rely=0.4, anchor=CENTER)
email_entry_f3.insert(0,"Ex. jason25@gmail.com")

Password_f3 = Label(frame3, text="Password: ")
Password_f3.place(relx=0.45, rely=0.43, anchor=CENTER)

Password_entry_f3 = Entry(frame3, width=30)
Password_entry_f3.place(relx=0.57, rely=0.43, anchor=CENTER)
Password_entry_f3.insert(0, "Ex. 123456789 (greater than 4 chars)")

Username_f3 = Label(frame3, text="Username: ")
Username_f3.place(relx=0.45, rely=0.46, anchor=CENTER)


Username_entry_f3 = Entry(frame3, width=30)
Username_entry_f3.place(relx=0.57, rely=0.46, anchor=CENTER)
Username_entry_f3.insert(0, "Ex. Jason24 (greater than 4 chars)")

Birthdate_f3 = Label(frame3, text="Birthdate: ")
Birthdate_f3.place(relx=0.45, rely=0.49, anchor=CENTER)

Birthdate_entry_f3 = Entry(frame3, width=30)
Birthdate_entry_f3.place(relx=0.57, rely=0.49, anchor=CENTER)
Birthdate_entry_f3.insert(0, "Ex. 17/3/2002")

Gender_f3 = Label(frame3, text="Gender: ")
Gender_f3.place(relx=0.45, rely=0.52, anchor=CENTER)

Gender_entry_f3 = Entry(frame3, width=30)
Gender_entry_f3.place(relx=0.57, rely=0.52, anchor=CENTER)
Gender_entry_f3.insert(0, "M/F")

FavClub_f3 = Label(frame3, text="Favorite Club: ")
FavClub_f3.place(relx=0.44, rely=0.55, anchor=CENTER)

FavClub_entry_f3 = Entry(frame3, width=30)
FavClub_entry_f3.place(relx=0.57, rely=0.55, anchor=CENTER)
FavClub_entry_f3.insert(0, "Ex. Liverpool")

reg_button_f3 = Button(frame3, text="Register", height=3, width=8, command= reg, bg='green')
reg_button_f3.place(relx=0.58, rely= 0.62, anchor=CENTER)

ret_button_f3 = Button(frame3, text="Return", height=3, width=7, command=ret3, bg='pink')
ret_button_f3.place(relx=1, rely=0, anchor=NE)

#Frame for feature 4 (Show all the players from a certain nationality and their home teams history)
nationality_entry_f4 = Entry(frame4, width=30)
nationality_entry_f4.grid(row = 0, column=0, padx=20, pady=3)
nationality_entry_f4.insert(0, "Ex. England")

def srch_f4():
    global output_text_f4
    for item in output_text_f4.get_children():
          output_text_f4.delete(item)
    mydb = mysql.connector.connect(
    host="db4free.net",
    user="sql11488194",
    password="I6pWKd1e91",
    database="sql11488194"
    )
    c = mydb.cursor(buffered=True)

    sql = """
    Select FName, LName, C_Name, Season
        FROM player AS p INNER JOIN player_club AS c
        ON p.FName = c.P_FName AND p.LName = c.P_LName AND p.DoB = c.DoB
        WHERE p.Nationality =  %s 
    """
    temp = (nationality_entry_f4.get(),)
    c.execute(sql, temp)
    result = c.fetchall()
    
    i = 1
    for r_f4 in result:
        output_text_f4.insert('', 'end', text=str(i), values=(r_f4[0],r_f4[1],r_f4[2],r_f4[3]))
        i = i + 1
    else:
        output_text_f2.insert('', 'end', text=str(i), values=("No Record","No Record","No Record","No Record"))
    
    
    

srch_button_f4 = Button(frame4, text="Search", height=1, width=5, command=srch_f4, bg="cyan")
srch_button_f4.place(relx=0.51, rely=-0.002, anchor='n')

output_text_f4 = ttk.Treeview(frame4, column=("c1","c2","c3","c4"), show='headings', height=30)
output_text_f4.column("# 1", anchor=CENTER)
output_text_f4.heading("# 1", text="FName")
output_text_f4.column("# 2", anchor=CENTER)
output_text_f4.heading("# 2", text="LName")
output_text_f4.column("# 3", anchor=CENTER)
output_text_f4.heading("# 3", text="C_Name")
output_text_f4.column("# 4", anchor=CENTER)
output_text_f4.heading("# 4", text="Season")
output_text_f4.grid(row=1, column=0)

scroll_f4 = Scrollbar(frame4 ,command= output_text_f4.yview).grid(row=1,column=1, sticky='nsew')

ret_button_f4 = Button(frame4, text="Return", height=3, width=7, command=ret4, bg='pink')
ret_button_f4.place(relx=1, rely=0, anchor=NE)

#Frame 5 for feature 5 (Show the top 10 teams by matches won, home matches won, yellow cards, fouls, and shots)

ret_button_f5 = Button(frame5, text="Return", height=3, width=7, command=ret5, bg='pink')
ret_button_f5.place(relx=1, rely=0, anchor=NE)

#Top 10 teams by wins in the last 4 seasons
output_text_f51 = ttk.Treeview(frame5, column=("c1", "c2"), show='headings', height=17)
output_text_f51.column("# 1", anchor=W)
output_text_f51.heading("# 1", text="Team (Matches won)")
output_text_f51.column("# 2", anchor=CENTER)
output_text_f51.heading("# 2", text="No. Wins")

output_text_f51.grid(row=0, column=0)

mydb = mysql.connector.connect(
host="db4free.net",
user="sql11488194",
password="I6pWKd1e91",
database="sql11488194"
)
c = mydb.cursor(buffered=True)

sql = """
SELECT Winner, COUNT(Winner) FROM matches
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10 
"""

c.execute(sql)
result = c.fetchall()
mydb.commit()
i = 1
for r in result:
  output_text_f51.insert('', 'end', text=str(1), values=(str(i) + ") "+r[0], r[1]))  
  i = i + 1

# output_text_f51.insert('', 'end', text=str(1), values=('1)   Manchester United', 702))
# output_text_f51.insert('', 'end', text=str(2), values=('2)   Arsenal', 616))
# output_text_f51.insert('', 'end', text=str(3), values=('3)   Chelsea', 616))
# output_text_f51.insert('', 'end', text=str(4), values=('4)   Liverpool', 606))
# output_text_f51.insert('', 'end', text=str(5), values=('5)   Tottenham Hotspur', 498))
# output_text_f51.insert('', 'end', text=str(6), values=('6)   Manchester City', 469))
# output_text_f51.insert('', 'end', text=str(7), values=('7)   Everton', 415))
# output_text_f51.insert('', 'end', text=str(8), values=('8)   Newcastle United', 380))
# output_text_f51.insert('', 'end', text=str(9), values=('9)   Aston Villa', 352))
# output_text_f51.insert('', 'end', text=str(10), values=('10) West Ham United', 334))

scroll_f51 = Scrollbar(frame5 ,command= output_text_f51.yview).grid(row=0,column=1, sticky='nsew')

#Top 10 wins as hometeam
output_text_f52 = ttk.Treeview(frame5, column=("c1", "c2"), show='headings', height=17)
output_text_f52.column("# 1", anchor=W)
output_text_f52.heading("# 1", text="Team (Home matches won)")
output_text_f52.column("# 2", anchor=CENTER)
output_text_f52.heading("# 2", text="Win rate in home")

output_text_f52.grid(row=0, column=2)

mydb = mysql.connector.connect(
host="db4free.net",
user="sql11488194",
password="I6pWKd1e91",
database="sql11488194"
)
c = mydb.cursor(buffered=True)

sql = """
SELECT Winner, COUNT(Winner) FROM matches as m
WHERE Winner = HomeTeam
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10 
"""

c.execute(sql)
result = c.fetchall()
mydb.commit()
i = 1
for r in result:
  output_text_f52.insert('', 'end', text=str(1), values=(str(i) + ") "+r[0], r[1]))  
  i = i + 1

# output_text_f52.insert('', 'end', text=str(1), values=('1)   Manchester United', '73 %'))
# output_text_f52.insert('', 'end', text=str(2), values=('2)   Arsenal', '64 %'))
# output_text_f52.insert('', 'end', text=str(3), values=('3)   Liverpool', '63 %'))
# output_text_f52.insert('', 'end', text=str(4), values=('4)   Chelsea', '62 %'))
# output_text_f52.insert('', 'end', text=str(5), values=('5)   Manchester City', '56 %'))
# output_text_f52.insert('', 'end', text=str(6), values=('6)   Tottenham Hotspur', '53 %'))
# output_text_f52.insert('', 'end', text=str(7), values=('7)   Leeds', '50 %'))
# output_text_f52.insert('', 'end', text=str(8), values=('8)   Newcastle United', '50 %'))
# output_text_f52.insert('', 'end', text=str(9), values=('9)   Blackburn', '49 %'))
# output_text_f52.insert('', 'end', text=str(10), values=('10) Everton', '47 %'))

scroll_f52 = Scrollbar(frame5 ,command= output_text_f52.yview).grid(row=0,column=3, sticky='nsew')

#Top 10 teams by yellow cards
output_text_f53 = ttk.Treeview(frame5, column=("c1", "c2"), show='headings', height=17)
output_text_f53.column("# 1", anchor=W)
output_text_f53.heading("# 1", text="Team (Yellow cards)")
output_text_f53.column("# 2", anchor=CENTER)
output_text_f53.heading("# 2", text="No. Yellow cards")

output_text_f53.grid(row=0, column=4)

mydb = mysql.connector.connect(
host="db4free.net",
user="sql11488194",
password="I6pWKd1e91",
database="sql11488194"
)
c = mydb.cursor(buffered=True)

sql = """
SELECT Club_Name, SUM(YellowCards) FROM club_matches
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10 
"""

c.execute(sql)
result = c.fetchall()
mydb.commit()
i = 1
for r in result:
  output_text_f53.insert('', 'end', text=str(1), values=(str(i) + ") "+r[0], r[1]))  
  i = i +1

scroll_f53 = Scrollbar(frame5 ,command= output_text_f53.yview).grid(row=0,column=5, sticky='nsew')

#top 10 teams by fouls
output_text_f54 = ttk.Treeview(frame5, column=("c1", "c2"), show='headings', height=17)
output_text_f54.column("# 1", anchor=W)
output_text_f54.heading("# 1", text="Team (Fouls)")
output_text_f54.column("# 2", anchor=CENTER)
output_text_f54.heading("# 2", text="No. Fouls")

output_text_f54.grid(row=1, column=0)

scroll_f54 = Scrollbar(frame5 ,command= output_text_f54.yview).grid(row=1,column=1, sticky='nsew')

mydb = mysql.connector.connect(
host="db4free.net",
user="sql11488194",
password="I6pWKd1e91",
database="sql11488194"
)
c = mydb.cursor(buffered=True)

sql = """
SELECT Club_Name, SUM(Fouls) FROM club_matches
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10 
"""

c.execute(sql)
result = c.fetchall()
mydb.commit()
i = 1
for r in result:
  output_text_f54.insert('', 'end', text=str(1), values=(str(i) + ") "+r[0], r[1]))   
  i = i +1

#Top 10 teams by shots
output_text_f55 = ttk.Treeview(frame5, column=("c1", "c2"), show='headings', height=17)
output_text_f55.column("# 1", anchor=W)
output_text_f55.heading("# 1", text="Team (Shots)")
output_text_f55.column("# 2", anchor=CENTER)
output_text_f55.heading("# 2", text="No. Shots")

output_text_f55.grid(row=1, column=2)

mydb = mysql.connector.connect(
host="db4free.net",
user="sql11488194",
password="I6pWKd1e91",
database="sql11488194"
)
c = mydb.cursor(buffered=True)

sql = """
SELECT Club_Name, SUM(Shots) FROM club_matches
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10 
"""

c.execute(sql)
result = c.fetchall()
mydb.commit()
i = 1
for r in result:
  output_text_f55.insert('', 'end', text=str(1), values=(str(i) + ") "+r[0], r[1]))  
  i = i+1

scroll_f55 = Scrollbar(frame5 ,command= output_text_f55.yview).grid(row=1,column=3, sticky='nsew')

#Frame 6 for feature "Show all the teams who won the most games by season"

ret_button_f6 = Button(frame6, text="Return", height=3, width=7, command=ret6, bg='pink')
ret_button_f6.place(relx=1, rely=0, anchor=NE)

#Top 10 teams by wins in the last 4 seasons

#Season 2021/22
output_text_f61 = ttk.Treeview(frame6, column=("c1", "c2"), show='headings', height=17)
output_text_f61.column("# 1", anchor=W)
output_text_f61.heading("# 1", text="Team")
output_text_f61.column("# 2", anchor=CENTER)
output_text_f61.heading("# 2", text="No. Wins (Season 2021/22)")

output_text_f61.grid(row=0, column=0)

mydb = mysql.connector.connect(
host="db4free.net",
user="sql11488194",
password="I6pWKd1e91",
database="sql11488194"
)
c = mydb.cursor(buffered=True)

sql = """
SELECT Winner, COUNT(Winner), Season FROM matches WHERE Season = '2021/22'
GROUP BY 1,3
ORDER BY 2 DESC
LIMIT 20
"""

c.execute(sql)
result = c.fetchall()
mydb.commit()
i = 1
for r in result:
  output_text_f61.insert('', 'end', text=str(1), values=(str(i) + ") "+r[0], r[1]))  
  i = i + 1

scroll_f61 = Scrollbar(frame6 ,command= output_text_f61.yview).grid(row=0,column=1, sticky='nsew')

#Season 2020/21
output_text_f62 = ttk.Treeview(frame6, column=("c1", "c2"), show='headings', height=17)
output_text_f62.column("# 1", anchor=W)
output_text_f62.heading("# 1", text="Team")
output_text_f62.column("# 2", anchor=CENTER)
output_text_f62.heading("# 2", text="No. Wins (Season 2020/21)")

output_text_f62.grid(row=0, column=2)

mydb = mysql.connector.connect(
host="db4free.net",
user="sql11488194",
password="I6pWKd1e91",
database="sql11488194"
)
c = mydb.cursor(buffered=True)

sql = """
SELECT Winner, COUNT(Winner), Season FROM matches WHERE Season = '2020/21'
GROUP BY 1,3
ORDER BY 2 DESC
LIMIT 20
"""

c.execute(sql)
result = c.fetchall()
mydb.commit()
i = 1
for r in result:
  output_text_f62.insert('', 'end', text=str(1), values=(str(i) + ") "+r[0], r[1]))  
  i = i + 1

scroll_f62 = Scrollbar(frame6 ,command= output_text_f62.yview).grid(row=0,column=3, sticky='nsew')

#season 2019/2020
output_text_f63 = ttk.Treeview(frame6, column=("c1", "c2"), show='headings', height=17)
output_text_f63.column("# 1", anchor=W)
output_text_f63.heading("# 1", text="Team")
output_text_f63.column("# 2", anchor=CENTER)
output_text_f63.heading("# 2", text="No. Wins (Season 2019/20)")

output_text_f63.grid(row=1, column=0)

mydb = mysql.connector.connect(
host="db4free.net",
user="sql11488194",
password="I6pWKd1e91",
database="sql11488194"
)
c = mydb.cursor(buffered=True)

sql = """
SELECT Winner, COUNT(Winner), Season FROM matches WHERE Season = '2019/20'
GROUP BY 1,3
ORDER BY 2 DESC
LIMIT 20
"""

c.execute(sql)
result = c.fetchall()
mydb.commit()
i = 1
for r in result:
  output_text_f63.insert('', 'end', text=str(1), values=(str(i) + ") "+r[0], r[1]))  
  i = i + 1

scroll_f63 = Scrollbar(frame6 ,command= output_text_f63.yview).grid(row=1,column=1, sticky='nsew')

#Season 2018/19
output_text_f64 = ttk.Treeview(frame6, column=("c1", "c2"), show='headings', height=17)
output_text_f64.column("# 1", anchor=W)
output_text_f64.heading("# 1", text="Team")
output_text_f64.column("# 2", anchor=CENTER)
output_text_f64.heading("# 2", text="No. Wins (Season 2018/19)")

output_text_f64.grid(row=1, column=2)

mydb = mysql.connector.connect(
host="db4free.net",
user="sql11488194",
password="I6pWKd1e91",
database="sql11488194"
)
c = mydb.cursor(buffered=True)

sql = """
SELECT Winner, COUNT(Winner), Season FROM matches WHERE Season = '2018/19'
GROUP BY 1,3
ORDER BY 2 DESC
LIMIT 20
"""

c.execute(sql)
result = c.fetchall()
mydb.commit()
i = 1
for r in result:
  output_text_f64.insert('', 'end', text=str(1), values=(str(i) + ") "+r[0], r[1]))  
  i = i + 1

scroll_f64 = Scrollbar(frame6 ,command= output_text_f64.yview).grid(row=1,column=3, sticky='nsew')


#Frame 7 for feature Query and view a given team information

ret_button_f7 = Button(frame7, text="Return", height=3, width=7, command=ret7, bg='pink')
ret_button_f7.place(relx=1, rely=0, anchor=NE)



output_text_f7 = ttk.Treeview(frame7, column=("c1", "c2", "c3"), show='headings', height=17)
output_text_f7.column("# 1", anchor=CENTER)
output_text_f7.heading("# 1", text="Name")
output_text_f7.column("# 2", anchor=CENTER)
output_text_f7.heading("# 2", text="Website")
output_text_f7.column("# 3", anchor=CENTER)
output_text_f7.heading("# 3", text="Home Stadium")
output_text_f7.grid(row=1, columnspan=4)

def srch_f7():
    global output_text_f7
    for item in output_text_f7.get_children():
          output_text_f7.delete(item)
    mydb = mysql.connector.connect(
    host="db4free.net",
    user="sql11488194",
    password="I6pWKd1e91",
    database="sql11488194"
    )
    c = mydb.cursor(buffered=True)

    sql = """
    SELECT * FROM club WHERE Name = %s
    """
    temp = (team_entry_f7.get(),)
    c.execute(sql,temp)
    result = c.fetchall()
    mydb.commit()
    if(c.rowcount == 1):
        for r in result:
            output_text_f7.insert('', 'end', text=str(1), values=(r[0], r[1], r[2])) 
    else:
        output_text_f7.insert('', 'end', text=str(1), values=('No Record', 'No Record', 'No Record')) 

team_label_f7= Label(frame7, text="Team's name: ")
team_label_f7.grid(row=0, column=0, padx= 0.5)

team_entry_f7 = Entry(frame7, width=30)
team_entry_f7.grid(row=0, column=1)
team_entry_f7.insert(0,"Ex. Liverpool")

srch_button_f7 = Button(frame7, text="Search", height=2, width=6, command=srch_f7, bg='cyan')
srch_button_f7.grid(row=0, column=2)


#Frame 8 for feature Query and view a given player information (by their first and last name)

ret_button_f8 = Button(frame8, text="Return", height=3, width=7, command=ret8, bg='pink')
ret_button_f8.place(relx=1, rely=0, anchor=NE)



output_text_f8 = ttk.Treeview(frame8, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings', height=17)
output_text_f8.column("# 1", anchor=CENTER)
output_text_f8.heading("# 1", text="FName")
output_text_f8.column("# 2", anchor=CENTER)
output_text_f8.heading("# 2", text="LName")
output_text_f8.column("# 3", anchor=CENTER)
output_text_f8.heading("# 3", text="Current Club")
output_text_f8.column("# 4", anchor=CENTER)
output_text_f8.heading("# 4", text="Weight(Kgs)")
output_text_f8.column("# 5", anchor=CENTER)
output_text_f8.heading("# 5", text="Position")
output_text_f8.column("# 6", anchor=CENTER)
output_text_f8.heading("# 6", text="Nationality")
output_text_f8.column("# 7", anchor=CENTER)
output_text_f8.heading("# 7", text="Date of Birth (Y-M-D)")
output_text_f8.column("# 8", anchor=CENTER)
output_text_f8.heading("# 8", text="Height (Cms)")
output_text_f8.grid(row=1, columnspan=8)

def srch_f8():
    global output_text_f8
    for item in output_text_f8.get_children():
          output_text_f8.delete(item)
    mydb = mysql.connector.connect(
    host="db4free.net",
    user="sql11488194",
    password="I6pWKd1e91",
    database="sql11488194"
    )
    c = mydb.cursor(buffered=True)

    sql = """
    SELECT * FROM player WHERE FName LIKE %s AND LName LIKE %s 
    """
    temp = (FName_entry_f8.get(),LName_entry_f8.get())
    c.execute(sql,temp)
    result = c.fetchall()
    mydb.commit()
    if(c.rowcount == 1):
        for r in result:
            output_text_f8.insert('', 'end', text=str(1), values=(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7])) 
    else:
        output_text_f8.insert('', 'end', text=str(1), values=('No Record','No Record','No Record','No Record','No Record','No Record','No Record','No Record')) 

FName_label_f8= Label(frame8, text="First Name: ")
FName_label_f8.grid(row=0, column=0)

FName_entry_f8 = Entry(frame8, width=20)
FName_entry_f8.grid(row=0, column=1)
FName_entry_f8.insert(0,"Ex. Mohamed")

LName_label_f8= Label(frame8, text="Last Name: ")
LName_label_f8.grid(row=0, column=2)

LName_entry_f8 = Entry(frame8, width=20)
LName_entry_f8.grid(row=0, column=3)
LName_entry_f8.insert(0,"Ex. Salah")

srch_button_f8 = Button(frame8, text="Search", height=2, width=5, command=srch_f8, bg='cyan')
srch_button_f8.grid(row=0, column=4)

#Frame 9 for feature Identify the home team for a given stadium name

ret_button_f9 = Button(frame9, text="Return", height=3, width=7, command=ret9, bg='pink')
ret_button_f9.place(relx=1, rely=0, anchor=NE)

output_text_f9 = ttk.Treeview(frame9, column=("c1"), show='headings', height=17)
output_text_f9.column("# 1", anchor=CENTER)
output_text_f9.heading("# 1", text="Home Team Name")
output_text_f9.grid(row=1, column=0)

def srch_f9():
    global output_text_f9
    for item in output_text_f9.get_children():
          output_text_f9.delete(item)
    mydb = mysql.connector.connect(
    host="db4free.net",
    user="sql11488194",
    password="I6pWKd1e91",
    database="sql11488194"
    )
    c = mydb.cursor(buffered=True)

    sql = """
    SELECT Name FROM club WHERE HomeStadium_Name LIKE %s
    """
    temp = (stadium_entry_f9.get(),)
    c.execute(sql,temp)
    result = c.fetchall()
    mydb.commit()
    if(c.rowcount == 1):
        for r in result:
            output_text_f9.insert('', 'end', text=str(1), values=(r)) 
    else:
        output_text_f9.insert('', 'end', text=str(1), values=('NoRecord')) 

stadium_label_f9= Label(frame9, text="Home Stadium's name: ")
stadium_label_f9.grid(row=0, column=0)

stadium_entry_f9 = Entry(frame9, width=20)
stadium_entry_f9.grid(row=0, column=1)
stadium_entry_f9.insert(0,"Ex. Anfield")

srch_button_f9 = Button(frame9, text="Search", height=2, width=7, command=srch_f9, bg='cyan')
srch_button_f9.grid(row=0, column=2)


#Frame 10 for feature Show all the players who played a certain position

ret_button_f10 = Button(frame10, text="Return", height=3, width=7, command=ret10, bg='pink')
ret_button_f10.place(relx=1, rely=0, anchor=NE)

output_text_f10 = ttk.Treeview(frame10, column=("c1", "c2"), show='headings', height=17)
output_text_f10.column("# 1", anchor=CENTER)
output_text_f10.heading("# 1", text="Player's First Name")
output_text_f10.column("# 2", anchor=CENTER)
output_text_f10.heading("# 2", text="Player's Last Name")
output_text_f10.grid(row=1, columnspan=3)

def srch_f10():
    global output_text_f10
    for item in output_text_f10.get_children():
          output_text_f10.delete(item)
    mydb = mysql.connector.connect(
    host="db4free.net",
    user="sql11488194",
    password="I6pWKd1e91",
    database="sql11488194"
    )
    c = mydb.cursor(buffered=True)

    sql = """
    SELECT FName, LName FROM player WHERE Position LIKE %s
    """
    temp = (position_entry_f10.get(),)
    c.execute(sql,temp)
    result = c.fetchall()
    mydb.commit()
    if(c.rowcount >= 1):
        for r in result:
            output_text_f10.insert('', 'end', text=str(1), values=(r[0], r[1])) 
    else:
        output_text_f10.insert('', 'end', text=str(1), values=('No Record', 'No Record')) 

position_label_f10= Label(frame10, text="Position: ")
position_label_f10.grid(row=0, column=0)

position_entry_f10 = Entry(frame10, width=20)
position_entry_f10.grid(row=0, column=1)
position_entry_f10.insert(0,"Ex. Defender")

srch_button_f10 = Button(frame10, text="Search", height=2, width=7, command=srch_f10, bg='cyan')
srch_button_f10.grid(row=0, column=2)

scroll_f10 = Scrollbar(frame10 ,command= output_text_f10.yview).grid(row=1,column=3, sticky='nsew')

#frame 11 for bonus feature Identify all the teams in a given city in the UK

ret_button_f11 = Button(frame11, text="Return", height=3, width=7, command=ret11, bg='pink')
ret_button_f11.place(relx=1, rely=0, anchor=NE)

output_text_f11 = ttk.Treeview(frame11, column=("c1"), show='headings', height=17)
output_text_f11.column("# 1", anchor=CENTER)
output_text_f11.heading("# 1", text="Club")
output_text_f11.grid(row=1, columnspan=2)

def srch_f11():
    global output_text_f11
    for item in output_text_f11.get_children():
          output_text_f11.delete(item)
    mydb = mysql.connector.connect(
    host="db4free.net",
    user="sql11488194",
    password="I6pWKd1e91",
    database="sql11488194"
    )
    c = mydb.cursor(buffered=True)

    sql = """
    SELECT c.Name FROM stadium AS s INNER JOIN club AS c ON s.Name = c.HomeStadium_Name  WHERE Address LIKE CONCAT('%', %s, '%')
    """
    temp = (city_entry_f11.get(),)
    c.execute(sql,temp)
    result = c.fetchall()
    mydb.commit()
    if(c.rowcount >= 1):
        for r in result:
            output_text_f11.insert('', 'end', text=str(1), values=(r)) 
    else:
        output_text_f11.insert('', 'end', text=str(1), values=('NoRecord'))

city_label_f11= Label(frame11, text="City: ")
city_label_f11.grid(row=0, column=0)

city_entry_f11 = Entry(frame11, width=20)
city_entry_f11.grid(row=0, column=1)
city_entry_f11.insert(0,"Ex. London")

srch_button_f11 = Button(frame11, text="Search", height=2, width=7, command=srch_f11, bg='cyan')
srch_button_f11.grid(row=0, column=3)

scroll_f11 = Scrollbar(frame11 ,command= output_text_f11.yview).grid(row=1,column=2, sticky='nsew')






root.mainloop()




# sql = """
# Select * FROM stadium
# """
# c.execute(sql)

# result = c.fetchall()
# for r in result:
#  print(r)
 
