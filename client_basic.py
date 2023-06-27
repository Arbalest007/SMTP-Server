from socket import *
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.mailosaur.net", 587)

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv) 
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

loginName = base64.b64encode(('xkctbakc@mailosaur.net').encode()) + ('\r\n').encode()
loginPassword = base64.b64encode(('6yaM5rIQQZVQqBsKfJ5qPpuw4GmwIZul').encode()) + ('\r\n').encode()

clientSocket.send(('EHLO smtp.mailosaur.net\r\n').encode())
clientSocket.send(('AUTH LOGIN\r\n').encode())
print(clientSocket.recv(1024).decode())
clientSocket.send(loginName)
print(clientSocket.recv(1024).decode())
clientSocket.send(loginPassword)
print(clientSocket.recv(1024).decode())

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = "MAIL FROM: <xkctbakc@mailosaur.net>\r\n"
clientSocket.send(mailFromCommand.encode())
print(clientSocket.recv(1024).decode())
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptToCommand = "RCPT TO: <recipient@xkctbakc.mailosaur.net>\r\n"
clientSocket.send(rcptToCommand.encode())
print(clientSocket.recv(1024).decode())
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
print("DATA")
print(clientSocket.recv(1024).decode())
# Fill in end

# Send message data.
# Fill in start
clientSocket.send("To: recipient@xkctbakc.mailosaur.net\r\n".encode())
clientSocket.send("From: xkctbakc@mailosaur.net\r\n".encode())
clientSocket.send("Subject: Hello World\r\n".encode())
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
# Fill in end

# Send QUIT command and get server response.
# Fill in start
clientSocket.send(('QUIT\r\n').encode())
print(clientSocket.recv(1024).decode())
# Fill in end

clientSocket.close()