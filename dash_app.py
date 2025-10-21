import pandas as pd

def ler_excel(caminho, nome):
    print(f'Lendo o DataFrame {nome}')
    df = pd.read_excel(caminho)
    return df

df_2001_2012 = ler_excel('/Users/magnosouza/PycharmProjects/AnaliseCombustivel/data/mensal-estados-2001-a-2012.xlsx','Ano 2001 até 2012')
df_2013_2015 = ler_excel('/Users/magnosouza/PycharmProjects/AnaliseCombustivel/data/mensal-municipios-2013-a-2015.xlsx', 'Ano 2013 até 2015')
df_2016_2018 = ler_excel('/Users/magnosouza/PycharmProjects/AnaliseCombustivel/data/mensal-municipios-2016-a-2018.xlsx', 'Ano 2016 até 2018')
df_2019_2021 = ler_excel('/Users/magnosouza/PycharmProjects/AnaliseCombustivel/data/mensal-municipios-2019-a-2021.xlsx', 'Ano 2019 até 2021')
df_2022_2025 = ler_excel('/Users/magnosouza/PycharmProjects/AnaliseCombustivel/data/mensal-municipios-jan2022-2025.xlsx', 'Ano 2022 até 2025')

df_total = pd.concat([df_2001_2012, df_2013_2015, df_2016_2018, df_2019_2021, df_2022_2025])
df_total.to_excel('database_anp.xlsx')
print(f'Arquivo salvo com Sucesso ')