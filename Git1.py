import requests
from bs4 import BeautifulSoup
import csv
import os

# URL da página web
url = 'https://data.who.int/countries/076'

# Realiza a solicitação GET para obter o conteúdo da página
response = requests.get(url)
html = response.text

# Analisa o HTML usando BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontra todas as tabelas na página
tables = soup.find_all('table')

# Diretório onde os arquivos CSV serão salvos
directory = 'C:/Users/55119/Documents/Mackenzie/Semestre 2/ProjetoAplicadoI/Projeto-Aplicad'

# Verifica se o diretório existe; se não, cria o diretório
if not os.path.exists(directory):
    os.makedirs(directory)

# Loop pelas tabelas encontradas
for idx, table in enumerate(tables, start=1):
    # Inicializa uma lista vazia para armazenar os dados da tabela
    table_data = []

    # Loop pelas linhas da tabela
    for row in table.find_all('tr'):
        # Obtém os textos das células em cada linha e armazena em uma lista
        row_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
        # Adiciona a lista de dados da linha à lista de dados da tabela
        table_data.append(row_data)

    # Define o nome do arquivo CSV
    csv_file = os.path.join(directory, f'tabela_{idx}.csv')

    # Escreve os dados no arquivo CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escreve os dados da tabela no arquivo CSV
        for row_data in table_data:
            writer.writerow(row_data)

    print(f'Dados da tabela {idx} salvo em {csv_file}')
