from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()
    response.say("Hello Sujith, your Twilio voice application is working.")
    return str(response)

@app.route("/")
def home():
    return "Twilio Voice App Running"

if __name__ == "__main__":
    app.run(debug=True)