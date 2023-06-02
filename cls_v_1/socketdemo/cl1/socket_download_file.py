from socket import socket, AF_INET, SOCK_STREAM

"""
def main():
    client_scoket = socket(AF_INET, SOCK_STREAM)
    client_scoket.bind(('',7788))
    client_scoket.listen(124)
    while True:
        client_scoket_src,client_scoket_addr = client_scoket.accept()
        recv_data = client_scoket_src.recv(1024 * 1024)
        while True:
            if recv_data :
                client_scoket_src.send('已接受,请继续发送'.encode('utf-8'))
            else:
                break
        client_scoket_src.close()
        break
    client_scoket.close()
"""


def main():
    """
    全双工下载文件保存
    :return: 
    """
    client_scoket = socket(AF_INET, SOCK_STREAM)
    client_scoket.bind(('', 7788))
    client_scoket.listen(124)
    while True:
        client_scoket_src, client_scoket_addr = client_scoket.accept()
        recv_data = client_scoket_src.recv(1024 * 1024)
        if recv_data:
            with open('pathname','ab+') as f:
                f.write(recv_data)
            client_scoket_src.send('已接受,请继续发送'.encode('utf-8'))

        client_scoket_src.close()
        break
    client_scoket.close()
if __name__ == '__main__':
    main()