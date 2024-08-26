import pandas as pd
import matplotlib.pyplot as plt


# Cria a classe Investimentos com os dados que serão requeridos
class Investimentos:
    def __init__(self, nome, valor, taxa, periodo):
        self.nome = nome
        self.valor = valor
        self.taxa = taxa
        self.periodo = periodo


# Cria um dicionario vazio para receber os dados
investimentos = {}

# O usuario digita quantos investimentos ele possui
qtd_investimentos = int(input("Digite a quantidade de investimentos que possui "))

# Cria um laço para receber os dados digitados pelo usuario
for count in range(1, qtd_investimentos + 1):

    nome = input("Digite o nome de investimento: ")
    valor = int(input("Digite o valor do investimento: "))
    taxa = float(input("Digite a taxa do tipo de investimento: "))
    periodo = int(input("Digite o periodo de investimento: "))

    # Cria o dicionario com os dados digitados pelo usuario
    investimentos[f"Invest{count}"] = Investimentos(nome, valor, taxa, periodo)

# Cria um laço para receber o dicionario com os seus valores
l_investmentos = [i.__dict__ for i in investimentos.values()]

# Recebe os dados e importa para o pandas com chave e valor
df_investimentos = pd.DataFrame(l_investmentos, index=investimentos.keys())
df_investimentos["Retorno"] = df_investimentos.apply(
    lambda l: l["valor"] * (1 + l["taxa"]) ** l["periodo"], axis=1
)

print(df_investimentos)

# cria o grafico bar para mostrar os investimentos
df_investimentos.plot(kind="bar", y="Retorno", legend="none")
plt.title("Retorno dos investimentos")
plt.xlabel("Investimentos")
plt.ylabel("Retorno em Reais")
plt.show()
