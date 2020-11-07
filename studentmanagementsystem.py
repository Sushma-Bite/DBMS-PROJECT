    
def addstudent():
	def submitadd():
		id=idval.get()
		name=nameval.get()
		mobile=mobileval.get()
		email=emailval.get()
		address=addressval.get()
		gender=genderval.get()
		dob=dobval.get()
		addedtime=time.strftime("%H:%M:%S")
		addeddate=time.strftime("%d/%m/%Y")
		print(addeddate,addedtime)	
		try:
			strr='insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
			mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
			con.commit()
			res = messagebox.askyesnocancel('Notifications','Id {} Name {} Added successfully.... and want to clean the form'.format(id,name),parent=addroot)
			if(res==True):
				idval.set('') 
				nameval.set('') 
				mobileval.set('') 
				emailval.set('') 
				addressval.set('') 
				genderval.set('') 
				dobval.set('') 
		except:
			messagebox.showerror('Notifocations','Id already exist try another Id',parent=addroot)
		strr='select * from studentdata1'
		mycursor.execute(strr)
		datas=mycursor.fetchall()
		studenttable.delete(*studenttable.get_children())
		for i in datas:
			vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
			studenttable.insert('',END,values=vv)
			
		
			
	addroot = Toplevel(master=DataEntryFrame)
	addroot.grab_set()
	addroot.geometry('470x470+220+200')
	addroot.title('Student Management System')
	addroot.config(bg='blue')
    #addroot.iconbitmap('logo.ico')
	addroot.resizable(False,False)
    #------------------------------- add student label
	idlabel = Label(addroot,text='Enter Id :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
	idlabel.place(x=10,y=10)

	namelabel = Label(addroot,text='Enter Name :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
	namelabel.place(x=10,y=70)

	mobilelabel = Label(addroot,text='Enter Mobile :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
	mobilelabel.place(x=10,y=130)

	emaillabel = Label(addroot,text='Enter Email :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
	emaillabel.place(x=10,y=190)

	addresslabel = Label(addroot,text='Enter Address :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
	addresslabel.place(x=10,y=250)

	genderlabel = Label(addroot,text='Enter Gender :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
	genderlabel.place(x=10,y=310)

	doblabel = Label(addroot,text='Enter D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
	doblabel.place(x=10,y=370)
    ##----------------------------------------------------add student entry
	idval =StringVar()
	nameval=StringVar()
	mobileval=StringVar()
	emailval=StringVar()
	addressval=StringVar()
	genderval=StringVar()
	dobval=StringVar()
    
	identry =Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval,width=17)
	identry.place(x=200,y=10)
    
	nameentry =Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval,width=17)
	nameentry.place(x=200,y=70)
    
	mobileentry =Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval,width=17)
	mobileentry.place(x=200,y=130)
    
	emailentry =Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval,width=17)
	emailentry.place(x=200,y=190)
    
	addressentry =Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval,width=17)
	addressentry.place(x=200,y=250)
    
	genderentry =Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval,width=17)
	genderentry.place(x=200,y=310)
    
	dobentry =Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval,width=17)
	dobentry.place(x=200,y=370)
     ######---------------------------------------------------------------- add button
	submitbtn =Button(addroot,text='submit',font=('roman',15,'bold'),width=15,bd=5,activebackground='blue',activeforeground='white',bg='red',command=submitadd)
	submitbtn.place(x=120,y=420)
	addroot.mainloop()
	print('student added')

