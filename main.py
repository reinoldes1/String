#url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
url = " "
print (url)

# Sanitização da URL
url = url.replace(" ", "")

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia")

# Separa a base dos parametros
interrogacao = url.find('?')

url_base = url [:interrogacao]
print (url_base)

url_parametros = url [interrogacao+1:]
print (url_parametros)

# Busca os valores 
parametro_de_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_de_busca)
indice_valor = indice_parametro + len(parametro_de_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
valor = url_parametros[indice_valor:indice_e_comercial]

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print (valor)

# https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100