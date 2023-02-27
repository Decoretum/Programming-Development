SHOW databases;
USE pinevalley;

SHOW tables;

DESC customer_t;
DESC product_t;

SELECT customer_name, city, postal_code
FROM customer_t
WHERE (postal_code LIKE "%20%");

SELECT DISTINCT state
FROM customer_t;

SELECT customer_name, state
FROM customer_t
WHERE (state NOT LIKE "%NJ%")
AND (state NOT LIKE "%NY%")
AND (state NOT LIKE "%FL%");

SELECT product_description, product_finish, standard_price
FROM product_t
WHERE (standard_price < 300) OR (standard_price > 500)
ORDER BY standard_price DESC;

SELECT product_description
FROM product_t
WHERE (product_description NOT LIKE "%Table%")
AND (product_description NOT LIKE "%desk%");

SELECT CONCAT(product_description, ": The price is ", standard_price, ", ", 700 -
standard_price, " below 700.00.") AS "PRODUCT"
FROM product_t
WHERE (standard_price < 700);
