import math

# Imaginemos que uma empresa de frete faz entregas para os estados de MG, SP, RJ, RR e RS. Para que haja um gasto
# menor de tempo e gasolina, esse programa foi criado, para buscar pelo melhor trajeto entre os objetivos.
# Como protótipo, utilizamos as coordenadas de um plano cartesiano de duas dimensões para os estados em questão.
# Esse programa foi feito para fins didáticos de desenvolvimento de software de automação e logística.

# Variáveis e listas iniciais
base = (0, 0)
enderecos = []
sequencia_logica = []


# Função para cálculo de distância no plano cartesiano
def distancia(x0, x1, y0, y1):
    a = x1 - x0
    b = y1 - y0
    dist = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

    return dist


# Dicionário com estados e suas coordenadas
locais = {
    "SP": (15, 8),
    "MG": (-4, 1),
    "RJ": (7, -9),
    "RR": (10, 19),
    "RS": (2, -14)
}

# Seleciona quais serão os estados de entrega
while True:
    endereco = input("Estado: ")
    if endereco != "nn":
        enderecos.append(endereco)
    else:
        break


# Inicia o loop para verificar a distância entre os estados
while len(enderecos) > 0:

    # O nome do estado e sua distância mais próxima da base é o primeiro da lista de adicionados
    nome_proximo = enderecos[0]
    distancia_proximo = distancia(base[0], locais[nome_proximo][0], base[1], locais[nome_proximo][1])

    # Para cada item da lista, verifica-se a menor distância desde a base até o mesmo
    for item in enderecos:
        d = distancia(base[0], locais[item][0], base[1], locais[item][1])
        if d <= distancia_proximo:
            nome_proximo = item
            d = distancia_proximo

    # Adiciona-se o mais próximo da base na sequência lógica
    sequencia_logica.append(nome_proximo)

    # As coordenadas da base passam a ser a do local selecionado anteriormente (atual)
    base = locais[nome_proximo]

    i = 0

    # Remove-se o local adicionado da lista de destinos
    for item in enderecos:
        if item == nome_proximo:
            enderecos.pop(i)
            break
        else:
            i += 1

# Mostra qual a sequência lógica a se seguir para menor distância
print("Melhor rota a se seguir: ", end="")
for item in sequencia_logica:
    print(item, end=" ")
