import socket
import threading


HOST = "127.0.0.1"
PORT = 12345

# 동작이 active인지 확인
is_active = True

# Full-Duplex (양방향 통신) 방식
# 보내는 함수(Transmit)
def handler_tx():
    while is_active:
        # 입력 받기 
        input_msg = input("input: ")
        # 만약 exit면 종료 = 클라이언트 소켓 종료, active -> false
        if input_msg.lower == "exit":
            client_socket.close()
            is_active = False
            break
        # 보내기 sendall
        client_socket.sendall(input_msg.encode('utf-8'))

# 받는 함수 (Receive)
def handler_rx():
    while is_active:
        # 받기 recv
        rcvd_msg = client_socket.recv(1024).decode('utf-8')
        # null면 종료 = active -> false
        if not rcvd_msg:
            is_active = False
            break
        print(f"received msg : {rcvd_msg}")


# 소켓 생성 코낵트
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect((HOST, PORT))


# 스래드 명시 및 시작, join
thread_tx = threading.Thread(target=handler_tx, args=client_socket)
thread_rx = threading.Thread(target=handler_rx, args=client_socket)

thread_tx.start()
thread_rx.start()

thread_tx.join()
thread_rx.join()

