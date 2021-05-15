import telebot
import math
from random import randint

token = #your token
bot = telebot.TeleBot(token)
langNumber1 = [0]

def log(message):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Бота использует {0} {1}. (id = {2}) \n ".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id)))
def funcRandQueue():
    CategoriasBankRus = ["Кассовые операции: перел вами ", "Оформление кредита/депозита: перел вами ",
                         "Денежные переводы: перел вами ", "Консультации: перел вами "]
    CategoriasBankKaz = ["Кассалық операциялар: сіздің алдыңызда", "Несие/депозит өндеу: сіздің алдыңызда", "Ақша аударымдары: сіздің алдыңызда", "Консультациялар: cіздің алдыңызда"]
    CategoriasBankEng = ["Cash transactions: before you ", "Registration of the loan / deposit: before you ", "Money transfers: before you ",
                         "Consultation: before you "]

    CategoriasBank = [CategoriasBankRus, CategoriasBankKaz, CategoriasBankEng]
    st = ""
    for i in range(0, 4):
        rNumber = randint(5, 20)
        st += str(CategoriasBank[langNumber1[0]][i])
        st += ": "
        st += str(rNumber)
        st += "\n"
    return st


@bot.message_handler(commands=['start'])
def lang(message):
    bot.send_message(message.from_user.id, "Добро Пожаловать!\nҚош келдіңіз!\nWelcome!")
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(text='rus', callback_data='r')
    callback_button2 = telebot.types.InlineKeyboardButton(text='kaz', callback_data='k')
    callback_button3 = telebot.types.InlineKeyboardButton(text='eng', callback_data='e')
    keyboard.add(callback_button1, callback_button2, callback_button3)
    bot.send_message(message.from_user.id, 'Выберите язык:\nТілді таңдаңыз:\nSet language:', reply_markup=keyboard)


listLang = ['Русский язык', 'Қазақ тілі', 'English language']
listLang_SendLocation = ['Отправить местоположение', 'Геолокация жіберу', 'Send your location']
listLangDef = ['Вы выбрали:', 'Сіз таңдадыңыз:', 'You have chosen:']

listHalyk = ['Халык банк', 'Халық банк', 'Halyk Bank']
listBank = ['Выберите банк! ', 'Банкiнi таңдаңыз! ', 'Choose bank! ']
list3Bank = ['3 ближайших банка: ', '3 жақын банктар:', 'Closest 3 banks :']


listOperations = ['Операции:', 'Операциялар:', 'Operations:']

listSuc = ['Вы успешно заняли очередь на кассовые операции, ваш номер:', 'Кассалық операцияларғa кезекке тұрдыңыз, cіздің нөмірі: ',
           'You have successfully occupied a queue for cash transactions, your number: ']
listCredit = ['Вы успешно заняли очередь на оформление кредиты и депозиты, ваш номер: ', 'Несие/депозит өндеуге кезекке тұрдыңыз, cіздің нөмірі: ', 'You have successfully occupied a queue for loans and deposits, your number: ']

listCash = ['Вы успешно заняли очередь на денежные переводы, ваш номер: ', 'Ақша аударымдарғa кезекке тұрдыңыз, cіздің нөмірі: ', 'You have successfully occupied a queue for money Transfers, your number: ']
listConsul = ['Вы успешно заняли очередь на консультацию, ваш номер: ', 'Консультацияғa кезекке тұрдыңыз, cіздің нөмірі: ', 'You have successfully occupied a queue for сonsultation, your number: ']


listR_rus = ['Кассовые операции', 'Оформление кредита/депозита', 'Денежные переводы', 'Консультации']
listR_kaz = ['Кассалық операциялар', 'Несие/депозит өндеу', 'Ақша аударымдары', 'Консультациялар']
listR_eng = ["Cash transactions", "Registration of the loan / deposit", "Money transfers", "Consultation"]

listRLists = [listR_rus, listR_kaz, listR_eng]

listNumbers = ['87272590777', '87272890777', '87272590776']

