import matplotlib.pyplot as plt

ans = list(map(str, range(1980,2014)))
data.loc['senegal', ans].plot(kind = 'line')
plt.title('Immigration du Senegal vesr Canada')
plt.ylabel('nombre de migrants')
plt.xlabel('Annees')
plt.show