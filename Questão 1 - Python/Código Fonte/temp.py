# -*- coding: utf-8 -*-
"""
"""
#1 Ler o arquivo house_infos.csv na forma de um dataframe.
import pandas as pd
house = pd.read_csv('house_infos.csv')
#b) Neste dataframe, qual a quantidade de casas que possuem “LotArea” > 5000 e “CentralAir” = N?
cont =0
for i in range (0,1459):
        if ((house.loc[i][1]>5000) and (house.loc[i][7]=='N')):
            cont=cont+1
print('Quantidade de casas que possuem “LotArea” > 5000 e “CentralAir” = {}'.format(cont))
#c) Filtrar dataframe para conter apenas as linhas que tenham “GrLivArea” > 2000
copy = house.filter(items=['GrLivArea'])
copy = copy.loc[copy['GrLivArea']>2000]
