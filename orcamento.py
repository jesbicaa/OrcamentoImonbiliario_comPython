import csv

def calculoContrato(aluguel, num_parcela):
    # O contrato imobiliário é de R$ 2.000,00 divididos em até 5 vezes
    valorParcelado = (2000 / num_parcela) + aluguel

    # Mostrar o valor do aluguel mensal contendo o valor do contrato que pode ser parcelado em até 5x
    print(f'Durante {num_parcela} mes(es) o valor do aluguel ({aluguel}) vai ser: R${valorParcelado}')

    return valorParcelado

def arqCsv(aluguel, parcelas):
    # Pode gerar um arquivo “.csv” com as 12 parcelas do orçamento
    aluguel_fixo = aluguel
    valor_parcela_contrato = 2000 / parcelas
    
    nome_arquivo = "orcamento_RM.csv"
    
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8-sig') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';')
        escritor.writerow(['Mes', 'Aluguel Base', 'Parcela Contrato', 'Total Mensal'])
        
        for i in range(1, 13):
            p_contrato = valor_parcela_contrato if i <= parcelas else 0
            total = aluguel_fixo + p_contrato
            escritor.writerow([i, f"R$ {aluguel_fixo:.2f}", f"R$ {p_contrato:.2f}", f"R$ {total:.2f}"])
            
    print(f"Sucesso! O arquivo '{nome_arquivo}' foi gerado na sua pasta.")