import smtplib, ssl



def send_mail():
   

    sender_email = "osirisowen040@gmail.com"
    receiver_email = "rohan31sai@gmail.com"
    message = """\
    Subject: Cowin Vaccine Available

    This message is sent from Python."""


    port = 465  # For SSL
    password = "brorocks"

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("osirisowen040@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)
