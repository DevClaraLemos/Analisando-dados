import pandas as pd 
import matplotlib.pyplot as plt

data = {'Produto': ['Pizza', 'Hambúrguer', 'Hot Dog', 'Bolo de chocolate', 'Sorvete'],
        'Data de Fabricação': ['', '', '', '', ''],
        'Quantidade': [10, 15, 8, 12, 20]}
df = pd.DataFrame(data)

df['Data de Fabricação'] = pd.to_datetime(df['Data de Fabricação'])

df = df.sort_values('Data de Fabricação')

largura_barras = 0.6

# Use a coluna 'Quantidade' como altura das barras
plt.bar(df['Produto'], df['Quantidade'], color='purple', width=largura_barras)  

plt.title('As comidas mais gostosas')
plt.xlabel('Comidas')
plt.ylabel('')

plt.tight_layout()
plt.show()
