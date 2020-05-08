def exists(ls,x,y):
    path_exists=False
    if y!=0:
        try:
            if ls[y-1][x]==0:
                path_exists=True
        except:
            pass
        
    if y!=len(ls)-1:
        try:
            if ls[y+1][x]==0:
                path_exists=True
        except:
            pass
        
    if x!=0:
        try:
            if ls[y][x-1]==0:
                path_exists=True
        except:
            pass
    if x!=len(ls[y])-1:
        try:
            if ls[y][x+1]==0:
                path_exists=True
        except:
            pass
        
    return path_exists
        



def vert_up(ls,x,y):
    try:
        if y==0:
                return {"status":False,"x":None,"y":None}
        elif ls[y][x]==1:
            return {"status":False,"x":None,"y":None}
        else:
            val=ls[y][x]
            if val==0:
                if ls[y-1][x]==0:
                    return {"status":True,"x":x,"y":y-1}
                else:
                    return {"status":False,"x":None,"y":None}
            else:
                return {"status":False,"x":None,"y":None}
    except:
        return {"status":False,"x":None,"y":None}

        
        
        
def vert_down(ls,x,y):
    try:
        if y==len(ls)-1:
            return {"status":False,"x":None,"y":None}
        elif ls[y][x]==1:
            return {"status":False,"x":None,"y":None}
        else:
            val=ls[y][x]
            if val==0:
                if ls[y+1][x]==0:
                    return {"status":True,"x":x,"y":y+1}
                else:
                    return {"status":False,"x":None,"y":None}
            else:
                return {"status":False,"x":None,"y":None}
    except:
        return {"status":False,"x":None,"y":None}
        
        
        
def hort_left(ls,x,y):
    try:
        if x==0:
                return {"status":False,"x":None,"y":None}
        elif ls[y][x]==1:
            return {"status":False,"x":None,"y":None}
        else:
            val=ls[y][x]
            if val==0:
                if ls[y][x-1]==0:
                    return {"status":True,"x":x-1,"y":y}
                else:
                    return {"status":False,"x":None,"y":None}
            else:
                return {"status":False,"x":None,"y":None}
    except:
        return {"status":False,"x":None,"y":None}
        
        
        
def hort_right(ls,x,y):
    try:
        if x==len(ls[y])-1:
                return {"status":False,"x":None,"y":None}
        elif ls[y][x]==1:
            return {"status":False,"x":None,"y":None}
        else:
            val=ls[y][x]
            if val==0:
                if ls[y][x+1]==0:
                    return {"status":True,"x":x+1,"y":y}
                else:
                    return {"status":False,"x":None,"y":None}
            else:
                return {"status":False,"x":None,"y":None}
    except:
        return {"status":False,"x":None,"y":None}

        
        
        
def get_all_possible(ls):
    d={}
    for y in range(0,len(ls)):
        for x in range(0,len(ls[y])):
            d[str(x)+","+str(y)]=[]
    for y in range(0,len(ls)):
        for x in range(0,len(ls[y])):
            try:
                vu=vert_up(ls,x,y)
                if vu["status"]==True:
                    tmp=d[str(x)+","+str(y)]
                    tmp.append(vu)
                    d[str(x)+","+str(y)]=tmp
            except:
                pass
            try:
                vd=vert_down(ls,x,y)
                if vd["status"]==True:
                    tmp=d[str(x)+","+str(y)]
                    tmp.append(vd)
                    d[str(x)+","+str(y)]=tmp
            except:
                pass
            try:
                hl=hort_left(ls,x,y)
                if hl["status"]==True:
                    tmp=d[str(x)+","+str(y)]
                    tmp.append(hl)
                    d[str(x)+","+str(y)]=tmp
            except:
                pass
            try:
                hr=hort_right(ls,x,y)
                if hr["status"]==True:
                    tmp=d[str(x)+","+str(y)]
                    tmp.append(hr)
                    d[str(x)+","+str(y)]=tmp

            except:
                pass
    return d












def get_min_path(ls):
    import copy
    d=get_all_possible(ls)
    n=1
    found=False
    d1=copy.deepcopy(d)
    next_moves=d1["0"+","+"0"]
    current_x=0
    current_y=0
    visited=[]
    visited.append({"status":True,"x":0,"y":0})
    while found==False and next_moves!=[]:
        
#         print(next_moves)
        n+=1
        temp_next=[]
        temp_iter=copy.deepcopy(next_moves)
        for x in temp_iter:
            to_check={"status":True,"x":len(ls[-1])-1,"y":len(ls)-1}
            if to_check in next_moves:
                found=True
                return n
            current_x=x["x"]
            current_y=x["y"]
#             print(current_x,current_y)
#             print("")
            visited.append({"status":True,"x":current_x,"y":current_y})
            tmp=d[str(current_x)+","+str(current_y)]
            for t in tmp:
                if t not in visited:
#                     if to_check in next_moves:
#                         found=True
#                         return n+1
                    temp_next.append(t)
            
        #temp_next=[z for z in temp_next if z not in visited]
        next_moves=temp_next
#         to_check={"status":True,"x":len(ls[-1])-1,"y":len(ls)-1}
#         print("to check: ",to_check," in ",next_moves)
#         if to_check in next_moves:
#             found=True
#             return n+1
    if next_moves==[]:
#         print("Unsolvable")
        return 9999


def get_min_path_2(ls):
    d=get_all_possible(ls)
    found=False
    visited=[]
    n=1
    visited.append((0,0))
    next_move=[(x["x"],x["y"]) for x in d["0"+","+"0"]]
    while found==False:
#         print(next_move)
        tmp_next=[]
        n+=1

        for one in next_move:
            next_x,next_y=one
            tmp=[(x["x"],x["y"]) for x in d[str(next_x)+","+str(next_y)]]
            tmp_next=tmp_next+tmp
            visited.append((next_x,next_y))
        next_move=tmp_next
        if (len(ls[-1])-1,len(ls)-1) in next_move:
#             print("Found true,",n)
            return n+1

        next_move=[x for x in next_move if x not in visited]
        if next_move==[]:
#             print("Unsolvable")
            return 9999











def solution(ls):
#     max_len=0
#     lss=[]
#     for x in ls:
#         if len(x)>max_len:
#             max_len=len(x)

#     for x in range(0,len(ls)):
#         if len(ls[x])!=max_len:
#             tmp=ls[x]+[2 for z in range(1,(max_len-len(ls[x]))+1)]
#             lss.append(tmp)
#         else:
#             lss.append(ls[x])
#     ls=lss
    if len(ls)==1:
        if len(ls[0])==1:
            return 1
    import copy
    minimum=get_min_path(ls)
    for x in range(0,len(ls)):
        for y in range(0,len(ls[x])):
#             pass
            if ls[x][y]==1:
                #if exists(ls,x,y)==True:
                iter_list = copy.deepcopy(ls)
                iter_list[x][y]=0
                try_minimum=get_min_path(iter_list)
                if try_minimum<minimum:
                    minimum=try_minimum
                
    return minimum


ls=[
    [0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0]
]

solution(ls)
            
            