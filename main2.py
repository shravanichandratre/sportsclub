#popup- delete
from kivy.app import App
import time
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty,BooleanProperty,ObjectProperty,ListProperty,OptionProperty,NumericProperty
import sqlite3 as sql
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
Window.clearcolor = (1,1,1,1)
from kivy.uix.scatterlayout import ScatterLayout
# from kivy.base import EventLoop
# EventLoop.window.clear_color = (51, 110, 123, 1)

class EditScreen(GridLayout, Screen):
    idE = ObjectProperty(None)
    nameE=ObjectProperty(None)
    passE = ObjectProperty(None)
    addE=ObjectProperty(None)
    adhaarE = ObjectProperty(None)
    phoneE=ObjectProperty(None)
    emailE = ObjectProperty(None)
    
    # def __init__(self, **kwargs):
    #     super(EditScreen,self).__init__(**kwargs)

    def con(self):
        con=sql.connect("userdata.db")
        cur=con.cursor()
        return cur
    
    def checkIfInvalid(self):
        l=[]
        cur=self.con()
        cur.execute("select id from player")
        a=cur.fetchall()
        
        for i in range (0,len(a)):
            l.append(str(a[i][0]))
        print(l)
        
        if self.idE.text.isalpha() or self.idE.text not in l or self.idE.text=="":
            self.checks()
        else:
            self.nE.text=self.getn()
            self.cE.text=self.getc()
            self.eE.text=self.gete()
            self.gE.text=self.getg()
            self.phnE.text=self.getphn()
            self.lE.text=self.getl()
            self.sE.text=self.gets()

    def getn(self):
        cur=self.con()
        cur.execute("SELECT name from player where id=?",[str(self.idE.text)])
        a=cur.fetchall()
        return str(a[0][0])

    def getc(self):
        cur=self.con()
        cur.execute("SELECT city from player where id=?",[str(self.idE.text)])
        a=cur.fetchall()
        return str(a[0][0])

    def getphn(self):
        cur=self.con()
        cur.execute("SELECT ph from player where id=?",[str(self.idE.text)])
        a=cur.fetchall()
        return str(a[0][0])
 
    def getl(self):
        cur=self.con()
        cur.execute("SELECT level from player where id=?",[str(self.idE.text)])
        a=cur.fetchall()
        return str(a[0][0])

    def gete(self):
        cur=self.con()
        cur.execute("SELECT email from player where id=?",[str(self.idE.text)])
        a=cur.fetchall()
        return str(a[0][0])

    def getg(self):         
        con=sql.connect("userdata.db")
        cur=con.cursor()
        cur.execute("SELECT gender from player where id=?",[str(self.idE.text)])
        a=cur.fetchall()
        return str(a[0][0])

    def gets(self):         
        con=sql.connect("userdata.db")
        cur=con.cursor()
        cur.execute("SELECT sport from player where id=?",[str(self.idE.text)])
        a=cur.fetchall()
        return str(a[0][0])
    
    def checks(self):
        c1=Button(text="Close", size_hint_y=None, size=("40dp","40dp"))
        popupE2=Popup(title="Enter valid User ID", content=c1,size_hint=(None,None),size=("270dp","270dp"), auto_dismiss=False,title_align="center",title_size="23sp")
        c1.bind(on_press=popupE2.dismiss)
        popupE2.open()
        
    def updateRecord(self):
        c=Button(text="Close", size_hint_y=None, size=("40dp","40dp"))
        popupE=Popup(title="Saved Successfully", content=c,size_hint=(None,None),size=("270dp","270dp"), auto_dismiss=False,title_align="center",title_size="23sp")
        c.bind(on_press=popupE.dismiss)

        con=sql.connect("userdata.db")
        cur=con.cursor()
        
        # cur.execute("select * from user")
        # a1=cur.fetchall()

        l=[]
        
        cur.execute("select id from player")
        a=cur.fetchall()
        
        for i in range (0,len(a)):
            l.append(str(a[i][0]))
        print(l)

        if self.idE.text.isalpha() or str(self.idE.text) not in l or self.nE.text=="" or self.phnE.text=='' or self.gE.text=='' or self.cE.text=='' or self.lE.text=='' or self.sE.text=='' or self.eE.text=='' or self.idE.text=='':
            print("e1")
            self.checks()
        else:
            try:
                print("t")
                cur.execute("UPDATE player SET name=?, ph=?, gender=?, city=?, level=?, sport=?, email=?  where id=?",[str(self.nE.text),str(self.phnE.text),str(self.gE.text),str(self.cE.text),str(self.lE.text),str(self.sE.text),str(self.eE.text),str(self.idE.text)])
                a=cur.fetchall()
                print(a)
                # if(a==a1):
                #     self.checks()
                # else:
                con.commit()
                con.close()
                popupE.open()
            except:
                print("e")
                self.checks()

