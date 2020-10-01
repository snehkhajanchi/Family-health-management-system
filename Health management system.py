#learn object oriented programming. This code will reduce to half it's sizzeee!!!. Good work tho

print("WELCOME TO THE FAMILY HEALTH MANAGEMENT SYSTEM")
print("Identify Yourself ")
print("Press-1 For Shaurya \nPress-2 For Bhavya\nPress-3 For Rashmi\nPress-4 For Deepak ")
a=int(input("Number: "))
if a==1:
    shaurya= input("What do you want to open Exercise or Diet: ")
    if shaurya=="diet":
        data=input("You want to Read or Write your data: ")
        if data=="read":
            q=open("shaurya1.txt")
            content=q.read()
            print(content)
        elif data=="write":
            q=open("shaurya1.txt","a")
            write=input("Enter What you ate along with Date: ")
            q.write(write)
            print("Data entered successfully")
    elif shaurya=="exercise":
        raw=input("You want to Read or Write your data: ")
        if raw=="read":
            q=open("shaurya2.txt")
            content=q.read()
            print(content)
        elif raw=="write":
            q=open("shaurya2.txt","a")
            write=input("Enter What exercise you did along with Date: ")
            q.write(write)
            print("Data entered successfully")
elif a==2:
    bhavya= input("What do you want to open Exercise or Diet: ")
    if bhavya=="diet":
        data=input("You want to Read or Write your data: ")
        if data=="read":
            q=open("bhavya1.txt")
            content=q.read()
            print(content)
        elif data=="write":
            q=open("bhavya1.txt","a")
            write=input("Enter What you ate along with Date: ")
            q.write(write)
            print("Data entered successfully")
    elif bhavya=="exercise":
        raw=input("You want to Read or Write your data: ")
        if raw=="read":
            q=open("bhavya2.txt")
            content=q.read()
            print(content)
        elif raw=="write":
            q=open("bhavya2.txt","a")
            write=input("Enter What exercise you did along with Date: ")
            q.write(write)
            print("Data entered successfully")


elif a==3:
    rashmi= input("What do you want to open Exercise or Diet: ")
    if rashmi=="diet":
        data=input("You want to Read or Write your data: ")
        if data=="read":
            q=open("rashmi1.txt")
            content=q.read()
            print(content)
        elif data=="write":
            q=open("rashmi1.txt","a")
            write=input("Enter What you ate along with Date: ")
            q.write(write)
            print("Data entered successfully")
    elif rashmi=="exercise":
        raw=input("You want to Read or Write your data: ")
        if raw=="read":
            q=open("rashmi2.txt")
            content=q.read()
            print(content)
        elif raw=="write":
            q=open("rashmi2.txt","a")
            write=input("Enter What exercise you did along with Date: ")
            q.write(write)
            print("Data entered successfully")
elif a==4:
    deepak= input("What do you want to open Exercise or Diet: ")
    if deepak=="diet":
        data=input("You want to Read or Write your data: ")
        if data=="read":
            q=open("deepak1.txt")
            content=q.read()
            print(content)
        elif data=="write":
            q=open("deepak1.txt","a")
            write=input("Enter What you ate along with Date: ")
            q.write(write)
            print("Data entered successfully")
    elif deepak=="exercise":
        raw=input("You want to Read or Write your data: ")
        if raw=="read":
            q=open("deepak2.txt")
            content=q.read()
            print(content)
        elif raw=="write":
            q=open("deepak2.txt","a")
            write=input("Enter What exercise you did along with Date: ")
            q.write(write)
            print("Data entered successfully")
    
