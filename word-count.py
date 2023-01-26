##Developed by : Lubindher
##Register number: 22009019
def program():
    count=0
    with open("new1.txt","r") as f:
        for data in f:
            words=data.split()
            for word in words:
                count+=1
    print("Total number of words:",count)
program()