def searchstudent():
	def search():
		id=idval.get()
		name=nameval.get()
		mobile=mobileval.get()
		email=emailval.get()
		address=addressval.get()
		gender=genderval.get()
		dob=dobval.get()
		date=dateval.get()
		addedtime=time.strftime("%H:%M:%S")
		addeddate=time.strftime("%d/%m/%Y")
		if(id!=''):
			strr = 'select * from studentdata1 where id=%s'
			mycursor.execute(strr,(id))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)
		elif(name!=''):
			strr = 'select * from studentdata1 where name=%s'
			mycursor.execute(strr,(name))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)
		elif(mobile!=''):
			strr = 'select * from studentdata1 where mobile=%s'
			mycursor.execute(strr,(mobile))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)
		elif(email!=''):
			strr = 'select * from studentdata1 where email=%s'
			mycursor.execute(strr,(email))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)
		elif(address!=''):
			strr = 'select * from studentdata1 where address=%s'
			mycursor.execute(strr,(address))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)
		elif(gender!=''):
			strr = 'select * from studentdata1 where gender=%s'
			mycursor.execute(strr,(gender))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)
		elif(dob!=''):
			strr = 'select * from studentdata1 where dob=%s'
			mycursor.execute(strr,(dob))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)
		elif(date!=''):
			strr = 'select * from studentdata1 where date=%s'
			mycursor.execute(strr,(date))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)
		
		
			
			
	searchroot = Toplevel(master=DataEntryFrame)
	searchroot.grab_set()
	searchroot.geometry('470x540+220+160')
	searchroot.title('Student Management System')
	searchroot.config(bg='firebrick1')
    #searchroot.iconbitmap('logo.ico')
	searchroot.resizable(False,False)
    #------------------------------- add student label
	idlabel = Label(searchroot,text='Enter Id :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	idlabel.place(x=10,y=10)

	namelabel = Label(searchroot,text='Enter Name :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	namelabel.place(x=10,y=70)

	mobilelabel = Label(searchroot,text='Enter Mobile :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	mobilelabel.place(x=10,y=130)

	emaillabel = Label(searchroot,text='Enter Email :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	emaillabel.place(x=10,y=190)

	addresslabel = Label(searchroot,text='Enter Address :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	addresslabel.place(x=10,y=250)

	genderlabel = Label(searchroot,text='Enter Gender :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	genderlabel.place(x=10,y=310)

	doblabel = Label(searchroot,text='Enter D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	doblabel.place(x=10,y=370)
	
	datelabel = Label(searchroot,text='Enter Date:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	datelabel.place(x=10,y=430)

	
    ##----------------------------------------------------add student entry
	idval =StringVar()
	nameval=StringVar()
	mobileval=StringVar()
	emailval=StringVar()
	addressval=StringVar()
	genderval=StringVar()
	dobval=StringVar()
	dateval=StringVar()
    
	identry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval,width=17)
	identry.place(x=202,y=10)
    
	nameentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval,width=17)
	nameentry.place(x=202,y=70)
    
	mobileentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval,width=17)
	mobileentry.place(x=202,y=130)
    
	emailentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval,width=17)
	emailentry.place(x=202,y=190)
    
	addressentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval,width=17)
	addressentry.place(x=202,y=250)
    
	genderentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval,width=17)
	genderentry.place(x=202,y=310)
    
	dobentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval,width=17)
	dobentry.place(x=202,y=370)
	
	dateentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval,width=17)
	dateentry.place(x=202,y=430)

	
    
     ######---------------------------------------------------------------- add button
	submitbtn =Button(searchroot,text='submit',font=('roman',15,'bold'),width=15,bd=5,activebackground='blue',activeforeground='white',bg='red',command=search)
	submitbtn.place(x=130,y=490)
	searchroot.mainloop()


