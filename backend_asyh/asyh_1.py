import socket
import selectors


selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    '''
    `fileobj` обычно представляет собой объект файла или сокета, на который нужно зарегистрировать события.

    `events` определяет тип события, которое нужно зарегистрировать. В данном случае, мы регистрируем событие чтения 
    (EVENT_READ), которое будет возникать, когда на серверный сокет поступят входящие данные.

    `data` представляет собой колбэк-функцию, которая будет вызываться, когда произойдет зарегистрированное событие.
    В данном случае, это функция `accept_connection`, которая будет вызываться при поступлении нового подключения к серверу.

    При регистрации событий чтения на `server_socket`, модуль `selectors` будет отслеживать, когда на этот
    сокет поступают входящие данные, и вызывать соответствующую функцию обратного вызова (колбэк), указанную в третьем аргументе `data`.
    '''
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print("Connection from",addr)
    
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)

def send_message(client_socket):
    
    request = client_socket.recv(4096)

    if not request:
        response = "hello world\n".encode()
        client_socket.send(response)

    else:
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:
        events = selector.select()

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)



if __name__ == "__main__":
    server()
    event_loop()

