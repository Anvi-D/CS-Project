import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="ananya",database="Automobiles")
cursor=mycon.cursor()
cursor.execute("CREATE TABLE if not exists Area(Sr_No integer,Area char(60));")
st1="INSERT INTO Area(Sr_No,Area)VALUES(1,'Kirkee')"
cursor.execute(st1)
st2="INSERT INTO Area(Sr_No,Area)VALUES(2,'Shivpeth')"
cursor.execute(st2)
st3="INSERT INTO Area(Sr_No,Area)VALUES(3,'Pimpri')"
cursor.execute(st3)
st4="INSERT INTO Area(Sr_No,Area)VALUES(4,'Hinjewadi')"
cursor.execute(st4)
st5="INSERT INTO Area(Sr_No,Area)VALUES(5,'Chandan Nagar')"
cursor.execute(st5)
mycon.commit()
st6="SELECT * FROM Area"
cursor.execute(st6)
data=cursor.fetchall()
for row in data:
    print(row)

cursor.execute("CREATE TABLE if not exists Bill_of_Materials(Part char(40) NOT NULL,Material_From char(50));")
st1="INSERT INTO Bill_of_Materials(Part,Material_From ) VALUES('Main Journal Bearing','Mhale')"
cursor.execute(st1)
st2="INSERT INTO Bill_of_Materials(Part,Material_From)VALUES('Connecting Rods','Bajaj Motors')"
cursor.execute(st2)
st3="INSERT INTO Bill_of_Materials(Part,Material_From)VALUES('Pistons','India Piston')"
cursor.execute(st3)
st4="INSERT INTO Bill_of_Materials(Part,Material_From)VALUES('Flywheel','Shakti Auto')"
cursor.execute(st4)
st5="INSERT INTO Bill_of_Materials(Part,Material_From)VALUES('Oil Pan','Novaris')"
cursor.execute(st5)
st6="INSERT INTO Bill_of_Materials(Part,Material_From)VALUES('Damper Pulley','Metaldyne')"
cursor.execute(st6)
st7="INSERT INTO Bill_of_Materials(Part,Material_From)VALUES('Intake manifold','Novaris')"
cursor.execute(st7)
st8="INSERT INTO Bill_of_Materials(Part,Material_From)VALUES('Air Filter','Mhale Filters')"
cursor.execute(st8)
st9="INSERT INTO Bill_of_Materials(Part,Material_From)VALUES('Valve','Rane Engine Valves')"
cursor.execute(st9)
st10="INSERT INTO Bill_of_Materials(Part,Material_From)VALUES('Starter Motor','TVS Electric')"
cursor.execute(st10)
mycon.commit()
st11="SELECT * FROM Bill_of_Materials"
cursor.execute(st11)
data=cursor.fetchall()
for row in data:
    print(row)

