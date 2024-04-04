#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel('data.xlsx')

# Agrupar o índice de morte por causa e somar
soma_mortes_por_causa = df.groupby('Cause')['Death rate per 100 000 population'].sum()

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
soma_mortes_por_causa.plot(kind='bar')
plt.xlabel('Causa da Morte')
plt.ylabel('Taxa de Mortalidade por 100.000 habitantes')
plt.title('Índice de Mortalidade por Causa')
plt.xticks(rotation=45, ha='right') 
plt.tight_layout()
plt.show()


# In[50]:


import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel('data.xlsx')

# Agrupar o índice de mortalidade por faixa etária e somar
soma_mortalidade_por_idade = df.groupby('Age Group')['Death rate per 100 000 population'].sum()

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
soma_mortalidade_por_idade.plot(kind='bar')
plt.xlabel('Faixa Etária')
plt.ylabel('Índice de Mortalidade por 100.000 habitantes')
plt.title('Índice de Mortalidade por Faixa Etária')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()  
plt.show()


# In[51]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel('data.xlsx')

# Criar o dot chart usando seaborn
plt.figure(figsize=(12, 8))
sns.stripplot(x='Cause', y='Age Group', data=df, jitter=True, size=8)
plt.xlabel('Causa da Morte')
plt.ylabel('Faixa Etária')
plt.title('Distribuição de Faixas Etárias por Causa de Morte')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[49]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel('data.xlsx')

# Definir paleta de cores personalizada
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Criar o gráfico de barras com Seaborn
plt.figure(figsize=(15, 8))
sns.barplot(data=df, x='Age Group', y='Deaths', hue='Cause', palette=colors, width=2)
plt.xlabel('Faixa Etária')
plt.ylabel('Número de Mortes')
plt.title('Número de Mortes por Faixa Etária e Causa de Morte')
plt.xticks(rotation=45, ha='right')

# Ajustar a legenda
plt.legend(title='Causa de Morte', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()

