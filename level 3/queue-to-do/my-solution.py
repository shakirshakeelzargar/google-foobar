def solution(start,length):


    final_list=[]
    ls=[[(start+x)+(j*length) for x in range(length)] for j in range(length)]
    if len(ls)==0 :
        return 0
    else:
        j=0
        for n in range(len(ls)):
            tmp=ls[n][:len(ls[n])-j]
            final_list=final_list+tmp
            j+=1
        ret_val=get_xor(final_list)
        return ret_val

def get_xor(ls):
    if len(ls)==1:
        return ls[0]
    ans=0
    for x in ls:
        ans=ans^x
    return ans
    


solution(0,3)