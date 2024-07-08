from tabulate import _table_formats, tabulate
from datetime import datetime
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="ananya",database="Automobiles")
cursor=mycon.cursor()
st="delete from MyCart1"
cursor.execute(st)
mycon.commit()
name=input("Enter your Name:")
print(" ")
print("*"*133)
print(" "*30,"WELCOME TO AUTHENTIC AUTOMOBILE MANUFACTURERS AND DEALERS-AAMD,", name,"!!")
print("*"*133)
print(" ")
now=datetime.now()
print("Entry Date and Time:",now)
print(" ")
print("Press 1 if you are an Admin")
print("Press 2 if you are a Customer")
choice=int(input("Enter your choice:"))
print(" ")
def ourStores(selectedarea):
    if selectedarea==1:
        cursor=mycon.cursor()
        st="SELECT Address FROM Our_Stores WHERE Area='{}'".format("Kirkee")
        cursor.execute(st)
        data=cursor.fetchall()
        for row in data:
            print(row)
            
    elif selectedarea==2:
        cursor=mycon.cursor()
        st="SELECT Address FROM Our_Stores WHERE Area='{}'".format("Shivpeth")
        cursor.execute(st)
        data=cursor.fetchall()
        for row in data:
            print(row)
            
    elif selectedarea==3:
        cursor=mycon.cursor()
        st="SELECT Address FROM Our_Stores WHERE Area='{}'".format("Pimpri")
        cursor.execute(st)
        data=cursor.fetchall()
        for row in data:
            print(row)

    elif selectedarea==4:
        cursor=mycon.cursor()
        st="SELECT Address FROM Our_Stores WHERE Area='{}'".format("Hinjewadi")
        cursor.execute(st)
        data=cursor.fetchall()
        for row in data:
            print(row)

    elif selectedarea==5:
        cursor=mycon.cursor()
        st="SELECT Address FROM Our_Stores WHERE Area='{}'".format("Chandan Nagar")
        cursor.execute(st)
        data=cursor.fetchall()
        for row in data:
            print(row)
                    