cursor.execute("CREATE TABLE if not exists Car_Exteriors(Part char(60) NOT NULL,Price decimal);")
st1="INSERT INTO Car_Exteriors(Part,Price)VALUES('Mud Flaps(Set of 4)',800)"
cursor.execute(st1)
st2="INSERT INTO Car_Exteriors(Part,Price)VALUES('Wheel Cover(Set of 4 basis Tyre Size & Design)',2200)"
cursor.execute(st2)
st3="INSERT INTO Car_Exteriors(Part,Price)VALUES('Body Side Moulding',2300)"
cursor.execute(st3)
st4="INSERT INTO Car_Exteriors(Part,Price)VALUES('Sun Door Visor-all 4 windows',1200)"
cursor.execute(st4)
st5="INSERT INTO Car_Exteriors(Part,Price)VALUES('Roof Luggage Carrier(For Ertiga)',10600)"
cursor.execute(st5)
st6="INSERT INTO Car_Exteriors(Part,Price)VALUES('Fog Light',3800)"
cursor.execute(st6)
st7="INSERT INTO Car_Exteriors(Part,Price)VALUES('Exhaust Pipe',3500)"
cursor.execute(st7)
st8="INSERT INTO Car_Exteriors(Part,Price)VALUES('Engine Mounting',4000)"
cursor.execute(st8)
st9="INSERT INTO Car_Exteriors(Part,Price)VALUES('Battery(Petrol)',4000)"
cursor.execute(st9)
st10="INSERT INTO Car_Exteriors(Part,Price)VALUES('Battery(Diesel)',6500)"
cursor.execute(st10)
st11="INSERT INTO Car_Exteriors(Part,Price)VALUES('Bonnet',15000)"
cursor.execute(st11)
st12="INSERT INTO Car_Exteriors(Part,Price)VALUES('Flywheel',1200)"
cursor.execute(st12)
st13="INSERT INTO Car_Exteriors(Part,Price)VALUES('Front Brake Pad Replacement',2000)"
cursor.execute(st13)
st14="INSERT INTO Car_Exteriors(Part,Price)VALUES('Side Indicator Bulb',115)"
cursor.execute(st14)
st15="INSERT INTO Car_Exteriors(Part,Price)VALUES('Side Window Glass)',1500)"
cursor.execute(st15)
st16="INSERT INTO Car_Exteriors(Part,Price)VALUES('AC Cooling Coil',2500)"
cursor.execute(st16)
st17="INSERT INTO Car_Exteriors(Part,Price)VALUES('Turbo Charger',35000)"
cursor.execute(st17)
st18="INSERT INTO Car_Exteriors(Part,Price)VALUES('AC Compressor Replacement',15000)"
cursor.execute(st18)
st19="INSERT INTO Car_Exteriors(Part,Price)VALUES('Radiator Assembly',20000)"
cursor.execute(st19)
st20="INSERT INTO Car_Exteriors(Part,Price)VALUES('Crank Shaft Assembly',22000)"
cursor.execute(st20)
st21="INSERT INTO Car_Exteriors(Part,Price)VALUES('Set of 4 New Tyres',20000)"
cursor.execute(st21)
st22="INSERT INTO Car_Exteriors(Part,Price)VALUES('Engine Transmission Assembly',300000)"
mycon.commit()
st23="SELECT * FROM Car_Exteriors"
cursor.execute(st23)
data=cursor.fetchall()
for row in data:
    print(row)

cursor.execute("CREATE TABLE if not exists Car_Interiors(Part char(60) NOT NULL,Price decimal );")
st1="INSERT INTO Car_Interiors(Part,Price)VALUES('Steering Wheel Cover(Fabric,Art Leather Range)',850)"
cursor.execute(st1)
st2="INSERT INTO Car_Interiors(Part,Price)VALUES('Perfume Range',500)"
cursor.execute(st2)
st3="INSERT INTO Car_Interiors(Part,Price)VALUES('Cabin Floor Mat(Designer Mat)',2500)"
cursor.execute(st3)
st4="INSERT INTO Car_Interiors(Part,Price)VALUES('Child Seat-KA500 for upto 27kg weight',9000)"
cursor.execute(st4)
st5="INSERT INTO Car_Interiors(Part,Price)VALUES('Door Sill Guard',900)"
cursor.execute(st5)
st6="INSERT INTO Car_Interiors(Part,Price)VALUES('Set of all 4 Door Power Window',13500)"
cursor.execute(st6)
st7="INSERT INTO Car_Interiors(Part,Price)VALUES('Rear Parcel Tray',1900)"
cursor.execute(st7)
st8="INSERT INTO Car_Interiors(Part,Price)VALUES('Oval Speaker',4500)"
cursor.execute(st8)
st9="INSERT INTO Car_Interiors(Part,Price)VALUES('Integrated Music System-Nippon(Only Head Unit)',16000)"
cursor.execute(st9)
st10="INSERT INTO Car_Interiors(Part,Price)VALUES('Pure Leather Seat Cover',30000)"
cursor.execute(st10)
st11="SELECT * FROM Car_Interiors"
cursor.execute(st11)
data=cursor.fetchall()
for row in data:
    print(row)

