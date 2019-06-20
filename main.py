from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="post">
            <label for="first_name">First Name</label>
            <input type="text" name="first_name" />
            <input type="submit" />
        </form>
    </body>
</html>
"""

# @app.route("/")
# def index():
#     return form

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text
    
@app.route("/hello", methods=['POST'])
def hello():
    # first_name = request.args.get('first_name')   # for GET request
    first_name = request.form['first_name']         # for a POST Request
    return '<h1>Hello, ' + first_name + '</h1>'

@app.route("/narnia/")
def narnia():
    return "Welcome to Narnia"

@app.route("/mexico/")
def mexico():
    return "Hola Mundo"

app.run()
