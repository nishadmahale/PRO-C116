# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
home=('localhost:5000'),
father=('http://127.0.0.1:5000'),
friend=('localhost:5000/friend')
mother=('localhost:5000/mother')
# default route or 'URL'
@app.route("/")
def home():

    name = "Alex" # write your name
    age = "12" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/")
def father():

    name="John"
    age="54"

    return render_template('father.html',name=name, age=age)



# define the route to mother webpage
@app.route("/")
def mother():

    name="Emily"
    age="45"
    return render_template('mother.html',name=name, age=age)

# define the route to friends webpage
@app.route("/")
def friend():

    name="Rocky"
    age="13"
    return render_template('friend.html',name=name, age=age)


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
