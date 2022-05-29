Выборка из двух таблиц - Декартово произведение
```
select * from product, category;
```
```
select * from product cross join category;
```
Запрос из нескольких таблиц. Тета-соединение.
```
select * from product inner join category on product.category_id = category.category_id;
```
```
select product.product.name, category.category_name, product.price
from product inner join category on product.category_id = category.category_id;
```
Применение сокращений
```
select p.product.name, c.category_name, p.price
from product as p inner join category as c on p.category_id = c.category_id;
```
Выведите все позиций списка товаров принадлежащие какой-либо категории с названиями товаров и названиями категорий. 
Список должен быть отсортирован по названию товара, названию категории. Для соединения таблиц необходимо использовать 
оператор INNER JOIN.
```
select good.name as good_name, category.name as category_name  
from category_has_good
inner join good
on category_has_good.good_id = good.id
inner join category
on category_has_good.category_id = category.id
order by good_name, category_name;
```
Выведите список клиентов (имя, фамилия) и количество заказов данных клиентов, имеющих статус "new".
```
select client.first_name, client.last_name, count(sale.id) as new_sale_num
from sale
inner join client
on sale.client_id = client.id
inner join status
on sale.status_id = status.id
where status.name = 'new'
group by client.first_name, client.last_name;
```