cursor.execute("CREATE TABLE if not exists Cost_Estimate(Category char(60),Estimate char(20));")
st1="INSERT INTO Cost_Estimate(Category,Estimate)VALUES('Materials','47%')"
cursor.execute(st1)
st2="INSERT INTO Cost_Estimate(Category,Estimate)VALUES('Direct Labour','21%')"
cursor.execute(st2)
st3="INSERT INTO Cost_Estimate(Category,Estimate)VALUES('Administration','10%')"
cursor.execute(st3)
st4="INSERT INTO Cost_Estimate(Category,Estimate)VALUES('Others(including advetising)','7%')"
cursor.execute(st4)
st5="INSERT INTO Cost_Estimate(Category,Estimate)VALUES('R&D','6%')"
cursor.execute(st5)
st6="INSERT INTO Cost_Estimate(Category,Estimate)VALUES('Depreciation','6%')"
cursor.execute(st6)
st7="INSERT INTO Cost_Estimate(Category,Estimate)VALUES('Logistics','3%')"
cursor.execute(st7)
st8="SELECT * FROM Cost_Estimate"
cursor.execute(st8)
data=cursor.fetchall()
for row in data:
    print(row)

cursor.execute("CREATE TABLE if not exists Employee_Hierarchy(Company_Level char(70),Designation  char(70),Vacancy char(20));")
st1="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Administrative Automobiles','President','No')"
cursor.execute(st1)
st2="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Administrative Automobiles','CTO','No')"
cursor.execute(st2)
st3="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Administrative Automobiles','Sales Professional','Yes')"
cursor.execute(st3)
st4="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Administrative Automobiles','Finance Professional','Yes')"
cursor.execute(st4)
st5="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Administrative Automobiles','Finance Sales Representative','Yes')"
cursor.execute(st5)
st6="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Administrative Automobiles','Sr. Technology Specialist','No')"
cursor.execute(st6)
st7="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Administrative Automobiles','Chief Administration Manager','No')"
cursor.execute(st7)
st8="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Administrative Automobiles','Research Head','No')"
cursor.execute(st8)
st9="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Administrative Automobiles','Development Manager','No')"
cursor.execute(st9)
st10="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Executive Automobiles','Sr.Technology Engineer','No')"
cursor.execute(st10)
st11="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Executive Automobiles','Hardware Systems Manager','No')"
cursor.execute(st11)
st12="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Executive Automobiles','Senior Manager','Yes')"
cursor.execute(st12)
st13="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Executive Automobiles','Senior Technology Analyst','Yes')"
cursor.execute(st13)
st14="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Executive Automobiles','Tyre and Service Provider','No')"
cursor.execute(st14)
st15="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Executive Automobiles','Construction Vehicle Repair','No')"
cursor.execute(st15)
st16="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Executive Automobiles','Tyre Technician','No')"
cursor.execute(st16)
st17="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Executive Automobiles','Maintainence Technician','No')"
cursor.execute(st17)
st18="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Executive Automobiles','Auto Technician','No')"
cursor.execute(st18)
st19="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Executive Automobiles','Automotive Mechanic','Yes')"
cursor.execute(st19)
st20="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Executive Automobiles','Automobile Engineer','Yes')"
cursor.execute(st20)
st21="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Operational Automobiles','Automotive Mechanic Assistant','Yes')"
cursor.execute(st21)
st22="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Operational Automobiles','Owner Operator','No')"
cursor.execute(st22)
st23="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Operational Automobiles','Technology Analyst','No')"
cursor.execute(st23)
st24="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Operational Automobiles','Quality Supervisor','No')"
cursor.execute(st24)
st25="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Operational Automobiles','Automotive Supplier','No')"
cursor.execute(st25)
st26="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Operational Automobiles','Tyre Care Manager','No')"
cursor.execute(st26)
st27="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Operational Automobiles','Washer and Vehicle Detailer','Yes')"
cursor.execute(st27)
st28="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Operational Automobiles','Automobile Dealer Clerk','Yes')"
cursor.execute(st28)
st29="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Operational Automobiles','Washer','Yes')"
cursor.execute(st29)
st30="INSERT INTO Employee_Hierarchy(Company_Level,Designation,Vacancy)VALUES('Operational Automobiles','Fueler','Yes')"
cursor.execute(st30)
mycon.commit()
st31="SELECT * FROM Employee_Hierarchy"
cursor.execute(st31)
data=cursor.fetchall()
for row in data:
    print(row)

