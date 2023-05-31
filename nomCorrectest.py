# Импортируем pandas и glob
import pandas as pd
import glob

# Создаем список файлов с расширением xlsx в заданной директории
path = "1year"  # ❗❗❗ЕСЛИ ГОД ❗❗❗
# path = "05year"  # ❗❗❗ ЕСЛИ ПОЛ ГОДА ❗❗❗
filenames = glob.glob(path + "/*.xlsx")
# print(filenames)

# Создаем пустой список для хранения DataFrame
dfs = []

# Проходим по списку файлов в цикле
for filename in filenames:
  # Читаем файл в DataFrame
  df = pd.read_excel(filename)
#   print(df)

  # Обрабатываем данные по user_id, status и ratio
  grouped = df.groupby("user_id").agg({"status": ["count", lambda x: (x == "correct").sum()]})
  grouped.columns = ["total", "correct"]
#   print(grouped)
  grouped["ratio"] = grouped["correct"] / grouped["total"]
  result = grouped.merge(df[["user_id", "last_name", "first_name"]].drop_duplicates(), on="user_id")

  # Добавляем столбец flow и приписку к user_id в зависимости от имени файла
  if filename.split('\\')[-1] == "1_1.xlsx":
    result["flow"] = "1"
    result["user_id"] = result["user_id"].astype(str) + "-1"
  elif filename.split('\\')[-1] == "1_2.xlsx":
    result["flow"] = "2"
    result["user_id"] = result["user_id"].astype(str) + "-2"

  # Добавляем DataFrame в список
  dfs.append(result)
#   print(dfs)

# Соединяем все DataFrame из списка в один большой DataFrame
final = pd.concat(dfs, ignore_index=True)

# Сортируем данные по ratio в убывающем порядке
final = final.sort_values("ratio", ascending=False)

# Выводим результат
print(final)

final.to_excel(f"{path}_nomCorrectest.xlsx", index=False)

