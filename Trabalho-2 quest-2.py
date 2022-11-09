def somaImposto(taxaImposto, custo):

    resultado_imposto = custo + (custo * taxaImposto / 100)

    print(f'resultado imposto: {resultado_imposto:.2f}')
    
    return resultado_imposto
    
while True:
    
    taxaImposto = int(input('taxaImposto: '))
    
    if taxaImposto <= -1: break
    
    custo = int(input('custo: '))
    
    somaImposto(taxaImposto,custo)
    
    print('■'*10)
    