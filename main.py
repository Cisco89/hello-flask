from flask import Flask, request, render_template, redirect
import cgi
import os
import jinja2

template_directory = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader= jinja2.FileSystemLoader(template_directory), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

def is_interger(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/")
def index():
    template = jinja_env.get_template('hello-form.html')
    return template.render()

# @app.route('/')
# def my_form():
#     return render_template('my-form.html')

# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text
    
@app.route("/hello", methods=['POST'])
def hello():
    # first_name = request.args.get('first_name')   # for GET request
    first_name = request.form['first_name']         # for a POST Request
    # cgi.escape turns the simbols into html format and does not inject 
    # html into our form
    template = jinja_env.get_template('hello-greeting.html')
    return  template.render(name=first_name)

@app.route("/narnia/")
def narnia():
    return "Welcome to Narnia"

@app.route("/mexico/")
def mexico():
    return "Hola Mundo"

@app.route('/validate-time')
def display_time_form():
    template = jinja_env.get_template('time-form.html')
    return template.render()

@app.route('/validate-time', methods=['POST'])
def validate_time():
    
    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_interger(hours):
        hours_error = 'Not a valid Interger'
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour value out of range (0-23)'

    if not is_interger(minutes):
        minutes_error = 'Not a valid Interger'
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
    
    if not minutes_error and not hours_error:
        time = str(hours) + ":" + str(minutes)
        return redirect('/valid-time?time={0}'.format(time))
    else:
        template = jinja_env.get_template('time-form.html')
        return template.render(
            hours_error=hours_error, 
            minutes_error=minutes_error,
            hours=hours,
            minutes=minutes)

@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submited {0}. Thanks for submiting a valid time!</h1>'.format(time)

app.run()