class SearchScreen(BoxLayout,Screen):
    searchInput = ObjectProperty(None)
    n = ObjectProperty(None)
    phn = ObjectProperty(None)
    g = ObjectProperty(None)
    c = ObjectProperty(None)
    l = ObjectProperty(None)
    s = ObjectProperty(None)
    e= ObjectProperty(None)
    
    def checkIfValid(self):
        l=[]
        con=sql.connect("userdata.db")
        cur=con.cursor()
        cur.execute("select id from player")
        a=cur.fetchall()
        
        for i in range (0,len(a)):
            l.append(str(a[i][0]))
        print(l)
        if self.searchInput.text.isalpha() or self.searchInput.text not in l or self.searchInput.text=="":
            c1=Button(text="Close", size_hint_y=None, size=("40dp","40dp"))
            popupE2=Popup(title="Enter valid ID", content=c1,size_hint=(None,None),size=("270dp","270dp"), auto_dismiss=False,title_align="center",title_size="23sp")
            c1.bind(on_press=popupE2.dismiss)
            popupE2.open()
        else:
            self.n.text= self.gn()
            self.e.text= self.ge()
            self.l.text= self.gl()
            self.phn.text= self.gphn()
            self.s.text= self.gs()
            self.g.text= self.gg()
            self.c.text= self.gc()

    def gn(self):
        con=sql.connect("userdata.db")
        cur=con.cursor()
        cur.execute("SELECT name from player where id=?",[str(self.searchInput.text)])
        a=cur.fetchall()
        return str(a[0][0])

    def ge(self):
        con=sql.connect("userdata.db")
        cur=con.cursor()
        cur.execute("SELECT email from player where id=?",[str(self.searchInput.text)])
        a=cur.fetchall()
        return str(a[0][0])

    def gphn(self):
        con=sql.connect("userdata.db")
        cur=con.cursor()
        cur.execute("SELECT ph from player where id=?",[str(self.searchInput.text)])
        a=cur.fetchall()
        return str(a[0][0])

    def gs(self):
        con=sql.connect("userdata.db")
        cur=con.cursor()
        cur.execute("SELECT sport from player where id=?",[str(self.searchInput.text)])
        a=cur.fetchall()
        return str(a[0][0])

    def gg(self):
        con=sql.connect("userdata.db")
        cur=con.cursor()
        cur.execute("SELECT gender from player where id=?",[str(self.searchInput.text)])
        a=cur.fetchall()
        return str(a[0][0])

    def gc(self):
        con=sql.connect("userdata.db")
        cur=con.cursor()
        cur.execute("SELECT city from player where id=?",[str(self.searchInput.text)])
        a=cur.fetchall()
        return str(a[0][0])

    def gl(self):
        con=sql.connect("userdata.db")
        cur=con.cursor()
        cur.execute("SELECT level from player where id=?",[str(self.searchInput.text)])
        a=cur.fetchall()
        return str(a[0][0])

        
class SignupScreen(ScatterLayout, Screen):
    nameInput = ObjectProperty(None)
    phInput = ObjectProperty(None)
    emailInput = ObjectProperty(None)
    sportInput = ObjectProperty(None)
    levelInput = ObjectProperty(None)
    cityInput = ObjectProperty(None)
    coachInput = ObjectProperty(None)
    genderInput = ObjectProperty(None)
 
    def level_spinner_clicked(self, value):
        self.ids.levelInput.text = value
 
    def gender_spinner_clicked(self, value):
        self.ids.genderInput.text = value
 
    def sport_spinner_clicked(self, value):
        self.ids.sportInput.text = value
 
    def popupWindow(self,str):
        c1=Button(text="Close", size_hint_y=None, size=("40dp","40dp"))
        popupl=Popup(title=str, content=c1,size_hint=(None,None),size=("270dp","270dp"), auto_dismiss=False,title_align="center",title_size="23sp")
        c1.bind(on_press=popupl.dismiss)
        popupl.open()
   
 
    def textValidationName(self):
        if ((self.nameInput.text.isnumeric()) or self.nameInput.text=='') :         #or ((not self.cityInput.text.isalpha()) or self.cityInput.text=='')
            self.popupWindow("Username must contain all alphabets")
            return 1
        else:
            return 0
 
    def textValidationPhNo(self):
        if (not self.phInput.text.isnumeric()) or self.phInput.text=='' or len(self.phInput.text)!=10 :
            self.popupWindow("Phone no. must contain 10 numbers")
            return 1
        else:
            return 0
 
    def textValidationEmail(self):
        f=0
        for i in self.emailInput.text:
            if (i=='@') and (".com" in self.emailInput.text or ".co.in" in self.emailInput.text) :
                f=1
        if f==0:
            self.popupWindow("Invalid Email ID\n(Eg. abc@gmail.com)")
            return 1
        else:
            return 0
   
 
    def submit(self):
        nameInput= self.nameInput.text
        phInput= self.phInput.text
        emailInput= self.emailInput.text
        genderInput= self.genderInput.text
        levelInput= self.levelInput.text
        sportInput= self.sportInput.text
        cityInput= self.cityInput.text
        #coachInput= self.coachInput.text
       
        print("username=",self.nameInput.text)
        print("Ph=",self.phInput.text)
        #print("Id=",self.idInput.text)
        print("sport=",self.sportInput.text)
        print("level=",self.levelInput.text)
        print("EmailID=",self.emailInput.text)
        print("gender=",self.genderInput.text)
        #print("coach=",self.coachInput.text)
 
       
        con=sql.connect('userdata.db')
        cur=con.cursor()
       
        #cur.execute("CREATE TABLE player( id integer primary key autoincrement, name text, ph text, gender text, city text,  level text, sport text, email text)")
       
        if self.textValidationName()==1 or self.textValidationEmail()==1 or self.textValidationPhNo()==1:
             #popup
            self.popupWindow("Problem occured while Submitting")
        else:
            sqlite_insert_with_param = """INSERT INTO player
                          ( name, ph, gender, city, level, sport, email)
                          VALUES (?, ?, ?, ?, ?, ?, ?);"""
 
            data_tuple = (nameInput, phInput, genderInput, cityInput, levelInput, sportInput, emailInput)
            cur.execute(sqlite_insert_with_param, data_tuple)
            # cur.execute("INSERT INTO id VALUES('Swati','Saaraja')")
            cur.execute("SELECT *from player")
            print(cur.fetchall())
            con.commit()
            con.close()
            self.popupWindow("Submitted Successfully")
 
 
