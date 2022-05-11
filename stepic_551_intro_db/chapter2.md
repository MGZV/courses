Корректное отображение запроса

```
SELECT
    count(1),
    avg(budget)
    client_name
FROM project
group by client_name;
```

Выведите общее количество заказов компании.
```
SELECT count(1) FROM project;
```
Выведите количество товаров в каждой категории. Результат должен содержать два столбца: 
название категории, 
количество товаров в данной категории.
```
SELECT category, count(1) FROM store
GROUP BY category
ORDER BY category;
```
Выведите 5 категорий товаров, продажи которых принесли наибольшую выручку. Под выручкой понимается сумма произведений стоимости товара на количество проданных единиц. Результат должен содержать два столбца: 
название категории,
выручка от продажи товаров в данной категории.

```
SELECT category, sum(sold_num*price) as revenue 
FROM store
GROUP BY category
ORDER BY revenue DESC
limit 5;
```
Выведите в качестве результата одного запроса общее количество заказов, сумму стоимостей (бюджетов) всех проектов, средний срок исполнения заказа в днях.
NB! Для вычисления длительности проекта удобно использовать встроенную функцию datediff().
```
SELECT count(1),
sum(budget) as revenue,
AVG(DATEDIFF(project_finish, project_start)) as avg_days
FROM project WHERE DATEDIFF(project_finish, project_start)>0;
```