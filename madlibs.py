from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person", "there")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_game_form():
    """Starts madlib game or allows user to exit."""

    want_to_play_game = request.args.get("playgame")

    if want_to_play_game == 'yes':
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Shows result of madlib."""

    #print "COLOR HERE**************", request.args.getlist("color", "NO COLOR")

    # player_color = request.args.getlist("color", "No Colors")
    # print player_color

    player_person = request.args.get("person").title()
    # print player_person
    player_color = choice(request.args.getlist("color"))
    player_noun = request.args.get("noun").lower()
    player_adjective = request.args.get("adjective").lower()

    return render_template("madlib.html",
                            person=player_person,
                            color=player_color,
                            noun=player_noun,
                            adjective=player_adjective)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