class AdminLScreen(ScatterLayout, Screen):
    pInput = ObjectProperty(None)
    def popupWindow(self,str):
        c1=Button(text="Close", size_hint_y=None, size=("40dp","40dp"))
        popupl=Popup(title=str, content=c1,size_hint=(None,None),size=("270dp","270dp"), auto_dismiss=False,title_align="center",title_size="23sp")
        c1.bind(on_press=popupl.dismiss)
        popupl.open()
   
    def submitAdmin(self):
        if (self.pInput.text !="12345"):
            self.popupWindow("Wrong Password")
            return False
 
class DisplayScreen(BoxLayout, Screen):
   
    #def dis(self):
        # con=sql.connect('userdata.db')
        # cur=con.cursor()
        # cur.execute("SELECT * from player")
        # a=cur.fetchall()
        # print(a)
        # con.commit()
        # con.close()
    data_items=ListProperty([]) #"name","ph","gender","city","level","sport","email"
    def __init__(self, **kwargs):
        super(DisplayScreen,self).__init__(**kwargs)
       
        self.rows=[]
        self.data_dict={}
       
    def on_enter(self):
        self.data_items.clear()
        con=sql.connect("userdata.db")
        cur=con.cursor()
        cur.execute("SELECT * from player")
        rows=cur.fetchall()
        print(rows)
        for row in rows:
            for col in row:
                self.data_items.append(col)
       
        # for row in rows:
        #     print(self.data_items)
        print(self.data_items)
 
        con.commit()
        con.close()
 
class DeleteScreen(BoxLayout, Screen):
   
    delInput = ObjectProperty(None)
    # def del1(self):
    #     return True
    def cd(self):
        c2=Button(text="Confirm", size_hint_y=None, size=("40dp","40dp"))
        popupDel3=Popup(title="Confirm Deletion", content=c2,size_hint=(None,None),size=("270dp","270dp"), auto_dismiss=False,title_align="center",title_size="23sp")
        c2.bind(on_press= popupDel3.dismiss)
        popupDel3.open()
        return 1
        #time.sleep(3)
   
    def delItem(self):
        c1=Button(text="Close", size_hint_y=None, size=("40dp","40dp"))
        c=Button(text="Close", size_hint_y=None, size=("40dp","40dp"))
        popupDel=Popup(title="Successfully deleted", content=c,size_hint=(None,None),size=("270dp","270dp"), auto_dismiss=False,title_align="center",title_size="23sp")
        c.bind(on_press=popupDel.dismiss)
        popupDel2=Popup(title="Invalid User ID", content=c1,size_hint=(None,None),size=("270dp","270dp"), auto_dismiss=False,title_align="center",title_size="23sp")
        c1.bind(on_press=popupDel2.dismiss)
        
        #c.bind(on_press=popupDel3.dismiss)
 
        con=sql.connect("userdata.db")
        cur=con.cursor()
        cur.execute("select * from player")
        a1=cur.fetchall()
        if self.cd()==1:
            try:

                cur.execute("DELETE from player WHERE id=?",[str(self.delInput.text)])
                cur.execute("select * from player")
                a=cur.fetchall()
                con.commit()
                con.close()
            except:
                popupDel2.open()
       
       
        # print("a",a)
        # print("**********************************")
        # print("a1",a1)
   
        if a1!=a:
            popupDel.open()
        else:
            popupDel2.open()
 
class MainScreen(ScatterLayout, Screen):
    pass
 
class AdminScreen(GridLayout, Screen):
    pass
 
class WindowManager(ScreenManager):
    pass
 
class sportsClubApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen())
        sm.add_widget(SignupScreen())
        sm.add_widget(AdminScreen())
        sm.add_widget(AdminLScreen())
        sm.add_widget(DisplayScreen())
        sm.add_widget(DeleteScreen())
        sm.add_widget(SearchScreen())
        sm.add_widget(EditScreen())
        return sm
 
if __name__ == '__main__':
    sportsClubApp().run()
