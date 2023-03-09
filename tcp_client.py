import socket
import sys

def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        
    server_address = '/tmp/socket_file'
    print('connecting to {}'.format(server_address))

    try:
        sock.connect(server_address)
    except socket.error as err: 
        print(err)
        sys.exit(1)
    try:
        message = input("input your message: ")
        sock.sendall(message.encode())
        
        sock.settimeout(4)
        try:
            while True:
                data = sock.recv(32)
                if data:
                    print('server response: ' + data.decode())
                else:
                    break
        except(TimeoutError):
            print('Socket timeout, ending listening for server messages')

    finally:
        print('closing socket')
        sock.close()

if __name__ == '__main__':
    main()