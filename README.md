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


Aula 3 Aplicando orientação a objetos no projeto
-------------------------------

Criar um if statement que verifica se a url está vazia e retornar o erro com o raise(retorna o erro ao usuario) e o ValueError (que da o valor do erro)

replace - substitui um argumento passado 

(" ", "") substitui os espaços por nada

pode ser utilizado o .strip que retira todos os espaços
.lstrip (leftstrip) e .rstrip(right strip)

Transferencia de todo o codigo para classes

Caso (None), adicionar no sanitiza a verificação da url ser uma str


Aula 4 Validando a URL
-------------------------------


Utilizamos a biblioteca do python (import re)que significa Regular Expressions(RegEx)

dessa biblioteca usamos o compile para mostrar os padrões que estamos buscando separando por colchetes[]

utilizamos o .search para buscar esse padrao em uma string

adicionando um "?" ao lado do padrao buscado, significa que ele é opcional

adicionando chaves "{}" ao lado do padrao, é possivel adicionar quantas repetiçoes existem

Queremos ver se a url é igual ao padrao que procuramos, entao usamos o match ao inves do search, e para usar o match precisamos compilar nossa string utilizando o re.compile