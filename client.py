import socket

HOST = 'localhost'  #melakukan assign nama host
PORT = 4080         #melakukan assign nomor port

filename = input("HTML file name: ")        #melakukan input nama file html
request = f"GET /{filename} HTTP/1.0\r\nHost: {HOST}\r\n\r\n"       #melakukan request akses file 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))     #melakukan connect antara host dan port
    
    # Send the GET request to the server
    client_socket.sendall(request.encode('utf-8'))      #mengirim get request kepada server
    
    # Receive the response from the server
    response = client_socket.recv(1024)                 #menerima respon dari server
    
    if not response:
        print("No response from the server.")
    else:
        # Parse the HTTP response
        response_parts = response.split(b'\r\n\r\n')
        if len(response_parts) < 2:
            print("Invalid response from the server.")
        else:
            status_code, content = response_parts[0], response_parts[1]
            if status_code == b'HTTP/1.0 200 OK':
                # Save the file to the local directory
                with open(f"C:\\Users\\Sofi\\OneDrive - Telkom University\\Documents\\semester 4\\jaringan komputer\\tubes\\{filename}", 'wb') as f:
                    f.write(content)
                print(f"Yeay file '{filename}' saved to the local directory ^_^")
            else:
                print("File not found on the server :(.")
