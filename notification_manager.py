from flight_data import FlightData
import smtplib

class NotificationManager:
    def __init__(self):
        self.my_email = "sbxp1966@gmail.com"
        self.my_pass = "gogatmuwcjufqlet"

    

    def send_email(self, flight_data):

        subject = "Cheaper Flight Deal Available !"
        message = f"Cheaper flight deal available {flight_data}"

        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.my_pass)
                email_message = f"Subject: {subject}\n\n{message}"
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=self.my_email,
                    msg=email_message
                )

                print("email sent succesfully")

        except Exception as e:
            print(f"Error Occured {e}")


    def notify(self, flight_data):
        self.send_email(flight_data)