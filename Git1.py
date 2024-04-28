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
directory = r'C:\Users\55119\Documents\Mackenzie\Semestre 2\ProjetoAplicadoI\ProjetoAplicadoI'
csv_file = os.path.join(directory, 'todas_tabelas.csv')  # Nome do arquivo CSV

# Verifica se o diretório existe; se não, cria o diretório
if not os.path.exists(directory):
    os.makedirs(directory)

# Abre o arquivo CSV para escrita
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Loop pelas tabelas encontradas
    for idx, table in enumerate(tables, start=1):
        table_data = []
        for row in table.find_all('tr'):
            row_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
            table_data.append(row_data)

        # Escreve os dados da tabela no arquivo CSV se houver dados
        if table_data:
            for row_data in table_data:
                writer.writerow(row_data)
        else:
            print(f'Tabela {idx} está vazia e não foi incluída.')

print(f'Todos os dados foram salvos em {csv_file}')
