
import requests
import json
import webbrowser

from requests.api import delete
class Student():
    get_url="http://127.0.0.1:8000/stulist/"
    create_url="http://127.0.0.1:8000/create/"
    update_url="http://127.0.0.1:8000/update/"
    delete_url="http://127.0.0.1:8000/delete/"
    def __init__(self,name=0,roll=0,city=0,id=0):
        self.id=id
        self.name=name
        self.roll=roll
        self.city=city
    
    def set_name(self):
        self.name=input("Enter your name : ")
        return self.name

    def set_roll(self):
        self.roll=int(input("Enter your roll : "))
        return self.roll

    def set_city(self):
        self.city=input("Enter your city :")
        return self.city

    def set_id(self):
        self.id=int(input("Enter the id :"))
        return self.id

    # Addning new student
    def add_student(self):
        return json.dumps({'name':self.set_name(),'roll':self.set_roll(),'city':self.set_city()})
    
    #updating Studant
    def update(self,data):
        if data=='name':
            return json.dumps({'id':self.set_id(),'name':self.set_name()})
        elif data=='roll':
            return json.dumps({'id':self.set_id(),'roll':self.set_roll()})
        elif data=='city':
            return json.dumps({'id':self.set_id(),'city':self.set_city()})
        elif data=='complete':
            return json.dumps({'id':self.set_id(),'name':self.set_name(),'roll':self.set_roll(),'city':self.set_city()})
    
    
    #deleting student
    def delete_student(self):
        return json.dumps({'id':self.set_id()})
            
        
    
stu=Student()

menu1=['1. View Student','2. Add New Student','3. Modify Stuedent','4. Delete Student','5. Exit']
menu2=['1. Complete Update','2. Update Name','3. Update Roll','4. Update City','5. Exit']





while(True):
    print('\n')
    for item in menu1:
        print(item)
    choice1=int(input('Enter Your Choice : '))
    if choice1==1:
        res=requests.get(stu.get_url)
        print(res.json())
    elif choice1==2:
        res=requests.post(stu.create_url,data=stu.add_student())
        print(res.json())
        # webbrowser.open('http://127.0.0.1:8000/admin/api/student/' , new=0 )
    elif choice1==3:
        while True:
            print('\n')
            for item in menu2:
                print(item)
            choice2=int(input('Enter Your choice : '))
            if choice2==1:
                res=requests.put(stu.update_url,stu.update('complete'))
                print(res.json())
                webbrowser.open('http://127.0.0.1:8000/admin/api/student/' , new=0 )
            elif choice2==2:
                res=requests.put(stu.update_url,stu.update('name'))
                print(res.json())
                webbrowser.open('http://127.0.0.1:8000/admin/api/student/' , new=0 )
            elif choice2==3:
                res=requests.put(stu.update_url,stu.update('roll'))
                print(res.json())
                webbrowser.open('http://127.0.0.1:8000/admin/api/student/' , new=0 )
            elif choice2==4:
                res=requests.put(stu.update_url,stu.update('city'))
                print(res.json())
                webbrowser.open('http://127.0.0.1:8000/admin/api/student/' , new=0 )
            elif choice2==5:
                exit()
            else:
                print('Invalid Input Try Again :')
            newchoice=input('Press C for Continue and E for Exit : ').lower
            if newchoice=='c':
                continue
            elif newchoice=='e':
                break

                
    elif choice1==4:
        res=requests.delete(stu.delete_url,data=stu.delete_student())
        webbrowser.open('http://127.0.0.1:8000/admin/api/student/' , new=0 )
        print(stu.id)
        print(res.json())
        webbrowser.open('http://127.0.0.1:8000/admin/api/student/' , new=0 )
    elif choice1==5:
        exit()


    

