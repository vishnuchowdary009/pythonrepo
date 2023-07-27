
def biggest(list):
    a = list[0]
    for x in list:
        if x>a:
            a = x
    print(a)
list=[1,2,3,4]
biggest(list)