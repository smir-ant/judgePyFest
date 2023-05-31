# Как с этим работать:

Скрипт сам прочтёт таблицу(-ы), все обработает и выведет в таблицу, но ему важно указать откуда брать данные.

👉 В начале каждого из скриптов есть следующие строки:

```python
# path = "1year"  # ❗❗❗ЕСЛИ ГОД ❗❗❗
path = "05year"  # ❗❗❗ ЕСЛИ ПОЛ ГОДА ❗❗❗
filenames = glob.glob(path + "/*.xlsx")
```

Этот фрагмент кода отвечает за то из какой папки он прочтёт таблицы. И уже в зависимости от этого немного иначе будет формировать итоги.

Что нужно сделать чтобы обработать годовых ребят с двух потоков:

```python
path = "1year"  # ❗❗❗ЕСЛИ ГОД ❗❗❗
# path = "05year"  # ❗❗❗ ЕСЛИ ПОЛ ГОДА ❗❗❗
filenames = glob.glob(path + "/*.xlsx")
```

Соответственно, что вот что нужно сделать чтобы обработать один поток полугодовых ребят:

```python
path = "1year"  # ❗❗❗ЕСЛИ ГОД ❗❗❗
# path = "05year"  # ❗❗❗ ЕСЛИ ПОЛ ГОДА ❗❗❗
filenames = glob.glob(path + "/*.xlsx")
```

<!-- ------------------------ -->
<picture> <img width="100%" src="https://user-images.githubusercontent.com/84059957/202753342-fd2ddfa9-2939-43a2-976a-b19a9f32905f.png"> </picture>

## Важный момент:

1) Файлы с табличными данными обязательно должны лежать в папке <code>"1year"</code> или <code>"05year"</code>.
2) Файлы с входными данными обязательно надо называть <code>"1_1.xlsx"</code> и <code>"1_2.xlsx"</code> для двух потоков. <sub>как называть файл для полугодовых неважно, главное чтобы он был один в папке</sub>

<!-- ------------------------ -->
<picture> <img width="100%" src="https://user-images.githubusercontent.com/84059957/202753342-fd2ddfa9-2939-43a2-976a-b19a9f32905f.png"> </picture>

### Уточнение:

- Колонка <code>flow</code> (появляется только при работе с двумя потоками(1year)) - <kbd>1</kbd> или <kbd>2</kbd> в зависимости от того пришел он из 1_1.xlsx или 1_2.xlsx.
- Колонка <code>user_id</code> (появляется всегда(и при 05year), но изменяется только при работе с двумя потоками (1year)) - добавляется приписка в конце <kbd>-1</kbd> если значение из 1_1.xlsx, и окончание <kbd>-2</kbd> если строка из 1_2.xlsx.

<!-- ------------------------ -->
<picture> <img width="100%" src="https://user-images.githubusercontent.com/84059957/202753342-fd2ddfa9-2939-43a2-976a-b19a9f32905f.png"> </picture>

# Про скрипты:

<!-- Toggle -->
<details>
<summary>
<code>totalScores.py</code> — победители олимпиады.
</summary>
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/84059957/215088292-cf50a16b-422b-43cc-a211-c4169553ca62.png">
    <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/84059957/210322548-b635bad5-c53d-4209-a73e-fb0adcc437bf.png">
    <img height="0.8">
</picture>

Поля:
- <kbd>correct_answers</kbd> - первостепенный показатель для результата. Правильные ответы в штуках.
- <kbd>total_time</kbd> - второстепенный показатель для результата. Время потраченное на решение.
- <kbd>start_time</kbd> и <kbd>end_time</kbd> - вспомогательные колонки, чтобы увидеть как высчиталось total_time.

> Создается <code>1year_winner.xlsx</code> или <code>05year_winner.xlsx</code>

<!-- Окончание -->
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/84059957/215088776-b06bbe95-42fd-4d78-bcae-70cdbeebbbd3.png">
    <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/84059957/210319906-4f1e79cb-1a45-4e5c-93e9-ae21e197e0b9.png">
    <img>
</picture>
</details>

<!-- Toggle -->
<details>
<summary>
<code>nomCorrectest.py</code> — Номинация 'Безошибочные решения' -  наибольший коэффициент правильных/неправильных решений среди всех.
</summary>
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/84059957/215088292-cf50a16b-422b-43cc-a211-c4169553ca62.png">
    <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/84059957/210322548-b635bad5-c53d-4209-a73e-fb0adcc437bf.png">
    <img height="0.8">
</picture>

Поля:
- <kbd>ratio</kbd> - первостепенный показатель для результата. Коэфициент сorrect / wrong.
- <kbd>total</kbd> - количество всех попыток решений.
- <kbd>correct</kbd> - количество правильных ответов.

> Создается <code>1year_nomCorrectest.xlsx</code> или <code>05year_nomCorrectest.xlsx</code>

<!-- Окончание -->
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/84059957/215088776-b06bbe95-42fd-4d78-bcae-70cdbeebbbd3.png">
    <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/84059957/210319906-4f1e79cb-1a45-4e5c-93e9-ae21e197e0b9.png">
    <img>
</picture>
</details>

<!-- Toggle -->
<details>
<summary>
<code>nomFastest.py</code> — Номинация 'Самое быстрое решение' - максимальная скорость решения задачи с правильным ответом.
</summary>
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/84059957/215088292-cf50a16b-422b-43cc-a211-c4169553ca62.png">
    <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/84059957/210322548-b635bad5-c53d-4209-a73e-fb0adcc437bf.png">
    <img height="0.8">
</picture>

Поля:
- <kbd>time</kbd> - минимальное время затраченное на решение задачи для каждого пользователя.

> Создается <code>1year_nomFastest.xlsx</code> или <code>05year_nomFastest.xlsx</code>

<!-- Окончание -->
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/84059957/215088776-b06bbe95-42fd-4d78-bcae-70cdbeebbbd3.png">
    <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/84059957/210319906-4f1e79cb-1a45-4e5c-93e9-ae21e197e0b9.png">
    <img>
</picture>
</details>

<!-- Toggle -->
<details>
<summary>
<code>nomStreak.py</code> — Номинация 'Наибольшая серия решений' -  наибольшая серия верных ответов подряд.
</summary>
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/84059957/215088292-cf50a16b-422b-43cc-a211-c4169553ca62.png">
    <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/84059957/210322548-b635bad5-c53d-4209-a73e-fb0adcc437bf.png">
    <img height="0.8">
</picture>

Поля:
- <kbd>streak</kbd> - первостепенный показатель для результата. Наибольшая серия подряд верно решенных задач для пользователя.
- <kbd>time_for_streak</kbd> - второстепенный показатель для результата. Показывает сколько времени ушло на эту серию задач.

> Создается <code>1year_nomStreak.xlsx</code> или <code>05year_nomStreak.xlsx</code>

<!-- Окончание -->
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/84059957/215088776-b06bbe95-42fd-4d78-bcae-70cdbeebbbd3.png">
    <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/84059957/210319906-4f1e79cb-1a45-4e5c-93e9-ae21e197e0b9.png">
    <img>
</picture>
</details>
