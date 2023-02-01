CREATE DATABASE accounts;
USE accounts;

CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT,
	username VARCHAR(24) NOT NULL CHECK ( username <> ''),
	userpass VARCHAR(24) NOT NULL CHECK ( userpass <> ''),
	PRIMARY KEY (id)
);

ALTER TABLE users ADD UNIQUE INDEX (username);