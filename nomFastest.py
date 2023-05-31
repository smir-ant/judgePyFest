# Импортируем библиотеки pandas и glob
import pandas as pd
import glob

# Создаем список файлов с расширением xlsx в заданной директории
# path = "1year"  # ❗❗❗ЕСЛИ ГОД ❗❗❗
path = "05year"  # ❗❗❗ ЕСЛИ ПОЛ ГОДА ❗❗❗
filenames = glob.glob(path + "/*.xlsx")

# Определяем функцию для обработки данных из файла excel
def process_data(filename):
    # Читаем данные из файла без указания листа
    df = pd.read_excel(filename)

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

# Создаем пустой список для хранения DataFrame
dfs = []

# Проходим по списку файлов в цикле
for filename in filenames:
    # Обрабатываем данные из текущего файла
    df = process_data(filename)

    # Добавляем столбец flow и приписку к user_id в зависимости от имени файла
    if filename.split('\\')[-1] == "1_1.xlsx":
        df["flow"] = "1"
        df["user_id"] = df["user_id"].astype(str) + "-1"
    elif filename.split('\\')[-1] == "1_2.xlsx":
        df["flow"] = "2"
        df["user_id"] = df["user_id"].astype(str) + "-2"
    # # Добавляем приписки в конец user_id в зависимости от номера файла
    # df = df.assign(user_id=df["user_id"].astype(str) + "-" + filename.split(".")[0][-1])  # дописываем -1 или -2 в конце

    # # Добавляем столбец flow в зависимости от номера файла
    # df = df.assign(flow=filename.split(".")[0][-1])

    # Добавляем обработанный dataframe в список результатов
    dfs.append(df)

# Соединяем результаты из всех файлов в один dataframe
df = pd.concat(dfs, ignore_index=True)

# Сортируем итоговый dataframe по колонке "time" по возрастанию
df = df.sort_values(by="time")

print(df)

# Выводим результат в файл nomFastest.xlsx без индексов слева
df.to_excel(f"{path}_nomFastest.xlsx", index=False)
