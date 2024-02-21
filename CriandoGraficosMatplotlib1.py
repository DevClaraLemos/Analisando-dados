import matplotlib.pyplot as plt

Quantidade = [10, 15, 8, 12, 15, 10]
nomes = ['MPB', 'Forró', 'Rock', 'Pop', 'Funk', 'Reggae']  # Adicionei 'Reggae'
cores = ['purple', 'purple', 'purple', 'purple', 'purple', 'purple']

plt.bar(nomes, Quantidade, color=cores)
plt.xlabel('Estilos musicais')
plt.ylabel('')
plt.title('Os melhores estilos de músicas')

for i, valor in enumerate(Quantidade):
    plt.text(i, valor + 1, str(valor), ha='center', va='bottom')

plt.show()
