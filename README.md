# 🏠 Sistema de Orçamento Imobiliário - R.M. Imóveis

Este projeto é uma aplicação de terminal desenvolvida em Python para a gestão e simulação de orçamentos de aluguéis imobiliários. O sistema foi estruturado de forma modular para facilitar a manutenção e organização da lógica de negócio.

## 📋 Sobre o Projeto

O software permite que o usuário escolha entre diferentes tipos de imóveis, personalize opcionais como quartos e vagas de garagem, e visualize o impacto de taxas contratuais no valor mensal.

### Funcionalidades Principais
* **Seleção de Imóveis:** Opções entre Apartamento, Casa e Estúdio.
* **Cálculo Dinâmico:** Ajuste automático de valores com base no número de quartos e vagas.
* **Regras de Negócio:** Aplicação de descontos (ex: 5% para apartamentos sem crianças).
* **Gestão de Contrato:** Parcelamento da taxa fixa de R$ 2.000,00 em até 5 vezes.
* **Exportação de Dados:** Geração de relatório detalhado em formato `.csv` para os primeiros 12 meses.

---

## 🛠️ Estrutura do Sistema

O projeto está dividido em três módulos principais:
1.  **`app.py`**: Gerencia a interface com o usuário, entradas de dados e o fluxo principal da aplicação.
2.  **`imoveis.py`**: Contém as funções de cálculo de preços base e adicionais para cada categoria de imóvel.
3.  **`orcamento.py`**: Responsável pelos cálculos financeiros do contrato e pela lógica de exportação de arquivos.

---

## 🚀 Como Executar

1.  Certifique-se de ter o **Python 3.x** instalado.
2.  Clone este repositório:
    ```bash
    git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
    ```
3.  Acesse a pasta do projeto:
    ```bash
    cd nome-do-repositorio
    ```
4.  Execute a aplicação:
    ```bash
    python app.py
    ```

---

## 📊 Regras de Prepificação

| Tipo | Valor Base | Detalhes |
| :--- | :--- | :--- |
| **Apartamento** | R$ 700,00 | +R$ 200 (2º quarto), +R$ 300 (2ª vaga), -5% de desconto se não houver crianças. |
| **Casa** | R$ 900,00 | +R$ 250 (2º quarto), +R$ 300 (2ª vaga). |
| **Estúdio** | R$ 1.200,00 | +R$ 250 (2 vagas), +R$ 60 por vaga excedente a partir da 3ª. |

---

## 🎓 Contexto Acadêmico
Projeto desenvolvido como parte da grade curricular do curso de **Análise e Desenvolvimento de Sistemas**, com foco em lógica de programação, modularização e manipulação de arquivos.

---
💡 *Desenvolvido para fins de estudo e portfólio.*
