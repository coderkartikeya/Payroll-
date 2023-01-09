from tkinter import *
import mysql.connector
from tkinter import filedialog 
from tkinter.filedialog import askopenfile

mainwindow=Tk()

mainwindow.geometry('1540x790+0+0')
mainwindow.title('PAROLL SYSTEM')
p2=PhotoImage(file='pogo.png')
mainwindow.iconphoto(False,p2)
#mainwindow.geometry("{0}x{1}+0+0".format(mainwindow.winfo_screenwidth(), mainwindow.winfo_screenheight()))

#_____________________________actual window ___________________________________

#_________________________________background in the main window_______________________________________
bac_=PhotoImage(file='bg2.png')
bac_a=bac_.subsample(3,3)

bac_image=Label(mainwindow,image=bac_a,bd=5)
bac_image.pack()

logi_n=PhotoImage(file='login.png')

im_login=Label(bac_image,image=logi_n,bd=10)
im_login.place(x=100,y=120)
#_________________________________frames_______________________________________________________
fm_m1=Frame(bac_image,bd=10,bg='black',relief='raise',padx=500)
fm_m1.place(x=-10,y=-1)


#__________________________________labels____________________________________________________
lm_m1=Label(fm_m1,bg='black',fg='white',text='LOGIN OF PAYROLL SYSTEM',font='comisans 25 bold',relief="raise")
lm_m1.pack()




