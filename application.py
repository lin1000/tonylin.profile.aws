from flask import Flask, render_template
from flask_socketio import SocketIO
from flask.json import jsonify
from jinja2 import Environment
import jinja2
from datetime import datetime
import simplejson
import logging
import sys
import os
from boto.s3.connection import S3Connection

if(len(sys.argv) == 1 ):
    logging.basicConfig(filename='/opt/python/log/myappl    ication.log', level=logging.DEBUG)
elif(len(sys.argv) == 2 and sys.argv[1]=='local'):
    logging.basicConfig(filename='myapplication.log', level=logging.DEBUG)
else:
    print "python application.py [local]"
    sys.exit(1)

#jinja2 template environment settings
def to_json(value):
    return simplejson.dumps(value)

jinja2.filters.FILTERS['to_json'] = to_json


# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test with websocket </title> </head>\n<body>'''
instructions = '''
    There is an endpoint of websocket (staged) 
    \n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)
application.config['SECRET_KEY'] = 'secret!'
application.jinja_env.line_statement_prefix = '#'
socketio = SocketIO(application)

# add a rule for the index page.
#application.add_url_rule('/', 'index', (lambda: header_text +
#    say_hello() + instructions + footer_text))

@application.route("/index")
def index():
    return render_template('index.html')

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))



@application.route("/s3")
def myS3():
    """
        list s3 buckets 
    """
    AWS_KEY = os.environ.get('awsappkey')
    AWS_SECRET = os.environ.get('awsappsecret')
    aws_connection = S3Connection(AWS_KEY, AWS_SECRET)
    bucket = aws_connection.get_bucket('lin1000')
    file_list = []
    for file_key in bucket.list():
        file_list.append(file_key.name)
    return jsonify({'file_list': file_list}) 

@socketio.on('message')
def handle_message(message):
    print 'received message: {%s}' % (message)

@socketio.on('my event')
def handle_my_custom_event(json):
    print 'received json: {%s}' % (str(json))

@socketio.on('2017_api_traffic_demo_register_api')
def handle_2017_api_traffic_demo_register_api(json):
    #Inbox of API Traffic and stored into a temp storage space or streaming container
    #Then visualize the traffic on a Ajax HTML page to demonstrate it.
    print 'received json: {%s}' % (str(json))
    logging.info("received json: {myjson}".format(myjson=str(json)))
    socketio.emit('2017_api_traffic_demo_register_api_push', json)

@socketio.on('2017_api_traffic_demo_track_api_start')
def handle_2017_api_traffic_demo_track_api_start(json):
    #Inbox of API Traffic and stored into a temp storage space or streaming container
    #Then visualize the traffic on a Ajax HTML page to demonstrate it.
    start_ts = datetime.utcnow().strftime("%s")
    print 'received json: {%s}' % (str(json))
    logging.info("received json: {myjson} at {datetime}".format(myjson=str(json),datetime=start_ts))
    json['timestamp'] = start_ts
    socketio.emit('2017_api_traffic_demo_track_api_start_push', json)

@socketio.on('2017_api_traffic_demo_track_api_end')
def handle_2017_api_traffic_demo_track_api_end(json):
    #Inbox of API Traffic and stored into a temp storage space or streaming container
    #Then visualize the traffic on a Ajax HTML page to demonstrate it.
    start_ts = datetime.utcnow().strftime("%s")
    print 'received json: {%s}' % (str(json))
    logging.info("received json: {myjson} at {datetime}".format(myjson=str(json),datetime=start_ts))
    json['timestamp'] = start_ts
    socketio.emit('2017_api_traffic_demo_track_api_end_push', json)


@application.route("/2017_api_traffic_demo")
def route_2017_api_traffic_demo():
    return render_template('2017_api_traffic_demo.html', \
        events=[["2017_api_traffic_demo_register_api", {"api_name":"OrderUberEATS"}],\
                ["2017_api_traffic_demo_register_api_push", {"api_name":"OrderUberEATS"}],\
                ["2017_api_traffic_demo_track_api_start", {"call_id":"00000001","to_api_name":"RestaurantAvailability", "from_api_name":"OrderUberEATS", "call_style":"sync"}],\
                ["2017_api_traffic_demo_track_api_start_push", {"call_id":"00000001", "to_api_name":"RestaurantAvailability", "from_api_name":"OrderUberEATS", "call_style":"sync", "timestamp":"1499863498"}],\
                ["2017_api_traffic_demo_track_api_end", {"call_id":"00000001", "to_api_name":"RestaurantAvailability", "from_api_name":"OrderUberEATS", "call_style":"sync"}],\
                ["2017_api_traffic_demo_track_api_end_push", {"call_id":"00000001", "to_api_name":"RestaurantAvailability", "from_api_name":"OrderUberEATS", "call_style":"sync", "timestamp":"1499863499"}]\
                ])

@application.route("/2017_api_traffic_demo_2")
def route_2017_api_traffic_demo_2():
    return render_template('2017_api_traffic_demo_2.html', \
        events=[["2017_api_traffic_demo_register_api", {"api_name":"OrderUberEATS"}],\
                ["2017_api_traffic_demo_register_api_push", {"api_name":"OrderUberEATS"}],\
                ["2017_api_traffic_demo_track_api_start", {"call_id":"00000001","to_api_name":"RestaurantAvailability", "from_api_name":"OrderUberEATS", "call_style":"sync"}],\
                ["2017_api_traffic_demo_track_api_start_push", {"call_id":"00000001", "to_api_name":"RestaurantAvailability", "from_api_name":"OrderUberEATS", "call_style":"sync", "timestamp":"1499863498"}],\
                ["2017_api_traffic_demo_track_api_end", {"call_id":"00000001", "to_api_name":"RestaurantAvailability", "from_api_name":"OrderUberEATS", "call_style":"sync"}],\
                ["2017_api_traffic_demo_track_api_end_push", {"call_id":"00000001", "to_api_name":"RestaurantAvailability", "from_api_name":"OrderUberEATS", "call_style":"sync", "timestamp":"1499863498"}]\
                ])                


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    #application.run()
    socketio.run(application)
