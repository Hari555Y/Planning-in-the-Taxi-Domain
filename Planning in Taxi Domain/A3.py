####################################################              part A                          ################################################################################




##############################                        part 1b              ####################################################
'''


import random
import numpy as np
import matplotlib.pyplot as plt
          
def simulate(xt, yt, xd, yd, xp, yp , a, blockup, blockdown, blockleft, blockright, bol):
    
    if xt==xd and xd==xp and yt==yd and yp==yt:
        if a == 'Pickup':
            bol = True
            return -1, xt, yt, xd, yd, xp, yp, bol
        elif a == 'Putdown':
            if bol:
                bol = False
                return 20, xt, yt, xd, yd, xp, yp, bol
            else:
                bol = False
                return -1, xt, yt, xd, yd, xp, yp, bol
        else:
            if a == 'North':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 5*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt, yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 5*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 5*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                else:
                    if xt + 5*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
            elif a == 'West':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 5*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1, yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 5*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 5*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                else:
                    if xt + 5*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
            elif a == 'South':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 5*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt, yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 5*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 5*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
                else:
                    if xt + 5*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
            elif a == 'East':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 5*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1, yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 5*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 5*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                else:
                    if xt + 5*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
    elif a == 'Pickup':
        if xt==xp and yt==yp:
            return -1, xt, yt, xd, yd, xp, yp, True
        else:
            return -10, xt, yt, xd, yd, xp, yp, bol
    elif a == 'Putdown':
        if xt==xp and yt ==yp:
            return -1, xt, yt, xd, yd,xp, yp, False
        else:
            return -10, xt, yt, xd, yd, xp, yp, bol
    elif a == 'North':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 5*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt, yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 5*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 5*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        else:
            if xt + 5*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
    elif a == 'West':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 5*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1, yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 5*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 5*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        else:
            if xt + 5*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
    elif a == 'South':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 5*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt, yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 5*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 5*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
        else:
            if xt + 5*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
    elif a == 'East':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 5*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1, yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 5*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 5*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        else:
            if xt + 5*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
    else:
        raise Exception("Unauthorized input")  


def preprocessing():
    blockup = {20, 21, 22, 23, 24}
    blockdown = {0, 1,2, 3, 4}
    blockleft = {0 ,5, 10, 15, 20, 1, 6, 3, 8, 17, 22}
    blockright = {4, 9, 14, 19, 24, 0, 5, 2, 7, 16, 21}
    return blockup, blockdown, blockleft, blockright

if __name__  == '__main__':
    setA , setB, setC, setD = preprocessing()
    rew, a, b , c, d, e, f , bol = simulate(0 ,2, 4, 0, 4, 4,'South', setA, setB, setC, setD, False)
    print(a, b)
    '''
    
    
    
    
############################################################             part 2a            #####################################################################
'''




import matplotlib.pyplot as plt
def val_iter(domain, eps):
    px, py, dx, dy, tx, ty = domain
    ps = px+5*py
    ds = dx+5*dy
    t = tx+5*ty

    y = 0.9

    actions = ['Pickup', 'Putdown', 'North', 'South', 'East', 'West']
    V = [0 for i in range(50)]
    act = ['' for i in range(50)]
    ite_ind =[]
    max_norm_dist = []
    qa = (1-y)/y
    dsq = qa*eps
    delt = 100000000
    count = 0
    while delt>dsq:
        count +=1
        ite_ind.append(count)
        delt = 0
        v = V.copy()
        for s in range(50):
            vl = -10000000
            for a in actions:
                tr, rw = trans_prob(s,ps,ds,a)
                if s>24:
                    tr, rw = trans_prob(s,s-25,ds,a)
                cur = 0
                for sl in tr:
                    if sl==500:
                        cur += tr[sl]*rw[sl]
                    else:
                        cur += tr[sl]*(rw[sl]+y*v[sl])
                if cur>vl:
                    act[s] = a
                    V[s] = cur
                    vl = cur
            conv = abs(v[s]-V[s])
            if conv>delt:
                delt = conv
        max_norm_dist.append(delt)
    print(count)
    #print(ite_ind)
    #print(max_norm_dist)
    #plt.plot(ite_ind, max_norm_dist)
    #plt.xlabel('Iteration Index')
    #plt.ylabel('Max-norm Distance')
    #plt.title('Iteration Index vs Max-norm Distance')
    #plt.legend()
   # plt.show()
    cur = t
    arr = []
    while cur!=ps:
        arr.append(act[cur])
        zx = act[cur]
        if zx=='North':
            cur += 5
        if zx=='South':
            cur -= 5
        if zx=='East':
            cur += 1
        if zx=='West':
            cur -= 1
    arr.append('Pickup')
    cur += 25
    while cur != ds+25:
        zx = act[cur]
        arr.append(zx)
        if zx=='North':
            cur += 5
        if zx=='South':
            cur -= 5
        if zx=='East':
            cur += 1
        if zx=='West':
            cur -= 1
    arr.append('Putdown')
    return arr

def trans_prob(s,ps,ds,a):
    trans = {}
    rew = {}
    blockup = {20, 21, 22, 23, 24}
    blockdown = {0, 1, 2, 3, 4}
    blockleft = {0 ,5, 10, 15, 20, 1, 6, 3, 8, 17, 22, 62}
    blockright = {4, 9, 14, 19, 24, 0, 5, 2, 7, 16, 21}
    s2 = s%25
    if a=='Pickup':
        if ps==s2:
            trans[s2+25] = 1
            rew[s2+25] = -1
            return trans,rew
        trans[s] = 1
        rew[s] = -10
        return trans, rew
    if a=='Putdown':
        if s2!=ps:
            trans[s] = 1
            rew[s] = -10
            return trans, rew
        if ps!=ds:
            trans[s2] = 1
            rew[s2] = -1
            return trans, rew
        trans[500] = 1
        rew[500] = 20
        return trans, rew
    
    if a=='North':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.85
        else:
            trans[s+5] = 0.85
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    
    if a=='South':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.85
        else:
            trans[s-5] = 0.85
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    
    if a=='East':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.85
        else:
            trans[s+1] = 0.85
            rew[s+1] = -1
    
    if a=='West':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.85
        else:
            trans[s-1] = 0.85
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    return trans, rew

answ = val_iter((0,0,3,0,4,4),0.001)
print(answ)
#print(total_count)


'''

