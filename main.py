from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import sys
from PIL import ImageTk, Image
from tkinter.font import Font
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np


flag = ""


def create():
	global nna,bsl,cod
	nna = eq1.get()
	bsl = eq2.get()
	cod = eq3.get()
	reco = (nna,str(bsl),str(cod))
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	ssq = "INSERT INTO balance(name, balance, pat_doc_no) VALUES(%s,%s,%s);"
	cur = my_db.cursor()
	try:
		cur.execute(ssq,reco)
		Label(k1,text="YOUR BANK ACCOUNT IS NOW SUCCESFULLY IN SYNC WITH THIS HOSPITAL").pack()
	except Exception as e:
		Label(k1,text="YOUR ACCOUNT ALREADY EXISTS").pack()

def set_bank_acc():
	global k1,eq1,eq2,eq3
	k1 = Tk()
	lq1 = Label(k1,text="Enter your name below: ")
	lq2 = Label(k1,text="Enter the amount you want to keep as balance in this hospital: ")
	lq3 = Label(k1,text="Enter your patient-doctor code: ")
	lq1.pack()
	eq1 = Entry(k1)
	eq1.pack()
	lq2.pack()
	eq2 = Entry(k1)
	eq2.pack()
	lq3.pack()
	eq3 = Entry(k1)
	eq3.pack()
	bbn = Button(k1,text="Submit",command=create).pack()
	bbh = Button(k1,text="Back to mainpage",command=lambda:[k1.destroy(),pat_show()]).pack()
	k1.mainloop()


def detailed_diagnostic():
	global lip,tri,bad,good,sugar,lip1,tri1,bad1,good1,sugar1
	lip = []
	tri = []
	bad = []
	good = []
	sugar = []
	po = []
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	cur.execute("select * from diagnostic where pat_name like '"+nan+"%'")
	for i in cur:
		po.append(i[2])
		po.append(i[3])
		po.append(i[5])
		po.append(i[4])
		po.append(i[6])
	fig = Figure()
	ax = fig.add_axes([0,0,1,1])
	langs = ['Lipid', 'TGC', 'Bad Chol', 'Good Chol', 'Sugar']
	ax.set_ylabel('Concentraion (in g/cc)')
	ax.set_xlabel('Proteins')
	ax.set_title('Detailed Diagnostics of '+name)
	ax.bar(langs,po)
	canvas = FigureCanvasTkAgg(fig, master = ro)
	canvas.draw()
	canvas.get_tk_widget().pack()
	Label(ro,text='Lipid                 '+' TGC                '+'     Bad Chol                 '+'     Good Chol                '+' Sugar').pack()
	toolbar = NavigationToolbar2Tk(canvas, ro) 
	toolbar.update()
	canvas.get_tk_widget().pack()
	Label(ro,text="YOUR HEALTH STATUS IS :").pack()
	if po[0] >= 150 :
		Label(ro,text="YOUR LIPID LEVEL IN YOUR BODY : HIGH RISK").pack()
	else :
		Label(ro,text="YOUR LIPID LEVEL IS NORMAL").pack()
	if po[1] >= 300 :
		Label(ro,text="YOUR triglyceride LEVEL IN YOUR BODY : HIGH RISK").pack()
	else :
		Label(ro,text="YOUR triglyceride LEVEL IS NORMAL").pack()
	if po[2] >= 200 :
		Label(ro,text="YOUR BAD CHOLESTROL LEVEL IN YOUR BODY : HIGH RISK").pack()
	else :
		Label(ro,text="YOUR BAD CHOLESTROL LEVEL IS NORMAL").pack()
	if po[3] >= 100 :
		Label(ro,text="YOUR GOOD CHOLESTROL LEVEL IN YOUR BODY : HIGH RISK").pack()
	else :
		Label(ro,text="YOUR GOOD CHOLESTROL LEVEL IS NORMAL").pack()
	if po[4] >= 500 :
		Label(ro,text="YOUR SUGAR LEVEL IN YOUR BODY : HIGH RISK").pack()
	else :
		Label(ro,text="YOUR SUGAR LEVEL IS NORMAL").pack()
	#byn = Button(ro,text="Back to mainpage",command=lambda:[ro.destroy(),pat_show()]).pack()

