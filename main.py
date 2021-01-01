import threading 
from threading import*
import time
dictionary={}
def create(key,value,t_out=0):
    if key in d:
        print("Error")
    else:
        if(key.isalpha()):
            if len(dictionary)<(1024*1024*1024) and value<=(16*1024*1024):  
                if t_out==0:
                    lst=[value,t_out]
                else:
                    lst=[value,time.time()+t_out]
                if len(key)<=32:
                    dictionary[key]=lst
            else:
                print("Error")
        else:
            print("Error")
            
def read(key):
    if key not in dictionary:
        print("Error")
    else:
        var=dictionary[key]
        if var[1]!=0:
            if time.time()<var[1]:
                string=str(key)+":"+str(var[0])
                return string
            else:
                print("Error")
        else:
            string=str(key)+":"+str(var[0])
            return string
def delete(key):
    if key not in dictionary:
        print("Error")
    else:
        var=dictionary[key]
        if var[1]!=0:
            if time.time()<var[1]:
                del dictionary[key]
                print("key is  Deleted")
            else:
                print("Error")
        else:
            del dictionary[key]
            print("key is successfully deleted")

def modify(key,value):
    var=dictionary[key]
    if var[1]!=0:
        if time.time()<var[1]:
            if key not in dictionary:
                print("Error")
            else:
                lst=[]
                lst.append(value)
                lst.append(var[1])
                dictionary[key]=lst
        else:
            print("Error")
    else:
        if key not in dictionary:
            print("Error")
        else:
            lst=[]
            lst.append(value)
            lst.append(var[1])
            d[key]=lst
