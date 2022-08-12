import pandas as pd
import datetime as dt
import random
import smtplib
import time

def run_program():
    for friends in user_data:
        if friends["month"] == current_month and friends["day"] == current_date:
            rand_file = f"letter_{random.randint(1, 3)}.txt"
            file_path = f"letter_templates/{rand_file}"
            friend_email = friends['email']

            with open(file_path) as letter_file:
                content = letter_file.read()

            new_content = content.replace("[NAME]", friends['name'])
            with smtplib.SMTP(host, port=587) as conn:
                conn.starttls()
                conn.login(user=user_name, password=password)
                conn.sendmail(from_addr=user_name,
                              to_addrs=friend_email,
                              msg=f"Subject: Happy Birth Day {friends['name']}\n\n{new_content}")
    time.sleep(86400)  # ait For 24 Hour before Running again
    run_program()

data = pd.read_csv("birthdays.csv")
user_data = data.to_dict(orient='records')

now = dt.datetime.now()
current_month = now.month
current_date = now.day

user_name = "yourgmail@gmail.com"
password = "gmail_app_password"
host = "smtp.gmail.com"

run_program()