def diagnostic():
	global ro,nan
	ro = Tk()
	ro.geometry("1920x1080")
	nan = e1.get()
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	cur.execute("select * from diagnostic where pat_name like '"+nan+"%'")
	for i in cur:
		p0 = Label(ro,text="Name of the patient : "+i[0])
		p = Label(ro,text="Lipid profile :\t" + str(i[2]))
		p1 = Label(ro,text="triglyceride :\t" + str(i[3]))
		p2 = Label(ro,text="Bad cholestrol :\t" + str(i[4]))
		p3 = Label(ro,text="good cholestrol :\t" + str(i[5]))
		p4 = Label(ro,text="Diet sugar level :\t" + str(i[6]))
		p0.pack()
		p.pack()
		p1.pack()
		p2.pack()
		p3.pack()
		p4.pack()
	j = Button(ro,text="Show detailed statistics",command=detailed_diagnostic).pack()
	kj = Button(ro,text="Back to mainpage",command=lambda:[ro.destroy(),pat_show()]).pack()
	ro.mainloop()

def Bill_generate():
	global n1,bala
	n1 = Tk()
	n1.title(name+"'s BILL")
	qq = Listbox(n1)
	qq.insert(1,"PHARMACY BILL")
	qq.insert(2,"------------------------")
	qq.insert(3,s1+"\t"+str(s9))
	qq.insert(4,s2+"\t"+str(s0))
	qq.insert(5,s3+"\t"+str(s8))
	qq.insert(6,s4+"\t"+str(s7))
	qq.insert(7,s5+"\t"+str(s6))
	qq.insert(8,"--------------------------")
	qq.insert(9,"total price :"+str(summ))
	qq.insert(10,"--------------------------")
	qq.insert(11,"PAYMENT CONFIRMED")
	qq.pack()
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True,buffered=True)
	cur = my_db.cursor()
	cur1 = my_db.cursor()
	cur.execute("update balance set balance = balance - "+str(summ)+" where name = '"+name+"';")
	cur1.execute("select balance from balance where name = '"+name+"';")
	for i in cur1:
		bala = i[0]
	Label(n1,text="REMAINING BALANCE IN YOUR BANK ACCOUNT IS : "+str(bala)).pack()
	Label(n1,text="STATUS : PAID").pack()
	n1.mainloop()


def confirm_pharm(): 
	global summ,flag,s1,bal,s2,s3,s4,s5,s6,s7,s8,s9,s0,bal
	summ = 0
	flag = 0
	s1 = ll4.get()
	s2 = ll5.get()
	s3 = ll6.get()
	s4 = ll7.get()
	s5 = ll8.get()
	s6 = h1.get()
	s7 = h2.get()
	s8 = h3.get()
	s9 = h4.get()
	s0 = h5.get()
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True,buffered=True)
	cur = my_db.cursor()
	cur1 = my_db.cursor()
	cur.execute("select * from PHARMACIST")
	cur1.execute("select * from balance where pat_doc_no = '"+str(code)+"';")
	for j in cur1:
		bal = j[1]
	for i in cur:
		if i[0] == s1 and s9<i[3]:
			summ = summ + s9*i[2]
			if summ < bal:
				cur.execute("update PHARMACIST set MED_STOCK = MED_STOCK - "+str(s9)+" where MED_NAME = '"+s1+"';")
			else:
				flag = 1
				break;
		elif i[0] == s2 and s0<i[3]:
			summ = summ + s0*i[2]
			if summ< bal: 
				cur.execute("update PHARMACIST set MED_STOCK = MED_STOCK - "+str(s0)+" where MED_NAME = '"+s2+"';")
			else:
				falg = 1;
				break;
		elif i[0] == s3 and s8<i[3]:
			summ = summ + s8*i[2]
			if summ < bal:
				cur.execute("update PHARMACIST set MED_STOCK = MED_STOCK - "+str(s8)+" where MED_NAME = '"+s3+"';")
			else:
				flag = 1
				break;
		elif i[0] == s4 and s7<i[3]:
			summ = summ + s7*i[2]
			if summ < bal:
				cur.execute("update PHARMACIST set MED_STOCK = MED_STOCK - "+str(s7)+" where MED_NAME = '"+s4+"';")
			else:
				flag = 1
				break;
		elif i[0] == s5 and s6<i[3]:
			summ = summ + s6*i[2]
			if summ < bal:
				cur.execute("update PHARMACIST set MED_STOCK = MED_STOCK - "+str(s6)+" where MED_NAME = '"+s5+"';")
			else:
				flag = 1
				break;
		