cursor.execute("CREATE TABLE if not exists Engine_Model(Type char(30) NOT NULL,Model_No char(30)NOT NULL PRIMARY KEY,Engine_Capacity char(30) NOT NULL,Price decimal);")
st1="INSERT INTO Engine_Model(Type,Model_No,Engine_Capacity,Price)VALUES('Petrol','C4A','2000',50000)"
cursor.execute(st1)
st2="INSERT INTO Engine_Model(Type,Model_No,Engine_Capacity,Price)VALUES('Petrol','C4DHS','1000',100000)"
cursor.execute(st2)
st3="INSERT INTO Engine_Model(Type,Model_No,Engine_Capacity,Price)VALUES('Diesel','HX5','2000',150000)"
cursor.execute(st3)
st4="SELECT * FROM Engine_Model"
cursor.execute(st4)
data=cursor.fetchall()
for row in data:
    print(row)

cursor.execute("CREATE TABLE if not exists Freqbought(Category_No integer,Category_Name char(60),Accesory_Name char(60));")
st1="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(1,'General Utility','Auto Dimming IRVM Mirror')"
cursor.execute(st1)
st2="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(2,'Safety and Security','Gear Lock')"
cursor.execute(st2)
st3="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(2,'Safety and Security','MGA Front Fog Light Pair')"
cursor.execute(st3)
st4="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(2,'Safety and Security','Nippon Reverse Parking Sensor')"
cursor.execute(st4)
st5="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(3,'Music System','Sony XAV65 Touchscreen')"
cursor.execute(st5)
st6="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(3,'Music System','Rear Seat Entertainmnet Android')"
cursor.execute(st6)
st7="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(4,'Car Interior','Child Seat-KA500 for upto 27kg weight')"
cursor.execute(st7)
st8="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(4,'Car Interior','Set of all 4 Door Power Window')"
cursor.execute(st8)
st9="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(4,'Car Interior','Pure Leather Seat Cover')"
cursor.execute(st9)
st10="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(5,'Car Exterior','Mud Flaps(Set of 4)')"
cursor.execute(st10)
st11="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(5,'Car Exterior','Sun Door Visor-all 4 windows')"
cursor.execute(st11)
st12="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(5,'Car Exterior','Roof Luggage Carrier')"
cursor.execute(st12)
st13="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(5,'Car Exterior','Fog Light')"
cursor.execute(st13)
st14="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(5,'Car Exterior','Battery')"
cursor.execute(st14)
st15="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(5,'Car Exterior','Side Indicator Bulb')"
cursor.execute(st15)
st16="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(5,'Car Exterior','Side Window Glass')"
cursor.execute(st16)
st17="INSERT INTO Freqbought(Category_No,Category_Name,Accesory_Name)VALUES(5,'Car Exterior','AC Cooling Coil')"
cursor.execute(st17)
st18="SELECT * FROM Freqbought"
cursor.execute(st18)
data=cursor.fetchall()
for row in data:
    print(row)

cursor.execute("CREATE TABLE if not exists General_Utility(Part char(60) NOT NULL,Price decimal);")
st1="INSERT INTO General_Utility(Part,Price)VALUES('Auto Dimming IRVM Mirror',6500)"
cursor.execute(st1)
st2="INSERT INTO General_Utility(Part,Price)VALUES('Sony XAV Ax5000 Touchscreen Music System',24990)"
cursor.execute(st2)
st3="INSERT INTO General_Utility(Part,Price)VALUES('Stylish Dual Tone Alloy Wheels',28000)"
cursor.execute(st3)
st4="SELECT * FROM General_Utility"
cursor.execute(st4)
data=cursor.fetchall()
for row in data:
    print(row)


