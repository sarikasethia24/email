import datetime as dt
import smtplib
my_email = 'sarikasethia2401@gmail.com'
my_pass = "xwcjkjgkdsicnnau"
# date = dt.datetime.now()
# week = date.weekday()
# if week == 4:
# creates SMTP session
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    # start TLS for security
    connection.starttls()
    # Authentication
    connection.login(my_email, my_pass)
    # sending the mail
    connection.sendmail(from_addr=my_email, to_addrs="smartengineer0786@gmail", msg="Subject: email through python \n\n hello sir \n name - sarika sethia \n branch - CSE \n college - Sobhasaria group of institutions \n course - Data science with ML and AI  ")
    # terminating the session

