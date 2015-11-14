from bottle import run, template, view, static_file, route, request 
  
@route('/home')
@view('home.tpl')
def home():
    return dict()

@route('/login')
@view('login.tpl')
def login():
    return dict()

def check_login(username, password):
    if username == "lol" and password == "lol":
        return True 
    else:
        return False 

@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    print(username , " " , password)
    if check_login(username, password):
        return template('home.tpl', name=username)
    else:
        return template('login.tpl', notauthorized=True)

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')
 
run(host='localhost', port=8080, debug=True)

