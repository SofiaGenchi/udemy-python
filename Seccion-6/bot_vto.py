import telegram
import datetime

# Aquí se debe reemplazar 'TOKEN' por el token de acceso del bot que obtuviste en el paso 2.
bot = telegram.Bot('TOKEN')

# Aquí se debe reemplazar 'CHAT_ID' por el ID del chat que creaste con tu bot en el paso 3.
chat_id = 'CHAT_ID'

# Aquí se debe reemplazar 'FECHA_VENCIMIENTO' por la fecha de vencimiento de tu factura de teléfono en formato 'YYYY-MM-DD'.
fecha_vencimiento = 'FECHA_VENCIMIENTO'

# Calculamos la cantidad de días que faltan hasta la fecha de vencimiento
dias_restantes = (datetime.datetime.strptime(fecha_vencimiento, '%Y-%m-%d') - datetime.datetime.now()).days

# Creamos el mensaje que se enviará al chat
if dias_restantes > 0:
    mensaje = f'Faltan {dias_restantes} días para el vencimiento de tu factura de teléfono.'
else:
    mensaje = '¡Hoy es la fecha de vencimiento de tu factura de teléfono! No olvides pagarla.'

# Enviamos el mensaje al chat
bot.send_message(chat_id=chat_id, text=mensaje)
