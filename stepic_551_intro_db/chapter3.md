Выборка из двух таблиц - Декартово произведение
```
select * from product, category;
```
```
select * from product cross join category;
```
запрос из нескольких таблиц. Тета-соединение.
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