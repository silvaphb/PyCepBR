from PyCepBR import BuscarCEP

buscador = BuscarCEP()

# Buscar por cep
resultado = buscador.porCep('64207203', texto=True)
print(resultado)

# Buscar por Informações
resultados = buscador.porInfo(rua='Prudente de Moraes', cidade='Parnaiba', uf='PI', texto=True)
print(resultados)

# Dados que cada buscador tem
data_criacao = buscador.criacao # Retorna a data de criação do buscador
usos = buscador.usos # Retorna a quantidade de usos (requisições) do buscador
