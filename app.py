from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from utils import fetch_reply

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    print(request.form)
    msg = request.form.get('Body')
    sender = request.form.get('From')

    # Create reply
    resp = MessagingResponse()
    R1=resp.message(fetch_reply(msg, sender))
    R1.media("https://bloximages.newyork1.vip.townnews.com/theadvocate.com/content/tncms/assets/v3/editorial/2/19/2190d8b6-d670-5edf-b0ca-b1e7570932b5/5cf92cd90e0ba.image.jpg?crop=1224%2C1224%2C234%2C0&resize=1224%2C1224&order=crop%2Cresize.jpg")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)