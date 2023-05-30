# Импортируем библиотеку pandas
import pandas as pd

# Определяем функцию для обработки данных из файла excel
def process_data(file_name):
    # Читаем данные из файла без указания листа
    df = pd.read_excel(file_name)

    # Фильтруем строки, где status равен "correct"
    df = df[df["status"] == "correct"]

    # Вычисляем время решения задачи как разность между submission_time и attempt_time
    df["time"] = df["submission_time"] - df["attempt_time"]

    # Убираем дубликаты из таблицы
    df = df.drop_duplicates()

    # Группируем данные по user_id и выбираем минимальное время решения для каждого участника
    df = df.groupby("user_id")[["time", "last_name", "first_name"]].min().reset_index()

    # Сортируем строки по возрастанию времени решения
    df = df.sort_values(by="time")

    # Возвращаем обработанный dataframe
    return df

# Обрабатываем данные из файлов 1_1.xlsx и 1_2.xlsx
df1 = process_data("1_1.xlsx")
df2 = process_data("1_2.xlsx")

# Добавляем приписки в конец user_id в зависимости от файла
df1 = df1.assign(user_id=df1["user_id"].astype(str) + "-1")
df2 = df2.assign(user_id=df2["user_id"].astype(str) + "-2")

# Добавляем столбец flow в зависимости от файла
df1 = df1.assign(flow="1")
df2 = df2.assign(flow="2")

# Соединяем результаты из двух файлов в один dataframe
df = pd.concat([df1, df2], ignore_index=True)

# Сортируем итоговый dataframe по колонке "time" по возрастанию
df = df.sort_values(by="time")

# Выводим результат в файл nomFastest.xlsx без индексов слева
df.to_excel("nomFastest.xlsx", index=False)
