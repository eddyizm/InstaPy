import random
     
def interactUser():
    ob = []
    t = random.randint(0,6)
    if t == 0:
        ob.append('eddyizm')
        return ob
    elif t == 1:
        ob.append('bengreenfieldfitness')
        return ob
    elif t == 2:
        ob.append('theyoungturks')
        return ob
    elif t == 3:
        ob.append('nasa')
        return ob
    elif t == 4:
        ob.append('tacoma_krew')
        return ob
    elif t == 5:
        ob.append('sonyalpha')
        return ob
    else:
        ob.append('ocasio2018')
        return ob

