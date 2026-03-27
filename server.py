import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("\n[Sistem] istemci bağlantıyı kesti.")
                break
            print(f"\n istemci: {data.decode('utf-8')}")
            print("Sizin mesajınız: ", end="") 
        except:
            break
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('10.17.31.21', 65427))
    server_socket.listen(1)
    print("Sunucu başlatıldı, bağlantı bekleniyor...")

    client_socket, addr = server_socket.accept()
    print(f"{addr} bağlandı. Sohbet başlayabilir!")

    
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    
    while True:
        msg = input("Sizin mesajınız: ")
        if msg.lower() == 'exit':
            break
        client_socket.sendall(msg.encode('utf-8'))

    client_socket.close()

if _name_ == "_main_":
    main()
