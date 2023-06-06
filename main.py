import pandas as pd
import openpyxl


# Criando um DateFrame (tabela no Pandas)
# Cada coluna é uma series

df = pd.DataFrame(
    {
        'Name': [
            'Braund, Mr. Owen Harris',
            'Allen, Mr. William Henry',
            'Bonnell, Miss. Elizaneth'
        ],

        'Age': [22, 35, 58],
        'Sex': ['male', 'male', 'female'],
    }
)

#print(df)



# Dados de uma coluna

#print(df['Age'])



# Criar uma coluna

#series_married = pd.Series(['Yes', 'Yes', 'No'], name='Married')
#print(series_married)




# Valor máximo de uma coluna
#print(df['Age'].max())



# Estatísticas básicas
#print(df.describe())










# Analisar dados do Titanic

titanic = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv')
#print(titanic)

#print(titanic.head()) # 5 primeiras linhas
#print(titanic.head(10)) # 10 primeiras linhas
#print(titanic.tail()) # 5 últimas linhas
#print(titanic.dtypes) # Tipos dos dados

#Para cada uma das colunas, o tipo de dados usado é registrado. Os tipos de dados DataFramesão inteiros (int64), floats (float64) e strings (object).

#titanic.to_excel('titanic.xlsx', sheet_name='passengers', index=False) # transformar o DataFrame em Excel

#titanic_one = pd.read_excel('titanic.xlsx', sheet_name='passengers') # ler planilha Excel
#print(titanic_one.head())


#print(titanic['Age'].shape) # quantidade de linhas

age_sex = titanic[['Age', 'Sex']] # selecionar duas
#print(age_sex)

above_35 = titanic[titanic['Age'] > 35] # utilizar filtros
#print(above_35)
#print(titanic['Age'] > 35)
#print(above_35.shape) # quantidade de passageiros que satisfazem a condição

class_23 = titanic[titanic['Pclass'].isin([2, 3])] #  passageiros do Titanic das classes de cabine 2 e 3
#print(class_23)
class_2_3 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)] # também pode ser usado assim. Para utilizar o 'or' o símbolo é | , 'and' é &
#print(class_2_3)


age_no_na = titanic[titanic["Age"].notna()]
#print(age_no_na)
#print(age_no_na.shape)

adult_names = titanic.loc[titanic["Age"] > 35, "Name"] # nomes dos passageiros com mais de 35 anos
#print(adult_names)

#print(titanic.iloc[9:25, 2:5]) # linhas de 10 a 25 e colunas de 3 a 5
#titanic.iloc[0:3, 3] = "anonymous" # atribuir o nome "anonymous" às três primeiras linhas da 3ª coluna
#print(titanic['Name'])













