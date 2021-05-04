from flask import Flask, render_template, app, request, session, redirect, json, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
import os
os.system("cls")

app = Flask(__name__)
app.secret_key = "super secret key"

#----------------------------------------------------------------------------------------------------

bot=ChatBot(name='ChatterBot',
            # Define the logic that ChatterBot 
            # uses to respond to input it receives.
            logic_adapters=[ 'chatterbot.logic.MathematicalEvaluation',
                             'chatterbot.logic.BestMatch'],
                             # 'chatterbot.logic.TimeLogicAdapter'],

            # Compares the input statement to known statements. 
            # Finds the closest match to the input statement, 
            # Selects one of the known responses to that statement.

            # Storage adapters - Provide an interface for ChatterBot 
            # to connect to various storage systems eg. local file storage.
            storage_adapter="chatterbot.storage.SQLStorageAdapter")

greetings=[ 'Hi',
            'Hello',
            'Hey there!',
            'Hey, how\'s your day going?',
            'Good',
            'i am good',
            'That\'s good to hear.',
            'Glad !',
            'How are you',
            'Awesome',
            'Glad to hear so..',
            'How you doing?',
            'Algorithm\'s working fine..',
            'Who are you?',
            'I am a newbie chatbot. Sorry if I misbehave',
            'Where do you stay?',
            'In your computer',
            'Whats the time?',
            'I am not smart enough to tell you the time']

random_talks=[  'Bored in pandemic?',
                'Yes too bored.',
                'what should i do now',
                'just stay home and stay safe',
                'ok',
                'hmmm',
                'hmmm',
                'are you a humming bird',
                'no i am a software',
                'covid',
                'Get vaccinated as soon as possible!',
                'pandemic',
                'just stay home and stay safe',
                ]

maths=[ 'multiplication',
        'x multiplied by y is equal to adding x, y times to itself',
        'multiply',
        'x multiplied by y is equal to adding x, y times to itself',
        'pythagorus',
        'Great mathematician.',
        'pythagorus theorem ',
        'a^2 + b^2 = c^2',
        'types of triangles',
        'right-angled, scalene and isosceles',
        ]

online_business=[   'Whats your company name?',
                    'Hello, its BurgerKing!',
                    'what do you sell?',
                    'tasty burgers',
                    'when are you open',
                    '9am to 11 pm',
                    'what is your address',
                    'we can send you a mail about everything',
                    'what time are you open',
                    '9am to 11 pm',
                    'What would you like to have sir?'
                ]

# Each item in the list becomes
# a possible response to it’s predecessor in the list.

training_lists=[greetings,maths,random_talks,online_business]

# Allows a chat bot to be trained using 
# a list of strings where the list represents a conversation.
list_trainer=ListTrainer(bot)
for x in training_lists:
    list_trainer.train(x)

# Train using chatterbot corpus
bot_trainer = ChatterBotCorpusTrainer(bot)
bot_trainer.train("chatterbot.corpus.english.greetings","chatterbot.corpus.english")

# Search algorithms
# naive Bayesian classification algorithms 
# to determine if an input statement meets a particular set of criteria 


#----------------------------------------------------------------------------------------------------


@app.route("/get_response_from_bot", methods=['POST','GET'])
def get_response_from_bot():
    user_msg=""
    if request.method == 'POST':
        user_msg = request.form['input']

    bot_response=str(bot.get_response(user_msg))    # Getting response from bot

    return bot_response

@app.route("/")
def home():
    return render_template("chatbot.html")


@app.after_request
def add_header(r):

    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True)