def deletestudent():
        cc = studenttable.focus()
        content = studenttable.item(cc)
        #print(content)
        pp=content['values'][0]
        strr='delete from studentdata1 where id=%s'
        mycursor.execute(strr,(pp))
        con.commit()
        messagebox.showinfo('Notification','ID {} deleted successfully...'.format(pp))
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
def updatestudent():
	def update():
		id=idval.get()
		name=nameval.get()
		mobile=mobileval.get()
		email=emailval.get()
		address=addressval.get()
		gender=genderval.get()
		dob=dobval.get()
		date=dateval.get()
		time=timeval.get()
		strr='update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
		mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
		con.commit()
		messagebox.showinfo('Notifications','Id {} modified successfully...'.format(id),parent=updateroot)
		strr = 'select * from studentdata1'
		mycursor.execute(strr)
		datas = mycursor.fetchall()
		studenttable.delete(*studenttable.get_children())
		for i in datas:
			vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
			studenttable.insert('',END,values=vv)
                
	updateroot = Toplevel(master=DataEntryFrame)
	updateroot.grab_set()
	updateroot.geometry('470x585+220+160')
	updateroot.title('Student Management System')
	updateroot.config(bg='firebrick1')
	#updateroot.iconbitmap('logo.ico')
	updateroot.resizable(False,False)
        #------------------------------- add student label
	idlabel = Label(updateroot,text='Enter Id :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	idlabel.place(x=10,y=10)

	namelabel = Label(updateroot,text='Enter Name :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	namelabel.place(x=10,y=70)

	mobilelabel = Label(updateroot,text='Enter Mobile :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	mobilelabel.place(x=10,y=130)

	emaillabel = Label(updateroot,text='Enter Email :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	emaillabel.place(x=10,y=190)

	addresslabel = Label(updateroot,text='Enter Address :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	addresslabel.place(x=10,y=250)

	genderlabel = Label(updateroot,text='Enter Gender :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	genderlabel.place(x=10,y=310)

	doblabel = Label(updateroot,text='Enter D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	doblabel.place(x=10,y=370)

	datelabel = Label(updateroot,text='Enter Date:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	datelabel.place(x=10,y=430)

	timelabel = Label(updateroot,text='Enter Time:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
	timelabel.place(x=10,y=490)
        ##----------------------------------------------------add student entry
	idval =StringVar()
	nameval=StringVar()
	mobileval=StringVar()
	emailval=StringVar()
	addressval=StringVar()
	genderval=StringVar()
	dobval=StringVar()
	dateval=StringVar()
	timeval=StringVar()
    
    
	identry =Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval,width=17)
	identry.place(x=220,y=10)
    
	nameentry =Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval,width=17)
	nameentry.place(x=220,y=70)
    
	mobileentry =Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval,width=17)
	mobileentry.place(x=220,y=130)
    
	emailentry =Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval,width=17)
	emailentry.place(x=220,y=190)
    
	addressentry =Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval,width=17)
	addressentry.place(x=220,y=250)
    
	genderentry =Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval,width=17)
	genderentry.place(x=220,y=310)
    
	dobentry =Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval,width=17)
	dobentry.place(x=220,y=370)

	dateentry =Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval,width=17)
	dateentry.place(x=220,y=430)

	timeentry =Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=timeval,width=17)
	timeentry.place(x=220,y=490)
    
     ######---------------------------------------------------------------- add button
	submitbtn =Button(updateroot,text='submit',font=('roman',15,'bold'),width=16,bd=5,activebackground='blue',activeforeground='white',bg='red',command=update)
	submitbtn.place(x=120,y=540)
	
	cc = studenttable.focus()
	content = studenttable.item(cc)
	pp=content['values']
	if(len(pp)!=0):
		idval.set(pp[0]) 
		nameval.set(pp[1]) 
		mobileval.set(pp[2]) 
		emailval.set(pp[3]) 
		addressval.set(pp[4]) 
		genderval.set(pp[5]) 
		dobval.set(pp[6])
		dateval.set(pp[7])
		timeval.set(pp[8])
	updateroot.mainloop()