######################################## #############################     part 2b  (plotting)  ###########################################################################


'''

import matplotlib.pyplot as plt
def val_iter(domain, eps):
    px, py, dx, dy, tx, ty = domain
    ps = px+5*py
    ds = dx+5*dy
    t = tx+5*ty

    y = float(input("Enter the value of discount factor: "))

    actions = ['Pickup', 'Putdown', 'North', 'South', 'East', 'West']
    V = [0 for i in range(50)]
    act = ['' for i in range(50)]
    ite_ind =[]
    max_norm_dist = []
    qa = (1-y)/y
    dsq = qa*eps
    delt = 100000000
    count = 0
    while delt>dsq:
        count +=1
        ite_ind.append(count)
        delt = 0
        v = V.copy()
        for s in range(50):
            vl = -10000000
            for a in actions:
                tr, rw = trans_prob(s,ps,ds,a)
                if s>24:
                    tr, rw = trans_prob(s,s-25,ds,a)
                cur = 0
                for sl in tr:
                    if sl==500:
                        cur += tr[sl]*rw[sl]
                    else:
                        cur += tr[sl]*(rw[sl]+y*v[sl])
                if cur>vl:
                    act[s] = a
                    V[s] = cur
                    vl = cur
            conv = abs(v[s]-V[s])
            if conv>delt:
                delt = conv
        max_norm_dist.append(delt)
   # print(count)
  #  print(ite_ind)
   # print(max_norm_dist)
    plt.scatter(ite_ind, max_norm_dist)
    plt.plot(ite_ind, max_norm_dist)
    plt.xlabel('Iteration Index')
    plt.ylabel('Max-norm Distance')
    plt.title('Iteration Index vs Max-norm Distance')
  #  plt.legend()
    plt.show()
    cur = t
    arr = []
    while cur!=ps:
        arr.append(act[cur])
        zx = act[cur]
        if zx=='North':
            cur += 5
        if zx=='South':
            cur -= 5
        if zx=='East':
            cur += 1
        if zx=='West':
            cur -= 1
    arr.append('Pickup')
    cur += 25
    while cur != ds+25:
        zx = act[cur]
        arr.append(zx)
        if zx=='North':
            cur += 5
        if zx=='South':
            cur -= 5
        if zx=='East':
            cur += 1
        if zx=='West':
            cur -= 1
    arr.append('Putdown')
    return arr

def trans_prob(s,ps,ds,a):
    trans = {}
    rew = {}
    blockup = {20, 21, 22, 23, 24}
    blockdown = {0, 1, 2, 3, 4}
    blockleft = {0 ,5, 10, 15, 20, 1, 6, 3, 8, 17, 22, 62}
    blockright = {4, 9, 14, 19, 24, 0, 5, 2, 7, 16, 21}
    s2 = s%25
    if a=='Pickup':
        if ps==s2:
            trans[s2+25] = 1
            rew[s2+25] = -1
            return trans,rew
        trans[s] = 1
        rew[s] = -10
        return trans, rew
    if a=='Putdown':
        if s2!=ps:
            trans[s] = 1
            rew[s] = -10
            return trans, rew
        if ps!=ds:
            trans[s2] = 1
            rew[s2] = -1
            return trans, rew
        trans[500] = 1
        rew[500] = 20
        return trans, rew
    
    if a=='North':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.85
        else:
            trans[s+5] = 0.85
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    
    if a=='South':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.85
        else:
            trans[s-5] = 0.85
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    
    if a=='East':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.85
        else:
            trans[s+1] = 0.85
            rew[s+1] = -1
    
    if a=='West':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.85
        else:
            trans[s-1] = 0.85
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    return trans, rew

answ = val_iter((0,0,3,0,4,4),0.001)
# print(answ)
#print(total_count)



'''

################################################################### part 2c ####################################################################################

