import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data_set.csv")
df.set_index('Country', inplace=True)

anos = list(map(str, range(1980, 2014)))
brasil = df.loc['Brazil', anos]
brasil_dict = {'ano': brasil.index.tolist(), 'imigrantes': brasil.values.tolist()}
dados_brasil = pd.DataFrame(brasil_dict)

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
ax.set_title('Imigração Brasil x Canada\n1980 a 2013')
ax.set_xlabel('Ano')
ax.set_ylabel('Quantidade Imigrantes')
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('plot_imigracao_br_can.png')

fig, axs = plt.subplots(1 , 2, figsize = (15,5))
axs[0].plot(dados_brasil['ano'],dados_brasil['imigrantes'])
axs[0].set_title('Imigração Brasil x Canada\n1980 a 2013')
axs[0].set_xlabel('Ano')
axs[0].set_ylabel('Quantidade Imigrantes')
axs[0].xaxis.set_major_locator(plt.MultipleLocator(5))
axs[0].grid

axs[1].boxplot(dados_brasil['imigrantes'])
axs[1].set_title('Imigração Brasil x Canada\n1980 a 2013')
axs[1].set_xlabel('Brasil')
axs[1].set_ylabel('Quantidade Imigrantes')
axs[1].xaxis.set_major_locator(plt.MultipleLocator(5))
axs[1].grid
plt.savefig('plot_quantidade_imigrante_br_can.png')

america = df.query('Region == "South America"')
america = america.sort_values('Total', ascending=True)
cores = []
for pais in america.index:
  if pais == 'Brazil':
    cores.append('green')
  else:
    cores.append('silver')
fig, ax = plt.subplots(figsize=(12,5))
ax.barh(america.index, america['Total'], color = cores)
ax.set_title('Imigração América do Sul para o Canadá')
ax.set_xlabel('Número de imigrantes')
ax.set_ylabel('')
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
for i, v in enumerate(america['Total']):
  ax.text(v+40, i, str(v), color='black', ha='left', va='center')
ax.set_frame_on(False)
ax.get_xaxis().set_visible(False)
plt.savefig('plot_america_do_sul.png')

fig, ax = plt.subplots(figsize=(12,5))
sns.set_theme()
top_10 = df.sort_values('Total', ascending = False).head(10)
sns.barplot(data = top_10, y = top_10.index, x ='Total' , orient ='h')
ax = sns.barplot(data=top_10, y=top_10.index, x='Total',orient='h')
ax.set(title= 'Países com maior imigração para o Canadá',
       xlabel = 'Numero de Imigrantes',
       ylabel = '')
plt.savefig('plot_mundo.png')
