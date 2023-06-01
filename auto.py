import nomStreak, nomFastest, nomCorrectest, totalScores

# ИНСТРУКЦИЯ
print(" " * 10,"АВТОПРОВЕРКА MOVAVI SCHOOL FEST\n\n\n")
print("Убедитесь, что в папке raw лежат три файла:\n\n" +
      "• potok05.xlsx – отчёт 'Решения учащихся' потока 0.5 (ЭКСПОРТ СРАЗУ ПОСЛЕ ИХ ПОТОКА);\n\n" +
      "• potok1.xlsx – отчёт 'Решения учащихся' ПЕРВОГО потока;\n\n" +
      "• potok2.xlsx - отчёт 'Решения учащихся' ВТОРОГО потока;\n\n" +
      "Названия таблиц ВАЖНЫ.")
input('После подготовки файлов нажмите Enter:')



# разделение 05 от 1_2 из 05+2. И подготавливает таблицы распихивая их в 1year и 05year
exec(open('separateAndPrepare.py').read())  # разделяем 05 и 05+2, получая 1_2.xlsx в папке 1year, переносим 1_1.xlsx в 1year и 05.xlsx в 05year

print("=" * 15, " результаты MOVAVI SHOOL FEST (python)")

print()
print("-" * 10, "НОМИНАЦИЯ 'Лучшая серия'")
# лучшая серия
nomStreak.one_click("1year")  # годовые (два потока)

print()
print("-" * 10, "НОМИНАЦИЯ 'Самый быстрый'")
# самый быстрый
nomFastest.one_click("1year")  # годовые (два потока)

print()
print("-" * 10, "НОМИНАЦИЯ 'Самый точный'")
# самый точный
nomCorrectest.one_click("1year")  # годовые (два потока)

print()
print("-" * 10, "ПОБЕДИТЕЛИ")
# победители
print("-" * 5, "победители годовые")
totalScores.one_click("1year")  # годовые (два потока)
print("-" * 5, "победители полугодовые")
totalScores.one_click("05year")  # полугодовые

input()