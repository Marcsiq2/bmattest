CREATE DATABASE bmat_db;
USE bmat_db;
CREATE TABLE radiostations (
	name VARCHAR(150) NOT NULL, 
	PRIMARY KEY (name)
	);
CREATE TABLE performers (
	name VARCHAR(150) NOT NULL, 
	PRIMARY KEY (name)
	);
CREATE TABLE songs (
	title VARCHAR(150) NOT NULL, 
	performer VARCHAR(150) NOT NULL,
	PRIMARY KEY (title), 
	FOREIGN KEY (performer) references performers(name) ON UPDATE cascade
	);

CREATE TABLE plays (
	title VARCHAR (150) NOT NULL,
	channel VARCHAR (150) NOT NULL,
	start datetime NOT NULL,
	performer VARCHAR(150) NOT NULL,
	end datetime NOT NULL,
	FOREIGN KEY (title) references songs(title),
	FOREIGN KEY (channel) references radiostations(name),
	FOREIGN KEY (performer) references performers(name)
	);

SHOW tables;