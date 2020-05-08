def solution(xs):
    pos=[x for x in xs if x>0 ]
    neg=[x for x in xs if x<0]
    
    if len(xs)==1:
        return str(xs[0])
    
    elif max(xs)==0 and len(neg)%2!=0:
        return str(0)
    elif len(pos)==0 and len(neg)%2!=0:
        return str(0)
    elif len(neg)==0 and len(pos)==1:
        return str(0)
    elif len(pos)==1 and len(neg)==1:
        return str(max(xs))
        

    else:
        if(len(neg)%2!=0):

            neg.remove(max(neg))
        total_product=0
        pos_product=1
        for x in range(0,len(pos)):
            pos_product=pos_product*pos[x]
        neg_product=1
        for x in range(0,len(neg)):
            neg_product=neg_product*neg[x]

        total_product=pos_product*neg_product


        return str(total_product)
        
    
        
solution([2,-3,1,0,-5])