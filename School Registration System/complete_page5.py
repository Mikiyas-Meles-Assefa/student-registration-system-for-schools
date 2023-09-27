from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from PIL import ImageTk, Image
window = Tk()
window.title('Login Page')
height = 600
width = 1000
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.configure(bg="#003681")
global Login_emailName_entry
global Login_passwordName_entry
# ================Background Image ====================
Login_backgroundImage = ImageTk.PhotoImage(Image.open('assets\\bg1.png'))
bg_imageLogin = Label(
    window,
    image=Login_backgroundImage,
    bg="#003681"
)
bg_imageLogin.place(x=0, y=0)



Login_headerText1 = Label(
    bg_imageLogin,
    text="Welcome to School Registration System",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 30 * -1),
    bg="#003681"
)
Login_headerText1.place(x=110, y=23)



# ================ LOGIN TO ACCOUNT HEADER ====================
loginAccount_header = Label(
    bg_imageLogin,
    text="Please Login to continue",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 28 * -1),
    bg="#003681"
)
loginAccount_header.place(x=75, y=121)




# ================ Email Name Section ====================
Login_emailName_image = ImageTk.PhotoImage(Image.open('assets\\email.png'))
Login_emailName_image_Label = Label(
    bg_imageLogin,
    image=Login_emailName_image,
    bg="#003681"
)
Login_emailName_image_Label.place(x=76, y=200)

Login_emailName_text = Label(
    Login_emailName_image_Label,
    text="Username",
    fg="#000000",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#ffc700"
)
Login_emailName_text.place(x=25, y=0)

Login_emailName_icon = ImageTk.PhotoImage(Image.open('assets\\email-icon.png'))
Login_emailName_icon_Label = Label(
    Login_emailName_image_Label,
    image=Login_emailName_icon,
    bg="#ffc700"
)
Login_emailName_icon_Label.place(x=370, y=15)

Login_emailName_entry = Entry(
    Login_emailName_image_Label,
    bd=0,
    bg="#ffc700",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
Login_emailName_entry.place(x=25, y=17, width=345, height=27)


# ================ Password Name Section ====================
Login_passwordName_image =ImageTk.PhotoImage(Image.open('assets\\email.png'))
Login_passwordName_image_Label = Label(
    bg_imageLogin,
    image=Login_passwordName_image,
    bg="#003681"
)
Login_passwordName_image_Label.place(x=80, y=280)

Login_passwordName_text = Label(
    Login_passwordName_image_Label,
    text="Password",
    fg="#000000",
    font=("yu gothic ui Bold", 13 * -1),
    bg="#ffc700"
)
Login_passwordName_text.place(x=25, y=0)

Login_passwordName_icon = ImageTk.PhotoImage(Image.open('assets\\pass-icon.png'))
Login_passwordName_icon_Label = Label(
    Login_passwordName_image_Label,
    image=Login_passwordName_icon,
    bg="#ffc700"
)
Login_passwordName_icon_Label.place(x=370, y=15)

Login_passwordName_entry = Entry(
    Login_passwordName_image_Label,
    bd=0,
    bg="#ffc700",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    show='*',
)
Login_passwordName_entry.place(x=25, y=17, width=345, height=27)

# =============== Login Button ====================
forgotPassword = Button(
    bg_imageLogin,
    text="Log in",
    fg="#ffffff",
    font=("yu gothic ui Bold", 25 * -1),
    bg="#003681",
    bd=0,
    activebackground="#272A37",
    activeforeground="#FFFFFF",
    cursor="hand2",
    command=lambda: login(),
)
forgotPassword.place(x=190, y=360, width=150, height=35)


Login_headerText3 = Label(
    bg_imageLogin,
    text="Developed By Mikiyas Meles - Kidus Daniel - Yordanos Tsegaye",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
Login_headerText3.place(x=350, y=558)

# ================ Forgot Password ====================
forgotPassword = Button(
    bg_imageLogin,
    text="Forgot Password",
    fg="#ffffff",
    font=("yu gothic ui Bold", 15 * -1),
    bg="#003681",
    bd=0,
    activebackground="#ffc700",
    activeforeground="#FFFFFF",
    cursor="hand2",
    command=lambda: forgot_password(),
)
forgotPassword.place(x=180, y=410, width=150, height=35)


def forgot_password():

    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Forgot Password')
    # win.iconbitmap('images\\aa.ico')
    win.configure(background='#272A37')
    win.resizable(False, False)

    # ====== Email ====================
    email_entry3 = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                         bd=0)
    email_entry3.place(x=40, y=80, width=256, height=50)
    email_entry3.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    email_label3 = Label(win, text='• Email', fg="#FFFFFF", bg='#272A37',
                         font=("yu gothic ui", 11, 'bold'))
    email_label3.place(x=40, y=50)

    # ====  New Password ==================
    new_password_entry = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), show='•', highlightthickness=1,
                               bd=0)
    new_password_entry.place(x=40, y=180, width=256, height=50)
    new_password_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    new_password_label = Label(win, text='• New Password', fg="#FFFFFF", bg='#272A37',
                               font=("yu gothic ui", 11, 'bold'))
    new_password_label.place(x=40, y=150)

    # ======= Update password Button ============
    update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                         cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5")
    update_pass.place(x=40, y=260, width=256, height=45)

