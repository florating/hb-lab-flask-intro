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


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page. \
    <br><a href="/hello">Click here to say hello!</a>
    <br>This is a test!</html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <style>
            .submit {
                margin: 0
            }

        </style>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          <label for="compliment-select">Choose a compliment:</label>
          <select name="compliment" id="compliment-select">
            <option value="">--Please choose an option--</option>
            <option value="cool">cool</option> 
            <option value="gorgeous">gorgeous</option>
            <option value="fantastic">fantastic</option>
          </select><!--
       --><br><input type="submit" value="Submit"><input type="submit" value="Diss Submit" action="/diss">
        </form>
        <div>
            <h3>Do you want to be adventurous?</h3>
            <form action="/diss">
                What's your name? <input type="text" name="person">
                <br><label for="diss-select">Choose an insult:</label>
          <select name="insult" id="diss-select">
            <option value="">--Please choose an option--</option>
            <option value="mean">mean</option> 
            <option value="not a nice person">not a nice person</option>
            <option value="smelly">smelly</option>
          </select><!--
       --><br>
            <input type="submit" value="Diss Submit" action="/diss">
            </form>
        </div>
      </body>
    </html>
    """
    # Options from AWESOMENESS list? Or ones we create directly?
    # https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    # compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


@app.route('/diss')
def insult_person():
    """Insult the user by name."""

    player = request.args.get("person")

    insult = request.args.get("insult")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
