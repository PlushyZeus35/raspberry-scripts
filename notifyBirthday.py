from notionHelper import NotionUtils
from telegramUtils import TelegramUtils
from datetime import datetime, date
birthdays = NotionUtils.getBirthdays()
todaysBirthdays = []
SCRIPTNAME = 'Birth Notify'
for birth in birthdays:
    if birth.isToday:
        todaysBirthdays.append(birth)

if len(todaysBirthdays) > 0:
    cDate = date.today().strftime('%d %m')
    telegramMessage = f'<strong>Cumpleaños de hoy {cDate}</strong>\n'
    for birth in todaysBirthdays:
        telegramMessage += f'{birth.name} cumple {birth.age} años.\n'
    TelegramUtils.sendMessage(telegramMessage)
NotionUtils.createLog(name=SCRIPTNAME, tags=['cron'])