if choice==1:
    empemail=input("Enter your official Email-ID:")
    desg=input("Enter your Designation:")
    print(" ")
    more1=1
    r=1
    while more1==1:
        print("Press 1 for Inhouse Production Chart")
        print("Press 2 for Supplier Details")
        print("Press 3 for Altering Records")
        print("Press 4 for Production Cost Estimate")
        print("Press 5 for Employee Hirearchy")
        print("Press 6 to  View Reports")
        choice6=int(input("Enter your choice:"))
        print(" ")

        if choice6==1:
            more1=2
            cursor=mycon.cursor()
            table = [["Gears",5], ["Synchro rings",5], ["Trans case", 1],["Clutch housing",1], ["Hubs",5], ["Sleeve", 5],
                     ["Shifter Fork", 3],["Input Shaft",1], ["Output Shaft",1]]
            headers = ["Parts", "Quantity_per_car"]
            formatl=['fancy_grid',]
            for f in formatl:
                print(tabulate(table, headers, tablefmt=f))
            print("***Total Cost Rs 20,000 per car***")
            print("Production per day=400 cars")
            table = [["Cylinder Block",1500], ["Cylinder Head",1100], ["Crank Shaft", 800],["Cam Shaft",400]]
            headers = ["Parts", "Price"]
            formatl=['fancy_grid',]
            for f in formatl:
                print(tabulate(table, headers, tablefmt=f))
            more1=int(input("Would you like to go to another section? If yes, press 1 else enter 2:"))

        elif choice6==2:
            more1=2
            table = [["Rico Auto","Anurag Modi",9850345671], ["Kalyani Forge","Shreyas Reddy",9987905623],
                     ["Mhale","Nishant Kumar",9456793244],["Bajaj Motors","Pradyun Das",9564390811],
                     ["India Piston","Vineet Sharma",9080765644], ["Shakti Auto","Anubhav Gupta",9083467210],
                     ["Novaris","Chetan Jain",9234561898],["Metaldyne","Shivansh Sethi",9995566784],
                     ["Alicon Casting Pvt Ltd","Arjun Shah",9707722435],["Mhale Filters","Ayush Bhagat",9231567021],
                     ["Rhane Engine Valves","Aryan Dua",9890765213],["TVS Electric","Krish Gupta",9658902134],
                     ["Wheels India Ltd","Kalpesh Krishna",9899342567],["Valeo Plastics","Vikas Walke",9234517890],
                     ["Minda","Sujjet Shah",9999675431],["Safex","Sudip Nag",9966734210],["Exide","Siddharth Modi",9956432901]]
            headers = ["Supplier Name", "Supplier Head","Phone No."]
            formatl=['fancy_grid',]
            for f in formatl:
                print(tabulate(table, headers, tablefmt=f))
            
            choice7=int(input("Enter 1 to Email else enter 2:"))
            if choice7==1:
                suppname=input("Enter Supplier's Name to be emailed:")
                print("Press 1 for  Asking for update on delivery of next batch")
                print("Press 2 for Complaining of the poor quality of parts delivered.")
                print("Press 3 for For renewal of contract")
                print("Press 4 for Bi-monthly meetings")
                choice8=int(input("Enter your choice:"))
                print(" ")
                if choice8==1:
                    print("="*133)
                    print("From:",empemail)
                    cursor=mycon.cursor()
                    st1="SELECT Mail_Address FROM Supplier WHERE Supplier_Name='{}'".format(suppname)
                    cursor.execute(st1)
                    data=cursor.fetchall()
                    for row in data:
                        c=row
                    mycon.commit()
                    print("To:",c)
                    print(" ")
                    print("Subject:Updates on the next Batch")
                    print(" ")
                    cursor=mycon.cursor()
                    st1="SELECT Supplier_Head FROM Supplier WHERE Supplier_Name='{}'".format(suppname)
                    cursor.execute(st1)
                    data=cursor.fetchall()
                    for row in data:
                        c=row
                    print("Dear",c,",")
                    print("Request you to update on the parts for the next 2 weeks at the earliest.") 
                    print("Kindly attach the quality report and part images!")
                    print(" ")
                    print("Regards,")
                    print(name)
                    print(desg)
                    print("="*133)
                elif choice8==2:
                    print("="*133)
                    print("From:",empemail)
                    cursor=mycon.cursor()
                    st1="SELECT Mail_Address FROM Supplier WHERE Supplier_Name='{}'".format(suppname)
                    cursor.execute(st1)
                    data=cursor.fetchall()
                    for row in data:
                        c=row
                    mycon.commit()
                    print("To:",c)
                    print(" ")
                    print("Subject:Complaining about poor quality of parts")
                    print(" ")
                    cursor=mycon.cursor()
                    st1="SELECT Supplier_Head FROM Supplier WHERE Supplier_Name='{}'".format(suppname)
                    cursor.execute(st1)
                    data=cursor.fetchall()
                    for row in data:
                        c=row
                    print("Dear",c,",")
                    print("The batch received yesterday was not at par with what has been agreed upon in our contract."
                          "These parts can't be used in the making of our cars!At AAMD,we strive to serve our customers"
                          "to the highest degree.") 
                    print("Request you to revoke the batch and send a new one at the earliest and setup a meeting to "
                          "discuss the future of our contract as soon as possible.")
                    print(" ")
                    print("Regards,")
                    print(name)
                    print(desg)
                    print("="*133)
                
                elif choice8==3:
                    print("="*133)
                    print("From:",empemail)
                    cursor=mycon.cursor()
                    st1="SELECT Mail_Address FROM Supplier WHERE Supplier_Name='{}'".format(suppname)
                    cursor.execute(st1)
                    data=cursor.fetchall()
                    for row in data:
                        c=row
                    mycon.commit()
                    print("To:",c)
                    print(" ")
                    print("Subject: Renewal of our contract")
                    print(" ")
                    cursor=mycon.cursor()
                    st1="SELECT Supplier_Head FROM Supplier WHERE Supplier_Name='{}'".format(suppname)
                    cursor.execute(st1)
                    data=cursor.fetchall()
                    for row in data:
                        c=row
                    print("Dear",c,",")
                    cursor=mycon.cursor()
                    st1="SELECT Expiry_Date FROM Supplier WHERE Supplier_Name='{}'".format(suppname)
                    cursor.execute(st1)
                    data=cursor.fetchall()
                    for row in data:
                        c1=row
                    print("Our contract terminates on ",c1,". AAMD was pleased collaborating with you and looks forward "
                          "to renewing our contract and strengthening the relations between AAMD &",suppname,".") 
                    print("Call back to setup a meeting in the near future.")
                    print(" ")
                    print("Regards,")
                    print(name)
                    print(desg)
                    print("="*133)
                elif choice8==4:
                    print(" ")
                    print("="*133)
                    print("From:",empemail)
                    cursor=mycon.cursor()
                    st1="SELECT Mail_Address FROM Supplier WHERE Supplier_Name='{}'".format(suppname)
                    cursor.execute(st1)
                    data=cursor.fetchall()
                    for row in data:
                        c=row
                    mycon.commit()
                    print("To:",c)
                    print(" ")
                    print("Subject: Renewal of our contract")
                    print(" ")
                    cursor=mycon.cursor()
                    st1="SELECT Supplier_Head FROM Supplier WHERE Supplier_Name='{}'".format(suppname)
                    cursor.execute(st1)
                    data=cursor.fetchall()
                    for row in data:
                        c=row
                    print("Dear",c,",")
                    print("Call back to setup the venue and time for our next bi-weekly meeting.")
                    print("Agenda:") 
                    print("1)Ordering parts for the next 2 weeks")
                    print("2)Reviewing previous batch")
                    print("3)Suggested cost alterations ")
                    print(" ")
                    print("Regards,")
                    print(name)
                    print(desg)
                    print("="*133)
                     
                more1=int(input("Would you like to go to another section? If yes, press 1 else enter 2:"))

        elif choice6==3:
            more1=2
            print("Select the table you would like to edit")
            print("1)Engine Model")
            print("2)Transmission")
            print("3)Inhouse Machinig of engine parts")
            print("4)Bill of Materials")
            print("5)Tyres")
            print("6)Main Body")
            choice9=int(input("Enter your choice:"))
            print(" ")
            print("What changes would you like to do in the database?")
            while r==1:
                print("1)Delete records")
                print("2)Insert records")
                print("3)Update records")
                choice10=int(input("Enter your choice"))
                print(" ")
                if choice9==1:
                    cursor=mycon.cursor()
                    st="select * from Engine_Model"
                    cursor.execute(st)
                    data=cursor.fetchall()
                    for row in data:
                        print(row)
                    if choice10==1:
                        del1=input("Enter the Model No. that you would like to delete:")
                        cursor=mycon.cursor()
                        st1="DELETE FROM Engine_Model WHERE Model_No='%s'" % (del1)
                        cursor.execute(st1)
                        mycon.commit()
                        print("Record Successfully Deleted.")
                        print(" ")
                    
                    elif choice10==2:
                        etype=input("Enter the type(Petrol/Disesel):")
                        modelno=input("Enter the model number:")
                        enginecap=input("Enter the engine capacity:")
                        price=int(input("Enter the price:"))
                        cursor=mycon.cursor()
                        st1 = "INSERT INTO Engine_Model(Type,Model_No,Engine_Capacity,Price) VALUES('{}','{}','{}','{}')".format(etype,modelno,enginecap,price)
                        cursor.execute(st1)
                        mycon.commit()
                        print("Record Successfully Inserted")
                        print(" ")

                    elif choice10==3:
                        choice11=int(input("Press 1 to change the engine capacity and press 2 to change the price:"))
                        if choice11==1:
                            newvalue=input("Enter the new engine capacity:")
                            modelno=input("Enter the model number:")
                            cursor=mycon.cursor()
                            st="""UPDATE Engine_Model SET Engine_Capacity=%s WHERE Model_No=%s """
                            inputdata=(newvalue,modelno)
                            cursor.execute(st,inputdata)
                            mycon.commit()
                            print("Record Successfully Updated")
                            print(" ")
                            
                        elif choice11==2:
                            newvalue1=int(input("Enter the new price:"))
                            modelno=input("Enter the model number:")
                            cursor=mycon.cursor()
                            st="""UPDATE Engine_Model SET Price=%s WHERE Model_No=%s"""
                            inputdata=(newvalue1,modelno)
                            cursor.execute(st,inputdata)
                            mycon.commit()
                            print("Record Successfully Updated")
                    r=int(input("Enter 1 to further edit this table else enter 2:"))
                    if r==2:
                        continue

                elif choice9==2:
                    cursor=mycon.cursor()
                    st="select * from Transmission"
                    cursor.execute(st)
                    data=cursor.fetchall()
                    for row in data:
                        print(row)
                    if choice10==1:
                        del1=input("Enter the Part Name that you would like to delete:")
                        cursor=mycon.cursor()
                        st1="DELETE FROM Transmission WHERE Part='%s'" % (del1)
                        cursor.execute(st1)
                        mycon.commit()
                        print("Record Successfully Deleted.")
                        print(" ")
                    
                    elif choice10==2:
                        part=input("Enter the part name:")
                        quantity=int(input("Enter the quantity:"))
                        cursor=mycon.cursor()
                        st1 = "INSERT INTO Transmission(Part,Quantity_per_car) VALUES('{}','{}')".format(part,quantity)
                        cursor.execute(st1)
                        mycon.commit()
                        print("Record Successfully Inserted")
                        print(" ")

                    elif choice10==3:
                            quantity=int(input("Enter the new quantity:"))
                            partname=input("Enter the Part name:")
                            cursor=mycon.cursor()
                            st="""UPDATE Transmission SET Quantity_per_car=%s WHERE Part=%s"""
                            inputdata=(quantity,partname)
                            cursor.execute(st,inputdata)
                            mycon.commit()
                            print("Record Successfully Updated")
                            print(" ")
                            
                    r=int(input("Enter 1 to further edit this table else enter 2:"))
                    if r==2:
                        continue

                elif choice9==3:
                    cursor=mycon.cursor()
                    st="select * from Inhouse_Machining"
                    cursor.execute(st)
                    data=cursor.fetchall()
                    for row in data:
                        print(row)
                    if choice10==1:
                        del1=input("Enter the Part Name that you would like to delete:")
                        cursor=mycon.cursor()
                        st1="DELETE FROM Inhouse_Machining WHERE Part='%s'" % (del1)
                        cursor.execute(st1)
                        mycon.commit()
                        print("Record Successfully Deleted.")
                        print(" ")
                    
                    elif choice10==2:
                        part=input("Enter Part name:")
                        price=int(input("Enter the Price:"))
                        materialfrom=input("Enter the Supplier Name:")         
                        cursor=mycon.cursor()
                        st1 = "INSERT INTO Inhouse_Machining(Part,Price,Material_From) VALUES('{}','{}','{}')".format(part,price,materialfrom)
                        cursor.execute(st1)
                        mycon.commit()
                        print("Record Successfully Inserted")
                        print(" ")

                    elif choice10==3:
                        choice11=int(input("Press 1 to change the price and press 2 to update supplier name:"))
                        if choice11==1:
                            price=int(input("Enter the new Price:"))
                            part=input("Enter the part:")
                            cursor=mycon.cursor()
                            st="""UPDATE Inhouse_Machining SET Price=%s WHERE Part=%s """
                            inputdata=(price,part)
                            cursor.execute(st,inputdata)
                            mycon.commit()
                            print("Record Successfully Updated")
                            print(" ")
                            
                        elif choice11==2:
                            suppliername=input("Enter the Supplier Name:")
                            part=input("Enter the Part Name:")
                            cursor=mycon.cursor()
                            st="""UPDATE Inhouse_Machining SET Material_From=%s WHERE Part=%s"""
                            inputdata=(suppliername,part)
                            cursor.execute(st,inputdata)
                            mycon.commit()
                            print("Record Successfully Updated")
                            print(" ")
                            
                    r=int(input("Enter 1 to further edit this table else enter 2:"))
                    if r==2:
                        continue

                elif choice9==4:
                    cursor=mycon.cursor()
                    st="select * from Bill_of_Materials"
                    cursor.execute(st)
                    data=cursor.fetchall()
                    for row in data:
                        print(row)
                    if choice10==1:
                        del1=input("Enter the Part Name that you would like to delete:")
                        cursor=mycon.cursor()
                        st1="DELETE FROM Bill_of_Materials WHERE Part='%s'" % (del1)
                        cursor.execute(st1)
                        mycon.commit()
                        print("Record Successfully Deleted.")
                        print(" ")
                    
                    elif choice10==2:
                        part=input("Enter Part Name:")
                        materialfrom=input("Enter the Supplier Name:")
                        cursor=mycon.cursor()
                        st1 = "INSERT INTO Bill_of_Materials(Part,Material_From) VALUES('{}','{}')".format(part,materialfrom)
                        cursor.execute(st1)
                        mycon.commit()
                        print("Record Successfully Inserted")
                        print(" ")

                    elif choice10==3:
                        suppliername=input("Enter the Supplier Name:")
                        partname=input("Enter the Part name:")
                        cursor=mycon.cursor()
                        st="""UPDATE Bill_of_Materials SET Material_From=%s WHERE Part=%s"""
                        inputdata=(suppliername,partname)
                        cursor.execute(st,inputdata)
                        mycon.commit()
                        print("Record Successfully Updated")
                        print(" ")
                    r=int(input("Enter 1 to further edit this table else enter 2:"))
                    if r==2:
                        continue

                elif choice9==5:
                    cursor=mycon.cursor()
                    st="select * from Tyres"
                    cursor.execute(st)
                    data=cursor.fetchall()
                    for row in data:
                        print(row)
                    if choice10==1:
                        del1=input("Enter the Part Name that you would like to delete:")
                        cursor=mycon.cursor()
                        st1="DELETE FROM Tyres WHERE Parts='%s'" % (del1)
                        cursor.execute(st1)
                        mycon.commit()
                        print("Record Successfully Deleted.")
                        print(" ")
                    
                    elif choice10==2:
                        part=input("Enter Part name:")
                        materialfrom=input("Enter the Supplier Name:")         
                        cursor=mycon.cursor()
                        st1 = "INSERT INTO Tyres(Parts,Material_From) VALUES('{}','{}')".format(part,materialfrom)
                        cursor.execute(st1)
                        mycon.commit()
                        print("Record Successfully Inserted")
                        print(" ")

                    elif choice10==3:
                        suppliername=input("Enter the Supplier Name:")
                        partname=input("Enter the Part name:")
                        cursor=mycon.cursor()
                        st="""UPDATE Tyres SET Material_From=%s WHERE Parts=%s"""
                        inputdata=(suppliername,partname)
                        cursor.execute(st,inputdata)
                        mycon.commit()
                        print("Record Successfully Updated")
                        print(" ")
        
                    r=int(input("Enter 1 to further edit this table else enter 2:"))
                    if r==2:
                        continue

                elif choice9==6:
                    cursor=mycon.cursor()
                    st="select * from Main_body"
                    cursor.execute(st)
                    data=cursor.fetchall()
                    for row in data:
                        print(row)
                    if choice10==1:
                        del1=input("Enter the Part Name that you would like to delete:")
                        cursor=mycon.cursor()
                        st1="DELETE FROM Main_body WHERE Parts='%s'" % (del1)
                        cursor.execute(st1)
                        mycon.commit()
                        print("Record Successfully Deleted.")
                        print(" ")
                    
                    elif choice10==2:
                        part=input("Enter Part name:")
                        materialfrom=input("Enter the Supplier Name:")         
                        cursor=mycon.cursor()
                        st1 = "INSERT INTO Main_body(Parts,Material_From) VALUES('{}','{}')".format(part,materialfrom)
                        cursor.execute(st1)
                        mycon.commit()
                        print("Record Successfully Inserted")
                        print(" ")
            
                    elif choice10==3:
                        suppliername=input("Enter the Supplier Name:")
                        partname=input("Enter the Part name:")
                        cursor=mycon.cursor()
                        st="""UPDATE Main_body SET Material_From=%s WHERE Parts=%s"""
                        inputdata=(suppliername,partname)
                        cursor.execute(st,inputdata)
                        mycon.commit()
                        print("Record Successfully Updated")
                        print(" ")
        
                    r=int(input("Enter 1 to further edit this table else enter 2:"))
                    print(" ")
                    if r==2:
                        continue
            more1=int(input("Would you like to go to another section? If yes, press 1 else enter 2:"))
                    

        elif choice6==4:
            more1=2
            table = [["Materials","47%"], ["Direct Labour","21%"],["Administration","10%"],
                    ["Other(including advetisment)","7%"],["R&D","6%"],["Depreciation","6%"],["Logistics","3%"]]
            headers = ["Category","Percentage"]
            formatl=['fancy_grid',]
            for f in formatl:
                print(tabulate(table, headers, tablefmt=f))
            more1=int(input("Would you like to go to another section? If yes, press 1 else enter 2:"))

        elif choice6==5:
            table = [["Administrative Automobiles","President"],["Administrative Automobiles","CTO"],["Administrative Automobiles","Sales Professional"],
                    ["Administrative Automobiles","Finance Professional"],["Administrative Automobiles","Finance Sales Representative"],
                    ["Administrative Automobiles","Sr. Technology Specialist"],["Administrative Automobiles","Chief Administration Manager"],
                    ["Administrative Automobiles","Research Head"],["Administrative Automobiles","Development Manager"],["Executive Automobile","Sr.Technology Engineer"],
                    ["Executive Automobile","Hardware System Manager"],["Executive Automobile","Sr. Manager"],["Executive Automobile","Sr. Technology Analyst"],
                    ["Executive Automobile","Tyre and Service Provider"],["Executive Automobile","Construction Vehicle Repair"],["Executive Automobile","Tyre Technician"],
                    ["Executive Automobile","Auto Technician"],["Executive Automobile","Automotive Mechanic"],["Executive Automobile","Automotive Engineer"],
                    ["Operational Automobile","Automotive Mechanic Assistant"],["Operational Automobile","Owner Operator"],["Operational Automobile","Technology Analyst"],
                    ["Operational Automobile","Quality Supervisor"],["Operational Automobile","Automotive Supplier"],["Operational Automobile","Tyre Care Manager"],
                    ["Operational Automobile","Washer and Vehicle Dealer"],["Operational Automobile","Automobile Dealer Clerk"],["Operational Automobile","Washer"],
                    ["Operational Automobile","Fueler"]]
            headers = ["Company Level","Designation"]
            formatl=['fancy_grid',]
            for f in formatl:
                print(tabulate(table, headers, tablefmt=f))
            print(" ")
            print(" ")
            print("Vacancies avaliable in the company are.....")
            print(" ")
            table = [["Administrative Automobiles","Sales Professional"],["Administrative Automobiles","Finance Professional"],
                    ["Administrative Automobiles","Finance Sales Representative"],["Executive Automobile","Sr. Manager"],
                    ["Executive Automobile","Sr. Technology Analyst"],["Executive Automobile","Automotive Mechanic"],
                    ["Executive Automobile","Automotive Engineer"],["Operational Automobile","Automotive Mechanic Assistant"],
                    ["Operational Automobile","Washer and Vehicle Dealer"],["Operational Automobile","Automobile Dealer Clerk"],
                    ["Operational Automobile","Washer"],["Operational Automobile","Fueler"]]
            headers = ["Company Level","Designation"]
            formatl=['fancy_grid',]
            for f in formatl:
                print(tabulate(table, headers, tablefmt=f))
            print(" ")
            print("** Interested Candidates may fill application form from our website**")
            more1=int(input("Would you like to go to another section? If yes, press 1 else enter 2:"))
        elif choice6==6:
            print("*"*133)
            print(" "*55,"REPORT: CYLINDER BLOCK"," "*65)
            print("*"*133)
            table = [["2020-12-01",500,1500,2000,10,610,0,"2020-12-07"], ["2020-12-07",500,110,2500,29,3020,500,"2020-12-14"],
                     ["2020-12-14",500,500,3000,30,3030,500,"2020-12-21"],["2020-12-21",500,500,1500,15,1515,500,"2020-12-25"]]
            headers = ["Delivery Date","Min. Stock","QOH","Prod. Reqt.","Defective Piece","Reorder Level","Close Stock","Exp. Delivery"]
            formatl=['fancy_grid',]
            for f in formatl:
                print(tabulate(table, headers, tablefmt=f))
            print(" ")
            print(" ")
            print("*"*133)
            print(" "*55,"REPORT: BATTERY"," "*65)
            print("*"*133)
            table = [["2020-12-15",400,1200,15,1215,"2020-12-17"], ["2020-12-17",400,1000,10,1010,"2020-12-19"],
                     ["2020-12-19",400,1600,20,1620,"2020-12-21"],["2020-12-21",400,1600,20,1620,"2020-12-23"],
                     ["2020-12-23",400,1000,10,1010,"2020-12-25"]]
            headers = ["Delivery Date","QOH","Requirement","Defective Piece","Reorder Level","Expeceted Delivery"]
            formatl=['fancy_grid',]
            for f in formatl:
                print(tabulate(table, headers, tablefmt=f))
            print(" ")
            print(" ")
            print("*"*133)
            print(" "*55,"REPORT: FLYWHEEL"," "*65)
            print("*"*133)
            table = [["2020-12-15",400,800,10,810,"2020-12-17"], ["2020-12-17",400,1200,15,1215,"2020-12-19"],
                     ["2020-12-19",400,1200,15,1215,"2020-12-21"],["2020-12-21",400,1000,10,1010,"2020-12-23"],
                     ["2020-12-23",400,800,10,810,"2020-12-25"]]
            headers = ["Delivery Date","QOH","Requirement","Defective Piece","Reorder Level","Expected Delivery"]
            formatl=['fancy_grid',]
            for f in formatl:
                print(tabulate(table, headers, tablefmt=f))
            print("*"*133)
            more1=int(input("Would you like to go to another section? If yes, press 1 else enter 2:"))
            

