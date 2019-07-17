from flask import Flask, request, redirect
from twilio import twiml
import re

# set up Flask to connect this code to the local host, which will
# later be connected to the internet through Ngrok
app = Flask(__name__)
    
# Main method. When a POST request is sent to our local host through Ngrok 
# (which creates a tunnel to the web), this code will run. The Twilio service # sends the POST request - we will set this up on the Twilio website. So when # a message is sent over SMS to our Twilio number, this code will run
@app.route('/', methods=['POST'])
def incoming_sms():
    # Get the text in the message sent
    body = request.values.get('Body', None)
    body_lowercase = body.lower()
    clean_body = re.sub(r'[^\w]', '', body_lowercase)
    
    # Start our TwiML response
    resp = twiml.Response()

    # Determine the right reply for this message
    if clean_body == 'tellmeacard':
        resp.message("Sure, what about the three of hearts!")
    elif clean_body == 'cualesmicarta':
        resp.message("Tu carta es el siete de corazones")
    elif clean_body == 'whatismycard':
        resp.message("Tu carta es el siete de espadas")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