def pharmacy():
	global v1,lis,ll8,ll7,ll4,ll6,ll5,h1,h2,h3,h4,h5,lis,ki
	ki = 0
	v1 = Tk()
	v1.title("Pharmacy")
	#v1.geometry("1920x1080")
	lis = []
	Label(v1,text="MEDICINE NAME").grid(row=0,column=0)
	Label(v1,text="MANUFACTURER NAME").grid(row=0,column=1)
	Label(v1,text="|MEDICINE PRICE|").grid(row=0,column=2)
	Label(v1,text="|MEDICINE STOCK|").grid(row=0,column=3)
	Label(v1,text="MEDICINE EXPIRY DATE").grid(row=0,column=4)
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	cur.execute("select * from PHARMACIST")
	for i in cur:
		Label(v1,text=i[0]).grid(row=ki+1,column=0)
		Label(v1,text=i[1]).grid(row=ki+1,column=1)
		Label(v1,text=str(i[2])).grid(row=ki+1,column=2)
		Label(v1,text=str(i[3])).grid(row=ki+1,column=3)
		Label(v1,text=str(i[4])).grid(row=ki+1,column=4)
		ki = ki + 1
		lis.append(i[0])
	tup = tuple(lis)
	ll = Label(v1,text="You can buy only upto 5 medicines")
	ll.grid(row=len(lis)+1,column=0)
	ll9 = Label(v1, text="Enter name and quantity for 1st medicine")
	ll9.grid(row=len(lis)+2,column=0)
	ll8 = ttk.Combobox(v1,width=45,values=tup)
	ll8.grid(row=len(lis)+3,column=0)
	h1 = Scale(v1,from_=0,to=100,orient=HORIZONTAL)
	h1.grid(row=len(lis)+4,column=0)
	ll7 = ttk.Combobox(v1,width=45,values=tup)
	ll7.grid(row=len(lis)+5,column=0)
	h2 = Scale(v1,from_=0,to=100,orient=HORIZONTAL)
	h2.grid(row=len(lis)+6,column=0)
	ll6 = ttk.Combobox(v1,width=45,values=tup)
	ll6.grid(row=len(lis)+7,column=0)
	h3 = Scale(v1,from_=0,to=100,orient=HORIZONTAL)
	h3.grid(row=len(lis)+8,column=0)
	ll4 = ttk.Combobox(v1,width=45,values=tup)
	ll4.grid(row=len(lis)+9,column=0)
	h4 = Scale(v1,from_=0,to=100,orient=HORIZONTAL)
	h4.grid(row=len(lis)+10,column=0)
	ll5 = ttk.Combobox(v1,width=45,values=tup)
	ll5.grid(row=len(lis)+11,column=0)
	h5 = Scale(v1,from_=0,to=100,orient=HORIZONTAL)
	h5.grid(row=len(lis)+12,column=0)
	btn2 = Button(v1,text="Generate Bill",command=lambda:[confirm_pharm(),Bill_generate()]).grid(row=len(lis)+13,column=0)
	b67 = Button(v1,text="Go back to main page",command=lambda:[v1.destroy(),pat_show()]).grid(row=len(lis)+14,column=0)
	v1.mainloop()


