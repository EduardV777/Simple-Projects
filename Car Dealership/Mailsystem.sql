CREATE TABLE mailsystem(
conversation INT NOT NULL,
msgN INT NOT NULL,
sender VARCHAR(60) NOT NULL,
message VARCHAR(5000) NOT NULL,
receiver VARCHAR(60) NOT NULL,
sent VARCHAR(30) NOT NULL,
sortTime INT NOT NULL
);