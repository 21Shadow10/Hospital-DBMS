create database dharmik;

use dharmik;

create table Doctors(
		Name varchar(20),
        Doc_code numeric(5),
        gender char(1), 
        specialization varchar(20),
        Doc_ph_number numeric(10),
        Doc_address varchar(70),
		Password varchar(10)
        );
insert into Doctors values('Dr. Mahesh Panchal', 12345, 'M','cardiologist',9099123456,'Vidhannagar','iopt');

select * from Doctors;
insert into Doctors values('Dr. Rupa Panchal', 12346, 'F','gastrologist',9098170345,'Mumbai','efgh');

select * from Doctors;
insert into Doctors values('Dr. Shudh patwari', 12347, 'M','gynacologist',9199040456,'Chennai'),'ijkl';
insert into Doctors values('Dr. Mukesh banerjee', 12348, 'M','cardiologist',9034123456,'Delhi','mnop');
insert into Doctors values('Dr. Adarsh Tiwari', 12349, 'M','cardiologist',9099137456,'Ahmedabad','qrst');
insert into Doctors values('Dr. Rupasree Roy', 12350, 'F','gastrologist',9098723456,'Gurgaon','uvwx');
insert into Doctors values('Dr. Snigdha Thakkar', 12351, 'F','surgeon',9879123456,'Kashmir','yzab');
insert into Doctors values('Dr. jignesh Jain', 12352, 'M','cardiologist',9099123409,'Vidhannagar','cdef');

select * from Doctors;

use dharmik;
select * from Doctors;

insert into Doctors(Password) values('abcd');
select * from Doctors;
select * from Doctors;

update Doctors 
set Password = 'abcd'
where Doc_code = 12345;
update Doctors set Password = 'abcd'where Doc_code = 12345;

SET SQL_SAFE_UPDATES = 0;
update Doctors 
set Password = 'abcd'
where Doc_code = 12345;
select * from Doctors;
update Doctors 
set Password = 'efgh'
where Doc_code = 12346;
update Doctors 
set Password = 'ijkl'
where Doc_code = 12347;
update Doctors 
set Password = 'mnop'
where Doc_code = 12348;
update Doctors 
set Password = 'qrst'
where Doc_code = 12349;
update Doctors 
set Password = 'uvwx'
where Doc_code = 12350;
update Doctors 
set Password = 'yzab'
where Doc_code = 12351;
select * from Doctors;
update Doctors 
set Password = 'cdef'
where Doc_code = 12352;
select * from Doctors;
delete from Doctors where Doc_code is null;
select * from Doctors;
update Doctors 
set Password = 'iopt'
where Doc_code = 12345;
delete from Doctors where Password = null;
select * from Doctors;

create table Patients(
		Pat_Name varchar(40),
        Pat_Doc_code numeric(5),
        gender char(1), 
        Disease varchar(20),
        Pat_ph_number numeric(10),
        Pat_address varchar(70),
		Password varchar(8),
		Appointments varchar(5)
        );
        
select * from Patients;
alter table Patients add Password varchar(8);
select * from Patients;

use dharmik;
select * from Doctors where Name like 'Dr. Shudhanshu%';
select * from Doctors;
select * from Doctors where Name like 'Dr. Shudh%';
select * from Doctors;
select * from Patients;
alter table Patients add Appointments varchar(5);

CREATE TABLE PHARMACIST(
	MED_NAME VARCHAR(40),
	MED_MANUFACTURER VARCHAR(40),
	MED_PRICE INT,
	MED_STOCK INT,
	MED_EXPIRY_DATE DATE
);

CREATE TABLE ACCOUNTANT(
	PAT_NAME VARCHAR(20),
	PAT_GENDER CHAR(1),
	PAT_DOC_NUMBER INT,
	PAT_NUMBER numeric(10),
	PAT_ADDRESS VARCHAR(70),
	BILL DECIMAL(10,2)
);

INSERT INTO PHARMACIST VALUES 
	('DOLO-650' , 'MICRO LABS LTD' , 20 , 400 , '2021-10-11'),
	('LANTUS-INSULIN' , 'SANOFI' , 54 , 250 , '2020-12-23'),
	('ADALIMUMAB' , 'ZYDUS CADILA' , 150 , 300 , '2021-02-27'),
	('AB PHYLLINE' , 'SUN PHARMA LTD' , 15 , 500 , '2021-04-21'),
	('HYDROXYCHLOROQUINE DRUG' , 'DR. REDDYS LABORATORIES' , 60 , 200 , '2020-11-30'),
	('NOVAMOX-CV' , 'CIPLA LTD' , 20 , 450 , '2021-01-31');

