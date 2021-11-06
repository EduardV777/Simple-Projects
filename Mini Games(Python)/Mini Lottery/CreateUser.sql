CREATE USER 'accountControl'@'localhost' IDENTIFIED BY 'control';
GRANT SELECT,INSERT,UPDATE ON accounts TO 'accountControl'@'localhost';
GRANT SELECT,INSERT,UPDATE ON accountStats TO 'accountControl'@'localhost';