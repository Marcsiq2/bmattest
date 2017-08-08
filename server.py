#!/usr/bin/python
import ast
from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from flask import make_response
import datetime
import mysql.connector

server = Flask(__name__)

cnx = mysql.connector.connect(user= 'bmat',
	  password= 'bmat',
	  host= '127.0.0.1',
	  database= 'bmat_db')

cursor = cnx.cursor()


@server.route('/add_channel', methods=['POST'])
def add_channel():
	add_channel_sql = ("INSERT INTO radiostations (name) VALUES (%(name)s) ON DUPLICATE KEY UPDATE name = name;")
	data = request.form
	if not data or not 'name' in data:
		abort(404)
	cursor.execute(add_channel_sql, data)
	cnx.commit()
	return make_response(jsonify({}), 200)	

@server.route('/add_performer', methods=['POST'])
def add_performer():
	add_performer_sql = ("INSERT INTO performers (name) VALUES (%(name)s) ON DUPLICATE KEY UPDATE name = name;")
	data = request.form
	if not data or not 'name' in data:
		abort(400)
	cursor.execute(add_performer_sql, data)
	cnx.commit()
	return make_response(jsonify({}), 200)	

@server.route('/add_song', methods=['POST'])
def add_song():
	add_song_sql = ("INSERT INTO songs (title, performer) VALUES (%(title)s, %(performer)s) ON DUPLICATE KEY UPDATE title = title;")
	data = request.form
	if not data or not 'title' in data or not 'performer' in data:
		abort(400)
	cursor.execute(add_song_sql, data)
	cnx.commit()
	return make_response(jsonify({}), 200)	

@server.route('/add_play', methods=['POST'])
def add_play():
	add_play_sql = ("INSERT INTO plays (title, channel, performer, start, end) VALUES (%(title)s, %(channel)s, %(performer)s, %(start)s, %(end)s);")
	data = request.form
	if not data or not 'title' in data:
		abort(400)
	cursor.execute(add_play_sql, data)
	cnx.commit()
	return make_response(jsonify({}), 200)	

@server.route('/get_channel_plays', methods=['GET'])
def get_channel_plays():
	get_channel_plays_sql = ("SELECT * FROM plays WHERE channel=%(channel)s AND start > %(start)s AND end < %(end)s")
	data = request.args
	cursor.execute(get_channel_plays_sql, data)
	res = []
	for item in cursor.fetchall():
		res.append(dict(zip(cursor.column_names, item)))
	return make_response(jsonify({'result':res, 'code':0}), 200)

@server.route('/get_song_plays', methods=['GET'])
def get_song_plays():
	get_song_plays_sql = ("SELECT * FROM plays WHERE title=%(title)s AND performer=%(performer)s AND start > %(start)s AND end < %(end)s")
	data = request.args
	cursor.execute(get_song_plays_sql, data)
	res = []
	for item in cursor.fetchall():
		res.append(dict(zip(cursor.column_names, item)))
	return make_response(jsonify({'result':res, 'code':0}), 200)

@server.route('/get_top', methods=['GET'])
def get_top():
	data = request.args
	channels = ast.literal_eval(data['channels'])
	channels_str = '(\'%s\')' % '\', \''.join(map(str, channels))
	date = datetime.datetime.strptime(data['start'], '%Y-%m-%dT%H:%M:%S')

	get_top_sql = ("SELECT @rownum := @rownum +1 AS rank, prequery.title, prequery.performer, prequery.plays FROM "
	"( SELECT @rownum := -1 ) sqlvars, ( SELECT title, performer, count(title) plays FROM plays "
	"WHERE channel IN " + channels_str + " AND start BETWEEN \'"+ str(date.date()) + "\' AND \'" + str((date + datetime.timedelta(days=7)).date()) +
	"\' GROUP BY title, performer ORDER BY count(title) DESC ) prequery")

	cursor.execute(get_top_sql, data)

	res = []
	for item in cursor.fetchall():
		item_dict = dict(zip(cursor.column_names, item))
		item_dict['rank'] = int(item_dict['rank'])
		res.append(item_dict)

	songs = [i['title'].encode('utf-8') for i in res]
	songs_str = '(\'%s\')' % '\', \''.join(map(str, songs))

	get_pw_top_sql = ("SELECT @rownum := @rownum +1 AS previous_rank, prequery.title, prequery.performer, prequery.previous_plays FROM "
	"( SELECT @rownum := -1 ) sqlvars, ( SELECT title, performer, count(title) previous_plays FROM plays "
	"WHERE title IN " + songs_str + " AND start BETWEEN \'"+ str((date + datetime.timedelta(days=-7)).date()) + "\' AND \'" + str(date.date()) +
	"\' GROUP BY title, performer ORDER BY count(title) DESC ) prequery")

	cursor.execute(get_pw_top_sql, data)

	res_pw = []
	for item in cursor.fetchall():
		item_dict = dict(zip(cursor.column_names, item))
		item_dict['previous_rank'] = int(item_dict['previous_rank'])
		res_pw.append(item_dict)	

	results = []
	for item in res:
		for item2 in res_pw: 
			if item2['title'] == item['title'] and item2['performer'] == item['performer']:
				item.update(item2)	
		results.append(item)

	return make_response(jsonify({'result':results, 'code':0}), 200)


@server.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': "The request could not be understood by the server due to malformed syntax. "
    	"The client SHOULD NOT repeat the request without modifications."}), 400)

if __name__ == '__main__':
	server.run(debug=True)