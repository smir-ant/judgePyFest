# Импортируем библиотеку pandas
import pandas as pd

# Функция для обработки данных из одного файла
def process_data(filename):
  # Читаем данные из файла
  df = pd.read_excel(filename)

  # Группируем данные по user_id и подсчитываем количество строк и количество правильных ответов
  grouped = df.groupby("user_id").agg({"status": ["count", lambda x: (x == "correct").sum()]})

  # Переименовываем столбцы для удобства
  grouped.columns = ["total", "correct"]

  # Вычисляем отношение правильных ответов к общему числу ответов
  grouped["ratio"] = grouped["correct"] / grouped["total"]

  # Сортируем данные по убыванию отношения
  top = grouped.sort_values("ratio", ascending=False)

  # Добавляем столбцы с фамилией и именем участников из исходного датафрейма
  top = top.join(df[["user_id", "last_name", "first_name"]].drop_duplicates().set_index("user_id"))

  # Возвращаем обработанный датафрейм
  return top

# Обрабатываем данные из двух файлов
top1 = process_data("1_1.xlsx")
top2 = process_data("1_2.xlsx")

# Добавляем колонку "flow" с указанием источника данных
top1["flow"] = "1"
top2["flow"] = "2"

# Добавляем суффикс "-1" или "-2" к user_id в зависимости от источника данных
top1["user_id"] = top1.index.astype(str) + "-1"
top2["user_id"] = top2.index.astype(str) + "-2"

# Сбрасываем индекс для объединения датафреймов
top1.reset_index(drop=True, inplace=True)
top2.reset_index(drop=True, inplace=True)

# Объединяем два датафрейма в один
result = pd.concat([top1, top2], ignore_index=True)

# Сортируем результат по убыванию ratio
result.sort_values("ratio", ascending=False, inplace=True)

# Сохраняем результат в новый файл excel
result.to_excel("nomCorrectest.xlsx", index=False)
