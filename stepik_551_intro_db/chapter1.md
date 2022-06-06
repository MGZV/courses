#Основы
 _USE billing_simple;_ - название базы данных
```
CREATE TABLE IF NOT EXISTS `billing_simple`.`billing` (
  'payer_email' VARCHAR(255) NULL,
  `recipient_email` VARCHAR(255) NULL,
  `sum` DECIMAL(18,2) NULL,
  `currency` VARCHAR(3) NULL,
  `billing_date` DATE NULL,
  `comment` TEXT NULL)
ENGINE = InnoDB;
```
примеры выборки из таблицы
```
SELECT * FROM billing WHERE sum>900;
 ```
```
SELECT * FROM billing WHERE sum>900 AND currency NOT IN ('CHF', 'GBP');
```
---
### ДОБАВЛЕНИЕ ЗАПИСИ В ТАБЛИЦУ
```
SELECT * FROM billing

INSERT INTO billing VALUES (
'alex@mail.com',
'leo@mail.com',
'500', 'MYR',
'2010-08-20',
'Here are some money for you');
```
или 
```
INSERT INTO billing (
	payer_email, recipient_email,
sum, currency, billing_date)

VALUES (
'alex@mail.com',
'leo@mail.com',
'500', 'MYR',
'2010-08-20');
```
---
###ОБНОВЛЕНИЕ ЗАПИСИ В ТАБЛИЦУ
```
select* FROM billing    
WHERE recipient_email='leo@mail.com'
   AND sum=500.00;

UPDATE billing 
   SET currency='USD'
WHERE recipient_email='leo@mail.com'
   AND sum=500.00;
```
ПОИСК
```
select* FROM billing    
WHERE recipient_email='leo@mail.com'
   AND sum=500.00;
```
---

###УДАЛЕНИЕ ЗАПИСИ В ТАБЛИЦЕ
```
delete from billing 
where payer_email is NULL
OR recipient_email = ""
```
---
###РАСЧЕТ КОЛИЧЕСТВА СТРОК
```
SELECT COUNT(1) FROM project;
```
---
###СРЕДНЕЕ ЗНАЧЕНИЕ ПО ПОЛЮ
```
SELECT AVG(budget) FROM project;
```
```
SELECT project_finish,
project_start,
DATEDIFF(project_finish, project_start)
FROM project;
```
```
SELECT project_finish,
project_start,
DATEDIFF(project_finish, project_start)
FROM project WHERE project_finish is not null;
```
```
SELECT project_finish, project_start,
AVG(DATEDIFF(project_finish, project_start))
FROM project WHERE DATEDIFF(project_finish, project_start)>0;
```
```
SELECT project_finish, project_start,
AVG(DATEDIFF(project_finish, project_start)),
MAX(DATEDIFF(project_finish, project_start))
FROM project WHERE DATEDIFF(project_finish, project_start)>0;
```
```
SELECT project_finish, project_start,
AVG(DATEDIFF(project_finish, project_start)),
MAX(DATEDIFF(project_finish, project_start)),
MIN(DATEDIFF(project_finish, project_start))
FROM project WHERE DATEDIFF(project_finish, project_start)>0;
```
```
SELECT project_finish, project_start,
AVG(DATEDIFF(project_finish, project_start)) as avg_days,
MAX(DATEDIFF(project_finish, project_start)) as max_days,
MIN(DATEDIFF(project_finish, project_start)) as min_days,
client_name
FROM project WHERE DATEDIFF(project_finish, project_start)>0
GROUP BY client_name
ORDER BY max_days DESC #обратный счет как -
LIMIT 10;
```
```
SELECT count(1),
sum(budget) as revenue,
AVG(DATEDIFF(project_finish, project_start)) as avg_days
FROM project WHERE DATEDIFF(project_finish, project_start)>0;
```