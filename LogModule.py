import os
import time
import DirModule

def Mode1():

    t1 = time.strftime("%d-%m-%Y")
    t2 = time.strftime("%d-%m-%Y-%H-%M-%S")

    
    def CheckFile():
        n=os.path.exists('Records/Mode1/Logs/'+t1)
        if(n==True):
            #print("File Is Already Created..!!")
            WriteFile()
        else:
            f=open('Records/Mode1/Logs/'+t1,"x")
            print("File Is Created SuccessFully..!!")
            WriteFile()

    def WriteFile():
        f=open('Records/Mode1/Logs/'+t1,"a")
        f.write("Activity Detected On "+t2+"\n")
        print("Activity Detected On "+t2+"\n")

    if(os.path.exists('Records/Mode1/Logs')):
        CheckFile()
    else:
        DirModule.Dir()
        CheckFile()

def Mode2():
    
    t1 = time.strftime("%d-%m-%Y")
    t2 = time.strftime("%d-%m-%Y-%H-%M-%S")

    def CheckFile():
        n=os.path.exists('Records/Mode2/Logs/'+t1)
        if(n==True):
            #print("File Is Already Created..!!")
            WriteFile()
        else:
            f=open('Records/Mode2/Logs/'+t1,"x")
            print("File Is Created SuccessFully..!!")
            WriteFile()

    def WriteFile():
        f=open('Records/Mode2/Logs/'+t1,"a")
        f.write("Activity Detected On "+t2+"\n")

    if(os.path.exists('Records/Mode2/Logs')):
        CheckFile()
    else:
        DirModule.Dir()
        CheckFile()

def Mode3():
    
    t1 = time.strftime("%d-%m-%Y")
    t2 = time.strftime("%d-%m-%Y-%H-%M-%S")

    def CheckFile():
        n=os.path.exists('Records/Mode3/Logs/'+t1)
        if(n==True):
            #print("File Is Already Created..!!")
            WriteFile()
        else:
            f=open('Records/Mode3/Logs/'+t1,"x")
            print("File Is Created SuccessFully..!!")
            WriteFile()

    def WriteFile():
        f=open('Records/Mode3/Logs/'+t1,"a")
        f.write("Activity Detected On "+t2+"\n")

    if(os.path.exists('Records/Mode3/Logs')):
        CheckFile()
    else:
        DirModule.Dir()
        CheckFile()

def Mode4():
    
    t1 = time.strftime("%d-%m-%Y")
    t2 = time.strftime("%d-%m-%Y-%H-%M-%S")

    def CheckFile():
        n=os.path.exists('Records/Mode4/Logs/'+t1)
        if(n==True):
            #print("File Is Already Created..!!")
            WriteFile()
        else:
            f=open('Records/Mode4/Logs/'+t1,"x")
            print("File Is Created SuccessFully..!!")
            WriteFile()

    def WriteFile():
        f=open('Records/Mode4/Logs/'+t1,"a")
        f.write("Weapon Detected On "+t2+"\n")

    if(os.path.exists('Records/Mode4/Logs')):
        CheckFile()
    else:
        DirModule.Dir()
        CheckFile()

def Mode5():
    
    t1 = time.strftime("%d-%m-%Y")
    t2 = time.strftime("%d-%m-%Y-%H-%M-%S")

    def CheckFile():
        n=os.path.exists('Records/Mode5/Logs/'+t1)
        if(n==True):
            #print("File Is Already Created..!!")
            WriteFile()
        else:
            f=open('Records/Mode5/Logs/'+t1,"x")
            print("File Is Created SuccessFully..!!")
            WriteFile()

    def WriteFile():
        f=open('Records/Mode5/Logs/'+t1,"a")
        f.write("Log File Edited On "+t2+"\n")

    if(os.path.exists('Records/Mode5/Logs')):
        CheckFile()
    else:
        DirModule.Dir()
        CheckFile()
