use test;
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product

-- 2. Выбрать названия всех автоматизированных складов
select name from store
where is_automated = 1

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
select distinct store_id from sale

-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select store_id
from store
where store_id not in (select distinct store_id from sale)

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select name,
	avg(total/quantity)
from product
join sale on sale.product_id = product.product_id
group by name
-- order by avg(total/quantity)

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select p.name	
from sale s  
join product p on p.product_id = s.product_id 
group by s.product_id
having count(distinct s.store_id) = 1

-- 8. Получить названия всех складов, с которых продавался только один продукт
select st.name	
from sale s  
join store st on st.store_id = s.store_id
group by s.store_id
having count(distinct s.product_id) = 1

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select *
from sale s
where s.total = (select (max(total)) from sale)

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select date	
from sale
group by date
order by sum(total) desc
	, date 
limit 1

/*
select max(t1.s)
from
(
select sum(total) s
from sale
group by date
) as t1
*/