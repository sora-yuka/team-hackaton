from django.core.mail import send_mail
from main.celery import app

@app.task
def send_confirmation_email(email, code, title, price):
    full_link = f'Hi, confirm your order from Jellyfish \nTap this link -> http://localhost:8000/api/v1/order/confirm/{code}'    
    send_mail(
        f'Order confirm',
        f'Please click link to confirm order:  {full_link}',
        'sabyrkulov.nurmuhammed@gmail.com',
        [email]
    )