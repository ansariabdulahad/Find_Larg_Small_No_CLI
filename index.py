from lib.arrum import FindLarge, FindSmall

def Test() :
    data = []
    limit = int(input("Enter limit\n"))
    print("--------------------------------")
    for i in range(limit) :
        listData = int(input("Enter Your Data\n"))
        data.append(listData)
    print("Your List :", data)
    print("--------------------------------")
    print("Large number is :",FindLarge(data))
    print("Small number is :",FindSmall(data))
Test()

def DicExample() :
    ahadObj = {
        'name' : 'AhadAnsari',
        'roll': '1',
        'dob': '23/01/2001',
        'address': 'mumbai'
    }

    for key in ahadObj : 
        print(f"{key} = {ahadObj[key]}")
DicExample()