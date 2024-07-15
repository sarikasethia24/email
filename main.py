import datetime as dt
import smtplib
my_email = 'YOUR EMAIL'
my_pass = "YOUR PASSWORD"
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
    connection.sendmail(from_addr=my_email, to_addrs="RECEIVER'S EMAIL", msg= " " )
    # terminating the session

