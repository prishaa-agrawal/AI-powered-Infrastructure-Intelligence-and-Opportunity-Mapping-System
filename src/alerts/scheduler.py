import schedule
import time
import subprocess


def send_alert():

    print("Sending scheduled alert...")

    subprocess.run(
        ["python", "src/alerts/email_alert.py"]
    )


# Every day at 09:00 AM

schedule.every().day.at("09:00").do(send_alert)

print("Scheduler running...")

while True:

    schedule.run_pending()

    time.sleep(60)