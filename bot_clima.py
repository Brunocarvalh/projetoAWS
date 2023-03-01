import telebot
import requests

while True:

    token = '6121181851:AAGW01meCDYWtnWlMrML5H5uw9Ux49k2FlU'
    keyAPI = 'a55f44377b94c4cebde09fdf2772f6a4'
    bot = telebot.TeleBot(token)

    def clima(lat, lon): #chamada API para temperatura em Campanha
        link = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={keyAPI}&lang=pt_br'
        requisicao = requests.get(link)

        requisicao_dic = requisicao.json() 

        x = requisicao_dic['list'][0]['weather'][0]['description']
        dados = requisicao_dic['list'][0]['main']
        temperatura = dados['temp'] - 273.15
        temp_max = dados['temp_max'] - 273.15
        temp_min = dados['temp_min'] - 273.15
        umidade = dados['humidity']
        pressao = dados['pressure']
        
        texto = f'''

        Temperatura:{int(temperatura)} ºC
        Temperatura Máxima: {int(temp_max)} ºC
        Temperatura Mínima: {int(temp_min)} ºC
        Umidade: {int(umidade)} %
        Pressão: {int(pressao)} mb
        Previsão: {x}
        '''
        return texto

    @bot.message_handler(commands=['Campanha'])
    def cpa(mensagem):
            lat = '-21.832996392844816'
            lon = '-45.40033229564984'
            bot.send_message(1375101706, "DADOS CLIMÁTICOS EM CAMPANHA-MG")
            bot.reply_to(mensagem, clima(lat, lon))
            print(clima(lat, lon))

    @bot.message_handler(commands=['Santa_Rita_do_Sapucai'])
    def srs(mensagem):
            lat = '-22.25657254864942'
            lon = '-45.69758850048965'
            bot.send_message(1375101706, "DADOS CLIMÁTICOS EM Santa Rita do Sapucaí-MG")
            bot.reply_to(mensagem, clima(lat, lon))
            print(clima(lat, lon))

    @bot.message_handler(commands=['Pouso_Alegre'])
    def pa(mensagem):
            lat = '-22.230924686823894'
            lon = '-45.934944124622135'
            bot.send_message(1375101706, "DADOS CLIMÁTICOS EM Pouso Alegre-MG")
            bot.reply_to(mensagem, clima(lat, lon))
            print(clima(lat, lon))

    @bot.message_handler(commands=['Tres_Coracoes'])
    def tc(mensagem):
            lat = '-21.692500767149852'
            lon = '-45.25971064439421'
            bot.send_message(1375101706, "DADOS CLIMÁTICOS EM Três Corações-MG")
            bot.reply_to(mensagem, clima(lat, lon))
            print(clima(lat, lon))
    #clima()
    def verificar(mensagem):
        return True

    @bot.message_handler(func=verificar)
    def responder(mensagem):
        texto = '''
            Olá, tudo bem?
        Aqui está algumas cidades para você visualizar o clima
        /Campanha
        /Santa_Rita_do_Sapucai
        /Pouso_Alegre
        /Tres_Coracoes
        Escolha somente algumas dessas opções, caso contrário será uma entrada inválida. 
        '''
        bot.reply_to(mensagem, texto)


    bot.polling()
