import socket, os, time, threading

def check_file_exists(filepath):
    if not os.path.isfile(filepath):
        print(f"警告：文件 {filepath} 不存在。")
        os.system(f'mshta vbscript:msgbox("警告：缺少必要文件 {filepath} ,已创建文件请再次启动应用程序",64,"警告")(window.close)')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('组名不能为all,或者组名中间有空格,最好是英文无特殊符号\ngroups:')  # 创建默认内容
        return False

def read_group_config():
    with open(r'group_config.ini', 'r', encoding='utf-8') as gf:
        content = gf.read().strip()
        if ':' in content:
            group_str = content.split(':', 1)[1].strip()
            return group_str
    return False

def syscmd_execute(command):
    os.system(command)

def slave_receive_host_ip():
    port = 8888
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", port))  # 绑定所有网卡的8888端口

    print("从机正在监听主机IP广播...")
    try:
        while True:
            data = sock.recvfrom(1024)
            message = data[0].decode('utf-8')
            
            if message.startswith("syscmd:"):
                # 解析主机命令
                host_cmd = message.split(":", 1)[1]
                
                # 退出命令
                if host_cmd.strip() == 'pbye':
                    print("收到结束命令，停止监听。")
                    break
                # 解析命令行参数
                if host_cmd.startswith('g:'):
                    list_cmd = host_cmd.split(':',2)
                    group = list_cmd[1]
                    command = list_cmd[2]
                    print(f"组别: {group}")
                # 配置文件读取
                current_group = '0'  # 默认组别
                try:
                    current_group = read_group_config()
                    if current_group is False:
                        print('读取配置文件函数出现错误')
                    print('当前配置组别为:', current_group)
                except FileNotFoundError:
                    print("警告：group_config.ini文件不存在，使用默认组别0")
                except (ValueError, IndexError):
                    print("警告：group_config.ini格式错误（正确格式：groups:数字），使用默认组别0")
                # 执行主机命令
                if (str(group) == str(current_group)) or (group == 'all'):
                    print(f"执行主机命令: {command}")
                    t = threading.Thread(target=syscmd_execute, args=(command,))
                    t.start()
                # 清空临时变量
                command = None
                time.sleep(1)  

    except KeyboardInterrupt:
        print("\n监听被用户中断")
    finally:
        sock.close()
        print("监听套接字已关闭")

if __name__ == "__main__":
    if not check_file_exists('group_config.ini'):
        slave_receive_host_ip()