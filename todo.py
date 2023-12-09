print("")
print("----TO-DO___APPLICATION----")
print("")
print("INSTRUCTIONS :  ")
print("1:Add the task")
print("2:Delete the task")
print("3:Display  the task list")
print("4:Mark  the task as completed ")
print("5:Display the status of the tasks")
print("6:To Exit the application")

l=[]
c=[]

def todo():
    print("")
    a=int(input("enter the choice :  "))
    if a==1:
        add=input("enter the task  : ")
        l.append(add)
        print("task added succesfully!")
        todo()

    elif a==2:
        dlt=int(input("specify the task no to be deleted"))
        l.pop(dlt-1)
        print("task no",dlt,"successfully deleted!")
        todo()

    elif a==3:
        for i in range(len(l)):
            print(l[i]) 
        todo()    

    elif a==4:
        no=int(input("enter the task no that  has to  be mark as done : "))
        for i in range(len(l)):
            if i+1==no:
                c.append(l[i])
                print("task  no",no,"is marked as done")
                break
        todo()

    elif a==5:
        for i in range(len(l)):
            for  j  in range(len(c)):
                if l[i]==c[j]:
                    print([i+1],l[i],"[completed]")   
                    break
                elif j==len(c)-1:
                    print([i+1],l[i],"[pending]")     
        todo()

    elif a==6:
        print("THANK YOU!...")

    else:
        print("Enter correct choice")    

todo()

