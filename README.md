Patrick Lin pjlin@csu.fullerton.edu

Loc Nguyen lnguy121@csu.fullerton.edu

Saad Ansari  saad.ansari@csu.fullerton.com

# SMTP-Server

## client_basic.py
This Python file fulfills "Part A" of the project requirements and sends an email to an online SMTP server called Mailosaur. Mailosaur is an service which lets clients test email functionality and hosts multiple SMTP servers which users can connect to with provided credentials and trial email functionality.

To run this Python file, first navigate to the folder with the scripts.

Run the program with:
     
     python3 client_basic.py

Go to https://mailosaur.com/app/login

Sign in with the following credentials (Will expire on July 10, 2023):
>Email: csuf.tester.471@gmail.com
>
>Password: 2023Mail!

You can navigate to the mail inbox on the lefthand sidebar, and you should see that the Mailosaur email server received a Hello World email message. To verify the authenticity of the message, click on it to see more details such as when the message was received, the recipient and sender, as well as the text content in the email message.

<img src="https://github.com/Arbalest007/SMTP-Server/assets/47013008/1ee21e86-333e-490b-807c-90f4f216ab56" width="500" height="400">

## client_ssl.py
This Python file fulfills "Part B" of the project requirements and sends an email to the Gmail server by wrapping the socket in SSL security. 

To run this program, you will need to edit the client_ssl.py file.

On lines 62 and 80 where it says *PLACEHOLDER*, you will need to change it to your respective email address. For example, if you wanted the recipient to be the same as our pre-defined sender account, you would replace *PLACEHOLDER* with *csuf.tester.471@gmail.com*.

Save the changes and run the program with:
     
     python3 client_ssl.py

You should see an email that was sent to the email address inbox you entered.

<img src="https://github.com/Arbalest007/SMTP-Server/assets/47013008/89eb1db3-0f09-46c3-8154-59d7d2c2f807" width="500" height="400">