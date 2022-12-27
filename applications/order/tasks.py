from django.core.mail import send_mail
from main.celery import app

@app.task
<<<<<<< HEAD
def send_confirmation_email(email, code, title, price):
    full_link = f'Hi, confirm your order from Jellyfish \nTap this link -> http://localhost:8000/api/v1/order/confirm/{code}'    
=======
def send_confirmation_code(email, code):
    full_link = f'Tap this -> http://localhost:8000/api/v1/order/confirm/{code}'    
>>>>>>> d47deb2b96fe9c24981f24f944a60efa14bf1a40
    send_mail(
        f'Order confirm',
        f'Please click link to confirm order:  {full_link}',
        'sabyrkulov.nurmuhammed@gmail.com',
        [email]
    )