cursor.execute("CREATE TABLE if not exists Inhouse_Machining(Part char(40) NOT NULL,Price decimal,Material_From char(50));")
st1="INSERT INTO Inhouse_Machining(Part,Price,Material_From)VALUES('Cylinder Block',1500,'Rico Auto')"
cursor.execute(st1)
st2="INSERT INTO Inhouse_Machining(Part,Price,Material_From)VALUES('Cylinder Head',1100,'Alicon Casting Pvt Ltd')"
cursor.execute(st2)
st3="INSERT INTO Inhouse_Machining(Part,Price,Material_From)VALUES('Crank Shaft',800,'Kalyani Forge')"
cursor.execute(st3)
st4="INSERT INTO Inhouse_Machining(Part,Price,Material_From)VALUES('Cam Shaft',400,'Mhale')"
cursor.execute(st4)
st5="SELECT * FROM Inhouse_Machining"
cursor.execute(st5)
data=cursor.fetchall()
for row in data:
    print(row)



cursor.execute("CREATE TABLE if not exists Main_Body(Part char(40) NOT NULL,Material_From char(50));")
st1="INSERT INTO Main_Body(Part,Material_From)VALUES('Bumper','Valeo Plastics')"
cursor.execute(st1)
st2="INSERT INTO Main_Body(Part,Material_From)VALUES('Rear and Front Lamps/Fog Lamps','Valeo Headlights')"
cursor.execute(st2)
st3="INSERT INTO Main_Body(Part,Material_From)VALUES('Dashboard','Minda')"
cursor.execute(st3)
st4="INSERT INTO Main_Body(Part,Material_From)VALUES('Window Pane/Windshield and Rear Glass','Safex/Ashai')"
cursor.execute(st4)
st5="INSERT INTO Main_Body(Part,Material_From)VALUES('Battery','Exide')"
cursor.execute(st5)
st6="SELECT * FROM Main_Body"
cursor.execute(st6)
data=cursor.fetchall()
for row in data:
    print(row)

cursor.execute("CREATE TABLE if not exists Music_System(Part char(60) NOT NULL,Price decimal);")
st1="INSERT INTO Music_System(Part,Price)VALUES('Sony XAV65 Touchscreen AV',15990)"
cursor.execute(st1)
st2="INSERT INTO Music_System(Part,Price)VALUES('JVC V10 KW',17990)"
cursor.execute(st2)
st3="INSERT INTO Music_System(Part,Price)VALUES('Kenwood DDX 3035',18490)"
cursor.execute(st3)
st4="INSERT INTO Music_System(Part,Price)VALUES('Coaxial Speaker(Set of 4 speakers)',8000)"
cursor.execute(st4)
st5="INSERT INTO Music_System(Part,Price)VALUES('Component Speaker Pair(Set of 4 Speakers)',15000)"
cursor.execute(st5)
st6="INSERT INTO Music_System(Part,Price)VALUES('Amplifier Range',27990)"
cursor.execute(st6)
st7="INSERT INTO Music_System(Part,Price)VALUES('Rear Seat Entertainment Android',19990)"
cursor.execute(st7)
st8="SELECT * FROM Music_System"
cursor.execute(st8)
data=cursor.fetchall()
for row in data:
    print(row)

cursor.execute("CREATE TABLE if not exists Mycart(Name char(40) UNIQUE,Category_No integer,Category_Name char(60),Accessory_Name char(60),Quantity integer);")

cursor.execute("CREATE TABLE if not exists Mycart1(Category_No integer,Category_Name char(60),Accessory_Name char(60),Quantity integer DEFAULT'1');")

