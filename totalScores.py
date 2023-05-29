import pandas as pd

df = pd.read_excel("1_1.xlsx")  # читаем xlsx файл в датафрейм

# создаем датафрейм с минимальным временем начала задания для каждого user_id
df_start = df.groupby("user_id", as_index=False)["attempt_time"].min()

# удаляем строки с неправильными ответами
df = df[df["status"] == "correct"]

# группируем данные по user_id и step_id и выбираем минимальное время отправления ответа для каждой пары
df = df.groupby(["user_id", "step_id"], as_index=False)[["submission_time", "first_name", "last_name"]].min()

# создаем новый датафрейм с количеством решенных задач и максимальным временем отправления ответа для каждого user_id
df_score = df.groupby("user_id", as_index=False).agg({"step_id": "count", "submission_time": "max", "first_name": "first", "last_name": "first"})

# объединяем df_score и df_start по user_id
df_score = pd.merge(df_score, df_start, on="user_id")

# добавляем столбец с продолжительностью решения в исходном формате
df_score["total_time"] = df_score["submission_time"] - df_score["attempt_time"]

# удаляем лишние столбцы
df_score = df_score.drop(columns=["submission_time", "attempt_time"])

# добавляем столбец с flow равным 1
df_score["flow"] = 1

# переименовываем столбцы
df_score.columns = ["user_id", "score", "first_name", "last_name", "total_time", "flow"]

# читаем xlsx файл в датафрейм
df2 = pd.read_excel("1_2.xlsx")

# создаем датафрейм с минимальным временем начала задания для каждого user_id
df_start2 = df2.groupby("user_id", as_index=False)["attempt_time"].min()

# удаляем строки с неправильными ответами
df2 = df2[df2["status"] == "correct"]

# группируем данные по user_id и step_id и выбираем минимальное время отправления ответа для каждой пары
df2 = df2.groupby(["user_id", "step_id"], as_index=False)[["submission_time", "first_name", "last_name"]].min()

# создаем новый датафрейм с количеством решенных задач и максимальным временем отправления ответа для каждого user_id
df_score2 = df2.groupby("user_id", as_index=False).agg({"step_id": "count", "submission_time": "max", "first_name": "first", "last_name": "first"})

# объединяем df_score2 и df_start2 по user_id
df_score2 = pd.merge(df_score2, df_start2, on="user_id")

# добавляем столбец с продолжительностью решения в исходном формате
df_score2["total_time"] = df_score2["submission_time"] - df_score2["attempt_time"]

# удаляем лишние столбцы
df_score2 = df_score2.drop(columns=["submission_time", "attempt_time"])

# добавляем столбец с flow равным 2
df_score2["flow"] = 2

# переименовываем столбцы
df_score2.columns = ["user_id", "score", "first_name", "last_name", "total_time", "flow"]

# объединяем df_score и df_score2 в один датафрейм
df_score = pd.concat([df_score, df_score2])

# меняем порядок столбцов
df_score = df_score[["user_id", "flow", "score", "total_time", "first_name", "last_name"]]

# сортируем датафрейм по score в убывающем порядке, а при равенстве score - по total_time в возрастающем порядке
df_score = df_score.sort_values(by=["score", "total_time"], ascending=[False, True])

# выводим таблицу победителей без индекса
print(df_score.to_string(index=False))
