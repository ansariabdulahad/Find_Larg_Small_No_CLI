def FindLarge(data) :
    large = 0
    for num in data :
        if num > large :
            large = num
    return large

def FindSmall(data) :
    small = data[0]
    for num in data :
        if num < small :
            small = num
    return small