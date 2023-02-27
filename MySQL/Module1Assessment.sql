CREATE DATABASE Literature;
USE Literature;

CREATE TABLE Book(
ISBN VARCHAR(10) NOT NULL,
title VARCHAR(30) DEFAULT NULL,
pubdate DATE DEFAULT NULL,
pubID INTEGER(11) DEFAULT NULL,
cost FLOAT DEFAULT NULL,
retail FLOAT DEFAULT NULL,
category VARCHAR(12) DEFAULT NULL,
PRIMARY KEY (ISBN)
);

CREATE TABLE Author(
authorID INTEGER(4) PRIMARY KEY AUTO_INCREMENT,
lname VARCHAR(255) DEFAULT NULL,
fname VARCHAR(255) DEFAULT NULL
);

CREATE TABLE Book_author(
ISBN VARCHAR(10) NOT NULL,
authorid INTEGER(4) NOT NULL,
PRIMARY KEY (ISBN, authorid),
FOREIGN KEY (ISBN) REFERENCES Book(ISBN),
FOREIGN KEY (authorid) REFERENCES Author(authorid)
);

ALTER TABLE Book_author
modify ISBN VARCHAR(10) NOT NULL DEFAULT 'None';

ALTER TABLE Book
modify ISBN VARCHAR(30) NOT NULL DEFAULT 'None';


DESC Book_author;
DESC book;
DESC author;

#Test insertions
INSERT INTO Book(ISBN, title, cost, retail, category)
VALUES ('BOOKY1','Smith: How to Be Strong',521.21, 521.21, 'cooking'),
('BOOKY2','Danger: The Truth of Fire',400.921, 415, 'Wine'),
('BOOKY3','Database Designing: Basics',421, 499,'cocktails'),
('BOOKY4', 'DOOM',100,151,'GAMING');

INSERT INTO Book (ISBN, title, cost, retail, category)
VALUES('BOOKY5','How to be seductive',421.22, 500.12,'Social');

INSERT INTO Book (ISBN, title, cost, retail, category)
VALUES ('BOOKY6','Parallels of Multiverse', 571, 422.12, 'Science');

INSERT INTO Book (ISBN, title, cost, retail, category)
VALUES ('BOOKY7','Shut your Mouth', 900, 789, 'Social');

INSERT INTO Book (ISBN, title, category)
VALUES('BOOKY8','Design Patterns','Programming'),
('BOOKY9','Java Programming','Programming'),
('BOOKY10','Database Scripting','Scripting'),
('BOOKY11','SQL Scripting, Fundamentals','Scripting');

INSERT INTO Author (lname, fname)
VALUES ('Smith','Forsythe'),
('Margaux','Genevieve'),
('de Vera','Jose Alfredo');

INSERT INTO Author(lname, fname)
VALUES ('Smith','Will');


INSERT INTO Book_author
VALUES ('BOOKY1',1),
('BOOKY2',2),
('BOOKY3',3),
('BOOKY4',2);

INSERT INTO Book_author
VALUES ('BOOKY5',1);

INSERT INTO Book_author
VALUES ('BOOKY6',1);

INSERT INTO Book_author
VALUES ('BOOKY7',4);

SELECT * FROM BOOK
WHERE (category LIKE "%programming%")
OR (category LIKE "%scripting%");

#Start of Actual querying and updating of values

SELECT * FROM Book_author;
SELECT * FROM Book;
SELECT * FROM author;

SELECT ISBN, title, category 
FROM Book
where (category LIKE "%cooking%")
OR (category LIKE "%wine%")
OR (category LIKE "%cocktail%");

SELECT Book.ISBN, title, lname
FROM Book, author, book_author
WHERE (book_author.ISBN = Book.ISBN)
AND (book_author.authorid = author.authorID)
AND (author.lname = "Smith");

SELECT concat(Book.ISBN, " | ", title, " | ", fname, ", ", lname)
FROM Book, author, book_author
WHERE (book_author.ISBN = Book.ISBN)
AND (book_author.authorid = author.authorID)
AND (author.lname = "Smith")
AND (author.fname = "Forsythe");

SELECT concat(Book.ISBN, " | ", title, " | ", fname, ", ", lname)
FROM Book, author, book_author
WHERE (Book.ISBN = book_author.ISBN)
AND (author.authorID = book_author.authorid)
AND ((author.fname = "Forsythe" AND author.lname = "Smith") OR (author.fname = 'Genevieve' AND author.lname = 'Margaux'))
ORDER BY Book.cost DESC;

UPDATE Book
SET Cost = 300, Retail = 500
WHERE (title = 'DOOM');

SELECT * from Book;

INSERT INTO Author(fname, lname)
VALUES('Paul','Bocuse');

SELECT * FROM Author;
SELECT * FROM Book;

DELETE FROM Book
WHERE (category LIKE "%programming%")
OR (category LIKE "%scripting%");

SELECT * FROM Book;




