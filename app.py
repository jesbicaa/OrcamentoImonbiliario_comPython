# Importar as funções das outras paginas para essa
from imoveis import *
from orcamento import *

# Funcao para o texto de opcao invalida
def op_invalida():
    return print('\n\n*************************************'), print('\nOpção Invalida! Selecione uma opção valida!\n'), print('*************************************\n\n')

# Funcao para perguntar quantos quartos o cliente quer no imovel
def op_quarto():
    opcao_quarto = ''

    while opcao_quarto != '1' and opcao_quarto != '2':
        opcao_quarto = input("Deseja 1 ou 2 quartos?\n  (1) Um Quarto / (2) Dois Quartos: ")
    
        if opcao_quarto != '1' and opcao_quarto != '2':
            op_invalida()
        
    return opcao_quarto

# Funcao para perguntar quantas vagas o cliente quer no imovel
def op_vagas():
    opcao_vagas = ''

    while opcao_vagas != '1' and opcao_vagas != '2':
        opcao_vagas = input("Deseja 1 ou 2 vagas para o carro?\n  (1) Uma Vaga / (2) Duas Vagas: ")
    
        if opcao_vagas != '1' and opcao_vagas != '2':
            op_invalida()
        
    return opcao_vagas

# Nome da empresa
print('\n*************************************')
print('R.M. Imoveis')
print('*************************************\n')

opcao_imovel = ''

# Formulario para selecionar o tipo de imovel
while opcao_imovel != 'A' and opcao_imovel != 'C' and opcao_imovel != 'E':

    opcao_imovel = input(''' Selecione qual tipo de imovel deseja alugar: 
                   (A) Apartamento - a partir de R$700,00  
                   (C) Casa - a partir de R$900,00
                   (E) Estidio - a partir de R$1200,00
                   
                   Digite a opção desejada: ''').upper()
    
    if opcao_imovel != 'A' and opcao_imovel != 'C' and opcao_imovel != 'E':
        op_invalida()

# Alerta  para o cliente do valor do contrato
print('\n**** Valor do contrato imobiliário é de R$2.000,00 divididos em até 5 vezes ***\n')


# APARTAMENTOS
if opcao_imovel == 'A':
    # Caso queira 2 Quartos, + R$200
    num_quarto = op_quarto()
    
    # Caso queira 1 vaga a mais para o carro, + R$300,00
    num_vaga = op_vagas()

    # Caso não tenha crianças tem 5% de desconto no aluguel
    print('\nCaso não tenha crianças, ganha 5% de desconto no aluguel\n')
    tem_crianca = ''

    while tem_crianca != 'S' and tem_crianca != 'N':
        tem_crianca = input("Vai morar criança junto?  (S) Sim / (N) Não: ").upper()

        if tem_crianca != 'S' and tem_crianca != 'N':
           op_invalida()

    valorTotal = apartamento(num_quarto, num_vaga, tem_crianca)

    print(f'Valor mensal do aluguel: R${valorTotal}')
# CASAS
elif opcao_imovel == 'C':
    # Caso queira 2 Quartos, + R$250
    num_quarto = op_quarto()

    # Caso queira 1 vaga a mais para o carro, + R$300,00
    num_vaga = op_vagas()

    valorTotal = casa(num_quarto, num_vaga)

    print(f'Valor mensal do aluguel: R${valorTotal}')

# ESTUDIO
elif opcao_imovel == 'E':
    # Caso queira vaga para o carro + R$250,00 (2 vagas), mais que 2, será acrescentado R$60,00 por vaga 
    while True:
        try: 
            vagaEst = int(input('Digite quantas vagas deseja no imovel: '))
            break
        except ValueError:
            print("Valor informado não é um numero")
        
    valorTotal = estudio(vagaEst)

    print(f'Valor mensal do aluguel: R${valorTotal:.2f}')

# FINAL
# O contrato imobiliário é de R$ 2.000,00 divididos em até 5 vezes
while True:
    try: 
        numParcelas = int(input('Digite quantas vezes deseja parcelar o contrato imimobiliário (Maximo 5x): '))

        if numParcelas >= 1 and numParcelas <= 5:
            break

        print('Valor precisa ser entre 1 a 5!')
    except ValueError:
        print("Valor informado não é um numero!")
    
# Mostrar o valor do aluguel mensal contendo o valor do contrato que pode ser parcelado em até 5x
valorcContrato = calculoContrato(valorTotal, numParcelas)

# Pode gerar um arquivo “.csv” com as 12 parcelas do orçamento
csv = ''

while csv != 'S' and csv != 'N':
    csv = input("Deseja baixar um arquivo 'csv' com as parcelas dos 12 primeiros meses?  (S) Sim / (N) Não: ").upper()
        
    if csv != 'S' and csv != 'N':
        op_invalida()

if csv == 'S':
    arquvo_csv = arqCsv(valorTotal, numParcelas)