cursor.execute("CREATE TABLE if not exists Our_Stores(Telephone_No integer,Address char(70),Sales_Manager char(40),Area char(50));")
st1="INSERT INTO Our_Stores(Telephone_No,Address,Sales_Manager,Area)VALUES(201223675,'Shop 3 Alandi Road Kirkee,Pune-411028','Suresh Verma','Kirkee')"
cursor.execute(st1)
st2="INSERT INTO Our_Stores(Telephone_No,Address,Sales_Manager,Area)VALUES(209087864,'42/43 Shivpeth Opp. Shankar Road Pawar Seatcorner,Pune-411001','Rahul Sharma','Shivpeth')"
cursor.execute(st2)
st3="INSERT INTO Our_Stores(Telephone_No,Address,Sales_Manager,Area)VALUES(207889901,'Shop No.1 Mayur Prasth,Pimpri Chowk,ICICI Bank,Pune-413456','Ganesh Yadhav','Pimpri')"
cursor.execute(st3)
st4="INSERT INTO Our_Stores(Telephone_No,Address,Sales_Manager,Area)VALUES(203456897,'Shop 1 Opp. Bharat Restaurant,Hinjewadi,Pune-411030','Amit Kumar','Hinjewadi')"
cursor.execute(st4)
st5="INSERT INTO Our_Stores(Telephone_No,Address,Sales_Manager,Area)VALUES(206543290,'Sangharsh Chowk,Chandan Nagar,Pune-410012','Sachin Shetty','Chandan Nagar')"
cursor.execute(st5)
st6="SELECT * FROM Our_Stores"
cursor.execute(st6)
data=cursor.fetchall()
for row in data:
    print(row)

cursor.execute("CREATE TABLE if not exists Report_battery(Date_of_Delievery date,QOH integer,Production_Requirement integer,Expected_Defective_Piece integer,Reorder_Level integer,Expected_Delievery_Date date);")
st1="INSERT INTO Report_battery(Date_of_Delievery,QOH,Production_Requirement,Expected_Defective_Piece ,Reorder_Level,Expected_Delievery_Date)VALUES('2020-12-15',400,1200,15,1215,'2020-12-17')"
cursor.execute(st1)
st2="INSERT INTO Report_battery(Date_of_Delievery,QOH,Production_Requirement,Expected_Defective_Piece ,Reorder_Level,Expected_Delievery_Date)VALUES('2020-12-17',400,1000,10,1010,'2020-12-19')"
cursor.execute(st2)
st3="INSERT INTO Report_battery(Date_of_Delievery,QOH,Production_Requirement,Expected_Defective_Piece ,Reorder_Level,Expected_Delievery_Date)VALUES('2020-12-19',400,1600,20,1620,'2020-12-21')"
cursor.execute(st3)
st4="INSERT INTO Report_battery(Date_of_Delievery,QOH,Production_Requirement,Expected_Defective_Piece ,Reorder_Level,Expected_Delievery_Date)VALUES('2020-12-21',400,1600,20,1620,'2020-12-23')"
cursor.execute(st4)
st5="INSERT INTO Report_battery(Date_of_Delievery,QOH,Production_Requirement,Expected_Defective_Piece ,Reorder_Level,Expected_Delievery_Date)VALUES('2020-12-23',400,1000,10,1010,'2020-12-25')"
cursor.execute(st5)
st6="SELECT * FROM Report_battery"
cursor.execute(st6)
data=cursor.fetchall()
for row in data:
    print(row)

cursor.execute("CREATE TABLE if not exists Report_cb(Date_of_Delievery date,Minimum_Stock integer,QOH integer,Production_Requirement integer,Expected_Defective_Piece integer,Reorder_Level integer,Closing_Stock integer,Expected_Delievery_Date date);")
st1="INSERT INTO Report_cb(Date_of_Delievery,Minimum_Stock,QOH,Production_Requirement,Expected_Defective_Piece ,Reorder_Level,Closing_Stock,Expected_Delievery_Date)VALUES('2020-12-01',500,1500,2000,10,610,0,'2020-12-07')"
cursor.execute(st1)
st2="INSERT INTO Report_cb(Date_of_Delievery,Minimum_Stock,QOH,Production_Requirement,Expected_Defective_Piece ,Reorder_Level,Closing_Stock,Expected_Delievery_Date)VALUES('2020-12-07',500,110,2500,29,3020,500,'2020-12-14')"
cursor.execute(st2)
st3="INSERT INTO Report_cb(Date_of_Delievery,Minimum_Stock,QOH,Production_Requirement,Expected_Defective_Piece ,Reorder_Level,Closing_Stock,Expected_Delievery_Date)VALUES('2020-12-14',500,500,3000,30,3030,500,'2020-12-21')"
cursor.execute(st3)
st4="INSERT INTO Report_cb(Date_of_Delievery,Minimum_Stock,QOH,Production_Requirement,Expected_Defective_Piece ,Reorder_Level,Closing_Stock,Expected_Delievery_Date)VALUES('2020-12-21',500,500,1500,15,1515,500,'2020-12-25')"
cursor.execute(st4)
st6="SELECT * FROM Report_cb"
cursor.execute(st6)
data=cursor.fetchall()
for row in data:
    print(row)


