
import smtplib
import datetime as dt
import random

# getting current date
current_date = dt.datetime.now()
# getting week day
week_day = current_date.weekday()
# email address of sender

my_email = 'yourmail@yahoo.com'
password = '1Passwords'

if week_day == 0:
    with open('quotes.txt','r') as file:
        quotes = file.readlines()
        quote = random.choice(quotes)

        # Establishing the connection
    with smtplib.SMTP('smpt.mail.yahoo.com') as connection:
        # transport layer security
        connection.starttls()
        # login the mail
        connection.login(user=my_email,password=password)
        # send the email
        connection.sendmail(
            from_addr=my_email,
            to_addrs='receivermail@protonmail.com',
            msg=f"Subject:Message \n\n {quote}"
        )




