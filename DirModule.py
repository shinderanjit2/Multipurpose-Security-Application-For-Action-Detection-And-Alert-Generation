import os
import time

def Dir():
    
    list1=['Records']
    list2=['Mode1','Mode2','Mode3','Mode4','Mode5']
    list3=['Logs','Captures']

    for i in list1:
        if(os.path.exists(i)):
            print("I Folder Is Already Exists..!!")        
            for j in list2:
                if(os.path.exists(i+'/'+j)):
                    print("J Folder Is Already Exists..!!")
                    for k in list3:
                        if(os.path.exists(i+'/'+j+'/'+k)):
                            print("K Folder Is Already Exists..!!")
                        else:
                            os.mkdir(i+'/'+j+'/'+k)
                            print("K Folder Is Created..!!")
                else:
                    os.mkdir(i+'/'+j)
                    print("J Folder Is Created")
                    for k in list3:
                        os.mkdir(i+'/'+j+'/'+k)
                        print("J Folder Is Created..!!")
                    
        else:
            os.mkdir(i)
            print("I Folder Is Created..!!")
            for j in list2:
                os.mkdir(i+'/'+j)
                print("J Folder Is Created..!!")
                for k in list3:
                    os.mkdir(i+'/'+j+'/'+k)
                    print("K Folder Is Created..!!")
