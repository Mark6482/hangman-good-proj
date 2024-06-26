# ОНЛАЙН ИГРА ВИСЕЛИЦА

---

Данная курсовая работа написана на языке программирования **_Python_** с примеениением фремфворка **_Django_**. Для хранения данных использовалася реаляционная база данных **_PostgreSQL_**.

Приложение предоставляет возмозжность пользователю выбирать слова по категориям, создать, просматривать, изменять и удалять свой профиль.

Администратору предоставлен полный CRUD функционал, как над пользователями, так и над словами и категориями.

В самом приложении реализованы и описаны следующие алгоритмы:

- Алгоритм частотного анализа;
- Алгоритм сортировки подсчетом;
- Алгоритм Мерсенна-Твист;
- Алгоритм серединных квадратов;
- Алгоритм регистрации пользователя.

Блок-схемы алгоритмов представлены ниже.

---

## Алгоритм частотного анализа

Описан в /hang/analysisrus.py

Применяется в /hang/views.py    (def word_frequency_view)   (1.1)

(1.1) применяется в /hang/templates/hang/analysisrus.html

![Блок-схема алгоритма частотного анализа](<Схемы/Схемы (2)-3.png>)

---

## Алгоритм сортировки подсчетом

Описан в /hang/CountingSort.py 

Применяется в /hang/analysisrus.py 


![Блок-схема алгоритма сортировки](<Схемы/Схемы (2)-2.png>)

---

## Алгоритм Мерсенна-Твист

Описан в /hang/myrandom.py    (3.1)

(3.1) применяется в /hang/views.py (class WordView)    (3.2)

(3.2) применяется в /hang/templates/hang/num.html

![Блок-схема алгоритма Мерсенна-Твист](<Схемы/Схемы (2)-4.png>)

---

## Алгоритм серединных квадратов

Описан в /hang/MiddleSquareMethod.py    (4.1)

(4.1) применяется в /hang/views.py (def generate_random_number)    (4.2)

(4.2) применяется в /hang/templates/hang/num.html   (4.3)

(4.3) применяется в /hang/templates/hang/categories.html

![Блок-схема алгоритма серединных квадратов](<Схемы/Схемы (2)-5.png>)

---

## Алгоритм регистрации пользователя

Описан в /users/views.py    (5.1)

(5.1) применяется в /users/templates/hang/registration.html

![Блок-схема алгоритма регистрации пользователя](<Схемы/Схемы (2)-6.png>)

---