def appt_submit():
	global o,y2,name1,count,q
	y2 = Tk()
	name1 = q.get()
	name2 = q1.get()
	date = q2.get()
	time = q3.get()
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	cur.execute("select * from Appointment where Doc_name like '" + name1 + "%'")
	count = 0
	for i in cur:
		count = count + 1
	if count < 9:
		cur.execute("INSERT INTO Appointment (pat_name, Doc_name, Appt_date, Appt_time) VALUES (%s, %s, %s, %s)",(name2,name1,date,time))
		o = Label(y2,text="U have successfully booked an Appointment")
		o.pack()
	else:
		o = Label(y2,text="The Doctor already has 9 Appointments. Please select another doctor.")
		o.pack()
	btn1 = Button(y2,text="Go back to main page",command=lambda:[y2.destroy(),pat_show()]).pack()
	y2.mainloop()


def restock_pharmacy():
	global v2,lis,t,hh1,iy,ko
	v2 = Tk()
	v2.title("Pharmacy")
	Label(v2,text="MEDICINE NAME").grid(row=0,column=0)
	Label(v2,text="MANUFACTURER NAME").grid(row=0,column=1)
	Label(v2,text="|MEDICINE PRICE|").grid(row=0,column=2)
	Label(v2,text="|MEDICINE STOCK|").grid(row=0,column=3)
	Label(v2,text="MEDICINE EXPIRY DATE").grid(row=0,column=4)
	lis = []
	ko = 0
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	cur.execute("select * from PHARMACIST")
	for i in cur:
		Label(v2,text=i[0]).grid(row=ko+1,column=0)
		Label(v2,text=i[1]).grid(row=ko+1,column=1)
		Label(v2,text=str(i[2])).grid(row=ko+1,column=2)
		Label(v2,text=str(i[3])).grid(row=ko+1,column=3)
		Label(v2,text=str(i[4])).grid(row=ko+1,column=4)
		ko = ko + 1
		lis.append(i[0])
	t = tuple(lis)
	k = Label(v2,text="YOU CAN RESTOCK ONE MEDICINE AT A TIME (MAX AMT IS 100)")
	k.grid(row=len(lis)+1,column=0)
	iy = ttk.Combobox(v2,width = 45,values=t)
	iy.grid(row=len(lis)+2,column=0)
	hh1 = Scale(v2,from_=0,to_=100,orient=HORIZONTAL)
	hh1.grid(row=len(lis)+3,column=0)
	bbt = Button(v2,text="RESTOCK",command=restock)
	bbt1 = Button(v2,text="ADD NEW MEDICINE",command=new_med)
	bbt.grid(row=len(lis)+4,column=0)
	bbt1.grid(row=len(lis)+4,column=0)
	v2.mainloop()


def final_add_med():
	global na,mna,pr,st,exp
	na = x1.get()
	mna = x2.get()
	pr = x3.get()
	st = x4.get()
	exp = x5.get()
	re = (na,mna,str(pr),str(st),str(exp))
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	ser = "INSERT INTO PHARMACIST(MED_NAME, MED_MANUFACTURER, MED_PRICE, MED_STOCK, MED_EXPIRY_DATE) VALUES(%s,%s,%s,%s,%s);"
	cur.execute(ser,re)
	Label(v3,text="Medicine added successfully!!").pack()

