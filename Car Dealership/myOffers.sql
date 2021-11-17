CREATE TABLE myoffers(
accountId INT PRIMARY KEY,
offerId INT NOT NULL,
posted VARCHAR(20) NOT NULL,
status VARCHAR(20) DEFAULT 'Listed'
);