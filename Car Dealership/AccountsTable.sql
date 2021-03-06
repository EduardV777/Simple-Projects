CREATE TABLE accounts (
id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(20) NOT NULL,
PASSWORD VARCHAR(100) NOT NULL,
email VARCHAR(60) NOT NULL,
dateCreated VARCHAR(10) NOT NULL,
rating DOUBLE DEFAULT '0.00',
ratedBy INT DEFAULT 0,
address VARCHAR(60) DEFAULT 'Not stated',
telephone VARCHAR(10) DEFAULT 'Not stated',
company VARCHAR(30) DEFAULT 'None',
ratedUsers TEXT,
accountFlags VARCHAR(500) DEFAULT '[HideAddress][HidePhone][HideCompany]'
);
