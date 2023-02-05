DELETE FROM order_line_t;
DELETE FROM order_t;
DELETE FROM product_t;
DELETE FROM customer_t;
DELETE FROM price_t;

INSERT INTO product_t
VALUES (1, 'End Table', 'Cherry', 175, 10001);

INSERT INTO product_t
VALUES (2, 'Coffee Table', 'Natural Ash', 200, 20001);

INSERT INTO product_t
VALUES (3, 'Computer Desk', 'Natural Ash', 375, 20001);

INSERT INTO product_t
VALUES (4, 'Entertainment Center', 'Natural Oak', 650, 30001);

INSERT INTO product_t
VALUES (5, 'Writers Desk', 'Cherry', 325, 10001);

INSERT INTO product_t
VALUES (6, '8-Drawer Dresser', 'White Ash', 750, 20001);

INSERT INTO product_t
VALUES (7, 'Dining Table', 'Natural Ash', 850, 20001);

INSERT INTO product_t
VALUES (8, 'Computer Desk', 'Walnut', 250, 30001);

INSERT INTO customer_t
VALUES (1, 'Contemporary Casuals', '1355 S Hines Blvd', 'Gainesville', 'FL', '32601');

INSERT INTO customer_t
VALUES (2, 'Value Furniture', ' 15145 S. W. 17th St.', 'Plano', 'TX', '75094');

INSERT INTO customer_t
VALUES (3, 'Home Furnishings', '1900 Allard Ave', 'Albany', 'NY', '12209');

INSERT INTO customer_t
VALUES (4, 'Eastern Furniture', '1925 Beltline Rd', 'Carteret', 'NJ', '07008');

INSERT INTO customer_t
VALUES (5, 'Impressions', '5585 Westcott Ct.', 'Sacramento', 'CA', '94206');

INSERT INTO customer_t
VALUES (6, 'Furniture Gallery', '325 Flatiron Dr.', 'Boulder', 'CO', '80514');

INSERT INTO customer_t
VALUES (7, 'Period Furniture', '394 Rainbow Dr.', 'Seattle', 'WA', '97954');

INSERT INTO customer_t
VALUES (8, 'California Classics', '816 Peach Rd', 'Santa Clara', 'CA', '96915');

INSERT INTO customer_t
VALUES (9, 'MH Casual Furniture', '3709 First Street', 'Clear Water', 'FL', '34620');

INSERT INTO customer_t
VALUES (10, 'Seminole Interiors', '2400 Rocky Point Dr.', 'Seminole', 'FL', '34646');

INSERT INTO customer_t
VALUES (11, 'American Euro Lifesytles', '2424 Missouri Ave', 'Prospect Park', 'NJ', '07508');

INSERT INTO customer_t
VALUES (12, 'Battle Creek Furniture', '345 Capitol Ave', 'Battle Creek', 'MI', '490154');

INSERT INTO customer_t
VALUES (13, 'Heritage Furnishings', '66789 College Ave', 'Carlisle', 'PA', '17013');

INSERT INTO customer_t
VALUES (14, 'Kaneohe Homes', '112 Kiowai Sr', 'Kaneohe', 'HI', '96744');

INSERT INTO customer_t
VALUES (15, 'Mountain Scenes', '4132 Main Street', 'Ogden', 'UT', '84403');

INSERT INTO order_t
VALUES (1001, '2000-10-21', 1);

INSERT INTO order_t
VALUES (1002, '2000-10-21', 8);

INSERT INTO order_t
VALUES (1003, '2000-10-22', 15);

INSERT INTO order_t
VALUES (1004, '2000-10-22', 5);

INSERT INTO order_t
VALUES (1005, '2000-10-24', 3);

INSERT INTO order_t
VALUES (1006, '2000-10-24', 2);

INSERT INTO order_t
VALUES (1007, '2000-10-27', 11);

INSERT INTO order_t
VALUES (1008, '2000-10-30', 12);

INSERT INTO order_t
VALUES (1009, '2000-11-05', 4);

INSERT INTO order_t
VALUES (1010, '2000-11-05', 1);

INSERT INTO order_line_t
VALUES (1001, 1, 2);

INSERT INTO order_line_t
VALUES (1001, 2, 2);

INSERT INTO order_line_t
VALUES (1001, 4, 1);

INSERT INTO order_line_t
VALUES (1002, 3, 5);

INSERT INTO order_line_t
VALUES (1003, 3, 3);

INSERT INTO order_line_t
VALUES (1004, 6, 2);

INSERT INTO order_line_t
VALUES (1004, 8, 2);

INSERT INTO order_line_t
VALUES (1005, 4, 4);

INSERT INTO order_line_t
VALUES (1006, 4, 1);

INSERT INTO order_line_t
VALUES (1006, 5, 2);

INSERT INTO order_line_t
VALUES (1006, 7, 2);

INSERT INTO order_line_t
VALUES (1007, 1, 3);

INSERT INTO order_line_t
VALUES (1007, 2, 2);

INSERT INTO order_line_t
VALUES (1008, 3, 3);

INSERT INTO order_line_t
VALUES (1008, 8, 3);

INSERT INTO order_line_t
VALUES (1009, 4, 2);

INSERT INTO order_line_t
VALUES (1009, 7, 3);

INSERT INTO order_line_t
VALUES (1010, 8, 10);

INSERT INTO price_t
VALUES (1, 100.00, 200.00);
INSERT INTO price_t
VALUES (2, 201.00, 300.00);
INSERT INTO price_t
VALUES (3, 301.00, 400.00);
INSERT INTO price_t
VALUES (4, 401.00, 500.00);
INSERT INTO price_t
VALUES (5, 501.00, 600.00);
INSERT INTO price_t
VALUES (6, 601.00, 700.00);
INSERT INTO price_t
VALUES (7, 701.00, 800.00);
INSERT INTO price_t
VALUES (8, 801.00, 900.00);