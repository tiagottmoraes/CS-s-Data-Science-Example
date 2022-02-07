def conta_ruas_lockdown(N,A,B):
    
    contagem = 0
    for i in range(0,N):
        if i%A == 0 or i%B == 0:
            contagem += 1    
    return contagem

print(conta_ruas_lockdown(1000000,28,32))








