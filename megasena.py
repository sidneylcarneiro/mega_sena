import random

def calcula_premio(numeros_apostados: list[int], premio_total: float) -> float:
    numeros_validos = []
    for apostado in numeros_apostados:
        if apostado < 1 or apostado > 60:
            return 0.0 # inválido
        if apostado in numeros_validos:
            return 0.0 # repetido
        numeros_validos.append(apostado)
        
    if len(numeros_validos) >= 6 and len(numeros_validos) <= 15:
        numeros_sorteados = []
        s = 0
        while len(numeros_sorteados) < 6:
            # random.randint(1, 60) é o equivalente ao new Random().nextInt(59) + 1
            s = random.randint(1, 60) 
            if s not in numeros_sorteados:
                numeros_sorteados.append(s)
        
        acertos = 0
        for apostado in numeros_apostados:
            if apostado in numeros_sorteados:
                acertos += 1
                
        if acertos == 6:
            return premio_total # 100%
        elif acertos == 5:
            return premio_total * 0.2 # 20%
        elif acertos == 4:
            return premio_total * 0.05 # 5%
            
    return 0.0