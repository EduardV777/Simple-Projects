CREATE USER 'admin2'@'localhost' IDENTIFIED BY 'admin';

GRANT SELECT,INSERT,UPDATE ON accounts TO 'admin'@'localhost';
GRANT SELECT,INSERT,UPDATE ON offerPostings TO 'admin'@'localhost';
GRANT SELECT,INSERT,UPDATE ON reservednames TO 'admin'@'localhost';
GRANT SELECT,INSERT,UPDATE ON postbox TO 'admin'@'localhost';
GRANT SELECT,INSERT,UPDATE ON usernotifications TO 'admin'@'localhost';
GRANT SELECT,INSERT,UPDATE ON userorders TO 'admin'@'localhost';
GRANT SELECT,INSERT,UPDATE ON myoffers TO 'admin'@'localhost';
