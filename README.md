# String
Aula de string

Entendendo o formato da url
-------------------------------

https://twiter.com/search?
q=alura&src=typed_query
q - query(consulta)
& - separa os parametros
src - source (origem da consulta)
typed_query - consulta digitada

https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100


Aula 1 Introdução ao fatiamento de strings
-------------------------------

Usa-se o [] para selecionar determinada area da string, exemplo:

    url = "bytebank.com/cambio?moedaOrigem=real"
    url_base = url [0:19] 
    print (url_base)

Ira printar "bytebank.com/cambio" sempre colocar no [] 1 a mais

Strings são imutaveis


Aula 2 Utilizando metodos de strings
-------------------------------

https://cursos.alura.com.br/search?query=python

? separa a base da url dos parametros

query=python
query - consulta
=python - pesquisa feita pelo usuario

usar o [.find] para achar o caractere "?" na url

Criação do parametro de busca e utilizando o find e len para determinar o inicio e final desse parametro e printar o valor

criação do parametro do & para simbolizar o final do valor

Utilizar a condição if para verificar aonde se encontra o parametro e fazer o fatiamento

if indice_e_comercial == -1:(caso não encontre o & apos o indice)
    valor = url_parametros[indice_valor:]

e utilizando o else para caso ache o & apos o indice finalizar aonde o & se encontra

else:
    valor = url_parametros[indice_valor:indice_e_comercial]