def new_med():
	global v3,x1,x2,x3,x4,x5
	v3 = Tk()
	v3.title("NEW MEDICINES ADDING PORTAL")
	Label(v3,text="Enter the name of The medicine :").pack()
	x1 = Entry(v3)
	x1.pack()
	Label(v3,text="Enter the name of The manufacturer :").pack()
	x2 = Entry(v3)
	x2.pack()
	Label(v3,text="Enter the price of The medcine :").pack()
	x3 = Entry(v3)
	x3.pack()
	Label(v3,text="Enter the stock u want to buy of The medicine :").pack()
	x4 = Entry(v3)
	x4.pack()
	Label(v3,text="Enter the expiry date of The medicine :").pack()
	x5 = Entry(v3)
	x5.pack()
	brt = Button(v3,text="Submit",command=final_add_med).pack()
	b66 = Button(y3,text="Go back to main page",command=lambda:[v3.destroy(),pat_show()]).pack()
	v3.mainloop()


def restock():
	global w,ww
	w = iy.get()
	ww = hh1.get()
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	cur.execute("update PHARMACIST set MED_STOCK = MED_STOCK + "+str(ww)+" where MED_NAME = '"+w+"';")
	lo = Label(v2,text="AMOUNT RESTOCKED SUCCESFULLY!!!")
	lo.pack()



def pat_appt_final():
	global y1,q,q1,q2,q3,llll,l,j
	y1 = Tk()
	y1.title("APPOINTMENT BOOKING PORTAL")
	j = 0
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	Label(y1,text="DOCTORS NAME").grid(row=0,column=0)
	Label(y1,text="SPECIALIZATION").grid(row=0,column=2)
	cur.execute("select Name, specialization from Doctors")
	for i in cur:
		l = Label(y1,text=i[0])
		l.grid(row=j+1,column=0)
		l47 = Label(y1,text=i[1])
		l47.grid(row=j+1,column=2)
		j = j + 1
	llll = Label(y1,text="Enter the name of the doctor below: ")
	ll1 = Label(y1,text="Enter your name: ")
	ll2 = Label(y1,text="Enter Date of Appointment: ")
	ll3 = Label(y1,text="Enter time of Appointment: ")
	llll.grid(row=14,column=1)
	q = Entry(y1)
	q.grid(row=15,column=1)
	ll1.grid(row=16,column=1)
	q1 = Entry(y1)
	q1.grid(row=17,column=1)
	ll2.grid(row=18,column=1)
	q2 = Entry(y1)
	q2.grid(row=19,column=1)
	ll3.grid(row=20,column=1)
	q3 = Entry(y1)
	q3.grid(row=21,column=1)
	btn = Button(y1,text="Submit",command=appt_submit).grid(row=22,column=1)
	b6n = Button(y1,text="Go back to main page",command=lambda:[y1.destroy(),pat_show()]).grid(row=23,column=1)
	y1.mainloop()


def pat_appt():
	global y,res,res1
	y = Tk()
	y.title("Patients' Appointment Portal")
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	cur.execute("select * from Patients where Password like '" + passwd + "%'")
	for i in cur:
		res = i[7]
		res1 = i[0]
	if i[7] == "no":
		l4 = Label(y,text="You dont have any current appointment")
		l4.pack()
		b5 = Button(y,text="Book one now!!",command=pat_appt_final).pack()
	else:
		cur.execute("select * from Appointment where pat_name like '" + i[0] + "%';")
		for i in cur:
			l5 = Label(y,text=i[0]+" has an appointment with "+i[1]+" at "+i[2])
			l5.pack()
		b6 = Button(y,text="Go back to main page",command=lambda:[y.destroy(),pat_show()]).pack()
	my_db.commit()
	cur.close()
	my_db.close()
	y.mainloop()

def doc_get():
	global res,code,passwd,numberr,res1,rrr
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	rrr = Tk()
	code = e.get()
	number = ee.get()
	cur.execute("select * from Doctors where Doc_code like '"+code+"%'")
	for i in cur:
		res=i[6]
		res1=i[4]
	if str(res1) == number:
		lll = Label(rrr,text="Your password is "+res)
		lll.pack()
	else:
		lll = Label(rrr,text="Invalid user")
		lll.pack()
	b1 = Button(rrr,text="Back to login Page",command=lambda:[rrr.destroy(),mainpage()]).pack()
	my_db.commit()
	cur.close()
	my_db.close()
	rrr.mainloop()

