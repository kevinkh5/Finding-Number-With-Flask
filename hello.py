from flask import Flask

app = Flask(__name__)
def make_bold(function):
    def wrapper_function():
        string = function()
        return '<b>'+string+'</b>'
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        string = function()
        return '<em>'+string+'</em>'
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        string = function()
        return '<u>'+string+'</u>'
    return wrapper_function

@app.route('/')
def hello_world():
    return '<h1 style="text-align:center"> Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbndkYmI4aGFhbDh6bDVmNmsxazRrN3ZhdmI3dHg5d2V5YnZjdmJxcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YRVP7mapl24G6RNkwJ/giphy.gif" width=200>'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye !'

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f'Hello there! {name} , you are {number}years old!'


if __name__  == "__main__":
    app.run(debug=True)


