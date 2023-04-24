
from django.core.mail import send_mail

def correo(userMail):

    
    send_mail(
        'Recuperación de contraseña', # Asunto del correo electrónico
        'Haz solicitado la recuperación de tu contraseña. Hacerlo es muy sencillo, simplemente debes hacer click en el siguiente enlace: http://192.168.0.116:8000/api/auth/reset/confirm/', # Cuerpo del correo electrónico
        'projectdjango15@gmail.com', # Dirección de correo electrónico de origen
        userMail, # Lista de direcciones de correo electrónico de los destinatarios
        fail_silently=False, # Levanta una excepción si no se puede enviar el correo electrónico
       
    )
    print("Email : ", userMail)
    