import nomStreak, nomFastest, nomCorrectest, totalScores

# разделение 05 от 1_2 из 05+2. И подготавливает таблицы распихивая их в 1year и 05year
exec(open('separateAndPrepare.py').read())  # разделяем 05 и 05+2, получая 1_2.xlsx в папке 1year, переносим 1_1.xlsx в 1year и 05.xlsx в 05year

# лучшая серия
nomStreak.one_click("1year")  # годовые, в два потока
nomStreak.one_click("05year")  # полугодовые

# самый быстрый
nomFastest.one_click("1year")  # годовые, в два потока
nomFastest.one_click("05year")  # полугодовые

# самый точный
nomCorrectest.one_click("1year")  # годовые, в два потока
nomCorrectest.one_click("05year")  # полугодовые

# победители
totalScores.one_click("1year")  # годовые, в два потока
totalScores.one_click("05year")  # полугодовые
