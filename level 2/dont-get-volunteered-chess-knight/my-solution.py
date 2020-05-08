board=[[(j*8)+x-1 for x in range(1,9)] for j in range(8)]
boundry_top=board[0]
boundary_right=[x[-1] for x in board]
boundary_bottom=board[-1]
boundary_left=[x[0] for x in board]
def vertical_pos(start):
    mov1=start+16
    if mov1 in boundary_right or mov1>boundary_bottom[-1]:
        return []
    else:
        return [mov1+1]
    
def vertical_neg(start):
    mov1=start+16
    if mov1 in boundary_left or mov1>boundary_bottom[-1]:
        return []
    else:
        return [mov1-1]
    
def horizontal_pos(start):
    mov1=start+2
    if start in boundary_bottom or mov1 in boundary_left or start in boundary_right:
        return []
    else:
        return [mov1+8]

def horizontal_neg(start):
    mov1=start+2
    if mov1 in boundry_top or mov1 in boundary_left or start in boundary_right or mov1>63:
        return []
    else:
        return [mov1-8]
    
    
def get_dict():  
    d={}
    for x in range(0,64):
        d[str(x)]=[]
    for x in range(0,64):
        ret=vertical_pos(x)
        ret2=vertical_neg(x)
        ret3=horizontal_pos(x)
        ret4=horizontal_neg(x)
        tmp_list=[ret,ret2,ret3,ret4]
        for one in tmp_list:
            for y in one:
                temp=d[str(x)]
                temp.append(y)
                d[str(x)]=temp


    for k,v in d.items():
        for one_item in v:
            temp=d[str(one_item)]
            temp.append(int(k))
            d[str(one_item)]=temp


    for k,v in d.items():
        un=list(set(v))
        d[k]=un
    return d



def find_minimum(start,end):
    import copy
    d=get_dict()
    n=1
    d1=copy.deepcopy(d)
    start_list=d1[str(start)]
    end_list=d[str(end)]
    if start==end or start<0 or start>63 or end <0 or end>63:
        return 0
    elif end in start_list:
        return 1

    else:
        
        found=False
        while found==False:
            n=n+1
            iter_list = copy.deepcopy(start_list)
            #print(iter_list)
            #print(n)
            for x in iter_list:
                tmp=d[str(x)]
                for t in tmp:
                    start_list.append(t)
                start_list=list(set(start_list))
                start_list =[x for x in start_list if x not in iter_list]
            #print(start_list)
                
            if end in start_list or n > 50:
                found=True
    #print(d)
    return n


def solution(src, dest):
    ret_val=find_minimum(src, dest)
    return ret_val
    


solution(62,50)