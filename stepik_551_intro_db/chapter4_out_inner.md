Результаты выборки не имеющие совпадения
```
select * from category;
```
```
select * from category as c left outer join product as p on p.category_id = c.category_id;
```
тоже самое
```
select * from product as p right outer join category as c on p.category_id = c.category_id;
```
Объединение
```
select * from product where price > 900
union
select * from product where price < 100;
```
Выведите список товаров с названиями товаров и названиями категорий, в том числе товаров, не принадлежащих 
ни одной из категорий.
```
select good.name as good_name, category.name as category_name  
from category_has_good

right outer join good
on category_has_good.good_id = good.id

left outer join category
on category_has_good.category_id = category.id
order by good_name, category_name;
```
Выведите список товаров с названиями категорий, в том числе товаров, не принадлежащих ни к одной из категорий, 
в том числе категорий не содержащих ни одного товара.
```
select good.name as good_name, category.name as category_name  
from category_has_good 
right outer join good on category_has_good.good_id = good.id 
left outer join category on category_has_good.category_id = category.id
union 
select good.name as good_name, category.name as category_name  
from category_has_good
left outer join good on category_has_good.good_id = good.id
right outer join category on category_has_good.category_id = category.id;

SELECT good.name as good_name, category.name as category_name
FROM category_has_good RIGHT OUTER JOIN good ON
category_has_good.good_id = good.id
LEFT OUTER JOIN category ON category_has_good.category_id = category.id
UNION
SELECT good.name as good_name, category.name as category_name
FROM category_has_good LEFT OUTER JOIN good ON
category_has_good.good_id = good.id
RIGHT OUTER JOIN category ON category_has_good.category_id = category.id;
```