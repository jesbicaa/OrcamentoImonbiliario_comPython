# APARTAMENTOS
def apartamento(quarto, vaga, crianca):
    # Valor inicial: R$700,00 / 1 Quarto
    apt_valorTotal = 700

    # Caso queira 2 Quartos, + R$200
    if quarto == '2':
        apt_valorTotal += 200

    # Caso queira 2 vagas para o carro, + R$300,00
    if vaga == '2':
        apt_valorTotal += 300

    # Caso não tenha crianças tem 5% de desconto no aluguel
    if crianca == 'N':
        apt_valorTotal *= 0.95
    return apt_valorTotal

# CASAS
def casa(quarto, vaga):
    # Valor inicial: R$900,00 / 1 Quarto
    casa_valorTotal = 900

    # Caso queira 2 Quartos, + R$250
    if quarto == '2':
        casa_valorTotal += 250

    # Caso queira 1 vaga a mais para o carro, + R$300,00
    if vaga == '2':
        casa_valorTotal += 300

    return casa_valorTotal

# ESTUDIO
def estudio(vaga):
    # Valor inicial: R$1200,00
    est_valorTotal = 1200

    # Caso queira vaga para o carro + R$250,00 (2 vagas), mais que 2, será acrescentado R$60,00 por vaga
    if vaga == 2:
        est_valorTotal += 250
    elif vaga >= 3:
        est_valorTotal += (250 + 60 * (vaga -  1))

    return est_valorTotal