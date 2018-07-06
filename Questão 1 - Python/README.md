#  Projeto Data Science - Questão 1 

## O que vai ser feito?

####
## Requisitos

####a. Ler o arquivo house_infos.csv na forma de um dataframe.
####b. Neste dataframe, qual a quantidade de casas que possuem “LotArea” > 5000 e “CentralAir” = N?
####c. Filtrar dataframe para conter apenas as linhas que tenham “GrLivArea” > 2000.
####d. A partir do dataframe filtrado no item anterior, crie uma coluna “SalePrice”, os valores desta coluna deverão ser o resultado da seguinte expressão: (LotFrontage + log(LotArea) + TotalBsmtSF + GrLivArea) * OverallQual.
####e. Crie a coluna “AvgOverallQual”, a qual deve conter a média aritmética de OverallQual para cada YearBuilt.
####f. Tratar os casos em que há NaN nos resultados do cálculo dos dados da coluna “SalePrice”, preenchendo-os com 0 (zero).
####g. Ler o arquivo year_condition.csv na forma de um dataframe.
####h. Fazer um merge entre o dataframe final do arquivo house_infos.csv e do arquivo year_condition.csv com base na coluna YearBuilt. Desta forma, o dataframe resultante deverá conter uma nova coluna “YearCondition”.
####i. Agrupar por “YearBuilt”, “AvgOverallQual” e “YearCondition” e obter a média. Ordenar o dataframe resultante por “YearBuilt” de forma crescente.
####j. Os valores da coluna “SalePrice” devem estar com apenas duas casas decimais.
####k. Com o dataframe resultante, faça um gráfico de barras para SalePrice x YearBuilt.
####l. Utilizando um eixo y secundário no mesmo gráfico, acrescente um gráfico de linha para AvgOverallQual x YearBuilt.
####m. Salvar o gráfico em formato png com o nome house_analysis.png.
####n. Exportar o dataframe final para um arquivo pickle com nome processed_data.p

## 
## 
## 

