import os
import random
import telebot
from flask import Flask, request

# -------------------------
# Configuração do bot
# -------------------------
CHAVE_API = "8378976247:AAGwzpdTg4avT0RyBQnDjT0gFAcYEdRCO74"
bot = telebot.TeleBot(CHAVE_API)

frases = [
    "“Sim, minha força está na solidão...” – Clarice Lispector",
    "'A leitura é para o intelecto o que o exercício é para o corpo.' – Joseph Addison",
    # ... restante das frases
]

livros_do_clube = [
    "'Dom Casmurro' - Machado de Assis",
    "'O Pequeno Príncipe' - Antoine de Saint-Exupéry",
    # ... restante dos livros
]

resumos_livros = {
    "dom casmurro": "Dom Casmurro é um romance de Machado de Assis...",
    "o pequeno príncipe": "O Pequeno Príncipe, de Antoine de Saint-Exupéry...",
    # ... restante dos resumos
}

quiz_perguntas = [
    {
        "pergunta": "Quem escreveu Dom Casmurro?",
        "alternativas": ["a) Álvares de Azevedo", "b) Machado de Assis", "c) José de Alencar"],
        "correta": "b) Machado de Assis"
    },
    # ... outras perguntas
]

# -------------------------
# Handlers do bot
# -------------------------
@bot.message_handler(commands=["start", "oi"])
def responder_inicio(mensagem):
    bot.reply_to(mensagem, "Olá! Aqui é o KindleBot. Use /frase, /clube, /livro, /quiz ou /resumo para interagir!")

@bot.message_handler(commands=["frase"])
def enviar_frase(mensagem):
    bot.reply_to(mensagem, random.choice(frases))

@bot.message_handler(commands=["clube"])
def enviar_livro_clube(mensagem):
    bot.reply_to(mensagem, random.choice(livros_do_clube))

@bot.message_handler(commands=["resumo"])
def enviar_resumo(mensagem):
    texto = mensagem.text.split("/resumo", 1)
    if len(texto) == 1 or not texto[1].strip():
        livros_disponiveis = "\n".join([f"- {livro.title()}" for livro in resumos_livros.keys()])
        bot.reply_to(mensagem, f"Livros disponíveis:\n{livros_disponiveis}\nUse /resumo nome_do_livro")
    else:
        nome_livro = texto[1].strip().lower()
        resumo = resumos_livros.get(nome_livro)
        if resumo:
            bot.reply_to(mensagem, f"Resumo de '{nome_livro.title()}':\n{resumo}")
        else:
            bot.reply_to(mensagem, "Desculpe, esse livro não está disponível.")

@bot.message_handler(commands=["quiz"])
def iniciar_quiz(mensagem):
    pergunta = random.choice(quiz_perguntas)
    msg = f"Pergunta: {pergunta['pergunta']}\n" + "\n".join(pergunta['alternativas'])
    bot.send_message(mensagem.chat.id, msg)
    bot.register_next_step_handler_by_chat_id(mensagem.chat.id, verificar_resposta, pergunta)

def verificar_resposta(mensagem, pergunta):
    resposta_usuario = mensagem.text.strip().lower()
    correta = pergunta["correta"].lower()
    letra_correta = correta[0]
    texto_correto = correta[3:].strip()

    if resposta_usuario == letra_correta or resposta_usuario == letra_correta + ")" or resposta_usuario == texto_correto.lower():
        bot.reply_to(mensagem, f"✅ Parabéns! Você acertou! A resposta correta é: {pergunta['correta']}")
    else:
        bot.reply_to(mensagem, f"❌ Errado! A resposta correta é: {pergunta['correta']}")
    bot.send_message(mensagem.chat.id, "Use /quiz para tentar outra pergunta!")

# -------------------------
# Flask para Webhook
# -------------------------
app = Flask(__name__)
WEBHOOK_URL = "https://bot-telegram-r4m4.onrender.com"  # Substitua pela URL do Render

bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

@app.route("/", methods=["POST"])
def webhook():
    json_data = request.get_json()
    update = telebot.types.Update.de_json(json_data)
    bot.process_new_updates([update])
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "🤖 KindleBot rodando!"

# -------------------------
# Rodando Flask
# -------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render define a porta automaticamente
    app.run(host="0.0.0.0", port=port)
