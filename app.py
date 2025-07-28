import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "check-in feito" in incoming_msg:
        msg.body("✅ Check-in recebido com sucesso! 💪")
    else:
        msg.body("👋 Olá! Envie 'check-in feito 💪' para registrar sua presença!")

    return str(resp)

if name == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