'''
import matplotlib.pyplot as plt
def val_iter(domain, eps):
    px, py, dx, dy, tx, ty = domain
    ps = px+5*py
    ds = dx+5*dy
    t = tx+5*ty

    y = float(input("Enter the value of discount factor: "))

    actions = ['Pickup', 'Putdown', 'North', 'South', 'East', 'West']
    V = [0 for i in range(50)]
    act = ['' for i in range(50)]
    ite_ind =[]
    max_norm_dist = []
    qa = (1-y)/y
    dsq = qa*eps
    delt = 100000000
    count = 0
    while delt>dsq:
        count +=1
        ite_ind.append(count)
        delt = 0
        v = V.copy()
        for s in range(50):
            vl = -10000000
            for a in actions:
                tr, rw = trans_prob(s,ps,ds,a)
                if s>24:
                    tr, rw = trans_prob(s,s-25,ds,a)
                cur = 0
                for sl in tr:
                    if sl==500:
                        cur += tr[sl]*rw[sl]
                    else:
                        cur += tr[sl]*(rw[sl]+y*v[sl])
                if cur>vl:
                    act[s] = a
                    V[s] = cur
                    vl = cur
            conv = abs(v[s]-V[s])
            if conv>delt:
                delt = conv
        max_norm_dist.append(delt)
    cur = t
    arr = []
    state =[]
    while cur!=ps:
        if len(state) >19:
            break
        state.append(cur)
        arr.append(act[cur])
        zx = act[cur]
        if zx=='North':
            cur += 5
        if zx=='South':
            cur -= 5
        if zx=='East':
            cur += 1
        if zx=='West':
            cur -= 1
    if len(state) <20 :
        arr.append('Pickup')
        state.append(cur)
        cur += 25
    while cur != ds+25:
        zx = act[cur]
        if len(state) >19:
            break
        state.append(cur)
        arr.append(zx)
        if zx=='North':
            cur += 5
        if zx=='South':
            cur -= 5
        if zx=='East':
            cur += 1
        if zx=='West':
            cur -= 1
    if len(state) < 19:
        state.append(cur)
        arr.append('Putdown')
        state.append(cur-25)
    return state,arr

def trans_prob(s,ps,ds,a):
    trans = {}
    rew = {}
    blockup = {20, 21, 22, 23, 24}
    blockdown = {0, 1, 2, 3, 4}
    blockleft = {0 ,5, 10, 15, 20, 1, 6, 3, 8, 17, 22, 62}
    blockright = {4, 9, 14, 19, 24, 0, 5, 2, 7, 16, 21}
    s2 = s%25
    if a=='Pickup':
        if ps==s2:
            trans[s2+25] = 1
            rew[s2+25] = -1
            return trans,rew
        trans[s] = 1
        rew[s] = -10
        return trans, rew
    if a=='Putdown':
        if s2!=ps:
            trans[s] = 1
            rew[s] = -10
            return trans, rew
        if ps!=ds:
            trans[s2] = 1
            rew[s2] = -1
            return trans, rew
        trans[500] = 1
        rew[500] = 20
        return trans, rew
    
    if a=='North':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.85
        else:
            trans[s+5] = 0.85
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    
    if a=='South':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.85
        else:
            trans[s-5] = 0.85
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    
    if a=='East':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.85
        else:
            trans[s+1] = 0.85
            rew[s+1] = -1
    
    if a=='West':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.85
        else:
            trans[s-1] = 0.85
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    return trans, rew

firs, answ = val_iter((0,4,3,0,2,3),0.01)
print(firs)
print(answ)
#print(total_count)
'''

###############################################################     part 3b (optimal policy)  ###################################################################################

'''

import random
import numpy as np
import matplotlib.pyplot as plt

def pol_iter(domain, eps):
    px, py, dx, dy, tx, ty = domain
    ps = px+5*py
    ds = dx+5*dy
    t = tx+5*ty

    y = 0.01

    actions = ['Pickup', 'Putdown', 'North', 'South', 'East', 'West']
    V = [0 for i in range(50)]
    act = [actions[int(random.random()*6)] for i in range(50)]
    #act[ds+25] = 'Putdown'

    qa = (1-y)/y
    dsq = qa*eps
    delt = 1000000

    iter = 0
    policy_stable = False
    while not policy_stable:
        #Policy Evaluation
        iter += 1
        policy_stable = True
        delt = 0
        v = V.copy()
        for s in range(50):
            tr, rw = trans_prob(s,ps,ds,act[s])
            if s>24:
                tr, rw = trans_prob(s,s-25,ds,act[s])
            cur = 0
            for sl in tr:
                if sl==500:
                    cur += tr[sl]*rw[sl]
                else:
                    cur += tr[sl]*(rw[sl]+y*v[sl])
            
            V[s] = cur
            conv = abs(v[s]-V[s])
            if conv>delt:
                delt = conv
        
        #Policy Improvement
        for s in range(50):
            pl = act[s]
            vl = -100000
            for p in range(5,-1,-1):
                a = actions[p]
                tr, rw = trans_prob(s,ps,ds,a)
                if s>24:
                    tr, rw = trans_prob(s,s-25,ds,a)
                cur = 0
                for sl in tr:
                    if sl==500:
                        cur += tr[sl]*rw[sl]
                    else:
                        cur += tr[sl]*(rw[sl]+y*V[sl])
                if cur>vl:
                    act[s] = a
                    vl = cur
            if act[s] != pl:
                policy_stable = False

    opt_act, opt_V = act.copy(), V.copy()

    V = [0 for i in range(50)]
    act = [actions[int(random.random()*6)] for i in range(50)]
    iter = 0
    arr = []
    policy_stable = False
    while not policy_stable:
        #Policy Evaluation
        iter += 1
        policy_stable = True
        delt = 0
        v = V.copy()
        for s in range(50):
            tr, rw = trans_prob(s,ps,ds,act[s])
            if s>24:
                tr, rw = trans_prob(s,s-25,ds,act[s])
            cur = 0
            for sl in tr:
                if sl==500:
                    cur += tr[sl]*rw[sl]
                else:
                    cur += tr[sl]*(rw[sl]+y*v[sl])
            
            V[s] = cur
            conv = abs(v[s]-opt_V[s])
            if conv>delt:
                delt = conv
        arr.append(delt)
        
        #Policy Improvement
        for s in range(50):
            pl = act[s]
            vl = -100000
            for p in range(5,-1,-1):
                a = actions[p]
                tr, rw = trans_prob(s,ps,ds,a)
                if s>24:
                    tr, rw = trans_prob(s,s-25,ds,a)
                cur = 0
                for sl in tr:
                    if sl==500:
                        cur += tr[sl]*rw[sl]
                    else:
                        cur += tr[sl]*(rw[sl]+y*V[sl])
                if cur>vl:
                    act[s] = a
                    vl = cur
            if act[s] != pl:
                policy_stable = False
    return V, act, arr

def trans_prob(s,ps,ds,a):
    trans = {}
    rew = {}
    blockup = {20, 21, 22, 23, 24}
    blockdown = {0, 1, 2, 3, 4}
    blockleft = {0 ,5, 10, 15, 20, 1, 6, 3, 8, 17, 22, 62}
    blockright = {4, 9, 14, 19, 24, 0, 5, 2, 7, 16, 21}
    s2 = s%25
    if a=='Pickup':
        if ps==s2:
            trans[s2+25] = 1
            rew[s2+25] = -1
            return trans,rew
        trans[s] = 1
        rew[s] = -10
        return trans, rew
    if a=='Putdown':
        if s2!=ps:
            trans[s] = 1
            rew[s] = -10
            return trans, rew
        if ps!=ds:
            trans[s2] = 1
            rew[s2] = -1
            return trans, rew
        trans[500] = 1
        rew[500] = 20
        return trans, rew
    
    if a=='North':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.85
        else:
            trans[s+5] = 0.85
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    
    if a=='South':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.85
        else:
            trans[s-5] = 0.85
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    
    if a=='East':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.85
        else:
            trans[s+1] = 0.85
            rew[s+1] = -1
    
    if a=='West':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.85
        else:
            trans[s-1] = 0.85
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    return trans, rew

V, act, arr = pol_iter((0,0,4,4,2,4),0.001)
print(act)


'''



