from lib.arrum import FindLarge, FindSmall

def Test() :
    data = []
    limit = int(input("Enter limit\n"))
    for i in range(limit) :
        listData = int(input("Enter Your Data\n"))
        data.append(listData)
    print("Large number is :",FindLarge(data))
    print("Small number is :",FindSmall(data))
Test()