while True:
    import os
    a=(input('enter the choice'))
    def f():
        print("1.create the file")
        print("2.read the file")
        print("3.list the file")
        print("4.edit the file")
        print("5.rewrite the file")
        print("6.stop the program")
    match a:
        case"1":
         name=input("enter the file name:")
         name=name+".txt"
         file=open(name,"w")
         print('------------------')
         print("file created successfully")
         print('------------------')
         f()
        case"2":
            print("reading the file")
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"r")
            print(file.read())
            f()
        case"3":
            path="C:\Users\USER-sves05\Desktop\bca1sem"
            files=os.listdir(path)
            for file in files:
                print(file)
            f()
        case"4":
            print("edit the file")
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"a")
            (file.write("varshitha"))
            print("-------------------")
            f()
        case"5":
            print("delete the file")
            name=input("enter the file name")
            name=name+".txt"
            file=(name,"delete")
            print(file.delete())
            print("----------------")
            f()
        case"6":
            print("******program end*******")
        
            
        
         
    
        
    
