"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']
ANIMALS = ['dog', 'cat', 'penguin', 'tiger', 'giraffe', 'yak', 'elephant']


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
        <body>
        Hi! This is the home page.
        <br>
        <br>
        <a href="/hello">link ToHello</a>
        </body>
    </html>
    """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""
    compliment_list = []
   

    x = " ".join(compliment_list)

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          <br>
           {%for item in AWESOMENESS%}
            <input type='radio' name='compliment' value='{{item}}'>
            {%endfor%}
          <br>
          <br>
          <input type="submit" value="Submit">
          <br>
          <br>
        </form>
        <form action="/animal">
          What's your name? <input type="text" name="person">
          <br>
          <br>
          <input type="radio" name="animal" value="dog">Dog</input>
          <input type="radio" name="animal" value="cat">Cat</input>
          <input type="radio" name="animal" value="penguin">Penguin</input>
          <input type="radio" name="animal" value="tiger">Tiger</input>
          <input type="radio" name="animal" value="elephant">Elephant</input>
          <input type="radio" name="animal" value="giraffe">Giraffe</input>
          <input type="radio" name="animal" value="yak">Yak</input>
          <br>
          <br>
          <input type="submit" value="Submit"></input>
        </form>


      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    # compliment = choice(AWESOMENESS)

    # y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)



@app.route("/animal")
def favorite_animal():
    """Get favorite animal abd get image"""

    player = request.args.get("person")
    animal = request.args.get("animal")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A animal</title>
      </head>
      <body>
        Hi, {}! Your favorite animal is {}!
      </body>
    </html>
    """.format(player, animal)





if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
