drop database pinevalley;
create database pinevalley;
use pinevalley;

CREATE TABLE customer_t 
(customer_id INTEGER(11) NOT NULL,
 customer_name VARCHAR(25) NOT NULL,
 customer_address VARCHAR(30),
 city VARCHAR(20),
 state VARCHAR(2),
 postal_code VARCHAR(9),
 CONSTRAINT customer_pk PRIMARY KEY (customer_ID));

CREATE TABLE order_t 
(order_id INTEGER(11) NOT NULL,
 order_date DATE,
 customer_id INTEGER(11),
 CONSTRAINT order_pk PRIMARY KEY (order_ID),
 CONSTRAINT order_fk FOREIGN KEY (customer_ID) REFERENCES customer_t(customer_ID));

CREATE TABLE product_t 
(product_id INTEGER NOT NULL,
 product_description VARCHAR(50),
 product_finish VARCHAR(20) CHECK (product_finish IN ('Cherry', 'Natural Ash', 'White Ash', 'Red Oak', 'Natural Oak', 'Walnut')),
 standard_price DECIMAL(6,2),
 product_line_id INTEGER,
 CONSTRAINT product_pk PRIMARY KEY (product_ID));

CREATE TABLE order_line_t 
(order_id INTEGER(11) NOT NULL,
 product_id INTEGER(11) NOT NULL,
 ordered_quantity INTEGER(11),
 CONSTRAINT order_line_pk PRIMARY KEY (order_id, product_ID),
 CONSTRAINT order_line_fk1 FOREIGN KEY (order_id) REFERENCES order_t(order_ID),
 CONSTRAINT order_line_fk2 FOREIGN KEY (product_ID) REFERENCES product_t(product_ID));
 
CREATE TABLE price_t 
(grade INTEGER(11) NOT NULL,
 low DECIMAL(6,2) NOT NULL,
 high DECIMAL(6,2) NOT NULL,
 CONSTRAINT price_pk PRIMARY KEY (grade));