def login():
    username=Login_emailName_entry.get()
    password=Login_passwordName_entry.get()
    if username=='' and password=='':
        messagebox.showerror('Login', 'Empty Field, Please Enter Correctly')
    elif username == 'Mikiyas' and password =='Mikiyas' or username == 'Kidus'and password =='Kidus' or username == 'Yordanos'and password =='Yordanos' or username == 'admin' and password =='admin' or username == 'zehab2k24' and password =='zehab2k24' or username == 'SJS2024' and password=="SJS2024" or username == 'z' and password =='z':
        #messagebox.showinfo('Login','Successed!')
        window.destroy()
        #insert your registration page

        import tkinter as tk
        from tkinter import filedialog
        from tkinter.filedialog import askopenfile
        import sqlite3
        from tkinter.tix import IMAGETEXT
        from PIL import ImageTk, Image

        my_w = tk.Tk()
        # my_w.geometry("400x300")  # Size of the my_w
        my_w.title('Registration Page')
        my_font1 = ('times', 18, 'bold')

        conn = sqlite3.connect('student_file_data.db')
        c = conn.cursor()
        # c.execute("""CREATE TABLE student_tebler (
        #      firstName_entry  text,
        #      MiddleName_entry text,
        #      lastName_entry  text,
        #      Age_entry integer,
        #      Sex_entry text,
        #      Address_entry text,
        #      emailName_entry text,
        #      id_entry integer,
        #      passwordName_entry integer,
        #      confirm_passwordName_entry integer,
        #      Grade_entry integer,
        #      acadamicback_entry float
        #     )""")
        conn.commit()

        # close connection
        conn.close()

        def save():
            global save
            conn = sqlite3.connect('student_file_data.db')
            c = conn.cursor()
            c.execute(
                "INSERT INTO student_tebler VALUES(:id_entry,:firstName_entry, :MiddleName_entry, :lastName_entry,:Age_entry, :Sex_entry, :Address_entry, :emailName_entry, :passwordName_entry, :confirm_passwordName_entry, :Grade_entry, :acadamicback_entry)",

                {
                    'firstName_entry': firstName_entry.get(),
                    'MiddleName_entry': MiddleName_entry.get(),
                    'lastName_entry': lastName_entry.get(),
                    'Age_entry': Age_entry.get(),
                    'Sex_entry': Sex_entry.get(),
                    'Address_entry': Address_entry.get(),
                    'emailName_entry': emailName_entry.get(),
                    'id_entry': id_entry.get(),
                    'passwordName_entry': passwordName_entry.get(),
                    'confirm_passwordName_entry': confirm_passwordName_entry.get(),
                    'Grade_entry': Grade_entry.get(),
                    'acadamicback_entry': acadamicback_entry.get(),
                })

            conn.commit()
            conn.close()

            firstName_entry.delete(0, END)
            MiddleName_entry.delete(0, END)
            lastName_entry.delete(0, END)
            Age_entry.delete(0, END)
            Sex_entry.delete(0, END)
            Address_entry.delete(0, END)
            emailName_entry.delete(0, END)
            id_entry.delete(0, END)
            passwordName_entry.delete(0, END)
            confirm_passwordName_entry.delete(0, END)
            Grade_entry.delete(0, END)
            acadamicback_entry.delete(0, END)


        def searcher():
            search_for = tk.Tk()
            search_for.title('student info')
            search_for.geometry("900x100")
            with sqlite3.connect('student_file_data.db') as conn:

                c = conn.cursor()
                # searched = search_entry.get()
                c.execute("SELECT * FROM student_tebler WHERE firstname_entry = ?", (Searchid_entry.get(),))

                # name = (searched, )
                # result = c.execute(sql)
                resultants = c.fetchall()

                if not resultants:
                    search_for.destroy()
                    messagebox.showerror('student info', 'Incorrect id')

                printerer = ''
                for resultant in resultants:
                    printerer += str(resultant[0]) + "\t " + str(resultant[1]) + "\t " + str(resultant[2]) + "\t " + str(
                            resultant[3]) + " \t" + str(resultant[4]) + "\t " + str(resultant[5]) + "\t " + str(resultant[6]) + "\t" + str(
                            resultant[7]) + "\t " + str(resultant[8]) + "\t " +str(resultant[9]) + "\t " +str(resultant[10]) + "\t "+str(resultant[11]) +"\n"

                search_for_label = Label(search_for, text=printerer)
                search_for_label.place(x=169, y=13)


        def delete():
            conn = sqlite3.connect('student_file_data.db')
            c = conn.cursor()

            c.execute("DELETE from student_tebler WHERE firstname_entry =?",  (Searchid_entry.get(),))

            conn.commit()
            conn.close()

            import tkinter as tk



        def query():
            global show
            show = tk.Tk()
            show.title('Show Student Lists')
            show.geometry("1300x400+-20+0")
            tree = ttk.Treeview(show)
            tree["columns"] = ("ID", "First Name", "Middle Name", "Last Name", "Age", "Sex", "Address", "Email", "School-Year", "Phone No", "Grade", "Average")

            # Set column headings
            tree.heading("#1", text="ID")
            tree.heading("#2", text="First Name")
            tree.heading("#3", text="Middle Name")
            tree.heading("#4", text="Last Name")
            tree.heading("#5", text="Age")
            tree.heading("#6", text="Sex")
            tree.heading("#7", text="Address")
            tree.heading("#8", text="Email")
            tree.heading("#9", text="School-Year")
            tree.heading("#10", text="Phone No")
            tree.heading("#11", text="Grade")
            tree.heading("#12", text="Average")

            # Set column widths
            tree.column("#0", width=1)
            tree.column("#1", width=50)
            tree.column("#2", width=115)
            tree.column("#3", width=115)
            tree.column("#4", width=115)
            tree.column("#5", width=35)
            tree.column("#6", width=30)
            tree.column("#7", width=100)
            tree.column("#8", width=200)
            tree.column("#9", width=50)
            tree.column("#10", width=150)
            tree.column("#11", width=30)
            tree.column("#12", width=50)



            tree.pack(fill="both", expand=True)

            # Add horizontal scrollbar
            xscroll = ttk.Scrollbar(show, orient="horizontal", command=tree.xview)
            xscroll.pack(side="bottom", fill="x")
            tree.configure(xscrollcommand=xscroll.set)

            conn = sqlite3.connect('student_file_data.db')
            c = conn.cursor()

            # Retrieve records from the database
            c.execute("SELECT * FROM student_tebler")
            records = c.fetchall()

            for record in records:
                tree.insert("", "end", values=record)

            conn.close()

            show.mainloop()








        def edit():
            conn = sqlite3.connect('student_file_data.db')
            c = conn.cursor()
            c.execute("""UPDATE student_tebler SET
                    id_entry= :M,
                    firstName_entry = :A,
                    MiddleName_entry = :B,
                    lastName_entry = :C,
                    Age_entry = :D,
                    Sex_entry = :E,
                    Address_entry = :F,
                    emailName_entry= :G,
                    passwordName_entry = :H,
                    confirm_passwordName_entry= :I,
                    Grade_entry = :J,
                    acadamicback_entry = :K
                    WHERE id_entry = :id_entry""",
                      {
                          'A': firstName_entrye.get(),
                          'B': MiddleName_entrye.get(),
                          'C': lastName_entrye.get(),
                          'D': Age_entrye.get(),
                          'E': Sex_entrye.get(),
                          'F': Address_entrye.get(),
                          'G': emailName_entrye.get(),
                          'H': passwordName_entrye.get(),
                          'I': confirm_passwordName_entrye.get(),
                          'J': Grade_entrye.get(),
                          'K': acadamicback_entrye.get(),
                          'M': id_entrye.get(),
                          'id_entry': id_entrye.get()
                      })
            conn.commit()

            # close connection
            conn.close()

            root.destroy()

        def update():
            global root
            root = tk.Tk()
            root.title('Update file page')
            # root.geometry("600X500")
            # my_font1('times', 18, 'bold')

            global firstName_entrye
            global MiddleName_entrye
            global lastName_entrye
            global Age_entrye
            global Sex_entrye
            global Address_entrye
            global emailName_entrye
            global passwordName_entrye
            global confirm_passwordName_entrye
            global Grade_entrye
            global acadamicback_entrye
            global id_entrye
            global height
            global width
            global x
            global y
            # root.configure(bg="#003399")

            height = 300
            width = 600
            x = (root.winfo_screenwidth() // 2) - (width // 2)
            y = (root.winfo_screenheight() // 4) - (height // 4)
            root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

            conn = sqlite3.connect('student_file_data.db')
            c = conn.cursor()
            c.execute("SELECT * FROM student_tebler WHERE id_entry= " + Searchid_entry.get())
            records = c.fetchall()

            firstName_entrye = Entry(root, width=20)
            firstName_entrye.grid(row=1, column=1)

            MiddleName_entrye = Entry(root, width=20)
            MiddleName_entrye.grid(row=2, column=1)

            lastName_entrye = Entry(root, width=20)
            lastName_entrye.grid(row=3, column=1)

            Age_entrye = Entry(root, width=20)
            Age_entrye.grid(row=4, column=1)

            Sex_entrye = Entry(root, width=20)
            Sex_entrye.grid(row=5, column=1)

            Address_entrye = Entry(root, width=20)
            Address_entrye.grid(row=6, column=1)

            emailName_entrye = Entry(root, width=20)
            emailName_entrye.grid(row=7, column=1)

            passwordName_entrye = Entry(root, width=20)
            passwordName_entrye.grid(row=8, column=1)

            confirm_passwordName_entrye = Entry(root, width=20)
            confirm_passwordName_entrye.grid(row=9, column=1)

            Grade_entrye = Entry(root, width=20)
            Grade_entrye.grid(row=10, column=1)

            acadamicback_entrye = Entry(root, width=20)
            acadamicback_entrye.grid(row=11, column=1)

            id_entrye = Entry(root, width=20)
            id_entrye.grid(row=0, column=1)

            id_labele = Label(root, text='Id number')
            id_labele.grid(row=0, column=0)

            f_name_labele = Label(root, text='First name')
            f_name_labele.grid(row=1, column=0)

            midle_labele = Label(root, text='Midle name')
            midle_labele.grid(row=2, column=0)

            l_name_labele = Label(root, text='Last name')
            l_name_labele.grid(row=3, column=0)

            age_labele = Label(root, text='Age ')
            age_labele.grid(row=4, column=0)

            sex_labele = Label(root, text='Sex')
            sex_labele.grid(row=5, column=0)

            adress_labele = Label(root, text='Address')
            adress_labele.grid(row=6, column=0)

            email_labele = Label(root, text='Email ')
            email_labele.grid(row=7, column=0)

            pass_labele = Label(root, text='School Year')
            pass_labele.grid(row=8, column=0)

            conf_labele = Label(root, text='Phone Number')
            conf_labele.grid(row=9, column=0)

            grade_labele = Label(root, text='Grade')
            grade_labele.grid(row=10, column=0)

            acc_labele = Label(root, text='Average ')
            acc_labele.grid(row=11, column=0)

            for record in records:
                firstName_entrye.insert(0, record[0])
                MiddleName_entrye.insert(0, record[1])
                lastName_entrye.insert(0, record[2])
                Age_entrye.insert(0, record[3])
                Sex_entrye.insert(0, record[4])
                Address_entrye.insert(0, record[5])
                emailName_entrye.insert(0, record[6])
                id_entrye.insert(0, record[7])
                passwordName_entrye.insert(0, record[8])
                confirm_passwordName_entrye.insert(0, record[9])
                Grade_entrye.insert(0, record[10])
                acadamicback_entrye.insert(0, record[11])

                button_save = Button(
                    root,
                    text="Update",
                    bd=0,
                    fg="#1b1b1b",
                    bg="#ffc800",
                    highlightthickness=0,
                    font=("yu gothic ui SemiBold", 16 * -1),
                    command=edit)
                button_save.grid(row=12, column=3)

            root.resizable(True, True)
            root.mainloop()

        height = 720
        width = 1280
        x = (my_w.winfo_screenwidth() // 2) - (width // 2)
        y = (my_w.winfo_screenheight() // 4) - (height // 4)
        my_w.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        my_w.configure(bg="#003399")

        conn = sqlite3.connect('student_file_data.db')
        c = conn.cursor()

        # ================ Background Image ====================
        backgroundImage = ImageTk.PhotoImage(Image.open('assets\\image_2.png'))
        bg_image = Label(
            my_w,
            image=backgroundImage,
            bg="#003399"
        )
        bg_image.place(x=1, y=1)

        # ================ Header Text Left ====================
        headerText_image_left = ImageTk.PhotoImage(Image.open('assets\\headerText_image.png'))
        headerText_image_label1 = Label(
            bg_image,
            image=headerText_image_left,
            bg="#003399"
        )
        headerText_image_label1.place(x=180, y=130)

        headerText1 = Label(
            bg_image,
            text="School Registration And Controlling System (SRCS)",
            fg="#FFFFFF",
            font=("yu gothic ui bold", 30 * -1),
            bg="#003399"
        )
        headerText1.place(x=220, y=125)

        # ================ CREATE ACCOUNT HEADER ====================
        createAccount_header = Label(
            bg_image,
            text="Student Application Form",
            fg="#FFFFFF",
            font=("yu gothic ui Bold", 20 * -1),
            bg="#003399"
        )
        createAccount_header.place(x=400, y=190)

        # ================ First Name Section ====================
        firstName_image = ImageTk.PhotoImage(Image.open('assets\\input_img.png'))
        firstName_image_Label = Label(
            bg_image,
            image=firstName_image,
            bg="#003681"
        )
        firstName_image_Label.place(x=80, y=235)

        firstName_text = Label(
            firstName_image_Label,
            text="First name",
            fg="#1b1b1b",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#ffc800"
        )
        firstName_text.place(x=25, y=0)

        firstName_icon = ImageTk.PhotoImage(Image.open('assets\\name_icon.png'))
        firstName_icon_Label = Label(
            firstName_image_Label,
            image=firstName_icon,
            bg="#ffc800"
        )
        firstName_icon_Label.place(x=159, y=15)

        firstName_entry = Entry(
            firstName_image_Label,
            bd=0,
            fg="#1b1b1b",
            bg="#ffc800",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        firstName_entry.place(x=25, y=17, width=140, height=27)

        # ================ Middle Name Section ====================
        MiddleName_image = ImageTk.PhotoImage(Image.open('assets\\input_img.png'))
        MiddleName_image_Label = Label(
            bg_image,
            image=MiddleName_image,
            bg="#003681"
        )
        MiddleName_image_Label.place(x=293, y=235)

        MiddleName_text = Label(
            MiddleName_image_Label,
            text="Middle name",
            fg="#1b1b1b",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#ffc800"
        )
        MiddleName_text.place(x=25, y=0)

        MiddleName_icon = ImageTk.PhotoImage(Image.open('assets\\name_icon.png'))
        MiddleName_icon_Label = Label(
            MiddleName_image_Label,
            image=MiddleName_icon,
            bg="#ffc800"
        )
        MiddleName_icon_Label.place(x=159, y=15)

        MiddleName_entry = Entry(
            MiddleName_image_Label,
            bd=0,
            fg="#1b1b1b",
            bg="#ffc800",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        MiddleName_entry.place(x=25, y=17, width=140, height=27)
        # ================ Last Name Section ====================
        lastName_image = ImageTk.PhotoImage(Image.open('assets\\input_img.png'))
        lastName_image_Label = Label(
            bg_image,
            image=lastName_image,
            bg="#003681"
        )
        lastName_image_Label.place(x=506, y=235)

        lastName_text = Label(
            lastName_image_Label,
            text="Last name",
            fg="#1b1b1b",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#ffc800"
        )
        lastName_text.place(x=25, y=0)

        lastName_icon = ImageTk.PhotoImage(Image.open('assets\\name_icon.png'))
        lastName_icon_Label = Label(
            lastName_image_Label,
            image=lastName_icon,
            bg="#ffc800"
        )
        lastName_icon_Label.place(x=159, y=15)

        lastName_entry = Entry(
            lastName_image_Label,
            bd=0,
            fg="#1b1b1b",
            bg="#ffc800",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        lastName_entry.place(x=25, y=17, width=140, height=27)

        # ================ Age Section ====================
        Age_image = ImageTk.PhotoImage(Image.open('assets\\input_img.png'))
        Age_image_Label = Label(
            bg_image,
            image=Age_image,
            bg="#003681"
        )
        Age_image_Label.place(x=719, y=235)

        Age_text = Label(
            Age_image_Label,
            text="Age",
            fg="#1b1b1b",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#ffc800"
        )
        Age_text.place(x=25, y=0)

        Age_icon = ImageTk.PhotoImage(Image.open('assets\\name_icon.png'))
        Age_icon_Label = Label(
            Age_image_Label,
            image=Age_icon,
            bg="#ffc800"
        )
        Age_icon_Label.place(x=159, y=15,)

        Age_entry = Entry(
            Age_image_Label,
            bd=0,
            fg="#1b1b1b",
            bg="#ffc800",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        Age_entry.place(x=25, y=20, width=140, height=27)

        # upload file
        frame = LabelFrame(my_w, text='')
        frame.place(x=1000, y=100)
        h = 100
        w = 100
        a = (frame.winfo_screenwidth() // 2) - (w // 2)
        b = (frame.winfo_screenheight() // 4) - (h // 4)

        # def upload_file():
        #     global img
        #     f_types = [('Jpg Files', '*.jpg')]
        #     f_types = [('Png Files', '*.png')]

        #     filename = filedialog.askopenfilename(filetypes=f_types)
        #     img = IMAGETEXT.PhotoImage(file=filename)

        # b1 = tk.Button(bg_image, text='Upload photo', font=("yu gothic ui SemiBold", 13 * -1), width=10,
        #                command=lambda: upload_file())
        # b1.place(x=820, y=500)

        # ================ Sex Section ====================
        Sex_image = ImageTk.PhotoImage(Image.open('assets\\input_img.png'))
        Sex_image_Label = Label(
            bg_image,
            image=Sex_image,
            bg="#003681"
        )
        Sex_image_Label.place(x=80, y=302)

        Sex_text = Label(
            Sex_image_Label,
            text="Sex",
            fg="#1b1b1b",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#ffc800"
        )
        Sex_text.place(x=25, y=0)

        Sex_icon = ImageTk.PhotoImage(Image.open('assets\\name_icon.png'))
        Sex_icon_Label = Label(
            Sex_image_Label,
            image=Sex_icon,
            bg="#ffc800"
        )
        Sex_icon_Label.place(x=159, y=15)

        Sex_entry = Entry(
            Sex_image_Label,
            bd=0,
            fg="#1b1b1b",
            bg="#ffc800",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        Sex_entry.place(x=25, y=20, width=140, height=27)

        # ================ Address Section ====================
        Address_image = ImageTk.PhotoImage(Image.open('assets\\input_img.png'))
        Address_image_Label = Label(
            bg_image,
            image=Address_image,
            bg="#003681"
        )
        Address_image_Label.place(x=293, y=302)

        Address_text = Label(
            Address_image_Label,
            text="Address",
            fg="#1b1b1b",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#ffc800"
        )
        Address_text.place(x=25, y=0)

        Address_icon = ImageTk.PhotoImage(Image.open('assets\\name_icon.png'))
        Address_icon_Label = Label(
            Address_image_Label,
            image=Address_icon,
            bg="#ffc800"
        )
        Address_icon_Label.place(x=159, y=15)

        Address_entry = Entry(
            Address_image_Label,
            bd=0,
            fg="#1b1b1b",
            bg="#ffc800",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        Address_entry.place(x=25, y=20, width=140, height=27)

        # ================ Email Name Section ====================
        emailName_image = ImageTk.PhotoImage(Image.open('assets\\email.png'))
        emailName_image_Label = Label(
            bg_image,
            image=emailName_image,
            bg="#003681"
        )
        emailName_image_Label.place(x=506, y=302)

        emailName_text = Label(
            emailName_image_Label,
            text="Email account",
            fg="#1b1b1b",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#ffc800"
        )
        emailName_text.place(x=25, y=0)

        emailName_icon = ImageTk.PhotoImage(Image.open('assets\\email-icon.png'))
        emailName_icon_Label = Label(
            emailName_image_Label,
            image=emailName_icon,
            bg="#ffc800"
        )
        emailName_icon_Label.place(x=370, y=15)

        emailName_entry = Entry(
            emailName_image_Label,
            bd=0,
            fg="#1b1b1b",
            bg="#ffc800",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        emailName_entry.place(x=25, y=17, width=354, height=27)

        # ================ School Year Section ====================
        passwordName_image = ImageTk.PhotoImage(Image.open('assets\\input_img.png'))
        passwordName_image_Label = Label(
            bg_image,
            image=passwordName_image,
            bg="#003681"
        )
        passwordName_image_Label.place(x=80, y=369)

        passwordName_text = Label(
            passwordName_image_Label,
            text="School Year",
            fg="#1b1b1b",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#ffc800"
        )
        passwordName_text.place(x=25, y=0)

        passwordName_icon = ImageTk.PhotoImage(Image.open('assets\\name_icon.png'))
        passwordName_icon_Label = Label(
            passwordName_image_Label,
            image=passwordName_icon,
            bg="#ffc800"
        )
        passwordName_icon_Label.place(x=159, y=15)

        passwordName_entry = Entry(
            passwordName_image_Label,
            fg="#1b1b1b",
            bd=0,
            bg="#ffc800",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        passwordName_entry.place(x=25, y=17, width=140, height=27)

        # ================ student Phone Number Section ====================
        confirm_passwordName_image = ImageTk.PhotoImage(
            Image.open('assets\\input_img.png'))
        confirm_passwordName_image_Label = Label(
            bg_image,
            image=confirm_passwordName_image,
            bg="#003681"
        )
        confirm_passwordName_image_Label.place(x=293, y=369)

        confirm_passwordName_text = Label(
            confirm_passwordName_image_Label,
            text="Student Phone No",
            fg="#1b1b1b",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#ffc800"
        )
        confirm_passwordName_text.place(x=25, y=0)

        confirm_passwordName_icon = ImageTk.PhotoImage(
            Image.open('assets\\name_icon.png'))
        confirm_passwordName_icon_Label = Label(
            confirm_passwordName_image_Label,
            image=confirm_passwordName_icon,
            bg="#ffc800"
        )
        confirm_passwordName_icon_Label.place(x=159, y=15)

        confirm_passwordName_entry = Entry(
            confirm_passwordName_image_Label,
            bd=0,
            fg="#1b1b1b",
            bg="#ffc800",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        confirm_passwordName_entry.place(x=25, y=17, width=140, height=27)

        # ================ Grade Section ====================
        Grade_image = ImageTk.PhotoImage(Image.open('assets\\input_img.png'))
        Grade_image_Label = Label(
            bg_image,
            image=Grade_image,
            bg="#003681"
        )
        Grade_image_Label.place(x=506, y=369)

        Grade_text = Label(
            Grade_image_Label,
            text="Grade",
            fg="#1b1b1b",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#ffc800"
        )
        Grade_text.place(x=25, y=0)

        Grade_icon = ImageTk.PhotoImage(Image.open('assets\\name_icon.png'))
        Grade_icon_Label = Label(
            Grade_image_Label,
            image=Grade_icon,
            bg="#ffc800"
        )
        Grade_icon_Label.place(x=159, y=15)

        Grade_entry = Entry(
            Grade_image_Label,
            bd=0,
            fg="#1b1b1b",
            bg="#ffc800",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        Grade_entry.place(x=25, y=20, width=140, height=27)
    
        # ================ acadamicback Section ====================
        acadamicback_image = ImageTk.PhotoImage(Image.open('assets\\input_img.png'))
        acadamicback_image_Label = Label(
            bg_image,
            image=acadamicback_image,
            bg="#003681"
        )
        acadamicback_image_Label.place(x=719, y=369)

        acadamicback_text = Label(
            acadamicback_image_Label,
            text="Last year's average ",
            fg="#1b1b1b",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#ffc800"
        )
        acadamicback_text.place(x=25, y=0)

        acadamicback_icon = ImageTk.PhotoImage(Image.open('assets\\name_icon.png'))
        acadamicback_icon_Label = Label(
            acadamicback_image_Label,
            image=acadamicback_icon,
            bg="#ffc800"
        )
        acadamicback_icon_Label.place(x=159, y=15)

        acadamicback_entry = Entry(
            acadamicback_image_Label,
            bd=0,
            fg="#1b1b1b",
            bg="#ffc800",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        acadamicback_entry.place(x=25, y=20, width=140, height=27)

        # ================ Header Text Down ====================

        headerText3 = Label(
            bg_image,
            text="Developed by Mikiyas Meles - Kidus Daniel - Yordanos Tsegaye",
            fg="#FFFFFF",
            font=("yu gothic ui bold", 17 * -1),
            bg="#272A37"
        )  
        headerText3.place(x=750, y=670)
        


        # =================Entry for id================

        id_image = ImageTk.PhotoImage(Image.open('assets\\input_img.png'))
        id_image_Label = Label(
             bg_image,
            image=id_image,
             bg="#003681"
        )
        id_image_Label.place(x=80, y=436)
        id_text = Label(
             id_image_Label,
             text="ID Number ",
             fg="#1b1b1b",
             font=("yu gothic ui SemiBold", 13 * -1),
             bg="#ffc800"
        )
        id_text.place(x=25, y=0)

        id_icon = ImageTk.PhotoImage(Image.open('assets\\name_icon.png'))
        id_icon_Label = Label(
             acadamicback_image_Label,
             image=acadamicback_icon,
             bg="#ffc800"
        )
        id_icon_Label.place(x=159, y=12)

        id_entry = Entry(
             id_image_Label,
             bd=0,
             fg="#1b1b1b",
             bg="#ffc800",
             highlightthickness=0,
             font=("yu gothic ui SemiBold", 16 * -1),
        )
        id_entry.place(x=25, y=20, width=140, height=27)



        # button_s = Button(
        #     my_w, 
        #     text='Submit', 
        #     command=save, 
        #     font=("yu gothic ui SemiBold", 13 * -1), width=10)
        # button_s.place(x=980, y=455)

        # ================ SUBMIT Button ====================
        subbut_image_1 = PhotoImage(
            file="assets\\1.png")
        button_s = Button(
            my_w,
            command=save,
            image=subbut_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#ffffff",
            bg="#003681",
            cursor="hand2",
        )
        button_s.place(x=1030, y=260)

        # ================ Update Button ====================
        subbut_image_2 = PhotoImage(
            file="assets\\updatebut.png")
        button_u = Button(
            my_w,
            command=update,
            image=subbut_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#ffffff",
            bg="#003681",
            cursor="hand2",
        )
        button_u.place(x=1030, y=300)

        # ================ Delete Button ====================
        subbut_image_3 = PhotoImage(
            file="assets\\delete.png")
        button_v = Button(
            my_w,
            command=delete,
            image=subbut_image_3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#ffffff",
            bg="#003681",
            cursor="hand2",
        )
        button_v.place(x=1030, y=340)

        # ================ Show Record Button ====================
        subbut_image_4 = PhotoImage(
            file="assets\\showrecord.png")
        button_w = Button(
            my_w,
            command=query,
            image=subbut_image_4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#ffffff",
            bg="#003681",
            cursor="hand2",
        )
        button_w.place(x=1030, y=380)

        # ================ Home Page Header Image ====================
        headerImage = PhotoImage(file="assets\\Home_Header.png")
        bg_image = Label(
            my_w,
            image=headerImage,
            bg="#ffffff"
        )
        bg_image.place(x=1, y=1)
        # =============== SJS Logo Header Image Button ====================
        logo_button_image_1 = PhotoImage(
            file="assets\\sjs_logo1.png")
        logo_button_1 = Button(
            image=logo_button_image_1,
            borderwidth=0,
            bg="#ffffff",
            highlightthickness=0,
            relief="flat",
            activebackground="#FFFFFF",
            cursor="hand2",
        )
        logo_button_1.place(x=45, y=25)

                # ================ Search Bar Section ====================
        SearchName_image = ImageTk.PhotoImage(Image.open('assets\\search.png'))
        SearchName_image_Label = Label(
            bg_image,
            image=SearchName_image,
            bg="#ffffff"
        )
        SearchName_image_Label.place(x=850, y=45)

        Searchid_entry = Entry(
            SearchName_image_Label,
            bd=0,
            fg="#ffffff",
            bg="#003681",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        Searchid_entry.place(x=50, y=14, width=180, height=27)

                # =============== Search Button ====================
        Login_button_image_1 = ImageTk.PhotoImage(Image.open('assets\\search_Icon.png'))
        Login_button_1 = Button(
            bg="#003681",
            image=Login_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#ffffff",
            cursor="hand2",
            command=searcher
        )
        Login_button_1.place(x=1180, y=65)


        
        # button_u = Button(my_w, text='Update', command=update, font=("yu gothic ui SemiBold", 13 * -1), width=10)
        # button_u.place(x=980, y=500)

        # button_d = Button(my_w, text='Delete', command=delete, font=("yu gothic ui SemiBold", 13 * -1), width=10)
        # button_d.place(x=1085, y=455)

        # 6 create show record button
        # show_button = Button(my_w, text='Show Record', font=("yu gothic ui SemiBold", 13 * -1), command=querry)
        # show_button.place(x=1085, y=500)

        # allow changes
        conn.commit()

        # close connection
        conn.close()

        my_w.resizable(True, True)
        my_w.mainloop()

    else:
        messagebox.showerror('Login', 'Incorect Password')


def Sign_up():
    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Create Account')
    # win.iconbitmap('images\\aa.ico')
    win.configure(background='#272A37')
    win.resizable(False, False)

    # ====== Email ====================
    email_entry3 = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                         bd=0)
    email_entry3.place(x=40, y=80, width=256, height=50)
    email_entry3.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    email_label3 = Label(win, text='• Email', fg="#FFFFFF", bg='#272A37',
                         font=("yu gothic ui", 11, 'bold'))
    email_label3.place(x=40, y=50)

    # ====  New Password ==================
    new_password_entry = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), show='•', highlightthickness=1,
                               bd=0)
    new_password_entry.place(x=40, y=180, width=256, height=50)
    new_password_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    new_password_label = Label(win, text='• New Password', fg="#FFFFFF", bg='#272A37',
                               font=("yu gothic ui", 11, 'bold'))
    new_password_label.place(x=40, y=150)

    # ======= Update password Button ============
    update_pass = Button(win, fg='#f8f8f8', text='Sign Up', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                         cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5")
    update_pass.place(x=40, y=260, width=256, height=45)








window.resizable(False, False)
window.mainloop()