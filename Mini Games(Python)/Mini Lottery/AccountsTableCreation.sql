CREATE TABLE accounts(
accountId INT AUTO_INCREMENT PRIMARY KEY,
accountName VARCHAR(10),
accountPassword VARCHAR(30),
creationDate VARCHAR(15),
accountStatus VARCHAR(20) DEFAULT 'active',
accountFlags INT DEFAULT 0
)