from socket import *    #import socket

serverName = 'localhost'    #menentukan nama server
serverPort = 4080           #menentukan nomor port server
serverSocket = socket(AF_INET, SOCK_STREAM)     #membuat server socket dengan parameter pertama menunjukan jaringan menggunakan IPv4 dan parameter kedua menunjukan socket bertipe SOCK_STREAM yang berarti socket TCP
print('Starting up on', serverName,'port', serverPort)
serverSocket.bind(('', serverPort))             #mengaitkan nomor port server
serverSocket.listen(1)                          #menunggu dan mendengarkan klien (3-way handshaking)
print('Server is Ready...')

while True:
    # Establish the connection
    connectionSocket, addr = serverSocket.accept()      #server melakukan accept terhadap request koneksi TCP dari klien. parameter menentukan jml maksimum koneksi antrian
    try:
        message = connectionSocket.recv(1024)           #menerima request message dari klien
        filename = message.split()[1]                   #melakukan split ke bagian kedua dari header HTML.            
        f = open(filename[1:], 'rb')                    #membuka file html dari karakter kedua yang dinyatakan melalui [1:] 
        outputdata = f.read()                           #membaca konten file yang diminta
        f.close()
        # Send the HTTP status code and content of the requested file to the client
        connectionSocket.send(b'HTTP/1.0 200 OK\r\n\r\n' + outputdata)      #mengirim kode status HTTP dan konten file yang direquest kepada klien
        connectionSocket.close()        #tutup koneksi socket
    except IOError:
        # Send response message for file not found
        connectionSocket.send(b'HTTP/1.0 Error 404 - File not found\r\n\r\n')        #mengirim pesan respon untuk file yang tidak ditemukan
        # Close client socket
        connectionSocket.close()        #tutup koneksi socket

serverSocket.close()        #tutup server socket
