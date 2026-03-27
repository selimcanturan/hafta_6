import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("\n[Sistem] Sunucu bağlantısı kapandı.")
                break
            print(f"\nSunucu: {data.decode('utf-8')}")
            print("Sizin mesajınız: ", end="")
        except:
            break
    client_socket.close()

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('10.17.31.21', 65427))
        print("Sunucuya bağlanıldı!")
    except:
        print("Sunucuya bağlanılamadı!")
        return

    # Sunucudan gelen mesajlarÄ± dinlemek iÃ§in thread baÅŸlat
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    # Mesaj gÃ¶nderme dÃ¶ngÃ¼sÃ¼
    while True:
        msg = input("Sizin mesajınız: ")
        if msg.lower() == 'exit':
            break
        client_socket.sendall(msg.encode('utf-8'))

    client_socket.close()

if _name_ == "_main_":
    main()
