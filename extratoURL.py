import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida")
    

    def get_url_base(self):
        interrogacao = self.url.find('?')
        url_base = self.url[:interrogacao]
        return url_base

    def get_url_parametros(self):
        interrogacao = self.url.find('?')
        url_parametros = self.url[interrogacao+1:]
        return url_parametros
    
    def get_valor_parametro(self, parametro_de_busca):
        indice_parametro = self.get_url_parametros().find(parametro_de_busca)
        indice_valor = indice_parametro + len(parametro_de_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]        
        return valor
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()
    
    def __eq__(self, other):
        return self.url == other.url
    
url = "https://bytebank.com/cambio?moedaDestino=real&quantidade=365&moedaOrigem=dolar"
extrator_url = ExtratorURL (url)
extrator_url_2 = ExtratorURL (url)
#extrator_url = ExtratorURL ("https://bytebank.com/cambio")
#extrator_url = ExtratorURL (None)
#extrator_url = ExtratorURL ("  ")
#print ("O tamanho da URL é: ", len(extrator_url))
#print(extrator_url)

print(id(extrator_url))
print(id(extrator_url_2))
print (extrator_url == extrator_url_2)

valor_dolar = 5.50
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "dolar" and moeda_destino == "real":
    conversao = int(valor_quantidade) * valor_dolar
    print("A conversão de " + valor_quantidade + " dolares é " + str(conversao) + " reais")
elif moeda_origem == "real" and moeda_destino == "dolar":
    conversao = int(valor_quantidade) / valor_dolar
    print("A conversão de " + valor_quantidade + " reais é " + str(conversao) + " dolares")
else:
    print(f"O cambio de {moeda_origem} para {moeda_destino} não está disponível.")