INSERT INTO PHARMACIST VALUES  
    ('PANTOPRAZOLE-40' , 'ESTRELLAS LABS LTD' , 200 , 40 , '2021-04-14'),
    ('ZENTEL-200' , 'MEHADIA TRADELINKS' , 10 , 800 , '2020-11-08');  

INSERT INTO PHARMACIST VALUES 
    ('DIGENE','ABOTT HEALTHCARE',70,300,'2020-12-29'),
    ('ULCIKIT-500','ABOTT HEALTHCARE',50,400,'2021-05-23'),
    ('DIABENORM-GL','ACME LIFESCIENCES',100,200,'2021-06-24'),
    ('AGROACE P','AGRO REMEDIES',52,148,'2020-12-13');

INSERT INTO ACCOUNTANT VALUES 
	('AMIT SHARMA' , 'M' , 213 , 56784 , '35, GREEN VILLA, GANDHI ROAD , AHMEDABAD' , 45000.00),
	('SHREYA RASTOGI' , 'F' , 354 , 56902 , '45, GREEN IRIS, JUDGES BUNGLAOW, AHMEDABAD', 89000.00),
	('VIJAY SINGH' , 'M' , 214 , 54361 , '21-B MAPLE TREES, MEMNAGAR, AHMEDABAD' , 200000.00 ),
	('WASIM KHAN' , 'M' , 950 , 23467 , '43-C ANAM BUNGALOWS, DARIYAPUR, AHMEDABAD' , 35000.00),
	('YASHI PARMAR', 'F' , 690 , 54367 , '81 YUKTA APARTMENTS PRAHLADNAGAR, AHMEDABAD' , 55000.00),
	('NIDHI PATEL' , 'F' , 573 , 65437 , '154 TRILOK SOC, K.K NAGAR, AHMEDABAD' , 70000.00);

select * from PHARMACIST;
INSERT INTO Patients VALUES 
	('AMIT SHARMA' , 12350 , 'M' ,'Appendicites', 9923456789 , '35, GREEN VILLA, GANDHI ROAD , AHMEDABAD' , 'aswq','no'),
	('SHREYA RASTOGI' , 12345 , 'F' ,'Pancreatitis', 5690212234 , '45, GREEN IRIS, JUDGES BUNGLAOW, AHMEDABAD', 'ddds','no'),
	('VIJAY SINGH' , 12346 , 'M' ,'Ulcers', 5436166475 , '21-B MAPLE TREES, MEMNAGAR, AHMEDABAD' , 'gbgf','no'),
	('WASIM KHAN' , 12347 , 'M' ,'liver disease',  2346743213 , '43-C ANAM BUNGALOWS, DARIYAPUR, AHMEDABAD' , 'qwer','no'),
	('YASHI PARMAR', 12348 , 'F' ,'Swine flu', 5436734564 , '81 YUKTA APARTMENTS PRAHLADNAGAR, AHMEDABAD' , 'fgtr','no'),
	('NIDHI PATEL' , 12349 , 'F' ,'dengue', 6543712345 , '154 TRILOK SOC, K.K NAGAR, AHMEDABAD' , 'dwsa','no');
select * from ACCOUNTANT;

create table balance(
	name varchar(20) primary key not null,
    balance numeric(10),
    pat_doc_no varchar(10)
    );

INSERT INTO balance VALUES 
	('AMIT SHARMA' ,100000, '12350'),
	('SHREYA RASTOGI' ,25000, '12345' ),
	('VIJAY SINGH' ,1000000, '12346' ),
	('WASIM KHAN' ,34456, '12347' ),
	('YASHI PARMAR',20089, '12348' ),
    ('Kunal Sharma' ,4405502, '12345'),
	('NIDHI PATEL' ,1000344, '12349' );
select * from balance;
create table Appointment(
	pat_name varchar(40),
    Doc_name varchar(40),
    Appt_date varchar(15),
    Appt_time varchar(10)
);

select * from Appointment;
delete from Appointment where  pat_name = 'AMIT SHARMA';
select * from Patients;
delete from Doctors where Doc_code = 0;
alter table Doctors add Appointment varchar(5);
update Doctors 
set Appointment = 'yes'
where Doc_code = 12323;
select * from Doctors;

create table diagnostic(
	pat_name varchar(30),
    pat_cod varchar(10),
    lipid int,
    triglycaride int,
    good_cholestrol int,
    bad_cholestrol int,
    sugar_level int
    );
    
insert into diagnostic values
		('AMIT SHARMA' , 12350 , 198, 390, 177, 204, 560),
		('Kunal Sharma' , 12345 , 144, 234, 340, 187, 310),
		('Vijay Singh', 12347, 451, 254, 150, 198, 500),
    	('Wasim Khan', 12347, 351, 200, 180, 260, 400),
		('Yashi Parmar',12348,200,325,190,200,450),
    	('Nidhi Patel',12349,180,200,150,250,480);
        
select * from diagnostic;