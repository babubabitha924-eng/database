CREATE DATABASE STORE;
USE STORE;
CREATE TABLE Product(
                    PdtId INT PRIMARY KEY,
                    Pname VARCHAR(50),
                    Price DECIMAL(10,2),
                    Quantity INT
                    );
CALL productinsertion(1,'book',55,2);
SELECT * FROM store.Product;
CALL productinsertion(2,'book',55,2);
CALL productinsertion(3,'pen',0,2);
CALL productinsertion(4,'pencil',3,4);
CALL productinsertion(5,'sketch',5,12);
CALL productinsertion(6,'paper',10,10);
CALL productinsertion(7,'bag',500,1);
SELECT * FROM store.Product;


