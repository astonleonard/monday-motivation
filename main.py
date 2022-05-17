import smtplib
import random
import datetime as dt
import os

my_email = "astonleonardlo22@gmail.com"
password = os.getenv("Email Password")

send_to = "astonleonardlo22@gmail.com"

with open("quotes.txt") as data_file:
    data = data_file.readlines()
    random_data = random.choice(data)

all_day_name = {"0": "Monday", "1": "Tuesday", "2": "Wednesday", "3": "Thursday", "4": "Friday", "5": "Saturday",
                "6": "Sunday"}

now = dt.datetime.now()
day_of_week = now.weekday()
day = all_day_name[f"{day_of_week}"]

if day == "Monday":
    with smtplib.SMTP("smtp.gmail.com", port=587) as connections:
        connections.starttls()
        connections.login(user=my_email, password=password)
        connections.sendmail(
            from_addr=my_email,
            to_addrs=send_to,
            msg=f"From: {my_email}\nTo: {send_to}\nSubject: Monday Motivation\n\n{random_data}"

        )
