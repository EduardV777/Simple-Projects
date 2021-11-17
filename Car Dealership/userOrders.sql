CREATE TABLE userOrders(
accountId INT PRIMARY KEY NOT NULL,
offerId INT NOT NULL,
title VARCHAR(100) NOT NULL,
description VARCHAR(500) NOT NULL,
TYPE VARCHAR(30) NOT NULL,
fuelType VARCHAR(30) NOT NULL,
driveType VARCHAR(10)NOT NULL,
yearProd VARCHAR(10)NOT NULL,
posted VARCHAR(20) NOT NULL,
ordered VARCHAR(20) NOT NULL,
orderstatus VARCHAR(20) DEFAULT 'Unknown',
SoldBy VARCHAR(20) NOT NULL,
ExpectedDelivery VARCHAR(20) DEFAULT 'Waiting for seller response'
);