# необязательная часть
class Foo(object):
    def __new__(c, arg1, arg2):
        return arg1 if arg2 == 0 else c(arg2, arg1 % arg2)

class Bar(Foo):
    def __new__(c, arg1, arg2):
        if not arg2:
            return arg1
        return c(Foo(arg1, arg2[0]), arg2[1:])
        

n = input()
arr = []
for i in range(int(n)): #memory saving
    input_s = input() #str is bad var name 
    new_number = int(input_s[2:])
    if input_s[0] == '-':
        arr.remove(new_number)
    else:
        arr.append(new_number)
    
    if not arr:
        print(1)
        continue
    
    # answer=0
    # answer = gcd(elem,answer)
    print(Bar(0, arr))
