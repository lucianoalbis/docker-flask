USE dbpython;
GRANT ALL ON `dbpython`.* TO `dbpython`@'%';
FLUSH PRIVILEGES;
CREATE TABLE IF NOT EXISTS `users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `age` INT NOT NULL,
  PRIMARY KEY (`id`));
