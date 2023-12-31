from socket import *
import ssl, base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com", 587)

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

# Gmail Authentication - START
clientSocket.send(('starttls\r\n').encode())
recvTTLS = clientSocket.recv(1024).decode()
print("Start TTLS: ")
print(recvTTLS)

# Need to wrap clientSocket with SSL for Gmail Security
secureClientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)
loginName = base64.b64encode(('csuf.tester.471@gmail.com').encode()) + ('\r\n').encode()

# Gmail login password must be generated via "App Passwords" as per new Gmail security protocols
loginPassword = base64.b64encode(('pjyv wroi tdjl raof').encode()) + ('\r\n').encode()

secureClientSocket.send(('AUTH LOGIN\r\n').encode())
print(secureClientSocket.recv(1024).decode())
secureClientSocket.send(loginName)
print(secureClientSocket.recv(1024).decode())
secureClientSocket.send(loginPassword)
print(secureClientSocket.recv(1024).decode())
# Gmail Authentication - END

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = "MAIL FROM: <csuf.tester.471@gmail.com>\r\n"
secureClientSocket.send(mailFromCommand.encode())
print(secureClientSocket.recv(1024).decode())
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start

# SAMPLE PLACEHOLDER CHANGE:
# rcptToCommand = "RCPT TO: <patrick.lin.117@gmail.com>\r\n"
rcptToCommand = "RCPT TO: <PLACEHOLDER>\r\n"

secureClientSocket.send(rcptToCommand.encode())
print(secureClientSocket.recv(1024).decode())
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = "DATA\r\n"
secureClientSocket.send(dataCommand.encode())
print(secureClientSocket.recv(1024).decode())
# Fill in end

# Send message data.
# Fill in start

# SAMPLE PLACEHOLDER CHANGE
# secureClientSocket.send("To: patrick.lin.117@gmail.com\r\n".encode())
secureClientSocket.send("To: PLACEHOLDER\r\n".encode())

secureClientSocket.send("From: csuf.tester.471@gmail.com\r\n".encode())
secureClientSocket.send("Subject: Hello World\r\n".encode())
secureClientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
secureClientSocket.send(endmsg.encode())
# Fill in end

# Send QUIT command and get server response.
# Fill in start
secureClientSocket.send(('QUIT\r\n').encode())
print(secureClientSocket.recv(1024).decode())
# Fill in end

secureClientSocket.close()
clientSocket.close()