CALL printnumbers();
CALL reverseprint();
CALL factorial(5);
CALL largest(10,12,13);DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `factorial`(IN num INT)
BEGIN
DECLARE i INT DEFAULT 1;
   DECLARE fact BIGINT DEFAULT 1;

   WHILE i <= num DO
      SET fact = fact * i;
      SET i = i + 1;
   END WHILE;

   SELECT fact AS factorial;
END$$
DELIMITER ;
