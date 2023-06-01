# импортируем библиотеку pandas
import pandas as pd
from shutil import copy  # для копирования и перемещения файла

df1 = pd.read_excel("raw/potok2.xlsx")  # читаем 05 + 2 (совмещенные потоки)
df2 = pd.read_excel("raw/potok05.xlsx")

# вычитаем данные одной таблицы из данных другой таблицы по строкам
df3 = df1[~df1.isin(df2)].dropna()

# сохраняем результат в новый файл в формате .xlsx
df3.to_excel("1year/1_2.xlsx", index=False)

copy("raw/potok1.xlsx", "1year/1_1.xlsx")
copy("raw/potok05.xlsx", "05year/05.xlsx")