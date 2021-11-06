CREATE TABLE accountStats(
accountId INT AUTO_INCREMENT PRIMARY KEY,
accountBalance DOUBLE DEFAULT '20',
playedGames INT DEFAULT '0',
wonGames INT DEFAULT '0',
lostGames INT DEFAULT '0'
);