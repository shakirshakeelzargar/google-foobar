import math
def solution(area):
    ls=[]
    sum=0
    val=0
    while sum != area:
        val=closest_sqruare(area-sum)
        sum+=val
        ls.append(val)
    return ls

def closest_sqruare(num):
    sq=square_root(num)
    while sq!=round(sq):
        num=num-1
        sq=square_root(num)
    return num
    
        
    
def square_root(num):
    return(math.sqrt(num))

solution(180)
    