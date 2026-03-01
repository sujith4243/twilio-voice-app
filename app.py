from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()

    # Create a Gather to collect keypad input
    gather = Gather(num_digits=1, action="/gather", method="POST")
    gather.say("Hello Sujith. Press 1 for a greeting. Press 2 to hear a fun fact.")
    response.append(gather)

    # If no input, repeat menu
    response.redirect("/voice")

    return str(response)

# Handle the input
@app.route("/gather", methods=["POST"])
def gather():
    response = VoiceResponse()
    digit = request.values.get('Digits')

    if digit == '1':
        response.say("Hello! This is your greeting from the Twilio app.")
    elif digit == '2':
        response.say("Here is a fun fact: Honey never spoils!")
    else:
        response.say("Sorry, I did not understand.")
        response.redirect("/voice")  # Go back to menu

    return str(response)

@app.route("/")
def home():
    return "Twilio Voice App Running"