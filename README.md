Bmat Test
=======

## Deliverable
+ ***Design Choices***

In order to store the described data, I chose to use a structured database. Using a structured database is not always an advantage, but for this kind of data it's very usefull. I created 4 different tables (radiostations, performers, songs, plays) with just the needed information described in the deliverable. This database can be extended very easily in order to add more information for each Class (song length, performer gender, radiostation country, ...).
From all structured databases I chose to use MySQL database as it is very easy to scalate, it is open-source, offers high performance and it is known as one of the most secure and reliable database management systems.

For the web service I used Flask for python because it is very simple and easy to prototype micro-framework and it does not require particular tools or libraries.

+ ***Improvements for use in production***
  + I would suggest adding a security protocol to query the server.
  + Add a threading model to server simultaneous requests as the current implementation is a single synchronous server on a single thread.
  + Use a distributed and replicated database.
  
+ ***Ten million songs and two thousend channels monitoring:***

I think that with the current implementation the server would crash, however with the proposed improvements for use in production the server would not have serious problems, despite probably a bit of latency.


## Requirements
```
mysql-server
python >= 2.7
python-flask
python-mysql.connector
```

## Usage
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
