from flask import Flask, request, redirect
from twilio import twiml
import re
import mailchimp

# set up Flask to connect this code to the local host, which will
# later be connected to the internet through Ngrok
app = Flask(__name__)
    
# Main method. When a POST request is sent to our local host through Ngrok 
# (which creates a tunnel to the web), this code will run. The Twilio service # sends the POST request - we will set this up on the Twilio website. So when # a message is sent over SMS to our Twilio number, this code will run
@app.route('/', methods=['POST'])

def incoming_sms():
  body = request.values.get('Body', None)

  email_pattern = re.compile("[a-zA-Z0-9\.\_\-]+@[a-zA-Z0-9\.\_\-]+\.[a-zA-Z]+")
 
  we_got_mail = 0

  # if we receive the keyword free the bot will ask for an email
  if body == "FREE" or body == "free":
    print ("Hi, at what email can I send you the report?")
  else: 
    #if no keyword is sent, then we will check if the message contains an email in it
    email = email_pattern.findall(body)
    if email[0] in body:
      we_got_mail = we_got_mail + 1
    
  # if the body contains an email this message will be sent
  if we_got_mail == 1:
    print ("Awesome, the report should be in your inbox in 12 minutes. Rock on!")

    return str(resp)

# now lets send this banana to mailchimp
API_KEY = 'my-api-key' # get this from mailchimp
LIST_ID = 'my-list-id' # get this from mailchimp

if we_got_mail == 1:
  api = mailchimp.Mailchimp(API_KEY)
  api.lists.subscribe(LIST_ID, {'email': email[0]})

if __name__ == "__main__":
    app.run(debug=True)
