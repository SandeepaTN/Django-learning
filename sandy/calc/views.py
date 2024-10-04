from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import mysql.connector



def home(request):
    def dicti():
        db=mysql.connector.connect(host="localhost",user='root',password='1234',database="college")
        mycursor=db.cursor()
        mycursor.execute("select name from student")
        name=''
        for i in mycursor:
            name=name+' '+ (i[0])
        
        return f"{str(name)}"

    

        
    
    return render(request,"home.html",{'name':dicti()})

def add(request):
    val1=int(request.POST["num1"])
    val2=int(request.POST["num2"])
    res=val1+val2
    return render(request,"result.html",{"result":res})















