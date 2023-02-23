from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Hello Sir"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFromCommand = 'MAIL FROM: ripunjay65@gmail.com \r\n'
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    if recv2[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptToCommand = 'RCPT TO: ripunjay65@gmail.com \r\n'
    clientSocket.send(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    if recv3[:3] != '250':
        print('250 reply not received from server')
    # Fill in end

    # Send DATA command and handle server response.
    dataCommand = 'data \r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    if recv4[:3] != '250':
        print('250 reply not received from server')
    # Fill in start
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    if recv5[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'quit \r\n'
    clientSocket.send(endmsg.encode())
    recv6 = clientSocket.recv(1024).decode()
    if recv6[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')