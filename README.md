# PyCepBR

Biblioteca criada com o intuito de facilitar a busca de localizações em todo o Brasil, seja por CEP ou outros dados.

## Agilidade com poucas linhas
A biblioteca pode ser utilizada com apenas 3 linhas de codigos! Ja entregando oque ela pode oferecer de melhor. Veja um exemplo abaixo:

```
from PyCepBR import BuscarCEP

buscador = BuscarCEP()
resultado = buscador.porCep('64207203', texto=True)
print(resultado)
```

# Como instalar?
Rode esse comando em seu terminal:
```
pip install PyCepBR
```

## Como usar?
Inicialmente nesta versão é oferecido dois tipos de busca de localidades. A primeira é a por CEP, retornando em texto ou dicionario as informações dessa localidade (Ex: Rua, Cidade, Bairro, Unidade...) e a segunda é por 3 informações, rua, cidade e uf. Abaixo será possivel visualizar a forma de utilização das duas formas de busca:

```
from PyCepBR import BuscarCEP

buscador = BuscarCEP()

# Buscar por cep
resultado = buscador.porCep('64207203', texto=True)
print(resultado)

# Buscar por Informações
resultados = buscador.porInfo(rua='Prudente de Moraes', cidade='Parnaiba', uf='PI', texto=True)
print(resultados)
```
Se você notar nas duas formas tem o parametro `texto`. Ele é utilizado para definir qual vai ser o tipo de resposta da requisição, se for `True` ele retorna um texto formatado completo, se for `False` (definido por padrão) ele retorna um dicionario com as informações (Normalmente o dicionario entrega mais dados que o texto).

# Historia do PyCep
Inicialmente um simples codigo feito no celular utilizando o PyDroid 3, por volta de 2023. Hoje em dia (2026) estou no curso de Desenvolvimento de Sistemas e voltei a ativa no meu GitHub para criação de portfolio e armazenar oque eu for fazendo, como primeiro projeto dessa mudança foi aprimorar/refazer aquele codigo e disponibilizar para todos instalarem no Pypi. Espero que ajude! Até a proxima.
