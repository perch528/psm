# psm
Multi-host Synchronized Operation and Maintenance Tool (多主机同步运维工具)
## flow
服务端:
通过广播ip(such as:255.255.255.255)
向局域网广播
通过“g:组名:”参数选择哪个组执行
客户端:
接受命令根据客户端配置文件.ini判断是否是本组
## ini file content
such as:
group:cat
group:dog
...
## command
g:组名: 命令
## 链接共享盘 (connect share disk)
g:dog: net use u: \\192.168.1.105\f 123456 /user:admin