def search():
	print('search')
	searchroot = Toplevel(master=DataEntryFrame)
	searchroot.grab_set()
	searchroot.geometry('470x585+220+160')
	searchroot.title('Student Management System')
	searchroot.config(bg='firebrick1')
   # searchroot.iconbitmap('logo.ico')
	searchroot.resizable(False,False)
    #------------------------------- add student label
	idlabel = Label(searchroot,text='Enter Id :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	idlabel.place(x=10,y=10)

	namelabel = Label(searchroot,text='Enter Name :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	namelabel.place(x=10,y=70)

	mobilelabel = Label(searchroot,text='Enter Mobile :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	mobilelabel.place(x=10,y=130)

	emaillabel = Label(searchroot,text='Enter Email :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	emaillabel.place(x=10,y=190)

	addresslabel = Label(searchroot,text='Enter Address :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	addresslabel.place(x=10,y=250)

	genderlabel = Label(searchroot,text='Enter Gender :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	genderlabel.place(x=10,y=310)

	doblabel = Label(searchroot,text='Enter D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	doblabel.place(x=10,y=370)

	datelabel = Label(searchroot,text='Enter D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	datelabel.place(x=10,y=430)

	timelabel = Label(searchroot,text='Enter Time:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	timelabel.place(x=10,y=490)
    ##----------------------------------------------------add student entry
	idval =StringVar()
	nameval=StringVar()
	mobileval=StringVar()
	emailval=StringVar()
	addressval=StringVar()
	genderval=StringVar()
	dobval=StringVar()
	dateval=StringVar()
	timeval=StringVar()
    
    
	identry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
	identry.place(x=250,y=10)
    
	nameentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
	nameentry.place(x=250,y=70)
    
	mobileentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
	mobileentry.place(x=250,y=130)
    
	emailentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
	emailentry.place(x=250,y=190)
    
	addressentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
	addressentry.place(x=250,y=250)
    
	genderentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
	genderentry.place(x=250,y=310)
    
	dobentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
	dobentry.place(x=250,y=370)

	dateentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
	dateentry.place(x=250,y=430)

	timeentry =Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
	timeentry.place(x=250,y=490)
    
     ######---------------------------------------------------------------- add button
	submitbtn =Button(searchroot,text='submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=search)
	submitbtn.place(x=150,y=540)
	searchroot.mainloop()

def showstudent():
	strr = 'select * from studentdata1'
	mycursor.execute(strr)
	datas = mycursor.fetchall()
	studenttable.delete(*studenttable.get_children())
	for i in datas:
		vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
		studenttable.insert('',END,values=vv)
def exportstudent():
	ff = filedialog.asksaveasfilename()
	gg = studenttable.get_children()
	id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
	for i in gg:
		content=studenttable.item(i)
		pp = content['values']
	id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
	dd=['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time']
	df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
	paths=r'{}.csv'.format(ff)
	df.to_csv(paths,index=False)
def exitstudent():
	res=messagebox.askyesnocancel('Notification',' Do you want to exit?')
	if(res == True):
		root.destroy()
    
    
###############################################################################connection of database
def Connectdb():
	def submitdb():
		global con,mycursor
		host = hostval.get()
		user = userval.get()
		password = passwordval.get()
		print(host)
		print(user)
		print(password)
		try:
			con = pymysql.connect(host=host,user=user,password=password)
			mycursor = con.cursor()
		except:
			messagebox.showerror('Notifications','Data is Incorrect please try again')
			return
		try:
			strr = 'create database studentmanagementsystem1'
			mycursor.execute(strr)
			mycursor.execute('use studentmanagementsystem1')
			mycursor.execute('create table studentdata1(id int(4),name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50));')
			strr = 'alter table studentdata1 modify column id int not null'
			mycursor.execute(strr)
			strr = 'alter table studentdata1 modify column id int primary key'
			mycursor.execute(strr)
			messagebox.showinfo('Notification','database created and now you are  connected to the database.....',parent=dbroot)
		except:
			messagebox.showinfo('Notification',"Database that you want to create is already exist!")
			strr = 'use studentmanagementsystem1'
			mycursor.execute(strr)
			messagebox.showinfo('Notification','Now you are connected to the database.....',parent=dbroot)
			dbroot.destroy()
            

                
                
                
            
            
	dbroot=Toplevel()
	dbroot.grab_set()
	dbroot.geometry('470x250+800+230')
	#dbroot.iconbitmap('logo.ico')
	dbroot.resizable(False,False)
	dbroot.config(bg='blue')
    #############.......................connect db labels
	hostlabel = Label(dbroot,text="Enter Host:",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=15)
	hostlabel.place(x=10,y=10)

	namelabel = Label(dbroot,text="Enter Name:",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=15)
	namelabel.place(x=10,y=70)
	passwordlabel = Label(dbroot,text="Enter Password:",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=15)
	passwordlabel.place(x=10,y=130)

    ###################################Connect_DB_Entry###################
	hostval = StringVar()
	userval = StringVar()
	passwordval = StringVar()
    
	hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=3,textvariable=hostval,width=17)
	hostentry.place(x=212,y=10)

	userentry = Entry(dbroot,font=('roman',15,'bold'),bd=3,textvariable=userval,width=17)
	userentry.place(x=212,y=70)

	passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=3,textvariable=passwordval,width=17)
	passwordentry.place(x=212,y=130)

    ###############################Connect_DB_Button...............
	submitbutton =Button(dbroot,text='Submit',font=('roman',15,'bold'),width=15,activebackground='blue',activeforeground='white',bd=5,bg='red',command=submitdb)
	submitbutton.place(x=125,y=190)
	dbroot.mainloop()
  
    
def tick():
	time_string=time.strftime("%H:%M:%S")
	date_string=time.strftime("%d:%m:%Y")
	Clock.config(text='Date:'+date_string+"\n"+"Time:"+time_string)
	Clock.after(200,tick)
########################################################################################
import random
colors=['red','green','blue','red2','gold2']
def IntroLabelColorTick():
	fg = random.choice(colors)
	#SliderLabel.config(fg=fg)
	#SliderLabel.after(2,IntroLabelTick)
def IntroLabelTick():
	global count,text
	if (count>=len(ss)):
		count=0
		text=''
		SliderLabel.config(text=text)
	else:
		text=text+ss[count]
		SliderLabel.config(text=text)
		count+=1
		SliderLabel.after(200,IntroLabelTick)
        
#########################################################################################

from tkinter import *
import time
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import pandas

root = Tk()
root.title("Student Management System")
root.config(bg ='gold2')
root.geometry('1174x700+200+600')

#root.iconbitmap('logo.ico')
root.resizable(False,False)
#########################.....................................Data entry frame........

DataEntryFrame=Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

frontlabel = Label(DataEntryFrame,text='-----------Welcome------------',width=30,font=('arial',22,'bold'),bg='gold2')
frontlabel.pack(side=TOP,expand=True)
addbtn = Button(DataEntryFrame,text='1. Add Student',width=25,font=('times',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('times',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('times',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Student',width=25,font=('times',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('times',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Export data',width=25,font=('times',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7. Exit',width=25,font=('times',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)


#########################.....................................Show entry frame........

ShowDataFrame=Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)

########################..................................Show data frame........

style=ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),background='cyan',foreground='black')

scroll_x=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable=Treeview(ShowDataFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show']='headings'
studenttable.pack(fill=BOTH,expand=1)
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)
studenttable['show'] = 'headings'
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)
studenttable.pack(fill=BOTH,expand=1)

#############################################################################################
ss='Welcome To Student Management System'
count = 0
text = ''
SliderLabel=Label(root,text=ss,font=('times',20,'italic bold'),width=40,bg='cyan',relief=RIDGE,borderwidth=5)
SliderLabel.place(x=230,y=0)
#IntroLabelTick()
IntroLabelColorTick()
###########################################################################################

Clock=Label(root,text=ss,font=('times',14,'bold'),bg='lawn green',relief=RIDGE,borderwidth=4)
Clock.place(x=00,y=00)

tick()

######################################################....connectToDatabaseButton


connectButton=Button(root,text='Connect To Database',width=20,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='green2',activebackground='blue',activeforeground='white',command=Connectdb)
connectButton.place(x=920,y=4)







root.mainloop()
