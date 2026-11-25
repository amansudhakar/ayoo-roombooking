"""

Ayoo! Rooms ------------  Source Code


--> Main Program
"""
from time import sleep
from os import startfile
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.scrolledtext import *
from random import choice
from json import load
from ayoosql import *
'''

'''
class AyooException (Exception) : pass

try :
    root = Tk()
    root.geometry("700x330")
    root.minsize(700, 330)
    root.maxsize(700, 330)
    root.iconbitmap(r'imges\icon.ico')
    root.attributes("-topmost", True)

    def autogreet() :

        global M
        M.x2.config(text = choice(title_greet))
        root.after(3000, autogreet)
        
    def reopen(current, parent = root):

        current.destroy()
        sleep(0.15)
        parent.deiconify()

    def toggle (action, username, toggle_ = None) :

        do = ayoocon()
        cur = do.cursor()
        if action.upper() == 'GET' :
            
            query =  f'select Toggles from user_data where Username = "{username}"'
            cur.execute(query)
            result = cur.fetchone()
            tggl = list(result[0])
            do.close()
            return tggl

        elif action.upper() == 'SET' :
            
            query = f'Update user_data set Toggles = "{toggle_}" where Username = "{username}"'
            cur.execute(query)
            do.commit()
            do.close()

    title_greet = load(open(r'greetings.json','r'))

    '''

    '''
    ayootit = PhotoImage(file = r'imges\logo.png')
    ayootitw = PhotoImage(file = r'imges\logow.png')
    sanam = PhotoImage(file = r'imges\logo 3.png')
    signinimg = PhotoImage(file = r'imges\signin.png')
    signupimg = PhotoImage(file = r'imges\signup.png')
    adminimg = PhotoImage(file = r'imges\admin.png')
    chin = PhotoImage(file = r'imges\chin.png')
    chot = PhotoImage(file = r'imges\chot.png')
    rmdet = PhotoImage(file = r'imges\rmdet.png')
    bkrm = PhotoImage(file = r'imges\bkrm.png')
    adrm = PhotoImage(file = r'imges\adrm.png')
    rmstat = PhotoImage(file = r'imges\rmstat.png')
    delrm = PhotoImage(file= r'imges\delrm.png')
    rm = PhotoImage(file= r'imges\rm.png')
    addrm = PhotoImage(file=r'imges\addrm.png')
    delerm = PhotoImage(file=r'imges\delete.png')
    rmst = PhotoImage(file=r'imges\rmst.png')
    rms = PhotoImage(file=r'imges\rooms.png')
    detlabel=PhotoImage(file=r'imges\rmdetlabel.png')
    '''

    '''
    theme = ('#F0F0F0', '#333333', '#D8DCD6', '#000000', ayootit)
    def themeset(themee):

        '''
                theme = ( <bg>, <fg>, <buttonbg>, <textg>, <logotitle> )
                all colours in hexcodes
        '''
        
        global theme, root, M
        if themee == 0 : theme = ('#F0F0F0', '#333333', '#D8DCD6', '#000000', ayootit)
        elif themee == 1 : theme = ('#F5F5DC', '#800020', '#DAA520', '#800020', ayootit)
        elif themee == 2 : theme = ('#001F54', '#D4AF37', '#2C6B56', '#F9F9F9', ayootitw)
        elif themee == 3 : theme = ('#333333', '#F4F4F4', '#FF6F61', 'lightblue', ayootitw)
        elif themee == 4 : theme = ('#2D6A4F', '#A1632C', '#2D6A4F', '#F1E3D3', ayootit)
        elif themee == 5 : theme = ('#00A9E0', '#FFCC00', '#FF6A13', '#FFFFFF', ayootit)
        elif themee == 6 : theme = ('#FFC0CB', '#FF1493', '#FF6347', '#DC143C', ayootit)
        elif themee == 7 : theme = ('#212121', '#FFCC00', '#212121', '#FFCC00', ayootitw)
        elif themee == 8 : theme = ('#000000', '#F1C27D', '#800020', '#F4F4F4', ayootitw)
        elif themee == 9 : theme = ('#888888', '#9C27B0', '#3F51B5', '#E1BEE7', ayootit)
        M.title.config(bg = theme[0])
        M.butts.config(bg = theme[0])
        M.view.config(bg = theme[0], fg = theme[1], activebackground = theme[2], activeforeground = theme[3])
        M.helpp.config(bg = theme[0], fg = theme[1], activebackground = theme[2],  activeforeground = theme[3])
        M.themes.config(bg = theme[0], fg = theme[1], activebackground = theme[2],  activeforeground = theme[3])
        M.x1.config(bg = theme[0], image = theme[4]); M.x2.config(bg = theme[0], fg = theme[3]); M.x3.config(bg = theme[0])
        M.y1.config(bg = theme[2], fg = theme[3]); M.y2.config(bg = theme[2], fg = theme[3]); M.y3.config(bg = theme[2], fg = theme[3])
        root.config(bg = theme[0])
    '''

    '''
    root.title('Ayoo! Rooms')

    class Main (Frame) :

        def __init__ (self,master):
            super().__init__(master)

            root.config(bg = theme[0])

            self.title = Frame(master, bg = theme[0])
            self.title.pack(fill = 'x')
            self.x1 = Label(self.title, image = theme[4], bg = theme[0], font = ('Montserrat', 30, 'bold')); self.x1.pack(fill = 'x')
            self.x2 = Label(self.title, text = choice(title_greet), bg = theme[0], fg = theme[3], font = ('times', 15, 'italic')); self.x2.pack(fill = 'x')
            self.x3 = Label(self.title, bg = theme[0]); self.x3.pack(fill = 'x')

            self.butts = Frame(master, bg = theme[0])
            self.butts.pack(fill = 'both', expand = True)
            self.y1 = Button(self.butts, text = 'Existing User? | Sign in', font = ('consolas', 10, 'normal'), command = self.silog, bg = theme[2], fg = theme[3]); self.y1.pack(fill = 'both', expand = True)
            self.y2 = Button(self.butts, text = 'New User? | Create New User', font = ('consolas', 10, 'normal'), command = self.sulog, bg = theme[2], fg = theme[3]); self.y2.pack(fill = 'both', expand = True)
            self.y3 = Button(self.butts, text = 'Admin Login', font = ('consolas', 10, 'normal'), command = self.admlog, bg = theme[2], fg = theme[3]); self.y3.pack(side = 'right')

            toolbar = Menu(master)
            master.config(menu = toolbar)

            self.view = Menu(toolbar, tearoff = False)
            self.themes = Menu(self.view, tearoff = True)
            self.themes.add_command(label = 'Default', command = lambda : themeset(0))
            self.themes.add_command(label = 'Soft Gold', command = lambda : themeset(1))
            self.themes.add_command(label = 'Titanic', command = lambda : themeset(2))
            self.themes.add_command(label = 'Charcoal', command = lambda : themeset(3))
            self.themes.add_command(label = 'Tree Vibes', command = lambda : themeset(4))
            self.themes.add_command(label = 'Lighter Light Mode', command = lambda : themeset(5))
            self.themes.add_command(label = 'Cupid', command = lambda : themeset(6))
            self.themes.add_command(label = 'Cyber Punk', command = lambda : themeset(7))
            self.themes.add_command(label = 'Batman', command = lambda : themeset(8))
            self.themes.add_command(label = 'End City', command = lambda : themeset(9))
            self.view.add_cascade(label = 'Theme', menu = self.themes)
            self.view.add_command(label = 'Collaborators', command = self.collab)
            toolbar.add_cascade(label = 'View', menu = self.view)

            self.helpp = Menu(toolbar, tearoff = False)
            self.helpp.add_command(label = 'About', command = self.about)
            self.helpp.add_command(label = 'Documentation', command = lambda : startfile(r'docs\doc.pdf'))
            self.helpp.add_command(label = 'Source Code', command = self.strtfiles)
            toolbar.add_cascade(label = 'Help', menu = self.helpp)

            self.view.config(bg = theme[0], fg = theme[1], activebackground = theme[2], activeforeground = theme[3])
            self.helpp.config(bg = theme[0], fg = theme[1], activebackground = theme[2], activeforeground = theme[3])
            self.themes.config(bg = theme[0], fg = theme[1], activebackground = theme[2], activeforeground = theme[3])
            

        def strtfiles (self) :

            startfile(r'docs\ayoosql.pdf')
            startfile(r'docs\ayoo.pdf')

        def collab (self) :

            root.withdraw()
            collaber = Toplevel(root)
            collaber.resizable(False, False)
            collaber.iconbitmap(r'imges\icon.ico')
            collaber.config(bg = theme[0])
            collaber.wm_protocol('WM_DELETE_WINDOW', func = lambda : reopen(collaber))
            collaber.title('We are Ayoo!')
            Collaber(collaber)

        def about (self) :

            root.withdraw()
            abouts = Toplevel(root)
            abouts.resizable(False, False)
            abouts.iconbitmap(r'imges\icon.ico')
            abouts.config(bg = theme[0])
            abouts.wm_protocol('WM_DELETE_WINDOW', func = lambda : reopen(abouts))
            abouts.title('Ayoo! | About Us')
            Abouts(abouts)
            
        def silog (self):

            root.withdraw()
            silogwin = Toplevel(root)
            silogwin.resizable(False, False)
            silogwin.iconbitmap(r'imges\icon.ico')
            silogwin.config(bg = theme[0])
            silogwin.wm_protocol('WM_DELETE_WINDOW', func = lambda : reopen(silogwin))
            silogwin.title('Ayoo! | User Login Page')
            silogwin.geometry('650x460')
            SignInLog(silogwin)
            
        def sulog (self):

            root.withdraw()
            sulogwin = Toplevel(root)
            sulogwin.resizable(False, False)
            sulogwin.iconbitmap(r'imges\icon.ico')
            sulogwin.config(bg = theme[0])
            sulogwin.wm_protocol('WM_DELETE_WINDOW', func = lambda : reopen(sulogwin))
            sulogwin.title('Ayoo! | New User Create Page')
            SignUpLog(sulogwin)
            
            
        def admlog (self):

            root.withdraw()
            admlogwin = Toplevel(root)
            admlogwin.resizable(False, False)
            admlogwin.iconbitmap(r'imges\icon.ico')
            admlogwin.config(bg = theme[0])
            admlogwin.wm_protocol('WM_DELETE_WINDOW', func = lambda : reopen(admlogwin))
            admlogwin.title('Ayoo! | Admin Login Page')
            AdminLog(admlogwin)
            
    class Collaber (Frame) :

        def __init__(self, master) :

            super().__init__(master)
            self.ctext = ScrolledText(master, width=80, height=20, wrap='word', font=('consolas', 12))
            self.ctext.pack(expand = True, fill = 'both')
            self.ctext.config(bg = theme[0], fg = theme[1])
            string = """Introducing Ayoo! – Your Ultimate Hotel Booking Companion.

    Our Mission :-
    Our mission is to leverage our skills in programming to develop solutions that make life easier and more enjoyable for everyone. We believe in the power of technology to solve real-world problems and enhance everyday experiences.


    Meet the Team :-

    Aman Sudhakar - Founder & Frontend / Backend Developer 
    Alipta Paul - Database Schema Engineer
    Amman Afzal Ahmed Khan - Query Engineer
    G Prasanna - Backend Developer and Bug Tester


    Our Values :-

    Innovation: We strive to bring new ideas to life.
    Collaboration: We believe that teamwork and diverse perspectives lead to the best solutions.
    Quality: We are committed to delivering high-quality products that meet our users' needs.

    Contact Us :-
    We'd love to hear from you! Whether you have questions, suggestions, or just want to say hello, feel free to reach out to us on github"""
            self.ctext.insert(END, string)
            self.ctext.config(state = 'disabled')

    class Abouts (Frame) :

        def __init__ (self, master) :

            super().__init__ (master)
            self.atext = ScrolledText(master, width=80, height=20, wrap='word', font=('consolas', 12))
            self.atext.pack(expand = True, fill = 'both')
            self.atext.config(bg = theme[0], fg = theme[1])
            string = """Introducing Ayoo! – Your Ultimate Hotel Booking Companion

    Experience the future of hotel bookings with the Ayoo! Hotel Room Booking App. Seamlessly blending efficiency, security, and user-friendliness, Ayoo! transforms the way you book and manage your stays. Engineered with a robust Python backend and an intuitive Tkinter interface, this app is not just powerful, it's also a joy to use.

    Why Choose Ayoo?
    Effortless Booking: Glide through the booking process with our streamlined interface.

    Cutting-Edge Technology: Built using Python and Tkinter, Ayoo! guarantees a smooth and reliable experience.

    Simple Check-In/Check-Out: Say goodbye to front desk lines. Check-in and out directly from your device.

    Dynamic Admin Panel: Our flexible admin panel empowers hotel managers to effortlessly oversee operations.

    Revolutionizing Hotel Stays

    Ayoo! is set to redefine hotel interactions by offering unparalleled convenience, top-notch security, and unbeatable affordability. Whether you're a globetrotter or a business traveler, Ayoo! ensures your booking experience is as delightful as your stay."""
            self.atext.insert(END, string)
            self.atext.config(state = 'disabled')

    class Login (Frame) :


        def __init__ (self, master, image_, fields, butt_title = 'Login'):

            super().__init__ (master)

            '''
                login window constructor
                change the button title (self.butt.config(text = '<Title>')
            '''
            
            self.title = Frame(master,bg=theme[0])
            self.title.pack()
            Label(self.title,image = image_, font = ('consolas', 30, 'bold'), bg=theme[0]).pack()

            self.entfrm = Frame(master, bg=theme[0])
            self.entfrm.pack()
            self.entries = self.makeentry(self.entfrm, fields) 
            self.entries[-1].bind('<Return>',self.run)

            self.buttfrm = Frame(master, bg=theme[0])
            self.buttfrm.pack()
            self.butt = Button(self.buttfrm, text = butt_title, command = self.run, fg=theme[1], bg=theme[2], font=('Arial', 14, 'bold' ))
            self.butt.pack(anchor = 'center')

        def makeentry (self, parent, fields) :

            '''
                auto creates entry fields just pass in
                required fields and parent window/frame
            '''
            
            frm_l = Frame(parent, bg = theme[0])
            frm_l.pack(side = 'left')
            
            frm_e = Frame(parent, bg = theme[0])
            frm_e.pack(side = 'left')

            entries = list()

            for field in fields :

                Label(frm_l, text = field, font = ('consolas', 11, 'normal'), bg = theme[0], fg = theme[3]).pack()
                entry = Entry(frm_e,font = ('consolas', 11, 'normal'), bg = theme[0], fg = theme[3])
                entry.pack()
                entries.append(entry)

            return entries
        
        def run (self, event = None):

            '''
                skeleton code, auto prints entries
            '''
            
            for entry in self.entries :
                    
                    print(entry.get())
                    entry.delete(0,END)

    ##

    class AdminLog (Login) :

        def __init__ (self, master):

            Login.__init__(self, master, adminimg, ['Admin ID', 'Passkey'])

        def run (self, even = None) :

            adminid = self.entries[0].get()
            passkey = self.entries[1].get()
            do = ayoocon()
            try :
                
                query = 'select passkey from admin where admin_id = {}'.format(int(adminid))
                cursor = do.cursor()
                cursor.execute(query)
                result = cursor.fetchone()

                if result :
                    
                    if result[0] == passkey :

                        self.adminid = adminid
                        self.master.destroy()
                        self.admn()

                    else:
                        showwarning('Ayoo!','Incorrect passkey')
                        for entry in self.entries :             
                            entry.delete(0,END)     

                else :

                    showerror('Ayoo!', f"Admin ID wrong or admin doesn't exist with id = {adminid}")
                    for entry in self.entries :             
                            entry.delete(0,END)

            except Exception :
                
                showerror('Ayoo !', 'Invalid Details Supplied, Try again')
                for entry in self.entries :             
                        entry.delete(0,END)

            
                        
            finally : do.close()

        def admn(self):
            admn=Toplevel(root, bg = theme[0])
            admn.resizable(False, False)
            admn.iconbitmap(r'imges\icon.ico')
            admn.wm_protocol('WM_DELETE_WINDOW', lambda : reopen(admn))
            AdmnWind(admn,self.adminid)

    class AdmnWind(Frame):

        def __init__ (self, master, aid) :
            super().__init__(master)

            self.aid = aid
            self.title = Frame(master, bg = theme[0])
            self.title.pack(expand = True, fill = 'both')
            Label(self.title, text = f'Welcome {self.aid}', font = ('consolas',16,'normal'), bg = theme[0], fg = theme[1]).pack()

            self.topbuttons = Frame(self.title, bg = theme[0])
            self.topbuttons.pack(side = 'top', expand = True, fill = 'both')

            self.botbuttons = Frame(self.title, bg = theme[0])
            self.botbuttons.pack(side = 'top', expand = True, fill = 'both')

            self.addrooms = Button(self.topbuttons, image = adrm ,command=self.AddRoom, bg = theme[2])
            self.addrooms.pack(side = 'left', expand = True, fill = 'both')

            self.roomstat = Button(self.topbuttons, image = rmstat,command=self.Rmstat, bg = theme[2])
            self.roomstat.pack(side = 'left', expand = True, fill = 'both')

            self.delroom = Button(self.botbuttons, image = delrm ,command=self.DelRoom, bg = theme[2])
            self.delroom.pack(side = 'left', expand = True, fill = 'both')

            self.rooms = Button(self.botbuttons, image = rm,command=self.Room, bg = theme[2])
            self.rooms.pack(side = 'left', expand = True, fill = 'both')

            

        def AddRoom(self):

            self.master.withdraw()
            adrmwin = Toplevel(root, bg = theme[0])
            adrmwin.resizable(False, False)
            adrmwin.iconbitmap(r'imges\icon.ico')
            adrmwin.wm_protocol('WM_DELETE_WINDOW', func = lambda : reopen(adrmwin, self.master))
            Addroom(adrmwin, self)

        def Rmstat(self):

            self.master.withdraw()
            rmstwin = Toplevel(root, bg = theme[0])
            rmstwin.resizable(False, False)
            rmstwin.iconbitmap(r'imges\icon.ico')
            rmstwin.wm_protocol('WM_DELETE_WINDOW', func = lambda : reopen(rmstwin, self.master))
            RoomStat(rmstwin, self)

        def Room(self):

            self.master.withdraw()
            rmwin = Toplevel(root, bg = theme[0])
            rmwin.resizable(False, False)
            rmwin.iconbitmap(r'imges\icon.ico')
            rmwin.wm_protocol('WM_DELETE_WINDOW', func = lambda : reopen(rmwin, self.master))

            self.framestar = Frame(rmwin)
            self.framestar.pack()
            self.label = ScrolledText(self.framestar,wrap=WORD,font=('Consolas',15),width=100, bg = theme[0], fg = theme[1])
            self.label.pack()

            do=ayoocon()
            query='select * from room'
            cursor=do.cursor()
            cursor.execute(query)
            result=cursor.fetchall()


            listed = ['Room No             Roomtype            City                Price               Availability\n']
            for record in result  :

                format_ = f'{record[0]:<20}{record[1]:<20}{record[2]:<20}{record[3]:<20}{record[4]:<20}\n'
                listed.append(format_)
                
            
            self.label.insert(END,''.join(listed))
            self.label.config(state = 'disabled')
            

        def DelRoom(self):

            self.master.withdraw()
            drmwin = Toplevel(root, bg = theme[0])
            drmwin.resizable(False, False)
            drmwin.iconbitmap(r'imges\icon.ico')
            drmwin.wm_protocol('WM_DELETE_WINDOW', func = lambda : reopen(drmwin, self.master))
            DelRoom(drmwin, self)
        
            
        
    class Addroom(Login):

        def __init__(self, master, hyper) :
            Login.__init__(self,master, addrm , ['Room Number', 'Room Type', 'City', 'Price'], butt_title = 'Add Room')

        def run (self, event = None) :

            rno=self.entries[0].get()
            rtype=self.entries[1].get().title()
            city=self.entries[2].get()
            price=self.entries[3].get()
            do=ayoocon()
            query=f'insert into room values({rno},"{rtype}","{city}",{price},"TRUE")'
            cursor=do.cursor()
            try :
                
                cursor.execute(query)
                do.commit()
                showinfo('Ayoo!','Room Added')
                
            except  :
                
                showerror('Ayoo !', '>> Incorrect Syntax, Please enter details again. \t\tSyntax :=> Room Number(int), Room Type(string), City(string), Price(int)')
                
            finally : do.close()

            for entry in self.entries :             
                        entry.delete(0,END)

                
    class DelRoom(Login):

    
        def __init__(self, master, hyper) :
            Login.__init__(self,master, delerm , ['Room Number'], butt_title = 'Delete Room')

        def run(self,event=None):
            rno=self.entries[0].get()
            if askyesno('Ayoo !',f'Do you want to Delete room {rno}') :
                do=ayoocon()
                try:
                    cursor=do.cursor()
                    query = f'select room_no from room where room_no = {rno} and Availability = "TRUE"'
                    cursor.execute(query)
                    r = cursor.fetchall()
                    if not r : raise AyooException
                    query=f'delete from room where room_no={rno}'
                    cursor.execute(query)
                    do.commit()
                    do.close()
                    showinfo('Ayoo!','Room Deleted Succesfully')
                except Exception :
                    showinfo('Ayoo!','Room does not exist or Room is currently in use')

                for entry in self.entries :             
                            entry.delete(0,END)

        


    class RoomStat(Login):

        def __init__(self, master, hyper) :
            Login.__init__(self,master, rmst , ['Room Number'], butt_title = 'Find Room')
            self.framestar = Frame(master, bg = theme[0])
            self.framestar.pack()
            self.text = ScrolledText(self.framestar, wrap = WORD, font = ("consolas",15,'italic'),width=50,height=1, bg = theme[0], fg = theme[1])
            self.text.pack(padx = 20, pady = 20)

        def run(self,event=None):
            rno=self.entries[0].get()
            do=ayoocon()
            query=f'select Room_no,Roomtype,Availability from room where Room_No={rno}'
            cursor=do.cursor()
            try : 
                cursor.execute(query)
                result=cursor.fetchall()
                if not result : raise AyooException
                count=cursor.rowcount


                if count==0:

                    self.text.config(state = 'normal')
                    self.text.delete('1.0',END)
                    self.text.insert(END, 'Room Not Found')
                    self.text.config(state = 'disabled')

                else :
                    
                    listed = ['Room No        Roomtype       Availability\n']
                    for record in result  :

                        format_ = f'{record[0]:<15}{record[1]:<15}{record[2]:<15}\n'
                        listed.append(format_)
                    self.text.config(state = 'normal')
                    self.text.delete('1.0',END)
                    self.text.insert(END, ''.join(listed))
                    self.text.config(state = 'disabled')

            except Exception :
                self.text.config(state = 'normal')
                self.text.delete('1.0',END)
                self.text.insert(END, 'Room Not Found')
                self.text.config(state = 'disabled')

        
    class SignInLog (Login) :

        def __init__ (self, master):

            Login.__init__(self, master, signinimg, ['User Name', 'Password'])

        def run (self, event = None) :

            self.userid=self.entries[0].get().lower().strip()
            pswd=self.entries[1].get()

            do=ayoocon()
            query=f'select password from user_data where username="{self.userid}" '
            cursor=do.cursor()
            cursor.execute(query)
            
            try:
                result=cursor.fetchone()
                if not result : raise AyooException


                if result[0] == pswd :
                    
                    self.master.destroy()
                    self.allo()

                else:
                    
                    showerror('Ayoo!','Incorrect Password')
                    for entry in self.entries :             
                        entry.delete(0,END)

            except AyooException as err:
                
                showerror('Ayoo!','User does not exist')
                for entry in self.entries :             
                        entry.delete(0,END)

        def allo (self)  :

            allo = Toplevel(root, bg = theme[0])
            allo.resizable(False, False)
            allo.iconbitmap(r'imges\icon.ico')
            allo.wm_protocol('WM_DELETE_WINDOW', func = lambda : reopen(allo))
            toggles = toggle('GET', self.userid)
            Wind(allo, self.userid, toggles)
            

    class SignUpLog (Login) :

        def __init__ (self, master):

            Login.__init__(self, master, signupimg, ['User Name', 'Name', 'Phone Number', 'Aadhar Number', 'Password', 'Confirm Password'], butt_title = 'Sign Up')

        def run (self, event = None) : 

            userid = self.entries[0].get().lower().strip()
            name = self.entries[1].get()
            phno = self.entries[2].get()
            adhno = self.entries[3].get()
            ipswd = self.entries[4].get()
            cpswd = self.entries[5].get()

            if ipswd == cpswd :

                do = ayoocon()
                query = f"insert into user_data values ('{userid}', '{ipswd}', '{name}', {phno}, {adhno}, 'ADDD');"
                try :
                    
                    do.cursor().execute(query)
                    do.commit()
                    showinfo('Ayoo!', 'New User Created Succesfully, Sign in again')
                    for entry in self.entries :             
                            entry.delete(0,END)
                    reopen(self.master)

                except Exception as err:

                    showerror('Ayoo !', 'Invalid Details Supplied, Try again')
                    for entry in self.entries :             
                            entry.delete(0,END)

                finally : do.close()
                
                
            else :

                showerror('Ayoo!', 'Your Password does not match! 😠')
                for entry in self.entries :             
                        entry.delete(0,END)

    ##
    class Wind (Frame) :

        def __init__ (self, master, uid, toggles) :
            super().__init__(master)

            do = ayoocon()
            self.uid = uid
            query = f'select Name from User_data where username = "{self.uid}"'
            cur = do.cursor()
            cur.execute(query)
            res = cur.fetchall()[0][0]
            self.title = Frame(master, bg = theme[0])
            self.title.pack(expand = True, fill = 'both')
            Label(self.title, text = f'Welcome {res}', font = ('Impact',15,'normal'), bg = theme[0], fg = theme[1]).pack()

            self.topbuttons = Frame(self.title, bg = theme[0])
            self.topbuttons.pack(side = 'top', expand = True, fill = 'both')

            self.botbuttons = Frame(self.title, bg = theme[0])
            self.botbuttons.pack(side = 'top', expand = True, fill = 'both')
            
            self.bookrm = Button(self.topbuttons, image = bkrm, command = self.bookroom, bg = theme[2], fg = theme[1])
            self.bookrm.pack(side = 'left', expand = True, fill = 'both')

            self.roomdet = Button(self.topbuttons, image = rmdet, command = self.roomdetails, bg = theme[2], fg = theme[1])
            self.roomdet.pack(side = 'left', expand = True, fill = 'both')

            self.checkin = Button(self.botbuttons, image = chin, command = self.checkinwin, bg = theme[2], fg = theme[1])
            self.checkin.pack(side = 'left', expand = True, fill = 'both')

            self.checkout = Button(self.botbuttons, image = chot, command = self.checkoutwin, bg = theme[2], fg = theme[1])
            self.checkout.pack(side = 'left', expand = True, fill = 'both')

            x = [self.bookrm, self.roomdet, self.checkin, self.checkout]
            y = 0
            
            for z in x :
                if toggles[y] == 'A' : w = 'active'
                else : w = 'disabled'
                y += 1
                z.config(state = w)

        def bookroom(self) :

            self.master.withdraw()
            bkrmwin = Toplevel(root, bg = theme[0])
            bkrmwin.resizable(False, False)
            bkrmwin.iconbitmap(r'imges\icon.ico')
            bkrmwin.wm_protocol('WM_DELETE_WINDOW', func = lambda : reopen(bkrmwin, self.master))
            BookRoom(bkrmwin, self)

        def roomdetails(self) :

            self.master.withdraw()
            rmdetwin = Toplevel(root, bg = theme[0])
            rmdetwin.resizable(False, False)
            rmdetwin.iconbitmap(r'imges\icon.ico')
            rmdetwin.wm_protocol('WM_DELETE_WINDOW', func = lambda : reopen(rmdetwin, self.master))      
            self.frmm = Frame(rmdetwin, bg = theme[0])
            self.frmm.pack()
            Frame(rmdetwin, height=2, bd=1, relief="sunken", bg = theme[0]).pack(fill="x", pady=10) 
            do = ayoocon()
            cur = do.cursor()
            query = f'select Room_No from bookings where Username = "{self.uid}"'
            cur.execute(query)
            rmno = cur.fetchall()
            rmno = rmno[0][0]
            query = f'select * from room where Room_No = {rmno}'
            cur.execute(query)
            rmno, rmtt, cit, price, avail = cur.fetchone()
            do.close()
            Label(self.frmm, image = detlabel, font = ('impact',25), bg = theme[0], fg = theme[1]).pack(anchor = 'center')
            self.frmm1 = Frame(rmdetwin, relief = 'sunken', bg = theme[0])
            self.frmm1.pack(side = 'left')
            Label(self.frmm1, text = f'Room Number {rmno:>8}', font = ('consolas', 15), bg = theme[0], fg = theme[3]).pack()
            Label(self.frmm1, text = f'Room Type {rmtt:>16}', font = ('consolas', 15), bg = theme[0], fg = theme[3]).pack()
            Label(self.frmm1, text = f'City {cit:>19}', font = ('consolas', 15), bg = theme[0], fg = theme[3]).pack()
            Label(self.frmm1, text = f'Price {price:>20}', font = ('consolas', 15), bg = theme[0], fg = theme[3]).pack()

            
        def checkinwin(self) :

                decision = askyesno('Ayoo !', 'Are you sure you want to Check in to your room?')
                
                if decision :

                    self.checkin.config(state = 'disabled')
                    self.checkout.config(state = 'active')

                    tggl = toggle('GET', self.uid)
                    tggl[2] = 'D'; tggl[3] = 'A'
                    tggls = ''
                    for tgl in tggl :
                        tggls = tggls + tgl
                    toggle('SET', self.uid, tggls)
                    
                    showinfo('Ayoo!', 'You have succesfully checked in')
                
        def checkoutwin(self) :

            decision = askyesno('Ayoo !', 'Are you sure you want to Check out?')
            
            if decision :

                self.checkout.config(state = 'disabled')
                self.bookrm.config(state = 'active')
                self.roomdet.config(state = 'disabled')

                tggl = toggle('GET', self.uid)
                tggl[0] = 'A'; tggl[1] = 'D'; tggl[3] = 'D'
                tggls = ''
                for tgl in tggl :
                    tggls = tggls + tgl
                toggle('SET', self.uid, tggls)

                do = ayoocon()
                cur = do.cursor()
                query = f'select Room_No from bookings where Username = "{self.uid}"'
                cur.execute(query)
                rmno = cur.fetchall()[0][0]
                query = f'update room set Availability = "TRUE" where Room_No = {rmno}'
                cur.execute(query)
                do.commit()
                query = f'delete from bookings where Room_No = {rmno}'
                cur.execute(query)
                do.commit()
                do.close()
                
                    
                showinfo('Ayoo!', 'You have succesfully checked out')

                

    class BookRoom(Frame) :

        def __init__(self, master, hyper) :
            super().__init__(master)

            do = ayoocon()
            self.hyper = hyper
            self.frm = Frame(master, bg = theme[0])
            self.frm.pack(fill = 'x')
            self.listfrm = Frame(master, bg = theme[0])
            self.listfrm.pack(fill = 'both')
            
            self.rmtvar = StringVar(self)
            query = f'select distinct(Roomtype) from room'
            cur = do.cursor()
            cur.execute(query)
            rmties = cur.fetchall()
            self.rmtype = OptionMenu(self.frm, self.rmtvar, *rmties)
            self.rmtype.config(bg = theme[0], fg = theme[1], activebackground = theme[2], activeforeground = theme[3], highlightbackground = theme[0])
            self.rmtype["menu"].config(bg = theme[0], fg = theme[3], activebackground = theme[2], activeforeground = theme[3])
            self.rmtvar.set('Select Room Type')
            self.rmtype.pack()
            
            query = f'select distinct(City) from room'
            cur = do.cursor()
            cur.execute(query)
            cities = cur.fetchall()
            self.citvar = StringVar(self)
            self.cit = OptionMenu(self.frm, self.citvar, *cities)
            self.cit.config( bg = theme[0], fg =theme[1], activebackground = theme[2], activeforeground = theme[3], highlightbackground = theme[0])
            self.cit["menu"].config(bg = theme[0], fg = theme[3], activebackground = theme[2], activeforeground = theme[3])
            self.citvar.set('Select City')
            self.cit.pack()

            query = f'select Min(Price), Max(Price) from room'
            cur = do.cursor()
            cur.execute(query)
            pricei, pricea = cur.fetchone()
            do.close()
            self.price = Scale(self.frm, from_ = pricei, to = pricea, resolution = 1000, orient = 'horizontal', length = 250, sliderlength = 50,troughcolor = 'lightgrey', label = '       Price Range', bg = theme[0], fg = theme[1], activebackground = theme[2])
            self.price.set(4000)
            self.price.pack()

            self.bar = Scrollbar(self.listfrm, bg = theme[1])
            self.bar.pack(side = 'right', fill = 'y')
            self.avails = Listbox(self.listfrm, font = ("Consolas", 12), yscrollcommand = self.bar.set, bg = theme[0], fg = theme[1])
            self.avails.pack(side = 'left', fill = 'both', expand = True)
            self.bar.config(command = self.avails.yview)

            Frame(master, height=2, bd=1, relief="sunken", bg = theme[0]).pack(fill="x", pady=10)
            Button(self.frm, text = 'Search', command = self.find, bg = theme[2], fg = theme[3]).pack()
            Frame(self.frm, height=2, bd=1, relief="sunken", bg = theme[0]).pack(fill="x", pady=10)        #separator
            Button(master, text = 'Book Room', command = self.book,bg = theme[2], fg = theme[3]).pack()

        def find (self) :

            self.avails.delete(0, END)
            rmt = self.rmtvar.get()[1:len(self.rmtvar.get())-2]
            cit = self.citvar.get()[1:len(self.citvar.get())-2]
            query = f'select * from room where Roomtype = {rmt} and City = {cit} and Price Between 0 and {self.price.get()} and Availability = "TRUE"'
            do = ayoocon()
            cur = do.cursor()
            try :
                
                cur.execute(query)
                self.result = cur.fetchall()
                if not(self.result) : showinfo('Ayoo !','Room not found for selected Options')
                else :
                    
                    for room in self.result:
                        text = f'{room[0]:<7}{room[2]:<10}{room[3]:<10}'
                        self.avails.insert(END, text)

            except Exception : 

                showerror('Ayoo !', 'Choose a Room Type and City')
                
            finally : do.close()
        
        def book(self) :

            if self.avails.curselection() :
                
                consent = askyesno('Ayoo!', 'Are you sure you want to book this room?')

                if consent :

                    self.hyper.bookrm.config(state = 'disabled')
                    self.hyper.roomdet.config(state = 'active')
                    self.hyper.checkin.config(state = 'active')

                    tggl = toggle('GET', self.hyper.uid)
                    tggl[0] = 'D'; tggl[1] = 'A'; tggl[2] = 'A'
                    tggls = ''
                    for tgl in tggl :
                        tggls = tggls + tgl
                    toggle('SET', self.hyper.uid, tggls)

                    rmno = int(self.avails.get(self.avails.curselection())[:7].strip())
                    query = f'insert into bookings (Username, Room_No) values ("{self.hyper.uid}", {rmno})'
                    do = ayoocon()
                    do.cursor().execute(query)
                    do.commit()
                    query = f'update room set Availability = "FALSE" where Room_No = {rmno}'
                    do.cursor().execute(query)
                    do.commit()
                    do.close()
                    
                    showinfo('Ayoo!', "Room succesfully booked")
                    reopen(self.master, self.hyper.master)

            else : showwarning('Ayoo !', 'Please Select a Room')

    M = Main(root)
    autogreet()
    root.mainloop()

except Exception as err : 
        
        showerror(f"Something Unexpected Occured\nError : {err}")