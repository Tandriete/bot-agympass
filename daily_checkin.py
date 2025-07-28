import os
from twilio.rest import Client

# Dados de autenticação do Twilio (estão nas variáveis de ambiente no Render)
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_number = os.environ.get("TWILIO_PHONE_NUMBER")

# Número do destinatário
to_number = "whatsapp:+5519997366483"

# Link do Google Forms de Check-in
form_link = "https://forms.gle/1CVMr9kQhXD8WYME7"  # <- coloque aqui o seu link encurtado, se quiser

# Mensagem
message_body = (
    "🌞 *Bom dia, guerreiro(a)!*\n\n"
    "Bora garantir o seu check-in de hoje? 💪\n"
    "Clique aqui e registre sua presença: 👉 " + form_link + "\n\n"
    "_Lembre-se: a consistência vence!_"
)

# Envia a mensagem
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=message_body,
    from_=twilio_number,
    to=to_number
)

print("✅ Mensagem de check-in enviada com sucesso!")
