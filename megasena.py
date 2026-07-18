import random

def megasena(num: list[int], valor: float) -> float:
    list = [] # válidos
    for n in num:
        if n < 1 or n > 60:
            return 0.0 # inválido
        if n in list:
            return 0.0 # repetido
        list.append(n)
        
    if len(list) >= 6 and len(list) <= 15:
        sort = []
        s = 0
        while len(sort) < 6:
            # random.randint(1, 60) é o equivalente ao new Random().nextInt(59) + 1
            s = random.randint(1, 60) 
            if s not in sort:
                sort.append(s)
        
        tot = 0
        for apostado in num:
            if apostado in sort:
                tot += 1
                
        if tot == 6:
            return valor # 100%
        elif tot == 5:
            return valor * 0.2 # 20%
        elif tot == 4:
            return valor * 0.05 # 5%
            
    return 0.0