@bot.message_handler(content_types=['location'])
def loco(message):
    langNumber = langNumber1[0]
    location_string = str(message.location)
    location_string = location_string.replace("'longitude': ", "")
    location_string = location_string.replace("}", "")
    #location_string = location_string.replace(",", "")

    location_string = location_string.replace(" 'latitude': ", "")
    location_doubleY = float(location_string[1:10])
    location_doubleX = float(location_string[11:20])



    print("Coordinates of user: ", location_doubleX, location_doubleY)
    log(message)

    address_halyk_rus = ["Райымбека проспект, 506", "ТК ARMADA, Кабдолова, 1/8", "Аксай 4-й микрорайон, 100",
                        "Райымбека проспект, 383", "Утеген батыра, 82а", "ТЦ Тигрохауд, 4-й микрорайон, 10а",
                         "Астана микрорайон, 8Б", "Алтынсарина проспект, 23", "Орбита 3-й микрорайон, 4", "Жандосова, 47",
                         "ЖК Манхеттен, Прокофьева, 140", "ТЦ Асыл, Туркебаева, 92", "Сатпаева, 78", "Розыбакиева, 101",
                         "ТРЦ Mega Center Alma-Ata,Розыбакиева, 247", "Орбита 2-й микрорайон, 2",
                         "Казахфильм микрорайон, 14", "Алмагуль микрорайон, 44", "Гагарина проспект, 167", "Айманова, 191",
                         "Globus, Абая проспект, 109в", "Толе би, 159", "Гоголя, 144", "Коктем 3-й микрорайон, 21",
                         "Коктем 2-й микрорайон, 1", "Байтурсынова, 72", "ТРК MEGA Park, Сейфуллина проспект, 483",
                         "Сейфуллина проспект, 567", "Аль-Фараби проспект, 40 блок D", "Абылай хана проспект, 93/95",
                         "Гоголя, 91", "Назарбаева проспект, 57", "Райымбека проспект, 101", "Жибек Жолы проспект, 54",
                         "Толе би, 40", "Достык проспект, 39", "Назарбаева проспект, 128", "Курмангазы, 20",
                         "ТРЦ DOSTYK PLAZA, Самал 2-й микрорайон, 111"]
    address_halyk_kaz = ["Райымбек даңғылы, 506", "\"СК ARMADA\", Қабдолов к., 1/8", "Ақсай 4-шi шағын ауданы, 100",
                        "Райымбек даңғылы, 383", "Өтеген батыр к., 82а",
                        "\"Тигрогуд\" сауда орталығы, 4-шi шағынауданы, 10а", "Астана ауданы, 8Б",
                        "Алтынсарин даңғылы, 23", "Орбита 3-шi шағын ауданы, 4", "Жандосов к., 47",
                        "Манхеттен ТҮК, Прокофьев к., 140", "СО Асыл, Туркебаев к., 92", "Сатпаев к., 78",
                        "Розыбакиев к., 101", "СО Mega Center Alma-Ata, Розыбакиев к., 247", "Орбита 2-шi ауданы, 2",
                        "Қазақфильм шағын ауданы, 14", "Алмагүл шағын ауданы, 44", "Гагарин даңғылы, 167",
                        "Айманов к., 191", "Globus, Абай даңғылы, 109в", "Төле би к., 159", "Гоголь к, 144",
                        "Көктем 3-шi шағын ауданы, 21", "Көктем 2-шi шағын ауданы, 1", "Байтурсынов к., 72",
                        "MEGA Park, Сейфуллин даңғылы, 483", "Сейфуллин даңғылы, 567", "Әл-Фараби даңғылы, 40 блок D",
                        "Абылай хан даңғылы, 93/95", "Гоголь к., 91", "Назарбаев даңғылы, 57", "Райымбек даңғылы, 101",
                        "Жiбек Жолы даңғылы, 54", "Төле би к., 40", "Достық даңғылы, 39", "Назарбаев даңғылы, 128",
                        "Құрманғазы к., 20", "DOSTYK PLAZA, Самал 2-шi шағын ауданы, 111"]
    address_halyk_eng = ["Raiymbek Avenue, 506", "SC ARMADA, Kabdolov st., 1/8", "Aksay 4th microdistrict, 100",
                        "Raiymbek Avenue, 383", "Utegen Batyr st., 82a", "Tigrohoud mall, 4th microdistrict, 10a ",
                        " Astana microdistrict, 8B ", " Altynsarin Avenue, 23 ", "Orbita 3rd microdistrict, 4 ",
                        " Zhandosov st., 47 ", " Manhattan RC, Prokofyev st., 140 ", " Asyl SC, Turkebaev st., 92 ",
                        " Satpayev st., 78 ", " Rozybakiyev st., 101 ",
                        " Mega Center Alma-Ata mall, Rozybakiyev st., 247 ", " Orbita 2nd microdistrict, 2 ",
                        " Kazakhfilm microdistrict, 14 ", " Almagul microdistrict , 44 ", " Gagarin Avenue, 167 ",
                        " Aimanov st., 191 ", " Globus, Abay Avenue, 109v ", " Tole Bi st., 159 ", " Gogol st., 144 ",
                        " Koktem 3rd Microdistrict, 21 ", " Koktem 2nd Microdistrict, 1 ", " Baitursynov st., 72 ",
                        "MEGA Park, Seifullin Avenue, 483 ", " Seifullin Avenue, 567 ",
                        " Al-Farabi Avenue, 40 Block D ", " Abylay Khan Avenue, 93 / 95 ", " Gogol st., 91 ",
                        " Nazarbayev Avenue, 57 ", " Raiymbek Avenue, 101 ", " Zhibek Zholy Avenue, 54 ",
                        " Tole Bi st., 40 ", " Dostyk Avenue, 39 ", " Nazarbayev Avenue, 128 ", " Kurmangazy st, 20 ",
                        "DOSTYK​PLAZA, Samal 2nd district, 111"]

    adressListofLists = [address_halyk_rus, address_halyk_kaz, address_halyk_eng]

    list_x = [43.246131, 43.235634, 43.229325, 43.255611, 43.241104, 43.2254, 43.211503, 43.222514, 43.201068,
              43.219292, 43.242565, 43.250076, 43.234112, 43.232343, 43.202758, 43.19866, 43.193545, 43.203763,
              43.21857, 43.229535, 43.24031, 43.252672, 43.257875, 43.235841, 43.227432, 43.244617, 43.264087,
              43.247388, 43.226055, 43.255467, 43.260035, 43.264764, 43.270984, 43.262376, 43.255155, 43.252004,
              43.249709, 43.245024, 43.233168]
    list_y = [76.840236, 76.845214, 76.840479, 76.862087, 76.859085, 76.859827, 76.851771, 76.866567, 76.879147,
              76.877836, 76.876021, 76.879298, 76.886146, 76.89014, 76.892008, 76.886767, 76.905635, 76.903800, 76.896992,
              76.897437, 76.906606, 76.909351, 76.916783, 76.917927, 76.922935, 76.927167, 76.930252, 76.933154,
              76.941645, 76.94093, 76.942163, 76.945148, 76.946657, 76.953151, 76.952504, 76.955445, 76.947655,
              76.954194, 76.957228]

    list_dist = []


    for i in range(0, len(list_x)):
        list_dist.append(math.sqrt((location_doubleX-list_x[i]) * (location_doubleX-list_x[i]) + (location_doubleY-list_y[i]) * (location_doubleY-list_y[i])))


    for i in range(0, len(list_x)):
        list_dist[i] = round(list_dist[i], 6)

    list_values = [x for x in range(0, len(list_x))]

    dictDistance = dict(zip(list_dist, list_values))
    SortedListDistance = list(sorted(list_dist))

    listClosest3Banks = []

    for i in range(0, 3):
        z = dictDistance.get(SortedListDistance[i])
        listClosest3Banks.append(z)

    print("Closest 3 banks :", listClosest3Banks)

    for i in range(0, 3):
        minDistIndex = listClosest3Banks[i]
        bot.send_venue(message.from_user.id, list_x[minDistIndex], list_y[minDistIndex], title=listHalyk[langNumber] + ' %i' %(i+1), address=adressListofLists[langNumber][minDistIndex])
        print(langNumber)
        bot.send_message(message.from_user.id, listNumbers[i])
    kb = telebot.types.InlineKeyboardMarkup(row_width=1)
    cb1 = telebot.types.InlineKeyboardButton(text=listHalyk[langNumber] + ' %i' %(1), callback_data="b1")
    cb2 = telebot.types.InlineKeyboardButton(text=listHalyk[langNumber] + ' %i' %(2), callback_data="b2")
    cb3 = telebot.types.InlineKeyboardButton(text=listHalyk[langNumber] + ' %i' %(3), callback_data="b3")
    kb.add(cb1, cb2, cb3)
    bot.send_message(message.from_user.id, list3Bank[langNumber], reply_markup=kb)

    um = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    um.row(listHalyk[langNumber] + ' %i' %(1), listHalyk[langNumber] + ' %i' %(2), listHalyk[langNumber] + ' %i' %(3))
    bot.send_message(message.from_user.id, listBank[langNumber], reply_markup=um)
