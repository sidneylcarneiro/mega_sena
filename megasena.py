import random

DEZENAS_MINIMAS = 6
DEZENAS_MAXIMAS = 15
SENA = 6
QUINA = 5
QUADRA = 4
INVALIDO = 0.0

def validar_numeros(numeros_apostados: list[int]) -> bool:
    if not (DEZENAS_MINIMAS <= len(numeros_apostados) <= DEZENAS_MAXIMAS):
        return False
    
    if len(set(numeros_apostados)) != len(numeros_apostados):
        return False
        
    for apostado in numeros_apostados:
        if apostado < 1 or apostado > 60:
            return False
            
    return True

def sortear_numeros() -> list[int]:
    return random.sample(range(1, 61), SENA)

def contar_acertos(apostados: list[int], sorteados: list[int]) -> int:
    acertos = set(apostados).intersection(sorteados)
    return len(acertos)

def calcula_premio(numeros_apostados: list[int], premio_total: float) -> float:
    if not validar_numeros(numeros_apostados):
        return INVALIDO
    
    numeros_sorteados = sortear_numeros()
    acertos = contar_acertos(numeros_apostados, numeros_sorteados)
                
    if acertos == SENA:
        return premio_total 
    elif acertos == QUINA:
        return premio_total * 0.2 
    elif acertos == QUADRA:
        return premio_total * 0.05
            
    return INVALIDO
