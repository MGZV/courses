"""
Необходимо написать запрос, который выдаст 3 пользователей,
 с лучшими результатами по любому из предметов и отсортировать по результату по убыванию.
Пример ответа:
Иван, 100.0, История
Владимир, 95.0, Математика
Кирилл, 93.0, История

*	Получить пользователей, которые сдавали по 3 предмета и у которых результат больше 200 по всем предметам и
отсортировать по результату по убыванию.
Пример ответа:
Иван, 251.0
Владимир, 230.5
Константин, 220.2

"""
"""
SELECT user.name as name, result, subject.name as subject
FROM result
JOIN user ON result.user_id = user.id
JOIN subject ON result.subject_id = subject.id
GROUP BY name
ORDER BY result DESC
LIMIT 3;
"""

"""
SELECT user.name as name, result, subject.name as subject
FROM result
JOIN user ON result.user_id = user.id
JOIN subject ON result.subject_id = subject.id
WHERE SUM(user.result.subject) = 3 
GROUP BY name
HAVING SUM(user.result.subject) > 200
ORDER BY result DESC
LIMIT 3;
"""