cursor.execute("CREATE TABLE if not exists Report_flywheel(Date_of_Delievery date,QOH integer,Production_Requirement integer,Expected_Defective_Piece integer,Reorder_Level integer,Expected_Delievery_Date date);")
st1="INSERT INTO Report_flywheel(Date_of_Delievery,QOH,Production_Requirement,Expected_Defective_Piece ,Reorder_Level,Expected_Delievery_Date)VALUES('2020-12-15',400,800,10,810,'2020-12-17')"
cursor.execute(st1)
st2="INSERT INTO Report_flywheel(Date_of_Delievery,QOH,Production_Requirement,Expected_Defective_Piece ,Reorder_Level,Expected_Delievery_Date)VALUES('2020-12-17',400,1200,15,1251,'2020-12-19')"
cursor.execute(st2)
st3="INSERT INTO Report_flywheel(Date_of_Delievery,QOH,Production_Requirement,Expected_Defective_Piece ,Reorder_Level,Expected_Delievery_Date)VALUES('2020-12-19',400,1200,15,1251,'2020-12-21')"
cursor.execute(st3)
st4="INSERT INTO Report_flywheel(Date_of_Delievery,QOH,Production_Requirement,Expected_Defective_Piece ,Reorder_Level,Expected_Delievery_Date)VALUES('2020-12-21',400,1000,10,1010,'2020-12-23')"
cursor.execute(st4)
st5="INSERT INTO Report_flywheel(Date_of_Delievery,QOH,Production_Requirement,Expected_Defective_Piece ,Reorder_Level,Expected_Delievery_Date)VALUES('2020-12-23',400,800,10,810,'2020-12-25')"
cursor.execute(st5)
st6="SELECT * FROM Report_flywheel"
cursor.execute(st6)
data=cursor.fetchall()
for row in data:
    print(row)

cursor.execute("CREATE TABLE if not exists Safety_Security(Part char(60) NOT NULL,Price decimal);")
st1="INSERT INTO Safety_Security(Part,Price)VALUES('Gear Lock',1600)"
cursor.execute(st1)
st2="INSERT INTO Safety_Security(Part,Price)VALUES('MGA Front Fog Light Pair',4000)"
cursor.execute(st2)
st3="INSERT INTO Safety_Security(Part,Price)VALUES('Nippon Reverse Parking Sensor',4000)"
cursor.execute(st3)
st4="INSERT INTO Safety_Security(Part,Price)VALUES('Rear View Camera',8500)"
cursor.execute(st4)
st5="SELECT * FROM Safety_Security"
cursor.execute(st5)
data=cursor.fetchall()
for row in data:
    print(row)


