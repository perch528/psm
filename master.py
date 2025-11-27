import socket
import time

def host_broadcast_ip():
    # UDP广播配置
        broadcast_addr = "255.255.255.255"  # 局域网广播地址
        port = 8888  # 与从机监听端口一致
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                        
        # 获取主机局域网IP
        hostname = socket.gethostname()
        host_ip = socket.gethostbyname(hostname)
        # 周期性广播IP
        print(f"主机IP: {host_ip}，开始向局域网广播...")
        order = ''
        try:
            while True:
                # message = f"HOST_IP:{host_ip}".encode("utf-8")
                order = input("请输入要发送的命令（如calc）:")
                if order.strip() == '':
                    print("命令为空，结束广播。")
                    break
                message = f"syscmd:{order}".encode('utf-8')
                sock.sendto(message, (broadcast_addr, port))
                # time.sleep(3)  # 每3秒广播一次
        except KeyboardInterrupt:
            print("广播停止")
            sock.close()
                                                                                                                    
if __name__ == "__main__":
    host_broadcast_ip()
