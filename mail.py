import smtplib


def sendmail(receiver_mail, choice1, name):
    try:
        # Create your SMTP session
        smtp = smtplib.SMTP('smtp.gmail.com', 587)

        # Use TLS to add security
        smtp.starttls()

        # User Authentication
        smtp.login("sender_mail_id", "sender_mail_password")

        # Defining The Message
        rules = "\n So here are my tips for making a goodbye video with your friends," \
                "\n Try to capture a mix of emotions " \
                "don't just focus on sadness or happiness." \
                "\n It's okay if there's silence during the video,it's part " \
                "of the experience." \
                "\n What would you say if your friend was looking at you while they were recording " \
                "this video," \
                "\n Don't worry about being cheesy the important thing is that your friend feels like they're being heard, even if it's just for 1 minute or 2 minutes (or 15 minutes). "
        message = f"Hey {name},\nIt's time for me to say goodbye. " \
                  f"I'm sad, and I know you are too. But we've got a lot of," \
                  f"great memories and amazing experiences in this community, and I can't wait to " \
                  f"see what the future,holds for all of us.To help celebrate our last day of service, " \
                  f"we're going to be doing something,special \n 'Talk about your Friend {choice1}!'" + rules

        # Sending the Email
        smtp.sendmail("sender_mail", receiver_mail, message)

        # Terminating the session
        smtp.quit()
        print("Email sent successfully!")

    except Exception as ex:
        print("Something went wrong....", ex)
