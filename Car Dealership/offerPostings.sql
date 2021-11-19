CREATE TABLE offerPostings (
accountId INT NOT NULL,
offerId INT PRIMARY KEY,
title VARCHAR(100) NOT NULL,
description VARCHAR(500) NOT NULL,
TYPE VARCHAR(30) NOT NULL,
fuelType VARCHAR(30) NOT NULL,
driveType VARCHAR(10)NOT NULL,
yearProd VARCHAR(10)NOT NULL,
offerPrice VARCHAR(30) DEFAULT 'Contact user for price details',
datePosted VARCHAR(20) NOT NULL,
comments VARCHAR(20)NOT NULL
);
