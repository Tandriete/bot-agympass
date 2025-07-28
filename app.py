from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

app = Flask(__name__)

# Autenticando com Google Sheets
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)

# Abre sua planilha (coloque o nome exato)
sheet = gc.open_by_url(os.environ.get("SHEET_URL")).sheet1

@app.route("/webhook", methods=['POST'])
def webhook():
    msg = request.form.get('Body')
    sender = request.form.get('From')
    nome = request.form.get('ProfileName') or 'Desconhecido'

    # Cria resposta padrão
    resp = MessagingResponse()

    if "check-in feito" in msg.lower():
        data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        sheet.append_row([data, nome, sender, msg])
        resp.message(f"Check-in registrado com sucesso, {nome}! 💪✅")
    elif "link" in msg.lower():
        resp.message("Aqui está o link do check-in de hoje: https://forms.gle/seulink")
    else:
        resp.message("Oi! Mande 'check-in feito 💪' para registrar sua presença.")

    return str(resp)