##########################################################################           part  3b  (graphing) #############################################################


'''
import random
import numpy as np
import matplotlib.pyplot as plt

def pol_iter(domain, eps):
    px, py, dx, dy, tx, ty = domain
    ps = px+5*py
    ds = dx+5*dy
    t = tx+5*ty

    y = 0.01

    actions = ['Pickup', 'Putdown', 'North', 'South', 'East', 'West']
    V = [0 for i in range(50)]
    act = [actions[int(random.random()*6)] for i in range(50)]
    #act[ds+25] = 'Putdown'

    qa = (1-y)/y
    dsq = qa*eps
    delt = 1000000

    iter = 0
    policy_stable = False
    while not policy_stable:
        #Policy Evaluation
        iter += 1
        policy_stable = True
        delt = 0
        v = V.copy()
        for s in range(50):
            tr, rw = trans_prob(s,ps,ds,act[s])
            if s>24:
                tr, rw = trans_prob(s,s-25,ds,act[s])
            cur = 0
            for sl in tr:
                if sl==500:
                    cur += tr[sl]*rw[sl]
                else:
                    cur += tr[sl]*(rw[sl]+y*v[sl])
            
            V[s] = cur
            conv = abs(v[s]-V[s])
            if conv>delt:
                delt = conv
        
        #Policy Improvement
        for s in range(50):
            pl = act[s]
            vl = -100000
            for p in range(5,-1,-1):
                a = actions[p]
                tr, rw = trans_prob(s,ps,ds,a)
                if s>24:
                    tr, rw = trans_prob(s,s-25,ds,a)
                cur = 0
                for sl in tr:
                    if sl==500:
                        cur += tr[sl]*rw[sl]
                    else:
                        cur += tr[sl]*(rw[sl]+y*V[sl])
                if cur>vl:
                    act[s] = a
                    vl = cur
            if act[s] != pl:
                policy_stable = False

    opt_act, opt_V = act.copy(), V.copy()

    V = [0 for i in range(50)]
    act = [actions[int(random.random()*6)] for i in range(50)]
    iter = 0
    arr = []
    policy_stable = False
    while not policy_stable:
        #Policy Evaluation
        iter += 1
        policy_stable = True
        delt = 0
        v = V.copy()
        for s in range(50):
            tr, rw = trans_prob(s,ps,ds,act[s])
            if s>24:
                tr, rw = trans_prob(s,s-25,ds,act[s])
            cur = 0
            for sl in tr:
                if sl==500:
                    cur += tr[sl]*rw[sl]
                else:
                    cur += tr[sl]*(rw[sl]+y*v[sl])
            
            V[s] = cur
            conv = abs(v[s]-opt_V[s])
            if conv>delt:
                delt = conv
        arr.append(delt)
        
        #Policy Improvement
        for s in range(50):
            pl = act[s]
            vl = -100000
            for p in range(5,-1,-1):
                a = actions[p]
                tr, rw = trans_prob(s,ps,ds,a)
                if s>24:
                    tr, rw = trans_prob(s,s-25,ds,a)
                cur = 0
                for sl in tr:
                    if sl==500:
                        cur += tr[sl]*rw[sl]
                    else:
                        cur += tr[sl]*(rw[sl]+y*V[sl])
                if cur>vl:
                    act[s] = a
                    vl = cur
            if act[s] != pl:
                policy_stable = False
    return V, act, arr

def trans_prob(s,ps,ds,a):
    trans = {}
    rew = {}
    blockup = {20, 21, 22, 23, 24}
    blockdown = {0, 1, 2, 3, 4}
    blockleft = {0 ,5, 10, 15, 20, 1, 6, 3, 8, 17, 22, 62}
    blockright = {4, 9, 14, 19, 24, 0, 5, 2, 7, 16, 21}
    s2 = s%25
    if a=='Pickup':
        if ps==s2:
            trans[s2+25] = 1
            rew[s2+25] = -1
            return trans,rew
        trans[s] = 1
        rew[s] = -10
        return trans, rew
    if a=='Putdown':
        if s2!=ps:
            trans[s] = 1
            rew[s] = -10
            return trans, rew
        if ps!=ds:
            trans[s2] = 1
            rew[s2] = -1
            return trans, rew
        trans[500] = 1
        rew[500] = 20
        return trans, rew
    
    if a=='North':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.85
        else:
            trans[s+5] = 0.85
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    
    if a=='South':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.85
        else:
            trans[s-5] = 0.85
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    
    if a=='East':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.05
        else:
            trans[s-1] = 0.05
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.85
        else:
            trans[s+1] = 0.85
            rew[s+1] = -1
    
    if a=='West':
        trans[s] = 0
        rew[s] = -1
        if s2 in blockup:
            trans[s] += 0.05
        else:
            trans[s+5] = 0.05
            rew[s+5] = -1
        
        if s2 in blockdown:
            trans[s] += 0.05
        else:
            trans[s-5] = 0.05
            rew[s-5] = -1

        if s2 in blockleft:
            trans[s] += 0.85
        else:
            trans[s-1] = 0.85
            rew[s-1] = -1
        
        if s2 in blockright:
            trans[s] += 0.05
        else:
            trans[s+1] = 0.05
            rew[s+1] = -1
    return trans, rew

V, act, arr = pol_iter((0,0,4,4,2,4),0.001)
ax = plt.subplot()
ax.plot(arr,'bo-')
ax.set_xticks(range(0,len(arr)+1))
plt.xlabel('Number of Iterations')
plt.ylabel('Policy Loss')
plt.title("Policy loss vs iterations for discount factor 0.01")
plt.show()


'''



