import matplotlib.pyplot as plt

ans = list(map(str,range(1980,2024)))
data.loc['senegal',ans].plot(kind = 'line')
plt.title('Immigration du Senegal vers canada')
plt.ylabel('Nombre de migrant' )
plt.xlabel('Annees')
plt.show