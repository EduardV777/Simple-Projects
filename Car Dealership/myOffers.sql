CREATE TABLE myoffers(
accountId INT PRIMARY KEY,
offerId INT NOT NULL,
askPrice VARCHAR(30) DEFAULT 'Discuss with customer',
posted VARCHAR(20) NOT NULL,
status VARCHAR(20) DEFAULT 'Listed'
);