######################################################################### part B ##################################################################






######################################################   part 2 and part 3  (Actions and plotting)   #####################################################################

'''
import random
import numpy as np
import matplotlib.pyplot as plt

def q_learn(domain, eps=0.1):
    px, py, dx, dy, tx, ty = domain
    ps = px+5*py
    ds = dx+5*dy
    t = tx+5*ty
    
    Q = [[0 for i in range(6)] for j in range(50)]
    actions = ['Pickup','Putdown','North','South','East','West']
    blockup, blockdown, blockleft, blockright = preprocessing()
    Q[ds+25][1] = 20
    alp = 0.25
    y = 0.99

    arr = []
    for k in range(2000):
        s = t
        it = 0
        rw =0
        dis =1
        while s!=ds and it<499:
            chnc = int(100*random.random())
            a = 3
            if chnc<100*eps:
                a = int(6*random.random())
            else:
                cur = Q[s][3]
                for j in range(5,-1,-1):
                    if Q[s][j]>cur:
                        cur = Q[s][j]
                        a = j
            
            bol = False
            if s>24:
                bol = True
            t1 = (s%25)%5
            t2 = (s%25)//5
            d1 = px
            d2 = py
            if bol:
                d1 = t1
                d2 = t2
            rwr, xt, yt, xd, yd, xp, yp, same = simulate(t1, t2, dx, dy, d1, d2, actions[a], blockup, blockdown, blockleft, blockright, bol)

            nxt = xt+5*yt
            if same:
                nxt += 25
            vl = -10000
            for m in range(6):
                vl = max(vl,Q[int(nxt)][m])
            if s!=ds+25 or a!=1:
                Q[s][a] = (1-alp)*Q[s][a] + (alp)*(rwr+y*vl)
            s = int(nxt)
            rw += dis*rwr
            dis*=y
            it += 1
        arr.append(rw)
    
    ans = [actions[np.argmax(Q[i])] for i in range(50)]

    plt.plot(range(1, 2001), arr)
    plt.xlabel('The Episodes number')
    plt.ylabel('The sum of discounted rewards')
    plt.title('Sum of Discounted Rewards vs The Training Episodes number')
    plt.show()
    return ans

def q_learn_exp(domain, eps=0.1):
    px, py, dx, dy, tx, ty = domain
    ps = px+5*py
    ds = dx+5*dy
    t = tx+5*ty
    
    Q = [[0 for i in range(6)] for j in range(50)]
    actions = ['Pickup','Putdown','North','South','East','West']
    blockup, blockdown, blockleft, blockright = preprocessing()
    Q[ds+25][1] = 20
    alp = 0.25
    y = 0.99

    arr = []
    for k in range(2000):
        s = t
        it = 1
        rw =0
        dis =1
        while s!=ds and it<500:
            chnc = int(100*random.random())
            a = 3
            if chnc<100*eps/it:
                a = int(6*random.random())
            else:
                cur = Q[s][3]
                for j in range(5,-1,-1):
                    if Q[s][j]>cur:
                        cur = Q[s][j]
                        a = j
            
            bol = False
            if s>24:
                bol = True
            t1 = (s%25)%5
            t2 = (s%25)//5
            d1 = px
            d2 = py
            if bol:
                d1 = t1
                d2 = t2
            rwr, xt, yt, xd, yd, xp, yp, same = simulate(t1, t2, dx, dy, d1, d2, actions[a], blockup, blockdown, blockleft, blockright, bol)

            nxt = xt+5*yt
            if same:
                nxt += 25
            vl = -10000
            for m in range(6):
                vl = max(vl,Q[int(nxt)][m])
            if s!=ds+25 or a!=1:
                Q[s][a] = (1-alp)*Q[s][a] + (alp)*(rwr+y*vl)
            s = int(nxt)
            rw += dis*rwr
            dis*=y
            it += 1
        arr.append(rw)
    
    ans = [actions[np.argmax(Q[i])] for i in range(50)]

    plt.plot(range(1,2001), arr)
    plt.xlabel('The Episodes number')
    plt.ylabel('The Sum of discounted rewards')
    plt.title('Sum of discounted rewards vs the Training Episodes number')
    plt.show()
    return ans

def sarsa(domain, eps=0.1):
    px, py, dx, dy, tx, ty = domain
    ps = px+5*py
    ds = dx+5*dy
    t = tx+5*ty
    
    Q = [[0 for i in range(6)] for j in range(50)]
    actions = ['Pickup','Putdown','North','South','East','West']
    blockup, blockdown, blockleft, blockright = preprocessing()
    Q[ds+25][1] = 20
    alp = 0.25
    y = 0.99

    arr = []
    for k in range(2000):
        s = t
        it = 0
        rw =0
        dis =1 
        while s!=ds and it<=499:
            chnc = int(100*random.random())
            a = 3
            if chnc<10:
                a = int(6*random.random())
            else:
                cur = Q[s][3]
                for j in range(5,-1,-1):
                    if Q[s][j]>cur:
                        cur = Q[s][j]
                        a = j
            
            bol = False
            if s>24:
                bol = True
            t1 = (s%25)%5
            t2 = (s%25)//5
            d1 = px
            d2 = py
            if bol:
                d1 = t1
                d2 = t2
            rwr, xt, yt, xd, yd, xp, yp, same = simulate(t1, t2, dx, dy, d1, d2, actions[a], blockup, blockdown, blockleft, blockright, bol)

            nxt = xt+5*yt
            if same:
                nxt += 25
            a_ = ''
            chnc = random.random()
            if chnc<eps:
                a_ = int(6*random.random())
            else:
                a_ = np.argmax(Q[nxt])

            if s!=ds+25 or a!=1:
                Q[s][a] = (1-alp)*Q[s][a] + (alp)*(rwr+y*Q[nxt][a_])
            s = int(nxt)
            rw +=dis*rwr
            dis*=y
            it += 1
        arr.append(rw)
    
    ans = [actions[np.argmax(Q[i])] for i in range(50)]

    plt.plot(range(1,2001), arr)
    plt.xlabel('The episodes number')
    plt.ylabel('The sum of discounted rewards')
    plt.title('Sum of discounted rewards vs the Training Episodes numbers')
    plt.show()
    return ans

def sarsa_decay(domain, eps=0.1):
    px, py, dx, dy, tx, ty = domain
    ps = px+5*py
    ds = dx+5*dy
    t = tx+5*ty
    
    Q = [[0 for i in range(6)] for j in range(50)]
    actions = ['Pickup','Putdown','North','South','East','West']
    blockup, blockdown, blockleft, blockright = preprocessing()
    Q[ds+25][1] = 20
    alp = 0.25
    y = 0.99

    arr = []
    for k in range(2000):
        s = t
        rw=0
        dis =1
        it = 1
        while s!=ds and it<=500:
            chnc = random.random()
            a = 3
            if chnc<eps/it:
                a = int(6*random.random())
            else:
                cur = Q[s][3]
                for j in range(5,-1,-1):
                    if Q[s][j]>cur:
                        cur = Q[s][j]
                        a = j
            
            bol = False
            if s>24:
                bol = True
            t1 = (s%25)%5
            t2 = (s%25)//5
            d1 = px
            d2 = py
            if bol:
                d1 = t1
                d2 = t2
            rwr, xt, yt, xd, yd, xp, yp, same = simulate(t1, t2, dx, dy, d1, d2, actions[a], blockup, blockdown, blockleft, blockright, bol)

            nxt = xt+5*yt
            if same:
                nxt += 25
            a_ = ''
            chnc = random.random()
            if chnc<eps/it:
                a_ = int(6*random.random())
            else:
                a_ = np.argmax(Q[nxt])

            if s!=ds+25 or a!=1:
                Q[s][a] = (1-alp)*Q[s][a] + (alp)*(rwr+y*Q[nxt][a_])
            s = int(nxt)
            rw += dis*rwr
            dis*=y
            it += 1
        arr.append(rw)
    
    ans = [actions[np.argmax(Q[i])] for i in range(50)]

    plt.plot(range(1,2001), arr)
    plt.xlabel('The episodes number')
    plt.ylabel('The sum of discounted rewards')
    plt.title('Sum of discounted rewards vs the Training Episodes numbers')
    plt.show()
    return ans
            
def simulate(xt, yt, xd, yd, xp, yp , a, blockup, blockdown, blockleft, blockright, bol):
    
    if xt==xd and xd==xp and yt==yd and yp==yt:
        if a == 'Pickup':
            bol = True
            return -1, xt, yt, xd, yd, xp, yp, bol
        elif a == 'Putdown':
            if bol:
                bol = False
                return 20, xt, yt, xd, yd, xp, yp, bol
            else:
                bol = False
                return -1, xt, yt, xd, yd, xp, yp, bol
        else:
            if a == 'North':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 5*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt, yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 5*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 5*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                else:
                    if xt + 5*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
            elif a == 'West':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 5*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1, yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 5*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 5*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                else:
                    if xt + 5*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
            elif a == 'South':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 5*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt, yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 5*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 5*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
                else:
                    if xt + 5*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
            elif a == 'East':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 5*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1, yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 5*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 5*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                else:
                    if xt + 5*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
    elif a == 'Pickup':
        if xt==xp and yt==yp:
            return -1, xt, yt, xd, yd, xp, yp, True
        else:
            return -10, xt, yt, xd, yd, xp, yp, bol
    elif a == 'Putdown':
        if xt==xp and yt ==yp:
            return -1, xt, yt, xd, yd,xp, yp, False
        else:
            return -10, xt, yt, xd, yd, xp, yp, bol
    elif a == 'North':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 5*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt, yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 5*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 5*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        else:
            if xt + 5*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
    elif a == 'West':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 5*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1, yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 5*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 5*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        else:
            if xt + 5*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
    elif a == 'South':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 5*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt, yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 5*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 5*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
        else:
            if xt + 5*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
    elif a == 'East':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 5*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1, yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 5*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 5*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        else:
            if xt + 5*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
    else:
        raise Exception("Unauthorized input")  


def preprocessing():
    blockup = {20, 21, 22, 23, 24}
    blockdown = {0, 1,2, 3, 4}
    blockleft = {0 ,5, 10, 15, 20, 1, 6, 3, 8, 17, 22}
    blockright = {4, 9, 14, 19, 24, 0, 5, 2, 7, 16, 21}
    return blockup, blockdown, blockleft, blockright

answ = sarsa_decay((4,4,0,4,3,3))
print(answ)  



'''