if choice==2:
    choice1=1
    if choice1==1:
        print("Dear Valued Customer, following is the list of frequently bought spare parts")
        table = [[1,"General Utility","Auto Dimming IRV Mirror"], [2,"Safety and Security","Gear Lock"],
                 [2,"Safety and Security","MGA Front Fog Light Pair"],[2,"Safety and Security","Nippon Reverse Parking Sensor"],
                 [3,"Music System","Sony XAV65 Touchscreen"], [3,"Music System","Coaxial Speakers(Set of 4)"],
                 [3,"Music System","Rear Seat Entertainment Android"],[4,"Car Interior","Child Seats-KA500 for upto 27kg weight"],
                 [4,"Car Interior","Set of all 4 doors Power Window"],[4,"Car Interior","Pure Leather Seat Cover"],
                 [5,"Car Exterior","Mud Flaps(Set of 4)"],[5,"Car Exterior","Sun door Visor-all 4 window"],
                 [5,"Car Exterior","Roof Luggage Carrier"],[5,"Car Exterior","Fog Light"],[5,"Car Exterior","Battery"],
                 [5,"Car Exterior","Side Indicator Bulb"],[5,"Car Exterior","Side Window Glass"],[5,"Car Exterior","AC Cooling Coil"]]
        headers = ["Parts", "Part Name"]
        formatl=['fancy_grid',]
        for f in formatl:
            print(tabulate(table, headers, tablefmt=f))
        print(" ")
        print("Hope the above helps you in your decision making....")
        print(" ")
        print("Press 1 for General Utility Spare Parts")
        print("Press 2 for Safety and Security Spare Parts")
        print("Press 3 for Music System Spare Parts")
        print("Press 4 for Car Interior Spare Parts")
        print("Press 5 for Car Exterior Spare Parts")
        choice2=int(input("Enter your choice:"))
        print(" ")
        while choice1==1:
            more=1
            if choice2==1:
                table = [["Auto Dimming IRVM Mirror",6500], ["Sony XAV Ax5000 Touchscreen Music System",24990],
                         ["Stylish Dual Tone Alloy Wheels",28000]]
                headers = ["Parts", "Price"]
                formatl=['fancy_grid',]
                for f in formatl:
                    print(tabulate(table, headers, tablefmt=f))
                leave=int(input("Enter 9 to Exit else any other number:"))
                while (leave!=9 and more==1):
                    selectedpart=input("Enter the part name that you wish to add to your cart:")
                    selectedqty=int(input("Enter the required quantity:"))
                    cursor=mycon.cursor()
                    st1 = "INSERT INTO MyCart1(Category_No,Category_Name,Accessory_Name,Quantity) VALUES('{}','{}','{}','{}')".format(1,'General Utility',selectedpart,selectedqty)
                    cursor.execute(st1)
                    mycon.commit()
                    print(" ")
                    more=int(input("Enter 1 to add more from the same category else 2:"))
                    if more==2:
                        break
                
            elif choice2==2:
                table = [["Gear Lock",1600], ["MGA Front Fog Light Pair",4000], ["Nippon Reverse Parking Sensor",4000],
                         ["Rear View Camera",8500]]
                headers = ["Parts", "Price"]
                formatl=['fancy_grid',]
                for f in formatl:
                    print(tabulate(table, headers, tablefmt=f))
                leave=int(input("Enter 9 to Exit else any other number:"))
                while (leave!=9 and more==1):
                    selectedpart=input("Enter the part name that you wish to add to your cart:")
                    selectedqty=int(input("Enter the required quantity:"))
                    cursor=mycon.cursor()
                    st1 = "INSERT INTO MyCart1(Category_No,Category_Name,Accessory_Name,Quantity) VALUES('{}','{}','{}','{}')".format(2,'Safety and Security',selectedpart,selectedqty)
                    cursor.execute(st1)
                    mycon.commit()
                    print(" ")
                    more=int(input("Enter 1 to add more from the same category else 2:"))
                    if more==2:
                        break
                    
            elif choice2==3:
                table = [["Sony XAV65 Touchscreen AV",15990], ["JVC V10 KW",17990], ["Kenwood DDX 3035",18490],
                        ["Coaxial Speaker(Set of 4 speaker)",8000], ["Component Speaker Pair(Set of 4 Speakers)",15000], ["Amplifier Range",27990],
                        ["Rear Seat Entertainment Android",19990]]
                headers = ["Parts", "Price"]
                formatl=['fancy_grid',]
                for f in formatl:
                    print(tabulate(table, headers, tablefmt=f))
                leave=int(input("Enter 9 to Exit else any other number:"))
                while (leave!=9 and more==1):
                    selectedpart=input("Enter the part name that you wish to add to your cart:")
                    selectedqty=int(input("Enter the required quantity:"))
                    cursor=mycon.cursor()
                    st1 = "INSERT INTO MyCart1(Category_No,Category_Name,Accessory_Name,Quantity) VALUES('{}','{}','{}','{}')".format(3,'Music System',selectedpart,selectedqty)
                    cursor.execute(st1)
                    mycon.commit()
                    print(" ")
                    more=int(input("Enter 1 to add more from the same category else 2:"))
                    if more==2:
                        break
                    
               
            elif choice2==4:
                table = [["Steering Wheel Cover(Fabric,Art Leather Range)",850],["Perfume Range",500],["Cabin Floor Mat(Designer Mat)",2500],
                         ["Child Seats-KA500 for upto 27kg weight",1000], ["Door Sill Guard",900], ["Set of all 4 Door Power Window",13500],
                         ["Rare Parcel Tray",1900],["Oval Speaker",4500], ["Integrated Music System-Nippon(Only Head Unit)",16000],
                         ["Pure Leather Seat Cover",30000]]
                headers = ["Parts", "Price"]
                formatl=['fancy_grid',]
                for f in formatl:
                    print(tabulate(table, headers, tablefmt=f))
                leave=int(input("Enter 9 to Exit else any other number:"))
                while (leave!=9 and more==1):
                    selectedpart=input("Enter the part name that you wish to add to your cart:")
                    selectedqty=int(input("Enter the required quantity:"))
                    cursor=mycon.cursor()
                    st1 = "INSERT INTO MyCart1(Category_No,Category_Name,Accessory_Name,Quantity) VALUES('{}','{}','{}','{}')".format(4,'Car Interior',selectedpart,selectedqty)
                    cursor.execute(st1)
                    mycon.commit()
                    print(" ")
                    more=int(input("Enter 1 to add more from the same category else 2:"))
                    if more==2:
                        break
                    
            elif choice2==5:
                table = [["Mud Flaps(Set of 4)",800], ["Wheel Cover(Set of 4 basis Tyre Size & Design",2200], ["Body Side Moulding",2300],
                         ["Sun Door Visor-All 4 Windows",1200], ["Roof Luggage Carrier(For Ertiga)",10600], ["Fog Light",3800],
                         ["Exhaust Pipe",3500],["Engine Mounting",4000], ["Battery(Petrol)",4000],["Battery(Diesel)",1600],["Bonnet",15000],
                         ["Flywheel",1200],["Front Brake Pad Replacement",2000],["Side Indicator Bulb",115],["Side Window Glass",1500],
                         ["AC Cooling Coil",2500],["Turbo Charger",35000],["AC Compressor Replacement",15000],["Radiator Assembly",20000],
                         ["Crank Shaft Assembly",22000],["Set of 4 New Tyres",20000],["Engine Transmission Assembly",300000]]
                headers = ["Parts", "Price"]
                formatl=['fancy_grid',]
                for f in formatl:
                    print(tabulate(table, headers, tablefmt=f))
                leave=int(input("Enter 9 to Exit else any other number:"))
                while (leave!=9 and more==1):
                    selectedpart=input("Enter the part name that you wish to add to your cart:")
                    selectedqty=int(input("Enter the required quantity:"))
                    cursor=mycon.cursor()
                    st1 = "INSERT INTO MyCart1(Category_No,Category_Name,Accessory_Name,Quantity) VALUES('{}','{}','{}','{}')".format(5,'Car Exterior',selectedpart,selectedqty)
                    cursor.execute(st1)
                    mycon.commit()
                    print(" ")
                    more=int(input("Enter 1 to add more from the same category else 2:"))
                    if more==2:
                        break
                    
            print(" ")
            print("Would you like to add something else from another category then press 1 else press 2:")
            choice3=int(input("Enter your choice:"))
            if choice3==1:
                choice1==1
                print(" ")
                choice2=int(input("Enter Category No. of your choice:"))
            else:
                print("="*133)
                print("*"*133)
                print(" "*45,"CURRENT ITEMS IN YOUR CART ARE....")
                print("-"*133)
                cursor=mycon.cursor()
                st="SELECT * FROM MyCart1"
                cursor.execute(st)
                data=cursor.fetchall()
                for row in data:
                    print(row)
                print(" ")
                print("*"*133)
                print("="*133)

                print("Visit our nearest store to get your car back as new!!")
                table = [[201223675,"Shop 3 Alandi Road Kirkee,Pune-411028","Suresh Verma","Kirkee"],
                         [209087864,"42/43 Shivpeth Opp. Shankar Road Pawar Seatcorner,Pune-411001","Rahul Sharma","Shivpeth"],
                         [207889901,"Shop No.1 Mayur Prasth,Pimpri Chowk,ICICI Bank,Pune-413456","Ganesh Yadhav","Pimpri "],
                         [203456897,"Shop 1 Opp. Bharat Restaurant,Hinjewadi,Pune-411030","Amit Kumar","Hinjewadi"],
                         [206543290,"Sangharsh Chowk,Chandan Nagar,Pune-410012","Sachin Shetty","Chandan Nagar"]]
                headers = ["Telephone No", "Address","Sales Manager","Area"]
                formatl=['fancy_grid',]
                for f in formatl:
                    print(tabulate(table, headers, tablefmt=f))
                print("Press 1 to request for an appointment else press 2:")
                choice4=int(input("Enter your choice:"))
                
                if choice4==1:
                    table = [[1,"Kirkee"], [2,"Shivpeth"], [3,"Pimpri"],[4,"Hinjewadi"], [5,"Chandan Nagar"]]
                    headers = ["Sr. No.", "Area"]
                    formatl=['grid',]
                    for f in formatl:
                        print(tabulate(table, headers, tablefmt=f))
                    selectedArea=int(input("Select the Sr No. of the nearest area from above:"))
                    print(" ")
                    print("The address for the store is:")
                    ourStores(selectedArea)
                    print(" ")
                    print("*"*133)
                    print("Dear", name,",")
                    print("Your appointment under your name has been made for tomorrow 5:00 PM!")
                    print("In case of inconvience please call your nearest store")
                    print("*"*133)
                else:
                    print("Would you like a reminder for a later visit??")
                    choice5=int(input("Enter 1 else enter 2:"))
                    if choice5==1:
                        table = [[1,"Kirkee"], [2,"Shivpeth"], [3,"Pimpri"],[4,"Hinjewadi"], [5,"Chandan Nagar"]]
                        headers = ["Sr. No.", "Area"]
                        formatl=['grid',]
                        for f in formatl:
                            print(tabulate(table, headers, tablefmt=f))
                        email=input("Please enter your email address:")
                        phoneno=input("Please enter your phone number:")
                        
                        selectedArea=int(input("Select the Sr No. of the nearest area from above:"))
                        print(" ")
                        print("The address for the store is:")
                        ourStores(selectedArea)
                        print(" ")
                        print("="*133)
                        print(" ")
                        print("A Reminder to visit your nearest store would be sent via email at", email,"and message on",phoneno,"!!")
                        print(" ")
                        print("="*133)
                        
                    else:
                        print("WE HOPE YOU WOULD VISIT OUR STORE SOON!")
                        
                    print(" ")    
                    print("Please Rate our website to help us improve and serve you better")
                    print("1:Very Poor")
                    print("2:Poor")
                    print("3:Good")
                    print("4:Very Good")
                    print("5:Excellent")
                    rating=int(input("Enter between 1 to 5:"))
                    print(" ")
                    print("Thankyou for valuable feedback")
                    print(" ")
                    
                break

now1=datetime.now()
print("Exit Date and Time:",now1)
print("-"*133)
            
