from bottle import Bottle, run, template
 
app = Bottle()
 
@app.route('/home')
def hello():
    return template("home.tpl")
 
run(app, host='localhost', port=8080)

