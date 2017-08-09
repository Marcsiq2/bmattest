# bmattest
Bmat Test
=========

# Table of contents
	* [Requirements](##Requirements)
	* [Usage](##Usage)

##Requirements
```
mysql-server
python >= 2.7
python-flask
python-mysql.connector

```
##Usage
+ MySQL DB creation
```
usage: mysql -u <user> -p < create_db.sql
```
+ Server
```
usage: server.py [-h] [-P SERVER_PORT] [-H MYSQL_HOSTNAME] [-U MYSQL_USER]
                 [-p MYSQL_PASSWORD] [-D MYSQL_DATABASE]

optional arguments:
  -h, --help         show this help message and exit
  -P SERVER_PORT     Server Listening Port
  -H MYSQL_HOSTNAME  MySQL Server host
  -U MYSQL_USER      MySQL Server user
  -p MYSQL_PASSWORD  MySQL Server password
  -D MYSQL_DATABASE  MySQL Server database
```
+ Test
```
usage: test.py [-h] [-H HOSTNAME] [-P PORT] [--add-data]

optional arguments:
  -h, --help   show this help message and exit
  -H HOSTNAME
  -P PORT
  --add-data   Insert test data (only use the first time you run the script
```
