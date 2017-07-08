from flask import Flask
from flask_socketio import SocketIO

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test with websocket </title> </head>\n<body>'''
instructions = '''
    There is an endpoint of websocket 
    \n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)
application.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(application)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

@socketio.on('message')
def handle_message(message):
    print 'received message: {%s}' % (message)

@socketio.on('my event')
def handle_my_custom_event(json):
    print 'received json: {%s}' % (str(json))

@socketio.on('2017_api_traffic_demo')
def handle_2017_api_traffic_demo(json):
    #Inbox of API Traffic and stored into a temp storage space or streaming container
    #Then visualize the traffic on a Ajax HTML page to demonstrate it.
    print 'received json: {%s}' % (str(json))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    #application.run()
    socketio.run(application)