#######################################################################3 part 4  #######################################################################3



'''

import random
import numpy as np
import matplotlib.pyplot as plt

def q_learn(domain, eps=0.1):
    px, py, dx, dy, tx, ty = domain
    ps = px+5*py
    ds = dx+5*dy
    t = tx+5*ty
    
    Q = [[0 for i in range(6)] for j in range(50)]
    actions = ['Pickup','Putdown','North','South','East','West']
    blockup, blockdown, blockleft, blockright = preprocessing()
    Q[ds+25][1] = 20
    
    alp = float(input("Enter your value of alpha here: "))
    y = 0.99

    arr = []
    for k in range(2000):
        s = t
        it = 0
        rw = 0
        dis = 1
        while s!=ds and it<499:
            chnc = int(100*random.random())
            a = 3
            if chnc<100*eps:
                a = int(6*random.random())
            else:
                cur = Q[s][3]
                for j in range(5,-1,-1):
                    if Q[s][j]>cur:
                        cur = Q[s][j]
                        a = j
            
            bol = False
            if s>24:
                bol = True
            t1 = (s%25)%5
            t2 = (s%25)//5
            d1 = px
            d2 = py
            if bol:
                d1 = t1
                d2 = t2
            rwr, xt, yt, xd, yd, xp, yp, same = simulate(t1, t2, dx, dy, d1, d2, actions[a], blockup, blockdown, blockleft, blockright, bol)

            nxt = xt+5*yt
            if same:
                nxt += 25
            vl = -10000
            for m in range(6):
                vl = max(vl,Q[int(nxt)][m])
            if s!=ds+25 or a!=1:
                Q[s][a] = (1-alp)*Q[s][a] + (alp)*(rwr+y*vl)
            s = int(nxt)
            rw += dis*rwr
            dis *= y
            it += 1
        arr.append(rw)
    
    ans = [actions[np.argmax(Q[i])] for i in range(50)]

    plt.plot(range(1,2001), arr)
    plt.xlabel('The episodes number')
    plt.ylabel('The sum of discounted rewards')
    plt.title('Sum of discounted rewards vs the number of Training episodes')
    plt.show()
    return ans
            
def simulate(xt, yt, xd, yd, xp, yp , a, blockup, blockdown, blockleft, blockright, bol):
    
    if xt==xd and xd==xp and yt==yd and yp==yt:
        if a == 'Pickup':
            bol = True
            return -1, xt, yt, xd, yd, xp, yp, bol
        elif a == 'Putdown':
            if bol:
                bol = False
                return 20, xt, yt, xd, yd, xp, yp, bol
            else:
                bol = False
                return -1, xt, yt, xd, yd, xp, yp, bol
        else:
            if a == 'North':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 5*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt, yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 5*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 5*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                else:
                    if xt + 5*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
            elif a == 'West':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 5*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1, yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 5*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 5*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                else:
                    if xt + 5*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
            elif a == 'South':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 5*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt, yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 5*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 5*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
                else:
                    if xt + 5*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
            elif a == 'East':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 5*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1, yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 5*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 5*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                else:
                    if xt + 5*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
    elif a == 'Pickup':
        if xt==xp and yt==yp:
            return -1, xt, yt, xd, yd, xp, yp, True
        else:
            return -10, xt, yt, xd, yd, xp, yp, bol
    elif a == 'Putdown':
        if xt==xp and yt ==yp:
            return -1, xt, yt, xd, yd,xp, yp, False
        else:
            return -10, xt, yt, xd, yd, xp, yp, bol
    elif a == 'North':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 5*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt, yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 5*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 5*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        else:
            if xt + 5*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
    elif a == 'West':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 5*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1, yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 5*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 5*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        else:
            if xt + 5*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
    elif a == 'South':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 5*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt, yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 5*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 5*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
        else:
            if xt + 5*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
    elif a == 'East':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 5*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1, yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 5*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 5*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        else:
            if xt + 5*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
    else:
        raise Exception("Unauthorized input")  


def preprocessing():
    blockup = {20, 21, 22, 23, 24}
    blockdown = {0, 1,2, 3, 4}
    blockleft = {0 ,5, 10, 15, 20, 1, 6, 3, 8, 17, 22}
    blockright = {4, 9, 14, 19, 24, 0, 5, 2, 7, 16, 21}
    return blockup, blockdown, blockleft, blockright

answ = q_learn((4,4,0,4,3,3))

'''
###############################################################################3 part 5 ###################################################################

