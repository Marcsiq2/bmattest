CREATE DATABASE bmat;
USE bmat;
CREATE TABLE radiostations (
	name VARCHAR(150) NOT NULL, 
	PRIMARY KEY (name)
	);
CREATE TABLE performers (
	name VARCHAR(150) NOT NULL, 
	PRIMARY KEY (name)
	);
CREATE TABLE songs (
	name VARCHAR(150) NOT NULL, 
	performer VARCHAR(150) NOT NULL,
	PRIMARY KEY (name), 
	FOREIGN KEY (performer) references performers(name) ON UPDATE cascade,
	);
CREATE TABLE plays (
	song VARCHAR (150) NOT NULL,
	radiostation VARCHAR (150) NOT NULL,
	start_time datetime NOT NULL,
	end_time datetime NOT NULL,
	FOREIGN KEY (song) references songs(name),
	FOREIGN KEY (radiostation) references radiostations(name)
	);
