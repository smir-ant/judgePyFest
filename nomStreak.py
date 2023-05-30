# импортируем pandas
import pandas as pd

# функция для обработки данных из файла
def process_data(filename):
    # читаем данные из файла
    df = pd.read_excel(filename)

    # создаем новые колонки "streak" и "time_for_streak" и заполняем их нулями
    df["streak"] = 0
    df["time_for_streak"] = 0

    # группируем данные по user_id
    groups = df.groupby("user_id")

    # для каждой группы
    for user_id, group in groups:
        # инициализируем текущую и максимальную серии правильных ответов
        current_streak = 0
        max_streak = 0
        
        # инициализируем минимальное время начала и максимальное время окончания для текущей и максимальной серий
        current_start_time = 0
        current_end_time = 0
        max_start_time = 0
        max_end_time = 0
        
        # для каждой строки в группе
        for index, row in group.iterrows():
            # если статус ответа "correct"
            if row["status"] == "correct":
                # увеличиваем текущую серию на 1
                current_streak += 1
                
                # если это первая правильная задача в серии
                if current_streak == 1:
                    # запоминаем время начала серии как attempt_time этой задачи
                    current_start_time = row["attempt_time"]
                
                # запоминаем время окончания серии как submission_time этой задачи
                current_end_time = row["submission_time"]
            else:
                # иначе обнуляем текущую серию и времена начала и окончания
                current_streak = 0
                current_start_time = 0
                current_end_time = 0
            
            # если текущая серия больше максимальной
            if current_streak > max_streak:
                # обновляем максимальную серию и времена начала и окончания для нее
                max_streak = current_streak
                max_start_time = current_start_time
                max_end_time = current_end_time
        
        # записываем максимальную серию в колонку "streak" для соответствующего user_id
        df.loc[df["user_id"] == user_id, "streak"] = max_streak
        
        # вычисляем время для лучшей серии как разность между максимальным временем окончания и минимальным временем начала
        time_for_streak = max_end_time - max_start_time
        
        # записываем время для лучшей серии в колонку "time_for_streak" для соответствующего user_id
        df.loc[df["user_id"] == user_id, "time_for_streak"] = time_for_streak
    
    # выбираем нужные колонки из dataframe
    df = df[["user_id", "last_name", "first_name", "streak", "time_for_streak"]]
    
    # убираем дубликаты по user_id
    df = df.drop_duplicates(subset="user_id")
    
    # сортируем dataframe по убыванию по значениям колонки streak
    df = df.sort_values(by="streak", ascending=False)
    
    # убираем индекс слева
    df = df.reset_index(drop=True)
    
    # возвращаем обработанный dataframe
    return df

# обрабатываем данные из первого файла "1_1.xlsx"
df1 = process_data("1_1.xlsx")

# добавляем приписку "-1" к значениям user_id в первом dataframe 
df1["user_id"] = df1["user_id"].astype(str) + "-1"

# добавляем колонку flow со значением "1" в первом dataframe 
df1["flow"] = 1

# обрабатываем данные из второго файла "1_2.xlsx"
df2 = process_data("1_2.xlsx")

# добавляем приписку "-2" к значениям user_id во втором dataframe 
df2["user_id"] = df2["user_id"].astype(str) + "-2"

# добавляем колонку flow со значением "2" во втором dataframe 
df2["flow"] = 2

# соединяем два dataframe в один
df = pd.concat([df1, df2])

# сортируем общий dataframe по убыванию по значениям колонки streak, а при равенстве по убыванию по значениям колонки time_for_streak
df = df.sort_values(by=["streak", "time_for_streak"], ascending=False)

# убираем индекс слева
df = df.reset_index(drop=True)

# сохраняем итоговый dataframe в файл "nomStreak.xlsx"
df.to_excel("nomStreak.xlsx", index=False)

# выводим сообщение об успешном сохранении
print("Итоговый dataframe успешно сохранен в файл 'nomStreak.xlsx'")
