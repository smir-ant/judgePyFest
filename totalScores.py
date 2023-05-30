# импортируем библиотеку pandas
import pandas as pd

# определяем функцию для обработки 1_1.xlsx
def process_1_1():
    # читаем xlsx файл в датафрейм
    df = pd.read_excel("1_1.xlsx")

    # сохраняем исходный датафрейм в отдельную переменную
    df_original = df.copy()

    # создаем столбец с баллами за каждый правильный ответ
    df["score"] = df["status"].apply(lambda x: 1 if x == "correct" else 0)

    # группируем данные по user_id и находим минимальное время начала задания и максимальное время отправки правильного ответа
    df_min = df.groupby("user_id")["attempt_time"].min().reset_index()
    df_max = df[df["status"] == "correct"].groupby("user_id")["submission_time"].max().reset_index()

    # объединяем два датафрейма по user_id
    df_time = pd.merge(df_min, df_max, on="user_id")

    # создаем столбец с потраченным временем на все задания
    df_time["time_spent"] = df_time["submission_time"] - df_time["attempt_time"]

    # удаляем лишние столбцы
    df_time = df_time.drop(["attempt_time", "submission_time"], axis=1)

    # группируем данные по user_id и суммируем баллы
    df_score = df.groupby("user_id")["score"].sum().reset_index()

    # объединяем два датафрейма по user_id
    df = pd.merge(df_score, df_time, on="user_id")

    # добавляем колонки с фамилией и именем из исходного датафрейма
    df = pd.merge(df, df_original[["user_id", "last_name", "first_name"]].drop_duplicates(), on="user_id")

    # сортируем данные по баллам и времени по возрастанию
    df = df.sort_values(by=["score", "time_spent"], ascending=[False, True])

    # добавляем колонку flow со значением 1
    df["flow"] = 1

    # добавляем окончание -1 к значениям user_id
    df["user_id"] = df["user_id"].astype(str) + "-1"

    # выводим таблицу на экран без индексов слева и в нужном порядке колонок
    print(df[["user_id", "score", "time_spent", "last_name", "first_name", "flow"]].to_string(index=False))

    # записываем таблицу в файл rating1.xlsx
    df.to_excel("rating1.xlsx", index=False)

    # возвращаем таблицу из функции
    return df

# определяем функцию для обработки 1_2.xlsx
def process_1_2():
    # читаем xlsx файл в датафрейм
    df = pd.read_excel("1_2.xlsx")

    # сохраняем исходный датафрейм в отдельную переменную
    df_original = df.copy()

    # создаем столбец с баллами за каждый правильный ответ
    df["score"] = df["status"].apply(lambda x: 1 if x == "correct" else 0)

    # группируем данные по user_id и находим минимальное время начала задания и максимальное время отправки правильного ответа
    df_min = df.groupby("user_id")["attempt_time"].min().reset_index()
    df_max = df[df["status"] == "correct"].groupby("user_id")["submission_time"].max().reset_index()

    # объединяем два датафрейма по user_id
    df_time = pd.merge(df_min, df_max, on="user_id")

    # создаем столбец с потраченным временем на все задания
    df_time["time_spent"] = df_time["submission_time"] - df_time["attempt_time"]

    # удаляем лишние столбцы
    df_time = df_time.drop(["attempt_time", "submission_time"], axis=1)

    # группируем данные по user_id и суммируем баллы
    df_score = df.groupby("user_id")["score"].sum().reset_index()

    # объединяем два датафрейма по user_id
    df = pd.merge(df_score, df_time, on="user_id")

    # добавляем колонки с фамилией и именем из исходного датафрейма
    df = pd.merge(df, df_original[["user_id", "last_name", "first_name"]].drop_duplicates(), on="user_id")

    # сортируем данные по баллам и времени по возрастанию
    df = df.sort_values(by=["score", "time_spent"], ascending=[False, True])

    # добавляем колонку flow со значением 2
    df["flow"] = 2

    # добавляем окончание -2 к значениям user_id
    df["user_id"] = df["user_id"].astype(str) + "-2"

    # выводим таблицу на экран без индексов слева и в нужном порядке колонок
    # print(df[["user_id", "score", "time_spent", "last_name", "first_name", "flow"]].to_string(index=False))

    # записываем таблицу в файл rating2.xlsx
    df.to_excel("rating2.xlsx", index=False)

    # возвращаем таблицу из функции
    return df

# определяем функцию для объединения результатов двух таблиц
def process_all():
    # вызываем функцию для обработки 1_1.xlsx и сохраняем результат в переменную
    df_1 = process_1_1()

    # вызываем функцию для обработки 1_2.xlsx и сохраняем результат в переменную
    df_2 = process_1_2()

    # объединяем два результата в один датафрейм
    df = pd.concat([df_1, df_2])

    # сортируем данные по баллам и времени по возрастанию
    df = df.sort_values(by=["score", "time_spent"], ascending=[False, True])

    # выводим таблицу на экран без индексов слева и в нужном порядке колонок
    # print(df[["user_id", "score", "time_spent", "last_name", "first_name", "flow"]].to_string(index=False))

    # записываем таблицу в файл ratingAll.xlsx
    df.to_excel("ratingAll.xlsx", index=False)

# вызываем функцию для объединения результатов двух таблиц
process_all()
