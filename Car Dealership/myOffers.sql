CREATE TABLE myoffers(
accountId INT NOT NULL,
offerId INT PRIMARY KEY,
askPrice VARCHAR(30) NOT NULL,
posted VARCHAR(20) NOT NULL,
status VARCHAR(100) DEFAULT 'Listed',
flags VARCHAR(200) DEFAULT ''
);