def doc_forgot():
	global rr,ee,e,l,ll
	rr = Tk()
	l = Label(rr,text="Enter below your doctor code: ")
	ll = Label(rr,text="Enter below your phone number: ")
	e = Entry(rr)
	ee = Entry(rr)
	l.pack()
	e.pack()
	ll.pack()
	ee.pack()
	bb = Button(rr,text="Get password",command=doc_get).pack()
	rr.mainloop()


def doct_appointment():
	global v7
	v7 = Tk()
	v7.title("Doctors Appt portal")
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	cur.execute("select * from Appointment where Doc_name = '" + name + "';")
	for i in cur:
		Label(v7,text="You have an Appointmennt with "+i[0]+" at "+i[3]+" on "+i[2]).pack()
	bt1 = Button(v7,text="Go back to menu page",command=lambda:[v7.destroy(),show()])
	bt1.pack()
	v7.mainloop()


def show():
	global name,passwd,l3,r2,res,l4
	flag="doc_show"
	res = ""
	r2 = Tk()
	r2.geometry("400x400")
	r2.title("Doctors' Page")
	name = e1.get()
	passwd = e2.get()
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	cur.execute("select * from Doctors where Name like '"+name+"%'")
	for i in cur:
		res = i[6]
	if res == passwd:
		l3 = Label(r2,text="Welcome to the page "+name)
		l4 = Label(r2,text="*"*80)
		l3.pack()
		l4.pack()
		b3 = Button(r2,text="Show all Appointments",command=doct_appointment).pack()
		b5 = Button(r2,text="Access Pharmacy",command=restock_pharmacy).pack()
	else:
		l3 = Label(r2,text="Invalid password or username")
		button0 = Button(r2,text="Forgot Password?",command=lambda:[r2.destroy(),doc_forgot()]).pack()
		l3.pack()
	cur.close()
	r2.mainloop()

	
def doct_login():
	global r1, e1, e2, l1, l2
	flag = "doc_login"
	root.destroy()
	r1 = Tk()
	r1.geometry("700x500")
	r1.title("Doctors login")
	l1 = Label(r1,text="Enter your name below: ")
	l2 = Label(r1,text="Enter your password below: ")
	l1.pack()
	e1 = Entry(r1)
	e1.pack()
	l2.pack()
	e2 = Entry(r1,show="*")
	e2.pack()
	button5 = Button(r1,text="Sign in",command=show).pack()
	button7 = Button(r1,text="back to Mainpage",command=lambda:[r1.destroy(),mainpage()]).pack()
	r1.mainloop()


def pat_show():
	global name,passwd,l3,r4,res,code
	flag = "pat_show"
	res = ""
	r4 = Tk()
	r4.geometry("400x400")
	r4.title("Patients Portal")
	name = e1.get()
	passwd = e2.get()
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	cur.execute("select * from Patients where Pat_Name like '"+name+"%'")
	for i in cur:
		res = i[6]
		code = i[1]
	if res == passwd:
		l3 = Label(r4,text="Welcome "+name+" to the page")
		l4 = Label(r4,text="-"*80)
		l3.pack()
		l4.pack()
		b2 = Button(r4,text="Book an Appointment",command=lambda:[r4.destroy(),pat_appt_final()]).pack()
		b3 = Button(r4,text="Show all Appointments",command=lambda:[r4.destroy(),pat_appt()]).pack()
		b4 = Button(r4,text="Show previous Diagnosotics",command=lambda:[r4.destroy(),diagnostic()]).pack()
		b5 = Button(r4,text="Access Pharmacy",command=lambda:[r4.destroy(),pharmacy()]).pack()
		Label(r4,text="----DONT CLICK IF U ALREADY HAVE SET UP YOUR ACCOUNT----").pack()
		b6 = Button(r4,text="SET BANK ACCOUNT IN SYNC WITH HOSPITAL",command=lambda:[r4.destroy(),set_bank_acc()]).pack()
	else:
		l3 = Label(r4,text="Invalid password or username")
		button0 = Button(r4,text="Forgot Password?",command=lambda:[r4.destroy(),pat_forgot()]).pack()
		l3.pack()
	cur.close()
	r4.mainloop()

