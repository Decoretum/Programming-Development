show databases;
CREATE DATABASE MSYS42;
use MSYS42;
show tables;

CREATE TABLE Items(
ItemID INTEGER(200) PRIMARY KEY AUTO_INCREMENT,
Price INTEGER(5) NOT NULL,
Description VARCHAR(200) NOT NULL
);

SELECT * FROM A1_item;
SELECT * FROM A1_order;
SELECT * FROM A1_item_order;
DELETE FROM A1_order
WHERE id = 1;

ALTER TABLE A1_item;
DROP TABLE A1_item;

INSERT INTO A1_item (item_name, item_price, description, stock, outofstock)
VALUES('Jal de Vera','999','He is the director of MIS in ADMU with Development Experience as well as Database Designing experience.','99','0');

INSERT INTO A1_item (item_name, item_price, description, stock, outofstock)
VALUES('Andrei Coronel','999','He is the director of MIS and CS in ADMU with Development Experience.','99','0');

INSERT INTO A1_item (item_name, item_price, description, stock, outofstock)
VALUES('Mark Zuckerberg','999','He is the owner of Facebook and is a developer.','99','0');

INSERT INTO A1_item (item_name, item_price, description, stock, outofstock)
VALUES('Mike','999','He is a Novice programmer.','99','0');

INSERT INTO A1_item (item_name, item_price, description, stock, outofstock)
VALUES('MIS Person','999','This entity enjoys College and prefers going out than learning programming frameworkds.','0.50','0');


desc Items;
desc A1_item;



