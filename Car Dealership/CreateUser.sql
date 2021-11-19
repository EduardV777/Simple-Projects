CREATE USER 'admin2'@'localhost' IDENTIFIED BY 'admin';

GRANT SELECT,INSERT,UPDATE,DELETE ON accounts TO 'admin'@'localhost';
GRANT SELECT,INSERT,UPDATE,DELETE ON offerPostings TO 'admin'@'localhost';
GRANT SELECT,INSERT,UPDATE,DELETE ON reservednames TO 'admin'@'localhost';
GRANT SELECT,INSERT,UPDATE,DELETE ON postbox TO 'admin'@'localhost';
GRANT SELECT,INSERT,UPDATE,DELETE ON usernotifications TO 'admin'@'localhost';
GRANT SELECT,INSERT,UPDATE,DELETE ON userorders TO 'admin'@'localhost';
GRANT SELECT,INSERT,UPDATE,DELETE ON myoffers TO 'admin'@'localhost';
GRANT SELECT,INSERT,UPDATE,DELETE ON mailsystem TO 'admin'@'localhost';