def pat_get():
	global res,code,passwd,numberr,res1,rrr
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	rrr = Tk()
	code = e.get()
	number = ee.get()
	cur.execute("select * from Patients where Pat_Doc_code like '"+code+"%'")
	for i in cur:
		res=i[6]
		res1=i[4]
	if str(res) == code:
		lll = Label(rrr,text="Your password is "+res)
		lll.pack()
	else:
		lll = Label(rrr,text="Invalid user")
		lll.pack()
	b1 = Button(rrr,text="Back to login Page",command=lambda:[rrr.destroy(),mainpage()]).pack()
	my_db.commit()
	cur.close()
	my_db.close()
	rrr.mainloop()

def pat_forgot():
	global rr,ee,e,l,ll
	rr = Tk()
	l = Label(rr,text="Enter below your patient doctor code: ")
	ll = Label(rr,text="Enter below your phone number: ")
	e = Entry(rr)
	ee = Entry(rr)
	l.pack()
	e.pack()
	ll.pack()
	ee.pack()
	bb = Button(rr,text="Get password",command=doc_get).pack()
	rr.mainloop()

def pat_login():
	global r3, e1, e2, l1, l2
	flag = "pat_login"
	root.destroy()
	r3 = Tk()
	r3.geometry("700x500")
	r3.title("Patient login")
	l1 = Label(r3,text="Enter your name below: ")
	l2 = Label(r3,text="Enter your password below: ")
	l1.pack()
	e1 = Entry(r3)
	e1.pack()
	l2.pack()
	e2 = Entry(r3,show="*")
	e2.pack()
	button5 = Button(r3,text="Sign in",command=pat_show).pack()
	button8 = Button(r3,text="back to Mainpage",command=lambda:[r3.destroy(),mainpage()]).pack()
	r3.mainloop()


def insert():
	global r6,apt,name,code,gender,disease,number,address,passwd,l1
	r6 = Tk()
	r6.title("Patient Signup")
	name = e1.get()
	code = e2.get()
	gender = e3.get()
	disease = e4.get()
	number = e5.get()
	address = e6.get()
	passwd = e7.get()
	apt = "no"
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	st = "INSERT INTO Patients (Pat_Name, Pat_Doc_code, gender, Disease, Pat_ph_number, Pat_address, Password, Appointments)VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
	record = (name,code,gender,disease,number,address,passwd,apt)
	cur.execute(st,record)
	my_db.commit()
	cur.close()
	my_db.close()
	l1 = Label(r6,text="SUCCESSFULLY INSERTED RECORD!")
	l1.pack()
	r6.mainloop()

def pat_signup():
	global r5,e1,e2,e3,e4,e5,e6,e7,l1,l2,l3,l4,l5,l6,l7
	root.destroy()
	r5 = Tk()
	r5.title("PATIENTS REGISTRATION PORTAL")
	l1 = Label(r5,text="Enter your name below: ")
	l2 = Label(r5,text="Enter your patient doctor code: ")
	l3 = Label(r5,text="Enter your gender: ")
	l4 = Label(r5,text="Enter your treated disease: ")
	l5 = Label(r5,text="Enter your phone number: ")
	l6 = Label(r5,text="Enter your address : ")
	l7 = Label(r5,text="Enter your password: ")
	l1.pack()
	e1 = Entry(r5)
	e1.pack()
	l2.pack()
	e2 = Entry(r5)
	e2.pack()
	l3.pack()
	e3 = Entry(r5)
	e3.pack()
	l4.pack()
	e4 = Entry(r5)
	e4.pack()
	l5.pack()
	e5 = Entry(r5)
	e5.pack()
	l6.pack()
	e6 = Entry(r5)
	e6.pack()
	l7.pack()
	e7 = Entry(r5)
	e7.pack()
	button6 = Button(r5,text="Register",command=insert).pack()
	button9 = Button(r5,text="back to Mainpage",command=lambda:[r5.destroy(),mainpage()]).pack()
	r5.mainloop()