@bot.message_handler(content_types=['text'])
def mes(message):
    if message.text == listHalyk[langNumber1[0]] + ' %i' %(1) or message.text == listHalyk[langNumber1[0]] + ' %i' %(2) or message.text == listHalyk[langNumber1[0]] + ' %i' %(3):
        kbd = telebot.types.InlineKeyboardMarkup(row_width=1)
        act1 = telebot.types.InlineKeyboardButton(text=listRLists[langNumber1[0]][0], callback_data="a1")
        act2 = telebot.types.InlineKeyboardButton(text=listRLists[langNumber1[0]][1], callback_data="a2")
        act3 = telebot.types.InlineKeyboardButton(text=listRLists[langNumber1[0]][2], callback_data="a3")
        act4 = telebot.types.InlineKeyboardButton(text=listRLists[langNumber1[0]][3], callback_data="a4")
        kbd.add(act1, act2, act3, act4)
        bot.send_message(message.from_user.id, listOperations[langNumber1[0]], reply_markup=kbd)



@bot.callback_query_handler(func=lambda call: True)
def callbackLang(call):
    if call.message:
        try:
            if call.data == "r" or call.data == "k" or call.data == "e":
                if call.data == "r":
                    langNumber1[0] = 0

                elif call.data == "k":

                    langNumber1[0] = 1

                elif call.data == "e":
                    langNumber1[0] = 2


                print(langNumber1[0], listLang[langNumber1[0]])
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=listLangDef[langNumber1[0]])
                keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                button_geo = telebot.types.KeyboardButton(text=listLang_SendLocation[langNumber1[0]], request_location=True)
                keyboard.add(button_geo)
                bot.send_message(call.message.chat.id,
                                 listLang[langNumber1[0]],
                                 reply_markup=keyboard)

            elif call.data == "b1" or call.data == "b2" or call.data == "b3":
                if call.data == 'b1':
                    print(call.data)
                    zzz = funcRandQueue()
                    #for i in range(0, 4):
                        #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=zzz)
                    bot.send_message(call.message.chat.id,  listHalyk[langNumber1[0]] + ' %i' %(1))
                    bot.send_message(call.message.chat.id, zzz)
                elif call.data == 'b2':
                    print(call.data)
                    zzz = funcRandQueue()
                    bot.send_message(call.message.chat.id,  listHalyk[langNumber1[0]] + ' %i' %(2))
                    bot.send_message(call.message.chat.id, zzz)
                    #oper()
                elif call.data == 'b3':
                    print(call.data)
                    zzz = funcRandQueue()
                    bot.send_message(call.message.chat.id,  listHalyk[langNumber1[0]] + ' %i' %(3))
                    #oper()
                    bot.send_message(call.message.chat.id, zzz)
            elif call.data == 'a1':
                print(call.data)
                zzz = randint(55, 789)
                bot.send_message(call.message.chat.id, listSuc[langNumber1[0]] + " " +str(zzz))
               # bot.send_message(call.message.chat.id, zzz)
            elif call.data == 'a2':
                print(call.data)
                zzz = randint(55, 789)
                bot.send_message(call.message.chat.id, listCredit[langNumber1[0]] + " " + str(zzz))
               # bot.send_message(call.message.chat.id, zzz)
            elif call.data == 'a3':
                print(call.data)
                zzz = randint(55, 789)
                bot.send_message(call.message.chat.id, listCash[langNumber1[0]] + " " + str(zzz))
               # bot.send_message(call.message.chat.id, zzz)
            elif call.data == 'a4':
                print(call.data)
                zzz = randint(55, 789)
                bot.send_message(call.message.chat.id, listConsul[langNumber1[0]] + " " + str(zzz))
               # bot.send_message(call.message.chat.id, zzz)

            else:
                print("Error")
        except:
            print('ERROROROR')


bot.polling(none_stop=True)