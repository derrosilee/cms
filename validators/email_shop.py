import smtplib
from shops.stores import Stores

def email_confirmation(store_name, store_email):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('derrosilee@gmail.com', "ezbu xaft psmf fcnq")
        message = f"Subject: Shop Added Successfully\n\nShop '{store_name}' added successfully."
        s.sendmail("derrosilee@gmail.com", store_email, message)
        s.quit()
        print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")