cursor.execute("CREATE TABLE if not exists Supplier(Supplier_Name char(60),Term_of_Contract char(40),Expiry_Date date,Supplier_Head char(60),Phoneno char(40),Mail_Address char(60));")
st1="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Rico Auto','2 years','2022-01-01','Anurag Modi',9850345671,'anurag07@rico.ac.in')"
cursor.execute(st1)
st2="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Kalyani Forge','4 years','2023-12-05','Shreyas Redddy',9987905623,'sreddy07@Kforge.ac.in')"
cursor.execute(st2)
st3="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Mhale','1 years','2021-12-01','Nishant Kumar',9456793244,'nishant@gmail.com')"
cursor.execute(st3)
st4="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Bajaj Motors','1 years','2021-12-15','Pradyun Das',9564390811,'pradyun@gmail.com')"
cursor.execute(st4)
st5="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('India Piston','2 years','2021-12-01','Vineet Sharma',9080765644,'vineet@gmail.com')"
cursor.execute(st5)
st6="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Shakti Auto','5 years','2024-01-21','Anubhav Gupta',9083467210,'anubhav@gmail.com')"
cursor.execute(st6)
st7="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Novaris','4 years','2023-01-20','Chetan Jain',9234561898,'chetan@gmail.com')"
cursor.execute(st7)
st8="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Metaldyne','3 years','2022-06-20','Shivansh Sethi',9995566784,'shivansh@gmail.com')"
cursor.execute(st8)
st9="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Alicon Casting Pvt Ltd','1.5 years','2021-06-15','Arjun Shah',9707722435,'arjun@alicon.ac.in')"
cursor.execute(st9)
st10="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Mhale Filters','2 years','2022-01-15','Ayush Bhagat',9231567021,'ayush@mfilters.ac.in')"
cursor.execute(st10)
st11="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Rhane Engine Valves','2 years','2022-01-01','Aryan Dua',9890765213,'aryan@gmail.com')"
cursor.execute(st11)
st12="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('TVS Electric','3 years','2023-01-01','Krish Gupta',9658902134,'krish@gmail.com')"
cursor.execute(st12)
st13="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Wheels India Ltd','5 years','2024-12-01','Kalpesh Krishna',9899342567,'kalpesh@gmail.com')"
cursor.execute(st13)
st14="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Valeo Plastics','4 years','2023-12-01','Vikas Walke',9234517890,'vikas@gmail.com')"
cursor.execute(st14)
st15="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Minda','3 years','2022-11-15','Sujeet Shah',9999675431,'sujeet@minda.ac.in')"
cursor.execute(st15)
st16="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Safex','1 years','2021-11-15','Sudip Nag',9966734210,'sudip@safex.ac.in')"
cursor.execute(st16)
st17="INSERT INTO Supplier(Supplier_Name,Term_of_Contract,Expiry_Date,Supplier_Head,Phoneno,Mail_Address)VALUES('Exide','1 years','2021-11-15','Siddharth Modi',9956432901,'siddharth@exide.ac.in')"
cursor.execute(st17)
st18="SELECT * FROM Supplier"
cursor.execute(st18)
data=cursor.fetchall()
for row in data:
    print(row)


cursor.execute("CREATE TABLE if not exists Transmission(Part char(40) NOT NULL,Quantity_per_car integer);")
st1="INSERT INTO Transmission(Part,Quantity_per_car)VALUES('Gears',5)"
cursor.execute(st1)
st2="INSERT INTO Transmission(Part,Quantity_per_car)VALUES('Synchro rings',5)"
cursor.execute(st2)
st3="INSERT INTO Transmission(Part,Quantity_per_car)VALUES('Trans Case',1)"
cursor.execute(st3)
st4="INSERT INTO Transmission(Part,Quantity_per_car)VALUES('Clutch Housing',1)"
cursor.execute(st4)
st5="INSERT INTO Transmission(Part,Quantity_per_car)VALUES('Hubs',5)"
cursor.execute(st5)
st6="INSERT INTO Transmission(Part,Quantity_per_car)VALUES('Sleeve',5)"
cursor.execute(st6)
st7="INSERT INTO Transmission(Part,Quantity_per_car)VALUES('Shifter Fork',3)"
cursor.execute(st7)
st8="INSERT INTO Transmission(Part,Quantity_per_car)VALUES('Input Shaft',1)"
cursor.execute(st8)
st9="INSERT INTO Transmission(Part,Quantity_per_car)VALUES('Output Shaft',1)"
cursor.execute(st9)
st10="SELECT * FROM Transmission"
cursor.execute(st10)
data=cursor.fetchall()
for row in data:
    print(row)


cursor.execute("CREATE TABLE if not exists Tyres(Part char(40) NOT NULL,Material_From char(50));")
st1="INSERT INTO Tyres(Part,Material_From)VALUES('Rim','Wheels India Ltd')"
cursor.execute(st1)
st2="INSERT INTO Tyres(Part,Material_From)VALUES('Tyre Tube','JK Tyres,MRF,CEAT Tyres')"
cursor.execute(st2)
st3="SELECT * FROM Tyres"
cursor.execute(st10)
data=cursor.fetchall()
for row in data:
    print(row)


    
mycon.close()

