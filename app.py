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
    R1.media("https://cdn.shopify.com/s/files/1/0885/7466/products/smiley-decal_740x.png?v=1537890800.jpg")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
