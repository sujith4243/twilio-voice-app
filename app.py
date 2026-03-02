import os
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
import openai

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()
    
    # Gather speech input
    gather = Gather(
        input="speech",
        action="/gather",
        method="POST",
        speech_model="default",
        timeout=5
    )
    gather.say("Hello! Ask me anything, and I will respond.")
    response.append(gather)

    # If no speech, repeat
    response.redirect("/voice")
    return str(response)

@app.route("/gather", methods=["POST"])
def gather():
    response = VoiceResponse()
    speech_result = request.values.get("SpeechResult")

    if speech_result:
        # Send speech to AI
        ai_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"The user said: {speech_result}. Reply clearly for a voice response.",
            max_tokens=50
        )
        reply = ai_response.choices[0].text.strip()
        response.say(reply)
    else:
        response.say("Sorry, I did not hear you.")
        response.redirect("/voice")

    return str(response)