def doc_insert():
	global r8,apt,name,code,gender,specialization,number,address,passwd,l1
	r8 = Tk()
	r8.title("SUCCESS PAGE")
	name = e1.get()
	code = e2.get()
	gender = e3.get()
	specialization = e4.get()
	number = e5.get()
	address = e6.get()
	passwd = e7.get()
	apt = "no"
	my_db = mysql.connector.connect(host="localhost", user="root", passwd="", database="dharmik", autocommit=True)
	cur = my_db.cursor()
	st = "INSERT INTO Doctors (Name, Doc_code, gender, specialization, Doc_ph_number, Doc_address, Password,Appointments) VALUES (%s, %s, %s, %s, %s, %s, %s) "
	record = (name,code,gender,specialization,number,address,passwd,apt)
	cur.execute(st,record)
	my_db.commit()
	cur.close()
	my_db.close()
	l1 = Label(r8,text="REGISTARTION DONE SUCCESSFULLY")
	l1.pack()
	r8.mainloop()

def doc_signup():
	global r7,e1,e2,e3,e4,e5,e6,e7,l1,l2,l3,l4,l5,l6,l7
	root.destroy()
	r7 = Tk()
	r7.title("DOCTORS REGISTRATION PORTAL")
	l1 = Label(r7,text="Enter your name below: ")
	l2 = Label(r7,text="Enter your doctor code: ")
	l3 = Label(r7,text="Enter your gender: ")
	l4 = Label(r7,text="Enter your specialization: ")
	l5 = Label(r7,text="Enter your phone number: ")
	l6 = Label(r7,text="Enter your address : ")
	l7 = Label(r7,text="Enter your password: ")
	l1.pack()
	e1 = Entry(r7)
	e1.pack()
	l2.pack()
	e2 = Entry(r7)
	e2.pack()
	l3.pack()
	e3 = Entry(r7)
	e3.pack()
	l4.pack()
	e4 = Entry(r7)
	e4.pack()
	l5.pack()
	e5 = Entry(r7)
	e5.pack()
	l6.pack()
	e6 = Entry(r7)
	e6.pack()
	l7.pack()
	e7 = Entry(r7)
	e7.pack()
	button6 = Button(r7,text="Register",command=doc_insert).pack()
	button7 = Button(r7,text="back to Mainpage",command=lambda:[r7.destroy(),mainpage()]).pack()
	r7.mainloop()


def mainpage():
	global root
	root = Tk()
	root.geometry("1920x1080")
	root.title("HOSPITAL")
	path1 = 'C:/Users/Dharmik Govani/Desktop/DBMS/Project/dbms.jpg'
	img = ImageTk.PhotoImage(Image.open(path1))
	panel = Label(root, image = img)
	panel.pack(side = "bottom", fill = "both", expand = "yes")
	k = Label(root,text="WELCOME TO DMSC HOSPITAL")
	k.config(font=("Courier",44))
	k1 = Label(root,text="")
	k.pack()
	k1.pack()
	button1 = Button(root,text="Log in as Doctor",command=doct_login).pack()
	k1.pack()
	button2 = Button(root,text="Log in as Patient",command=pat_login).pack()
	k1.pack()
	button3 = Button(root,text="Sign up as patient",command=pat_signup).pack()
	k1.pack()
	button4 = Button(root,text="Sign up as Doctor",command=doc_signup).pack()
	k1.pack()
	root.mainloop()
mainpage()