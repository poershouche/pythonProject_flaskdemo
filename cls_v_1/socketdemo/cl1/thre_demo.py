import socket
import threading
import time
"""
UPD实在全双工模式进行模拟QQ聊天
"""

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def send_msg(client_sock,dest_ip,dest_port):
    while True:
        content=input('请输入要发送的内容')
        client_sock.sendto(content.encode('utf-8'),(dest_ip,dest_port))


def recv_data(client_sock):
    revefrom_data = client_sock.recvfrom(1024)
    print(revefrom_data)


def main():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.bind(('', 9090))
    dest_ip = input('请输入目标ip:')
    dest_port = int(input('请输入目标port:'))
    t1 = threading.Thread(target=send_msg, args=(client_sock, dest_ip, dest_port))
    t2 = threading.Thread(target=recv_data, args=(client_sock,))
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()