'''
import random
import numpy as np
import matplotlib.pyplot as plt

def sarsa_decay(domain, eps=0.1):
    px, py, dx, dy, tx, ty = domain
    ps = px+10*py
    ds = dx+10*dy
    t = tx+10*ty
    
    Q = [[0 for i in range(6)] for j in range(200)]
    actions = ['Pickup','Putdown','North','South','East','West']
    blockup, blockdown, blockleft, blockright = preprocessing()
    Q[ds+100][1] = 20
    alp = 0.25
    y = 0.99

    arr = []
    for k in range(10000):
        s = t
        rw=0
        dis =1
        it = 1
        while s!=ds and it<=2000:
            chnc = random.random()
            a = 3
            if chnc<eps/it:
                a = int(6*random.random())
            else:
                cur = Q[s][3]
                for j in range(5,-1,-1):
                    if Q[s][j]>cur:
                        cur = Q[s][j]
                        a = j
            
            bol = False
            if s>99:
                bol = True
            t1 = (s%100)%10
            t2 = (s%100)//10
            d1 = px
            d2 = py
            if bol:
                d1 = t1
                d2 = t2
            rwr, xt, yt, xd, yd, xp, yp, same = simulate(t1, t2, dx, dy, d1, d2, actions[a], blockup, blockdown, blockleft, blockright, bol)

            nxt = xt+10*yt
            if same:
                nxt += 100
            a_ = ''
            chnc = random.random()
            if chnc<eps/it:
                a_ = int(6*random.random())
            else:
                a_ = np.argmax(Q[nxt])

            if s!=ds+100 or a!=1:
                Q[s][a] = (1-alp)*Q[s][a] + (alp)*(rwr+y*Q[nxt][a_])
            s = int(nxt)
            rw += dis*rwr
            dis*=y
            it += 1
        arr.append(rw)
    
    ans = [actions[np.argmax(Q[i])] for i in range(200)]

    #plt.plot(range(1,10001), arr)
    #plt.xlabel('The episodes number')
    #plt.ylabel('The sum of discounted rewards')
    #plt.title('Sum of discounted rewards vs the Training Episodes numbers')
    #plt.show()
    return ans, arr


def simulate(xt, yt, xd, yd, xp, yp , a, blockup, blockdown, blockleft, blockright, bol):
    
    if xt==xd and xd==xp and yt==yd and yp==yt:
        if a == 'Pickup':
            bol = True
            return -1, xt, yt, xd, yd, xp, yp, bol
        elif a == 'Putdown':
            if bol:
                bol = False
                return 20, xt, yt, xd, yd, xp, yp, bol
            else:
                bol = False
                return -1, xt, yt, xd, yd, xp, yp, bol
        else:
            if a == 'North':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 10*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt, yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 10*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 10*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                else:
                    if xt + 10*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
            elif a == 'West':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 10*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1, yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 10*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 10*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                else:
                    if xt + 10*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
            elif a == 'South':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 10*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt, yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 10*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 10*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
                else:
                    if xt + 10*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
            elif a == 'East':
                rand = random.random()
                choosing =int(100*(rand))
                if choosing <85:
                    if xt + 10*yt in blockright:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt+1, yt, xd, yd, xp+1, yp, bol
                        else:
                            return -1, xt+1, yt, xd, yd, xp, yp, bol
                elif choosing >= 85 and choosing<90:
                    if xt + 10*yt in blockup:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                        else:
                            return -1, xt, yt+1, xd, yd, xp, yp, bol
                elif choosing>=90 and choosing<95:
                    if xt + 10*yt in blockdown:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                        else:
                            return -1, xt, yt-1, xd, yd, xp, yp, bol
                else:
                    if xt + 10*yt in blockleft:
                        return -1, xt, yt, xd, yd, xp, yp, bol
                    else:
                        if bol == True:
                            return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                        else:
                            return -1, xt-1, yt, xd, yd, xp, yp, bol
    elif a == 'Pickup':
        if xt==xp and yt==yp:
            return -1, xt, yt, xd, yd, xp, yp, True
        else:
            return -10, xt, yt, xd, yd, xp, yp, bol
    elif a == 'Putdown':
        if xt==xp and yt ==yp:
            return -1, xt, yt, xd, yd,xp, yp, False
        else:
            return -10, xt, yt, xd, yd, xp, yp, bol
    elif a == 'North':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 10*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt, yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 10*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 10*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        else:
            if xt + 10*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
    elif a == 'West':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 10*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1, yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 10*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 10*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        else:
            if xt + 10*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
    elif a == 'South':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 10*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt, yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 10*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1,yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 10*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
        else:
            if xt + 10*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
    elif a == 'East':
        rand = random.random()
        choosing =int(100*(rand))
        if choosing <85:
            if xt + 10*yt in blockright:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt+1, yt, xd, yd, xp+1, yp, bol
                else:
                    return -1, xt+1, yt, xd, yd, xp, yp, bol
        elif choosing >= 85 and choosing<90:
            if xt + 10*yt in blockup:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt+1, xd, yd, xp, yp+1, bol
                else:
                    return -1, xt, yt+1, xd, yd, xp, yp, bol
        elif choosing>=90 and choosing<95:
            if xt + 10*yt in blockdown:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt,yt-1, xd, yd, xp, yp-1, bol
                else:
                    return -1, xt, yt-1, xd, yd, xp, yp, bol
        else:
            if xt + 10*yt in blockleft:
                return -1, xt, yt, xd, yd, xp, yp, bol
            else:
                if bol == True:
                    return -1, xt-1,yt, xd, yd, xp-1, yp, bol
                else:
                    return -1, xt-1, yt, xd, yd, xp, yp, bol
    else:
        raise Exception("Unauthorized input")

def preprocessing():
    blockup = {90, 91, 92, 93, 94, 95, 96, 97,98,99}
    blockdown = {0, 1,2, 3, 4, 5, 6, 7, 8, 9}
    blockleft = {0 ,10, 20, 30, 40, 50 ,60 ,70, 80, 90, 1,11, 21, 31, 4, 14, 24, 34, 8, 18, 28, 38, 63, 73, 83, 93, 46, 56, 66, 76, 68, 78, 88, 98}
    blockright = {9 ,19, 29, 39, 49, 59 , 69 ,79, 89, 99, 0,10, 20, 30, 3, 13, 23, 33, 7, 17, 27, 37, 62, 72, 82, 92, 45, 55, 65, 75, 67, 77, 87, 97}
    return blockup, blockdown, blockleft, blockright


answ,arr1 = sarsa_decay((4,0,6,5,2,4))

ansp1,arr2 = sarsa_decay((0,1,0,9,3,9))

an,arr3 = sarsa_decay((6,5,0,1,2,8))

ans1,arr4 = sarsa_decay((9,0,8,9,6,6))

a1,arr5 = sarsa_decay((8,9,6,5,8,1))

arr = arr1
for i in range(len(arr)):
    arr[i] += arr2[i] + arr3[i] + arr4[i] + arr5[i]
    arr[i] /= 5
plt.plot(range(1,10001), arr)
plt.xlabel('The episodes number')
plt.ylabel('Average of Sum of discounted rewards on  5 instances')
plt.title('Avg. Sum of rewards vs the Episode numbers')
plt.show()


'''

