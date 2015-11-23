#from fractions import gcd
#or 
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
    

            
n = raw_input()
arr = []
for i in xrange(int(n)): #memory saving
    input_s = raw_input() #str is bad var name 
    new_number = int(input_s[2:])
    if input_s[0] == '-':
        arr.remove(new_number)
    else:
        arr.append(new_number)
    
    if not arr:
        print(1)
        continue
    
    answer=0
    for elem in arr:
            answer = gcd(elem,answer)
            
    print(answer)