import telebot
import random

CHAVE_API = "8378976247:AAGwzpdTg4avT0RyBQnDjT0gFAcYEdRCO74"
bot = telebot.TeleBot(CHAVE_API)

frases = [
    "“Sim, minha força está na solidão. Não tenho medo nem de chuvas tempestivas, nem das grandes ventanias soltas, pois eu também sou o escuro da noite..” – Clarice Lispector",
    "'A leitura é para o intelecto o que o exercício é para o corpo.' – Joseph Addison",
    "'Um livro é um sonho que você segura com as mãos.' – Neil Gaiman",
    "'Ler é sonhar pela mão de outro.' – Fernando Pessoa!",
    "“Não há lugar como o nosso lar.” – O Mágico de Oz, L. Frank Baum",
    "“É só com o coração que se pode ver direito; o essencial é invisível aos olhos.” – O Pequeno Príncipe, Antoine de Saint-Exupéry",
    "“A liberdade é apenas uma oportunidade para ser melhor.” – Albert Camus, A Peste",
    "“Todos nós temos luz e sombra dentro de nós. O que importa é a parte que decidimos nutrir.” – O Hobbit, J.R.R. Tolkien",
    "“As pessoas que amamos nunca nos deixam de verdade.” – Harry Potter e o Cálice de Fogo, J.K. Rowling",
    "“Não se preocupe com o amanhã; ele se preocupará consigo mesmo.” – O Sol é Para Todos, Harper Lee",
    "“Se você quer mudar o mundo, comece por você mesmo.” – O Pequeno Príncipe, Antoine de Saint-Exupéry",
    "“A espécie humana finge ser tão resiliente. As vidas mortais são uma longa brincadeira de faz de conta. Se vocês não pudessem mentir para si mesmos, cortariam a própria garganta para acabar com sua infelicidade.” – O Príncipe Cruel, Holly Black",
    "Eu ficava feliz quando estava com ela, mas isso doía um pouco, e doía quando não estávamos juntos também. - Percy jackson, Rick riordan",
    "“O poder é bem mais fácil de adquirir do que de manter. - O Príncipe Cruel, Holly Black”"
]

livros_do_clube = [
    "'Dom Casmurro' - Machado de Assis",
    "'O Pequeno Príncipe' - Antoine de Saint-Exupéry",
    "'1984' – George Orwell",
    "'Capitães da Areia' – Jorge Amado",
    "'Água Viva' – Clarice Lispector",
    "'As mil partes do meu coração' – Collen Hoover",
    "'Melhor do que nos filmes' – Lynn Painter",
    "'Divinos rivais' - Rebeca Ross",
    "'O Príncipe Cruel', Holly Black",
    "'Percy Jackson e o O Ladrão de Raios - Rick Riordan",
    "'Memórias Póstumas de Brás Cubas' - Machado de Assis",
    "'O Cortiço' - Aluísio Azevedo",
    "'Vidas Secas' - Graciliano Ramos",
    "'Capitães da Areia' - Jorge Amado",
    "'Grande Sertão: Veredas' - Guimarães Rosa"
]

resumos_livros = {
    "dom casmurro": "Dom Casmurro é um romance de Machado de Assis que narra a vida de Bento Santiago, conhecido como Dom Casmurro, abordando temas como ciúmes, traição e a dúvida sobre a fidelidade de Capitu.",
    "o pequeno príncipe": "O Pequeno Príncipe, de Antoine de Saint-Exupéry, conta a história de um pequeno príncipe que viaja por planetas diferentes e aprende lições sobre amor, amizade e humanidade.",
    "1984": "1984, de George Orwell, é uma distopia que descreve um futuro totalitário onde o governo controla todos os aspectos da vida, incluindo pensamentos e comportamentos.",
    "capitães da areia": "Capitães da Areia, de Jorge Amado, narra a vida de um grupo de meninos de rua em Salvador e suas aventuras, desafios e sonhos.",
    "água viva": "Água Viva, de Clarice Lispector, é uma narrativa introspectiva e poética que explora pensamentos e sensações da narradora em fluxo de consciência.",
    "as mil partes do meu coração": "As Mil Partes do Meu Coração, de Colleen Hoover, conta a história de uma jovem lidando com um coração partido e os desafios do amor e amizade.",
    "melhor do que nos filmes": "Melhor do Que Nos Filmes, de Lynn Painter, acompanha a vida de uma adolescente enfrentando as dificuldades do primeiro amor e os desafios da vida adolescente."
}

quiz_perguntas = [
    {
        "pergunta": "Quem escreveu Dom Casmurro?",
        "alternativas": ["a) Álvares de Azevedo", "b) Machado de Assis", "c) José de Alencar"],
        "correta": "b) Machado de Assis"
    },
    {
        "pergunta": "Qual autor criou o personagem Sherlock Holmes?",
        "alternativas": ["a) Agatha Christie", "b) Arthur Conan Doyle", "c) Edgar Allan Poe"],
        "correta": "b) Arthur Conan Doyle"
    },
    {
        "pergunta": "Em qual livro aparece o personagem Frodo Bolseiro?",
        "alternativas": ["a) O Hobbit", "b) O Senhor dos Anéis", "c) As Crônicas de Nárnia"],
        "correta": "b) O Senhor dos Anéis"
    }
]

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
        bot.reply_to(mensagem, f"Livros disponíveis para resumo:\n{livros_disponiveis}\n\nUse /resumo nome_do_livro para receber o resumo.")
    else:
        nome_livro = texto[1].strip().lower()
        resumo = resumos_livros.get(nome_livro)
        if resumo:
            bot.reply_to(mensagem, f"Resumo de '{nome_livro.title()}':\n{resumo}")
        else:
            bot.reply_to(mensagem, "Desculpe, esse livro não está disponível no banco de resumos.")

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

    if (resposta_usuario == letra_correta or
        resposta_usuario == letra_correta + ")" or
        resposta_usuario == texto_correto.lower()):
        bot.reply_to(mensagem, f"✅ Parabéns! Você acertou! A resposta correta é: {pergunta['correta']}")
    else:
        bot.reply_to(mensagem, f"❌ Errado! A resposta correta é: {pergunta['correta']}")

    bot.send_message(mensagem.chat.id, "Use /quiz para tentar outra pergunta!")

print("🤖 Bot está rodando... Envie /start ou /oi no Telegram")
bot.infinity_polling()
