# импортируем pandas
import pandas as pd
import glob

# Создаем список файлов с расширением xlsx в заданной директории
path = "1year"  # ❗❗❗ЕСЛИ ГОД ❗❗❗
# path = "05year"  # ❗❗❗ ЕСЛИ ПОЛ ГОДА ❗❗❗
filenames = glob.glob(path + "/*.xlsx")

# Создаем пустой список для хранения DataFrame
dfs = []

# Проходим по списку файлов в цикле
for filename in filenames:
    # Обрабатываем данные из текущего файла
    df = pd.read_excel(filename)
    df["duration"] = df["submission_time"] - df["attempt_time"]


    # Добавляем столбец flow и приписку к user_id в зависимости от имени файла
    if filename.split('\\')[-1] == "1_1.xlsx":
        df["flow"] = "1"
        df["user_id"] = df["user_id"].astype(str) + "-1"
    elif filename.split('\\')[-1] == "1_2.xlsx":
        df["flow"] = "2"
        df["user_id"] = df["user_id"].astype(str) + "-2"

    dfs.append(df)

# Соединяем результаты из всех файлов в один dataframe
df = pd.concat(dfs, ignore_index=True)


# группируем данные по user_id и подсчитываем количество правильных ответов
correct_answers = df[df["status"] == "correct"].groupby("user_id")["status"].count().reset_index(name="correct_answers")

# группируем данные по user_id и находим время начала и окончания олимпиады для каждого пользователя
start_time = df.groupby("user_id")["attempt_time"].min().reset_index(name="start_time")
end_time = df[df["status"] == "correct"].groupby("user_id")["submission_time"].max().reset_index(name="end_time")

# объединяем данные по user_id в один dataframe
results = pd.merge(correct_answers, start_time, on="user_id")
results = pd.merge(results, end_time, on="user_id")

# создаем новую колонку с общим временем на олимпиаду для каждого пользователя
results["total_time"] = results["end_time"] - results["start_time"]

# сортируем данные по количеству правильных ответов и общему времени по возрастанию
results = results.sort_values(by=["correct_answers", "total_time"], ascending=[False, True])

if path == "05year":  # добавляем дополнительно столбики без flow если полугодовые(так как они в один поток)
    results = results.join(df[["user_id", "last_name", "first_name"]].drop_duplicates().set_index("user_id"), on="user_id")
    
    # выбираем нужные колонки и меняем их порядок
    results = results[["user_id", "last_name", "first_name", "correct_answers", "total_time", "start_time", "end_time"]]
    
else:  # если выбраны годовые ребята (они в два потока, поэтому добавим flow)
    results = results.join(df[["user_id", "flow", "last_name", "first_name"]].drop_duplicates().set_index("user_id"), on="user_id")
    
    # выбираем нужные колонки и меняем их порядок
    results = results[["user_id", "flow", "last_name", "first_name", "correct_answers", "total_time", "start_time", "end_time"]]


# выводим топ участников по количеству правильных ответов и общему времени без индексов
print(results.to_string(index=False))

results.to_excel(f"{path}_winner.xlsx", index=False)