#________________________________fuctions of mainwindow __________________________________________
def login():
	wn=Toplevel()
	wn.geometry('1540x793+0+0')
	wn.title('PAYROLL MANAGEMENT')
	wn.configure(bg='black')
	p1=PhotoImage(file='ff.png')
	wn.iconphoto(False,p1)



	#________________________________________________leave canvas_______________________________________________________
	def leave1():
		top=Toplevel()
		top.geometry('1400x900+0+0')
		top.title('LEAVE DETAILS')
		phot1=PhotoImage(file='m.png')
		photo2=phot1.subsample(1,1)
		
		image=Label(top,image=photo2,bd=100)
		image.pack()

		############ frames ##############################################################################

		fl_1=Frame(image,bd=5,bg='black',relief='raise')
		fl_1.place(x=-200,y=-100)

		fl_2=Frame(image,bd=3,bg='orange',relief=SUNKEN)
		fl_2.place(x=-100,y=-40)

		fl_3=Frame(image,bd=5,bg='pink',relief='raise')
		fl_3.place(x=-90,y=150)


		fl_4=Frame(image,bd=10,bg='pink',relief='raise')
		fl_4.place(x=-90,y=200)

		fl_5=Frame(image,bd=5,bg='orange',relief='raise')
		fl_5.place(x=600,y=-40)


			

			

			


		
		##################### labels #####################################################################
		ll_1=Label(fl_1,bg='black',fg='white',text='LEAVE RECORDS',font='comisans 25 bold',relief="raise",padx=668)
		ll_1.pack()

		ll_2=Label(fl_2,bg='black',fg='white',text='USER ID ',font='comisans 20 bold',relief="raise",bd=5)
		ll_2.grid(column=0,row=0)

		ll_3=Label(fl_3,bg='pink',fg='black',text='MONTH ',font='comisans 20 bold',relief="raise",bd=5,padx=100)
		ll_3.grid(column=0,row=0)

		ll_4=Label(fl_4,bg='pink',fg='black',text='CASUAL',font='comisans 20 bold')
		ll_4.grid(column=0,row=0)
		
		ll_5=Label(fl_4,bg='pink',fg='black',text='SICK LEAVE',font='comisans 20 bold')
		ll_5.grid(column=0,row=2)
		
		ll_6=Label(fl_4,bg='pink',fg='black',text='EARNED LEAVES ',font='comisans 20 bold')
		ll_6.grid(column=0,row=4)
		
		ll_7=Label(fl_4,bg='pink',fg='black',text='LEAVE WITHOUT PAY ',font='comisans 20 bold')
		ll_7.grid(column=0,row=6)

		
		ll_8=Label(image,bg='black',fg='white',text='MODIFY  AND ADD RECORDS ',font='comisans 20 bold',relief="raise",bd=5)
		ll_8.place(x=-90,y=50)

		ll_9=Label(fl_5,bg='black',fg='white',text='NAME ',font='comisans 20 bold',relief="raise",bd=5)
		ll_9.grid(column=0,row=0)


		############## variables ############################################################
		ew=StringVar()
		s=StringVar()
		ea=StringVar()
		wp=StringVar()
		nr1=StringVar()
		mm=StringVar()
		q=StringVar()





		######################### entry ####################################################################
		el_1=Entry(fl_2,bg='white',fg='black',font='comicsans 20 bold ',relief='raise',bd=5,textvariable=nr1)
		el_1.grid(column=1,row=0)

		el_2=Entry(fl_3,bg='white',fg='black',font='comicsans 20 bold ',relief='raise',bd=5,textvariable=mm)
		el_2.grid(column=1,row=0)

		el_3=Entry(fl_4,bg='white',fg='black',font='comicsans 20 bold ',relief=SUNKEN,bd=5,textvariable=ew)
		el_3.grid(column=1,row=0)

		el_4=Entry(fl_4,bg='white',fg='black',font='comicsans 20 bold ',relief=SUNKEN,bd=5,textvariable=s)
		el_4.grid(column=1,row=2)

		el_5=Entry(fl_4,bg='white',fg='black',font='comicsans 20 bold ',relief=SUNKEN,bd=5,textvariable=ea)
		el_5.grid(column=1,row=4)

		el_6=Entry(fl_4,bg='white',fg='black',font='comicsans 20 bold ',relief=SUNKEN,bd=5,textvariable=wp)
		el_6.grid(column=1,row=6)

		el_7=Entry(fl_5,bg='white',fg='black',font='comicsans 20 bold ',relief=SUNKEN,bd=5,textvariable=q)
		el_7.grid(column=1,row=0)


		############################## database connection ##################################################
		def al():
			import mysql.connector 
			mydb=mysql.connector.connect(
				host='localhost',
				user='root',
				password='sunilvats',
				database='payroll'
				)
			mycursor=mydb.cursor()

			#mycursor.execute("CREATE TABLE  recordleave (NO INTEGER AUTO_INCREMENT PRIMARY KEY ,user_id INTEGER(255),name VARCHAR(250),email VARCHAR(250),CAUSAL INTEGER(150),SICKLEAVE INTEGER(150),EARNEDLEAVES INTEGER(150),WITHOUTPAY INTEGER(150),MONTH VARCHAR(230))")
			#mycursor.execute('INSERT INTO recordleave(CAUSAL,SICKLEAVE,EARNEDLEAVES,WITHOUTPAY) VALUES (%s,%s,%s,%s)',(ew.get(),s.get(),ea.get(),wp.get()))
			#lea=mycursor.execute("SELECT  * FROM recordleave where user_id='" + nr1.get() + "'")
			lea="SELECT  * FROM recordleave where user_id='%s' and MONTH='%s'"%(nr1.get(),mm.get())
			mycursor.execute(lea)
			row1=mycursor.fetchone()

			y=str(row1[4])
			h=str(row1[5])
			r=str(row1[6])
			s=str(row1[7])
			il=str(row1[8])
			nl=str(row1[2])

			#el_2.insert(nr1.get(),il)
			el_3.insert(nr1.get(),y)
			el_4.insert(nr1.get(),h)
			el_5.insert(nr1.get(),r)
			el_6.insert(nr1.get(),s)
			el_7.insert(nr1.get(),nl)



			mydb.commit()
		def c():
			el_1.delete(0,END)
			el_3.delete(0,END)
			el_4.delete(0,END)
			el_5.delete(0,END)
			el_6.delete(0,END)
			el_2.delete(0,END)
			el_7.delete(0,END)

		def up():
			mydb=mysql.connector.connect(
				host='localhost',
				user='root',
				password='sunilvats',        #"select'" + nr +"'"+" from employee where '" + k +"'"
				database='payroll'
				)
			mycursor=mydb.cursor()

			

			up="UPDATE   recordleave SET CAUSAL='%s',SICKLEAVE='%s',EARNEDLEAVES='%s',WITHOUTPAY='%s',MONTH='%s'"%(ew.get(),s.get(),ea.get(),wp.get(),mm.get())
			mycursor.execute(up)

			mydb.commit()

		def o():
			mydb=mysql.connector.connect(
				host='localhost',
				user='root',
				password='sunilvats',        #"select'" + nr +"'"+" from employee where '" + k +"'"
				database='payroll'
				)
			mycursor=mydb.cursor()

			mycursor.execute('INSERT INTO recordleave(CAUSAL,SICKLEAVE,EARNEDLEAVES,WITHOUTPAY,MONTH,user_id,name) VALUES (%s,%s,%s,%s,%s,%s,%s)',(ew.get(),s.get(),ea.get(),wp.get(),mm.get(),nr1.get(),q.get()))
			mydb.commit()

		def b():
			top.destroy()







			



			


		####################### buttons #################################################################
		bl_1=Button(fl_2,bg='black',fg='white',text='SEARCH',font='comicsans 15 bold',relief='raise',bd=5,command=al)
		bl_1.grid(column=2,row=0)

		bl_2=Button(image,bg='black',fg='white',text='MODIFY',font='comicsans 25 bold',relief='raise',bd=5,command=up)
		bl_2.place(x=200,y=500)

		bl_3=Button(image,bg='black',fg='white',text='SAVE',font='comicsans 25 bold',relief='raise',bd=5,command=o)
		bl_3.place(x=0,y=500)

		bl_4=Button(image,bg='black',fg='white',text='CLEAR',font='comicsans 25 bold',relief='raise',bd=5,command=c)
		bl_4.place(x=400,y=500)

		bl_5=Button(image,bg='black',fg='white',text='CANCEL',font='comicsans 25 bold',relief='raise',bd=5,command=b)
		bl_5.place(x=600,y=500)


		top.mainloop()

	################################## end of leave ##################################################
		

	#######################################################reports######################################################

	def report():
		rr=Toplevel()
		rr.geometry('1200x700')
		fr_1=Frame(rr,bd=10)
		fr_1.pack()
		tr_1=Text(fr_1,bd=20,font='comicsans 15 bold')
		tr_1.pack()

		import mysql.connector
			
		mydb=mysql.connector.connect(
				host='localhost',
				user='root',
				password='sunilvats',
				database='payroll'
				)
		mycursor=mydb.cursor()
		resu=mycursor.execute("select'" + b +"'"+" from employee where '" + k +"'" )
		tb=mycursor.fetchall()
		for i in tb:
			print(i)


		#for tb in tll:
			#print(tb)


		rr.mainloop()
	#########################################################end report###############################################	





	############################# new employee start   ################################################################################################



	def lal():
		tt=Toplevel()
		
		tt.geometry('1400x700+0+0')
		tt.title('NEW EMPLOYEE')
		
		#____________________________________functions______________________________
		name1=StringVar()
		number=IntVar()
		designation=StringVar()
		gender=StringVar()
		address=StringVar()
		qualification=StringVar()
		fatherhusband=StringVar()
		dob=StringVar()
		doj=StringVar()
		experience=StringVar()
		employtp=StringVar()
		email=StringVar()
		basic=DoubleVar()
		gradepay=DoubleVar()
		tranport=DoubleVar()



		def quit():
			tt.destroy()
		def save():
			#global number,email,designation,gender,address,dob,doj,experience,fatherhusband,qualification,employtp
			n=name1.get()
			nm=number.get()
			em=email.get()
			de=designation.get()
			g=gender.get()
			a=address.get()
			db=dob.get()
			dj=doj.get()
			ex=experience.get()
			f=fatherhusband.get()
			q=qualification.get()
			ep=employtp.get()
			
			ba_=int(basic.get())
			gd_=int(gradepay.get())
			tpt_=int(tranport.get())
			da_=int((gd_+ba_)*(0.28))
			hra_=int((gd_+ba_)*(0.3))
			da_tpt=int(tpt_*(0.28))
			total=int(da_+hra_+da_tpt+tpt_)



			print(n)
			print(nm)
			print(em)
			print(de)
			print(g)
			print(a)
			print(db)
			print(dj)
			print(ex)
			print(f)
			print(q)
			print(ep)
			

			import mysql.connector

			mydb=mysql.connector.connect(
				host='localhost',
				user='root',
				password='sunilvats',
				database='payroll'
				)
			mycursor=mydb.cursor()

			mycursor.execute(' CREATE TABLE employee (user_id INTEGER AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(200),EMAIL VARCHAR(200),AGE INTEGER(20),SALARY INTEGER(200),MOBILE INT(20),DESIGNATION VARCHAR(255),GENDER VARCHAR(255),ADDRESS VARCHAR(225),QUALIFICATION VARCHAR(200),FATHERS  VARCHAR(200),HUSBAND VARCHAR(200),DOB VARCHAR(200),DOJ VARCHAR(200),EXPERIENCE VARCHAR(200),EMPLOYEETYPE VARCHAR(200) )')

			mycursor.execute('INSERT INTO employee (NAME ,EMAIL,MOBILE,DESIGNATION,GENDER ,ADDRESS ,QUALIFICATION ,FATHERS,DOB ,DOJ,EXPERIENCE ,EMPLOYEETYPE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(name1.get(),email.get(),number.get(),designation.get(),gender.get(),address.get(),qualification.get(),fatherhusband.get(),dob.get(),doj.get(),experience.get(),employtp.get())) #GENDER ,ADDRESS ,QUALIFICATION ,FATHERS,DOB ,DOJ,EXPERIENCE ,EMPLOYEETYPE) VALUES (%s,%s,%s,%s)',(name1.get(),number.get(),email.get(),email.get(),designation.get(),gender.get(),address.get(),dob.get(),doj.get(),experience.get(),fatherhusband.get(),qualification.get(),employtp.get()))
			

			#mycursor.execute('INSERT INTO employee (GENDER ,ADDRESS ,QUALIFICATION ,FATHERS) VALUES (%s,%s,%s,%s)',(gender.get(),address.get(),qualification.get(),fatherhusband.get()))
			

			#mycursor.execute('INSERT INTO employee(DOB ,DOJ,EXPERIENCE ,EMPLOYEETYPE) VALUES (%s,%s,%s,%s)',(dob.get(),doj.get(),experience.get(),employtp.get()))

			#b=mycursor.execute("SELECT  * FROM employee WHERE NAME='" + name1.get() + "'")
			#jp=mycursor.fetchone()

			'''while jp is not None:
				print(jp)
				jp=mycursor.fetchone()'''
			#rl=str(jp[0])
			

			
			#mycursor.execute('INSERT INTO recordleave (NAME,EMAIL,user_id) VALUES (%s,%s,%s)',(name1.get(),email.get(),rl))
			
			###salary table
			#mycursor.execute('INSERT INTO salary (BASIC,GRADEPAY,TRANSPORT_ALLOWANCE,DA,HRA,DA_TPT,TOTAL_SALARY) VALUES (%s,%s,%s,%s,%s,%s,%s)',(str(ba_),str(gd_),str(tpt_),str(da_),str(hra_),str(da_tpt),str(total)))                      
			



			mydb.commit()
		def r():
			te_1.delete(0,END)
			te_2.delete(0,END)
			te_3.delete(0,END)
			te_4.delete(0,END)
			te_5.delete(0,END)
			te_6.delete(0,END)
			te_7.delete(0,END)
			te_8.delete(0,END)
			te_9.delete(0,END)
			te_10.delete(0,END)
			te_11.delete(0,END)
			te_12.delete(0,END)
			te_13.delete(0,END)
			te_14.delete(0,END)
			te_15.delete(0,END)


		



		#______________________________frames____________________________________________________________
		
		'''def open_file():
			file = askopenfile(mode ='r', filetypes =[('EXCEL', '*.xls')])
			if file is not None:
				content = file.read()
				print(content)'''
		
		#____________________________________________________________________________________


		po=PhotoImage(file='lol.png')
		phot1=po.subsample(1,1)
		
		kartik=Label(tt,image=phot1,bd=400,bg='black')
		kartik.pack()

		#t_2=Frame(kartik,bg='black',bd=5,relief='raise')
		#t_2.place(x=-300,y=-200)
		
		def file_opener():
			#input1=filedialog.askopenfile(initialdir='/')
			filename=filedialog,askopenfile(filetypes=(("Excel files","*.xls"),))
			print('Selected',filename)
			

			'''
			import xlrd
			import mysql.connector

			mydb=mysql.connector.connect(
				host='localhost',
				user='root',
				password='sunilvats',
				database='payroll'
				)
			mycursor=mydb.cursor()

			


			book = xlrd.open_workbook(input1)
			sheet = book.sheet_by_name("source")

			




			query = """INSERT INTO employee (NAME ,EMAIL,MOBILE,DESIGNATION,GENDER ,ADDRESS ,QUALIFICATION ,FATHERS,DOB ,DOJ,EXPERIENCE ,EMPLOYEETYPE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""


			for r in range(1, sheet.nrows):
				NAME    	= sheet.cell(r,).value
				EMAIL   	= sheet.cell(r,1).value
				MOBILE			= sheet.cell(r,2).value
				DESIGNATION		= sheet.cell(r,3).value
				GENDER		= sheet.cell(r,4).value
				ADDRESS	= sheet.cell(r,5).value
				QUALIFICATION		= sheet.cell(r,6).value
				FATHERS		= sheet.cell(r,7).value
				DOB		= sheet.cell(r,8).value
				DOJ		= sheet.cell(r,9).value
				EXPERIENCE			= sheet.cell(r,10).value
				EMPLOYEETYPE	= sheet.cell(r,11).value
				

			
				values = (NAME ,EMAIL,MOBILE,DESIGNATION,GENDER ,ADDRESS ,QUALIFICATION ,FATHERS,DOB ,DOJ,EXPERIENCE ,EMPLOYEETYPE)


			
				mycursor.execute(query, values)

	# Close the cursor
			mycursor.close()

	# Commit the transaction
			mydb.commit()'''

			


		t_1=Frame(kartik,bg='black',bd=15,relief='raise',padx=470)
		t_1.place(x=-400,y=-400)
		l_1=Label(t_1,bg='black',fg='white',text='FILL THE FOLLOWING DETAILS',font='comisans 20 bold',relief="raise")
		l_1.pack()


		t_3=Frame(kartik,bg='pink',bd=5,relief='raise')
		t_3.place(x=-390,y=-300)

		t_4=Frame(kartik,bg='pink',bd=5,relief='raise')
		t_4.place(x=89,y=-300)



		
		#_________________labels_________________________________________________

		tl_1=Label(t_3,bd=10,bg='pink',fg='black',text=' NAME ',font='comisans 15 bold')
		tl_1.grid(column=0,row=0)
		
		tl_2=Label(t_3,bd=10,bg='pink',fg='black',text=' EMAIL ',font='comisans 15 bold')
		tl_2.grid(column=0,row=1)

		tl_3=Label(t_3,bd=10,bg='pink',fg='black',text='MOBILE NUMBER ',font='comisans 15 bold')
		tl_3.grid(column=0,row=2)

		tl_4=Label(t_3,bd=10,bg='pink',fg='black',text='DESIGNATION ',font='comisans 15 bold')
		tl_4.grid(column=0,row=3)

		tl_5=Label(t_3,bd=10,bg='pink',fg='black',text='GENDER ',font='comisans 15 bold')
		tl_5.grid(column=0,row=4)

		tl_6=Label(t_3,bd=10,bg='pink',fg='black',text='ADDRESS',font='comisans 15 bold')
		tl_6.grid(column=0,row=5)

		tl_7=Label(t_3,bd=10,bg='pink',fg='black',text='QUALIFICATION',font='comisans 15 bold')
		tl_7.grid(column=0,row=6)

		tl_8=Label(t_3,bd=10,bg='pink',fg='black',text='FATHERS/HUSBANDS NAME',font='comisans 15 bold')
		tl_8.grid(column=0,row=7)

		tl_9=Label(t_3,bd=10,bg='pink',fg='black',text='DATE OF BIRTH',font='comisans 15 bold')
		tl_9.grid(column=0,row=8)

		tl_10=Label(t_3,bd=10,bg='pink',fg='black',text='DATE OF JOINING',font='comisans 15 bold')
		tl_10.grid(column=0,row=9)

		tl_11=Label(t_3,bd=10,bg='pink',fg='black',text='EXPERIENCE ',font='comisans 15 bold')
		tl_11.grid(column=0,row=10)

		tl_12=Label(t_3,bd=10,bg='pink',fg='black',text='EMPLOYEE TYPE ',font='comisans 15 bold')
		tl_12.grid(column=0,row=11)

		tl_13=Label(t_4,bd=10,bg='pink',fg='black',text='SALARY',font='comisans 15 bold')
		tl_13.grid(column=0,row=0)

		tl_14=Label(t_4,bd=10,bg='pink',fg='black',text='BASIC',font='comisans 15 bold')
		tl_14.grid(column=0,row=1)

		tl_15=Label(t_4,bd=10,bg='pink',fg='black',text='GRADE PAY',font='comisans 15 bold')
		tl_15.grid(column=0,row=2)

		tl_16=Label(t_4,bd=10,bg='pink',fg='black',text='TPT',font='comisans 15 bold')
		tl_16.grid(column=0,row=3)

		

		#______________________entry____________________________________________________________________
		te_1=Entry(t_3,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=name1)
		te_1.grid(column=1,row=0)

		te_2=Entry(t_3,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=email)
		te_2.grid(column=1,row=1)

		te_3=Entry(t_3,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=number)
		te_3.grid(column=1,row=2)

		te_4=Entry(t_3,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=designation)
		te_4.grid(column=1,row=3)

		te_5=Entry(t_3,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=gender)
		te_5.grid(column=1,row=4)

		te_6=Entry(t_3,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=address)
		te_6.grid(column=1,row=5)

		te_7=Entry(t_3,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=qualification)
		te_7.grid(column=1,row=6)

		te_8=Entry(t_3,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=fatherhusband)
		te_8.grid(column=1,row=7)

		te_9=Entry(t_3,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=dob)
		te_9.grid(column=1,row=8)

		te_10=Entry(t_3,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=doj)
		te_10.grid(column=1,row=9)

		te_11=Entry(t_3,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=experience)
		te_11.grid(column=1,row=10)

		te_12=Entry(t_3,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=employtp)
		te_12.grid(column=1,row=11)

		te_13=Entry(t_4,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=basic)
		te_13.grid(column=1,row=1)

		te_14=Entry(t_4,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=gradepay)
		te_14.grid(column=1,row=2)

		te_15=Entry(t_4,bd=10,bg='white',fg='black',font='comisans 10 bold',textvariable=tranport)
		te_15.grid(column=1,row=3)

		#__________________________table for salary master______________
		'''
		def lol():
			mydb=mysql.connector.connect(
					host='localhost',
					user='root',
					password='sunilvats',        #"select'" + nr +"'"+" from employee where '" + k +"'"
					database='payroll'
					)
			mycursor=mydb.cursor()
			mycursor.execute(' CREATE TABLE salary(user_id INTEGER AUTO_INCREMENT PRIMARY KEY,BASIC  FLOAT(23),GRADEPAY FLOAT(23),TRANSPORT_ALLOWANCE FLOAT(23),DA FLOAT(23) ,HRA FLOAT(23),DA_TPT FLOAT(23),TOTAL_SALARY FLOAT(23))')
			mydb.commit()'''






		#__________________buttons____________________________________



		b_1=Button(tt,text='CANCEL',font='comisans 25 bold',relief="raise",command=quit,bg='black',fg='white')
		b_1.place(x=600,y=600)

		b_2=Button(tt,text='SAVE',font='comisans 25 bold',relief="raise",bg='black',fg='white',command=save)
		b_2.place(x=1200,y=600)

		b_3=Button(tt,text='CLEAR',font='comisans 25 bold',relief="raise",bg='black',fg='white',command=r)
		b_3.place(x=890,y=600)

		b_4=Button(tt,text='UPLOAD',font='comisans 25 bold',relief="raise",bg='black',fg='white',command=file_opener)
		b_4.place(x=590,y=400)




		tt.mainloop()


	###########################################end new employee################################################################	
		
		


		


	#___________________________________________________modify results canvas ________________________________________

	def pp():
		modify=Toplevel()
		modify.geometry('1200x700')
		modify.title('MODIFY DETAILS')
		modify.configure(bg='pink')


		##############################frames########################################################################
		fm_1=Frame(modify,bd=10,bg='cyan',relief='raise',padx=460)
		fm_1.place(x=0,y=0)

		fm_2=Frame(modify,bd=5,bg='red',relief='raise')
		fm_2.place(x=0,y=70)

		fm_3=Frame(modify,bd=5,bg='orange',relief='raise')
		fm_3.place(x=0,y=130)

		fm_4=Frame(modify,bd=5,bg='orange',relief='raise')
		fm_4.place(x=550,y=130)

		fm_5=Frame(modify,bd=5,bg='black',relief='raise')
		fm_5.place(x=550,y=195)

		fm_6=Frame(modify,bd=5,bg='black',relief='raise')
		fm_6.place(x=550,y=600)

		name=StringVar()
		na=StringVar()


		
		########################################## labels################################################
		lm_1=Label(fm_1,bd=5,font='comisans 20 bold',text='MODIFY RECORDS',bg='black',fg='white',relief='raise')
		lm_1.pack()

		lm_2=Label(fm_2,bd=5,font='comisans 15 bold',text='SEARCH USER ID',bg='red',fg='black')
		lm_2.grid(column=0,row=0)

		lm_3=Label(fm_3,bd=10,bg='orange',fg='black',text=' NAME ',font='comisans 15 bold')
		lm_3.grid(column=0,row=0)

		lm_4=Label(fm_3,bd=10,bg='orange',fg='black',text=' EMAIL ',font='comisans 15 bold')
		lm_4.grid(column=0,row=1)

		lm_5=Label(fm_3,bd=10,bg='orange',fg='black',text='MOBILE NUMBER ',font='comisans 15 bold')
		lm_5.grid(column=0,row=2)

		lm_6=Label(fm_3,bd=10,bg='orange',fg='black',text='DESIGNATION ',font='comisans 15 bold')
		lm_6.grid(column=0,row=3)

		lm_7=Label(fm_3,bd=10,bg='orange',fg='black',text='GENDER ',font='comisans 15 bold')
		lm_7.grid(column=0,row=4)

		lm_8=Label(fm_3,bd=10,bg='orange',fg='black',text='ADDRESS',font='comisans 15 bold')
		lm_8.grid(column=0,row=5)

		lm_9=Label(fm_3,bd=10,bg='orange',fg='black',text='QUALIFICATION',font='comisans 15 bold')
		lm_9.grid(column=0,row=6)

		lm_10=Label(fm_3,bd=10,bg='orange',fg='black',text='FATHERS/HUSBANDS NAME',font='comisans 15 bold')
		lm_10.grid(column=0,row=7)

		lm_11=Label(fm_3,bd=10,bg='orange',fg='black',text='DATE OF BIRTH',font='comisans 15 bold')
		lm_11.grid(column=0,row=8)

		lm_12=Label(fm_3,bd=10,bg='orange',fg='black',text='DATE OF JOINING',font='comisans 15 bold')
		lm_12.grid(column=0,row=9)

		lm_13=Label(fm_3,bd=10,bg='orange',fg='black',text='EXPERIENCE ',font='comisans 15 bold')
		lm_13.grid(column=0,row=10)

		lm_14=Label(fm_3,bd=10,bg='orange',fg='black',text='EMPLOYEE TYPE ',font='comisans 15 bold')
		lm_14.grid(column=0,row=11)

		lm_15=Label(fm_4,bd=10,bg='orange',fg='black',text='SALARY',font='comisans 15 bold')
		lm_15.grid(column=0,row=0)

		lm_16=Text(fm_5,fg='black',font='comisans 10 bold',pady=10,padx=30)
		lm_16.grid(column=0,row=0)

		def name2():
			
			
			nr=name.get()
			l=na.get()
			

			mydb=mysql.connector.connect(
				host='localhost',
				user='root',
				password='sunilvats',        #"select'" + nr +"'"+" from employee where '" + k +"'"
				database='payroll'
				)
			mycursor=mydb.cursor()
			resu=mycursor.execute("SELECT  * FROM employee where user_id='" + nr + "'")

			row=mycursor.fetchone()
			#global l

			l=str(row[1])
			m=str(row[2])
			l_=str(row[4])
			m_=str(row[5])
			o=str(row[6])
			o_=str(row[7])
			j=str(row[8])
			j_=str(row[9])
			e=str(row[10])
			e_=str(row[12])
			u=str(row[13])
			u_=str(row[14])
			p=str(row[15])
			#p_=str(row[16])

			
			em_2.insert(name.get(),l)
			em_3.insert(name.get(),m)
			em_4.insert(name.get(),m_)
			em_5.insert(name.get(),o)
			em_6.insert(name.get(),o_)
			em_7.insert(name.get(),j)
			em_8.insert(name.get(),j_)
			em_9.insert(name.get(),e)
			em_10.insert(name.get(),e_)
			em_11.insert(name.get(),u)
			em_12.insert(name.get(),u_)
			em_13.insert(name.get(),p)
			em_14.insert(name.get(),l_)

			while row is not None:
				print(row)
				row=mycursor.fetchone()
			mydb.commit()


		def run():
			em_1.delete(0,END)
			em_2.delete(0,END)
			em_3.delete(0,END)
			em_4.delete(0,END)
			em_5.delete(0,END)
			em_6.delete(0,END)
			em_7.delete(0,END)
			em_8.delete(0,END)
			em_9.delete(0,END)
			em_10.delete(0,END)
			em_11.delete(0,END)
			em_12.delete(0,END)
			em_13.delete(0,END)
			em_14.delete(0,END)



		e_1=StringVar()
		e_2=StringVar()
		e_3=StringVar()
		e_4=StringVar()
		e_5=StringVar()
		e_6=StringVar()
		e_7=StringVar()
		e_8=StringVar()
		e_9=StringVar()
		e_10=StringVar()
		e_11=StringVar()
		e_12=StringVar()
		e_13=StringVar()
		def cancel():
			modify.destroy()



		def update():
			mydb=mysql.connector.connect(
				host='localhost',
				user='root',
				password='sunilvats',        #"select'" + nr +"'"+" from employee where '" + k +"'"
				database='payroll'
				)
			nmae=IntVar()
			nr=name.get()
			mycursor=mydb.cursor()
			resu=mycursor.execute("SELECT  * FROM employee where user_id='" + nr + "'")
			
			row=mycursor.fetchone()
			#global l

			l=str(row[1])
			m=str(row[2])
			l_=str(row[4])
			m_=str(row[5])
			o=str(row[6])
			o_=str(row[7])
			j=str(row[8])
			j_=str(row[9])
			e=str(row[10])
			e_=str(row[12])
			u=str(row[13])
			u_=str(row[14])#u_p=((l,e_1.get())(m,e_2.get()),(l_,e_3.get()),(m_,e_4.get()),(o,e_5.get()),(o_,e_6.get()),(j,e_7.get()),(j_,e_8.get()),(e,e_9.get()),(e_,e_10.get()),(u,e_11.get()),(u_,e_12.get()),(p,e_13.get()))
			p=str(row[15])
			while row is not None:
				print(row)
				row=mycursor.fetchone()
		

			#up="UPDATE   employee SET NAME=%s,EMAIL=%s,MOBILE=%s,DESIGNATION=%s,GENDER =%s,ADDRESS=%s,QUALIFICATION=%s,FATHERS=%s,DOB=%s,DOJ=%s,EXPERIENCE=%s,EMPLOYEETYPE=%s , SALARY=%s, WHERE NAME=%s,EMAIL=%s,MOBILE=%s,DESIGNATION=%s,GENDER =%s,ADDRESS=%s,QUALIFICATION=%s,FATHERS=%s,DOB=%s,DOJ=%s,EXPERIENCE=%s,EMPLOYEETYPE=%s , SALARY=%s "
			up="UPDATE   employee SET NAME='%s',EMAIL='%s',MOBILE='%s',DESIGNATION='%s',GENDER ='%s',ADDRESS='%s',QUALIFICATION='%s',FATHERS='%s',DOB='%s',DOJ='%s',EXPERIENCE='%s',EMPLOYEETYPE='%s' , SALARY='%s' "%(e_1.get(),e_2.get(),e_3.get(),e_4.get(),e_5.get(),e_6.get(),e_7.get(),e_8.get(),e_9.get(),e_10.get(),e_11.get(),e_12.get(),e_13.get())
			

			mycursor.execute(up)

			mydb.commit()

			#lm_16.insert(END,l,'\n',m,'\n',l_,'\n',m_,'\n',o,'\n',o_,'\n',j,'\n',j_,'\n',e,'\n',e_,'\n',u,'\n',u_,p)







	#########################################entries########################################
		em_1=Entry(fm_2,bd=5,bg='white',fg='black',relief='raise',font='comisans 15 bold',textvariable=name)
		em_1.grid(column=1,row=0)

		em_2=Entry(fm_3,bd=10,bg='white',fg='black',font='comisans 15 bold',textvariable=e_1)
		em_2.grid(column=1,row=0)

		em_3=Entry(fm_3,bd=10,bg='white',fg='black',font='comisans 15 bold',textvariable= e_2)
		em_3.grid(column=1,row=1)

		em_4=Entry(fm_3,bd=10,bg='white',fg='black',font='comisans 15 bold',textvariable= e_3)
		em_4.grid(column=1,row=2)

		em_5=Entry(fm_3,bd=10,bg='white',fg='black',font='comisans 15 bold',textvariable= e_4)
		em_5.grid(column=1,row=3)

		em_6=Entry(fm_3,bd=10,bg='white',fg='black',font='comisans 15 bold',textvariable=e_5)
		em_6.grid(column=1,row=4)

		em_7=Entry(fm_3,bd=10,bg='white',fg='black',font='comisans 15 bold',textvariable=e_6)
		em_7.grid(column=1,row=5)

		em_8=Entry(fm_3,bd=10,bg='white',fg='black',font='comisans 15 bold',textvariable=e_7)
		em_8.grid(column=1,row=6)

		em_9=Entry(fm_3,bd=10,bg='white',fg='black',font='comisans 15 bold',textvariable=e_8)
		em_9.grid(column=1,row=7)

		em_10=Entry(fm_3,bd=10,bg='white',fg='black',font='comisans 15 bold',textvariable=e_9)
		em_10.grid(column=1,row=8)

		em_11=Entry(fm_3,bd=10,bg='white',fg='black',font='comisans 15 bold',textvariable=e_10)
		em_11.grid(column=1,row=9)

		em_12=Entry(fm_3,bd=10,bg='white',fg='black',font='comisans 15 bold',textvariable=e_11)
		em_12.grid(column=1,row=10)

		em_13=Entry(fm_3,bd=10,bg='white',fg='black',font='comisans 15 bold',textvariable=e_12)
		em_13.grid(column=1,row=11)

		em_14=Entry(fm_4,bd=10,bg='white',fg='black',font='comisans 15 bold',textvariable=e_13)
		em_14.grid(column=1,row=0)



		#####################################buttons##############################################

		bm_1=Button(fm_2,bd=0,font='comisans 15 bold',text='SEARCH',bg='black',fg='white',command=name2)
		bm_1.grid(column=2,row=0)

		bm_2=Button(fm_6,bd=0,font='comisans 25 bold',text='SAVE',bg='grey',fg='white',command=update)
		bm_2.grid(column=1,row=0)

		bm_3=Button(modify,bd=5,font='comisans 25 bold',text='CANCEL',bg='grey',fg='white',relief='raise',command=cancel)
		bm_3.place(x=900,y=600)

		bm_3=Button(modify,bd=5,font='comisans 25 bold',text='CLEAR',bg='grey',fg='white',relief='raise',command=run)
		bm_3.place(x=700,y=600)

	#________________________________________________salary master _________________________________________________
	def salarymaster():
		salary=Toplevel()
		salary.geometry('1457x700+5+5')
		salary.title('SALARY MASTER')


		#_________________________________records___________________________________________________________


		#__________________________________background image ___________________________________________________
		im_sa=PhotoImage(file='salary_back.png')
		im_sa1=im_sa.subsample(3,3)

		ima=Label(salary,image=im_sa1)
		ima.pack()

		#__________________________________frames _____________________________________________________________
		fs_r=Frame(ima,bd=10,bg='black',relief='raise')
		fs_r.place(x=0,y=-2)

		fs_r1=Frame(ima,bd=10,bg='black',relief='raise')
		fs_r1.place(x=0,y=50)

		fs_r2=Frame(ima,bd=10,bg='black',relief='raise')
		fs_r2.place(x=0,y=450)

		#__________________________________labels _____________________________________________________
		ls_r=Label(fs_r,bd=0,text='PAYROLL MANAGEMENT SYSTEM',font='comisans 20 bold',bg='black',fg="white",relief=SUNKEN,padx=494)
		ls_r.pack()

		ls_r1=Label(fs_r1,bd=0,text='SALARY GENERATION',font='comisans 20 bold',bg='black',fg="white",relief=SUNKEN)
		ls_r1.grid(row=0,column=0)

		#___________________________________entry_________________________________________________
		#es_r1=Entry(fs_r1,bd=0,bg='white',fg='black',font='comisans 15 bold')
		#es_r1.grid(row=0,column=1)

		#_____________________________table_____________________________________________
		from tkinter import ttk
		treev = ttk.Treeview(fs_r2, selectmode ='browse')
  
		# Calling pack method w.r.to treeview
		treev.pack(side ='right')
		  
		# Constructing vertical scrollbar
		# with treeview
		verscrlbar = ttk.Scrollbar(fs_r2, 
								   orient ="vertical", 
								   command = treev.yview)
		  
		# Calling pack method w.r.to verical 
		# scrollbar
		verscrlbar.pack(side ='right', fill ='x')
		  
		# Configuring treeview
		treev.configure(xscrollcommand = verscrlbar.set,style='black.Treeview')
		  
		# Defining number of columns
		treev["columns"] = ("1", "2", "3",'4','5','6','7','8','9')
		# Defining heading
		treev['show'] = 'headings'
		  
		# Assigning the width and anchor to  the
		# respective columns
		treev.column("1", width = 156, anchor ='c')
		treev.column("2", width = 156, anchor ='se')
		treev.column("3", width = 156, anchor ='se')
		treev.column("4", width = 156, anchor ='se')
		treev.column("5", width = 156, anchor ='se')
		treev.column("6", width = 156, anchor ='se')
		treev.column("7", width = 156, anchor ='se')
		treev.column("8", width = 156, anchor ='se')
		treev.column("9", width = 156, anchor ='se')
		 
		# Assigning the heading names to the 
		# respective columns
		treev.heading("1", text ="USER ID")
		treev.heading("2", text ="NAME")
		treev.heading("3", text ="Basic Pay")
		treev.heading("4", text ="Gradepay")
		treev.heading("5", text ="Transpor allowance")#BASIC,GRADEPAY,TRANSPORT_ALLOWANCE,DA,HRA,DA_TPT,TOTAL_SALARY
		treev.heading("6", text ="DA")
		treev.heading("7", text ="HRA")
		treev.heading("8", text ="DA ON TPT ")
		treev.heading("9", text ="TOTAL SALARY")
		  
		# Inserting the items and their features to the 
		# columns built
		'''treev.insert("", 'end', text ="L1", 
					 values =("Nidhi", "F", "25"))
		treev.insert("", 'end', text ="L2",
					 values =("Nisha", "F", "23"))
		treev.insert("", 'end', text ="L3",
					 values =("Preeti", "F", "27"))
		treev.insert("", 'end', text ="L4",
					 values =("Rahul", "M", "20"))'''
		
		salary.mainloop()






	#____________________________________________________leave records____________________________________________
	def records():
		#from tkinter import *
		leave=Toplevel()
		#leave.geometry('1200x700+0+0')
		leave.title("LEAVE RECORDS")
		


		def btn_clicked():
			print("Button Clicked")


			

		leave.geometry("1000x600")
		leave.configure(bg = "#ffffff")
		canvas = Canvas(
			leave,
			bg = "#6dd5ed",
			height = 600,
			width = 1000,
			bd = 0,
			highlightthickness = 0,
			relief = "ridge")
		canvas.place(x = 0, y = 0)

		entry0_img = PhotoImage(file = f"D:\\payroll web\\generated_code\\img_textBox0.png")
		entry0_bg = canvas.create_image(
			726.0, 124.5,
			image = entry0_img)

		entry0 = Entry(
			bd = 0,
			bg = "#ee9ca7",
			highlightthickness = 0)

		entry0.place(
			x = 596.0, y = 94,
			width = 260.0,
			height = 59)

		entry1_img = PhotoImage(file = f"D:\\payroll web\\generated_code\\img_textBox1.png")
		entry1_bg = canvas.create_image(
			729.5, 259.5,
			image = entry1_img)

		entry1 = Entry(
			bd = 0,
			bg = "#ee9ca7",
			highlightthickness = 0)

		entry1.place(
			x = 603.0, y = 227,
			width = 253.0,
			height = 63)

		img0 = PhotoImage(file = f"D:\\payroll web\\generated_code\\img0.png")
		b0 = Button(
			image = img0,
			borderwidth = 0,
			highlightthickness = 0,
			command = btn_clicked,
			relief = "flat")

		b0.place(
			x = 623, y = 364,
			width = 208,
			height = 65)

		background_img = PhotoImage(file = f"D:\\payroll web\\generated_code\\background.png")
		background = canvas.create_image(
			354.5, 300.0,
			image=background_img)

		leave.resizable(True, False)
		leave.mainloop()







	#_____________________frames______________________________________________________________________________

	f1=Frame(wn,bd=15,bg='black',relief='raise')
	f1.pack(fill='x')

	f2=Frame(wn,bd=13,bg='black',relief='raise')
	f2.pack()






	photo1=PhotoImage(file='bg3.png')
	photo=photo1.subsample(3,3)
	image=Label(f2,image=photo,bd=300,bg='black')
	image.pack(fill='x')

	'''f3=Frame(image,bd=5,relief='raise')
	f3.place(x=50,y=-300)'''

	'''p=PhotoImage(file='kv3.png')
	pho=p.subsample(3,3)
	image2=Label(f3,image=pho)
	image2.pack()'''
	f3=Frame(image,bd=10,bg='black',relief='raise',pady=155,width=5)
	f3.place(x=-300,y=-300)







	##############################################label
	l1=Label(f1,bd=0,text='PAYROLL MANAGEMENT SYSTEM',font='comisans 20 bold',bg='black',fg="white",relief=SUNKEN)
	l1.pack()

	l2=Label(image,bd=2,font='comisans 20 bold',text='KARTIKEYA VATS',bg='black',fg='white',relief='raise')
	l2.place(x=850,y=250)

	############################################################images
	'''

	ram=PhotoImage(file='em.png')
	ram1=ram.subsample(5,5)


	i_2=PhotoImage(file='add employee.png')
	i_3=i_2.subsample(4,3)


	i_4=PhotoImage(file='modify2.png')
	i_5=i_4.subsample(4,4)


	i_6=PhotoImage(file='leave2.png')
	i_7=i_6.subsample(4,4)



	i_8=PhotoImage(file='salary2.png')
	i_9=i_8.subsample(4,4)


	i_10=PhotoImage(file='records1.png')
	i_11=i_10.subsample(4,4)

	i_12=PhotoImage(file='print2.png')
	i_13=i_12.subsample(4,4)'''



	###############################################buttons

	b1=Button(f3,text='EMPLOYEE',font='comicsans 20 bold',bd=4,anchor='nw',relief='raise',bg='black',fg='white')
	b1.grid(row=0,column=0)



	b2=Button(f3,text='ADD EMPLOYEE',font='comicsans 20 bold',bd=0,anchor='nw',relief='raise',bg='black',fg='white',command=lal )
	b2.grid(row=1,column=0)


	b3=Button(f3,text='MODIFY RECORD',font='comicsans 20 bold',bd=0,anchor='w',relief='raise',bg='black',fg='white',command=pp)
	b3.grid(row=2,column=0)


	b4=Button(f3,text='LEAVE RECORD',font='comicsans 20 bold',bd=0,anchor='w',relief='raise',bg='black',fg='white',command=leave1)
	b4.grid(row=3,column=0)


	b5=Button(f3,text='SALARY MASTER',font='comicsans 20 bold',bd=0,anchor='w',relief='raise',bg='black',fg='white',command=salarymaster)
	b5.grid(row=4,column=0)

	b6=Button(f3,text='REPORTS',font='comicsans 20 bold',bd=0,anchor='w',relief='raise',bg='black',fg='white',command=records)
	b6.grid(row=5,column=0)

	b7=Button(f3,text='PRINT RECIPTS',font='comicsans 20 bold',bd=0,anchor='w',relief='raise',bg='black',fg='white')
	b7.grid(row=6,column=0)







	wn.mainloop()



#________________________________________buttons _________________________________________



bu_m2=Button(bac_image,bg='black',fg='white',text='LOGIN AS KARTIKEYA ',font='comicsans 25 bold',relief='raise',bd=5,command=login)
bu_m2.place(x=500,y=170)


#___________________________________________slider____________________________________________
'''#___SLIDER
char_index = 0
text = " "
slide_text = "WELCOME TO OUR PAYROLL SYSTEM CREATED BY KARTIKEYA VATS"

def slide():
	global char_index , text, slide_text
	if char_index >= len(slide_text):
		char_index = 0
		text = " "
		slider.config(text = text)
	else:
		text = text + slide_text[char_index]
		slider.configure(text = text)
		char_index = char_index + 1
	slider.after(700, slide)
		
slider = Label(image, text = text, font='comicsans 25 bold', width=50,bg='black',fg='white')
slider.place(x = 500 , y = 450)
slide()'''
def exit(a):
	mainwindow.destroy()

mainwindow.bind('<Return>',login)
mainwindow.bind('<Double Button>',exit)




mainwindow.mainloop()
