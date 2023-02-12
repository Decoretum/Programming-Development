show databases;
use pinevalley;
show tables;

#Equijoin - you use primary key and foreign key as comparison
desc order_line_t;
desc order_t;

select customer_t.customer_name, customer_t.customer_address, order_t.order_date
from customer_t, order_t
where (customer_t.customer_id = order_t.customer_id);

select  product_description, product_t.product_id, order_line_t.order_id
from order_line_t, product_t
where (product_t.product_id = order_line_t.product_id);

select customer_name, customer_address, product_description, ordered_quantity
from customer_t, order_line_t, order_t, product_t
where (order_line_t.order_id = order_t.order_id) and (order_t.customer_id = customer_t.customer_id)
and (order_line_t.product_id = product_t.product_id);


#non equijoins - no comparisons of primary & foreign keys
#we need to match column values from different tables using comparison operators
select product_description, product_finish, standard_price
from product_t, price_t
where standard_price between low and high
order by standard_price;

#outer joins - to see records from a table that do not satisfy join condition or must satisfy certain condition
#left join and right join
select customer_name, customer_address, order_date
from order_t left join customer_t
on (customer_t.customer_id = order_t.customer_id);

select customer_name, customer_address, order_date
from order_t right join customer_t
on (customer_t.customer_id = order_t.customer_id);


#practices
select * from customer_t
left join order_t
on (customer_t.customer_id = order_t.customer_id);

select customer_name, product_description, standard_price, ordered_quantity
from customer_t, order_t, order_line_t, product_t
where (customer_t.customer_id = order_t.customer_id)
and (order_t.order_id = order_line_t.order_id)
and (product_t.product_id = order_line_t.product_id);

desc customer_t;
desc order_t;

desc order_line_t;
desc product_t;






