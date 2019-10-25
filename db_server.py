"""
dict 服务端

* 处理业务逻辑
* 多进程并发模型
"""

from socket import *
from multiprocessing import Process
import signal,sys
from db_mysql import User

HOST = '0.0.0.0'
PORT = 8898
ADDR = (HOST,PORT)
db = User(database='counts') # 数据库操作对象

# 增加
def do_push(connfd,data):
    tmp = data.split(' ')
    modle = tmp[1]
    number1 = tmp[2]
    VIN = tmp[3]
    engine = tmp[4]
    check1 = tmp[5]
    run1 = tmp[6]
    order1 = tmp[7]
    company = tmp[8]
    address = tmp[9]
    name1 = tmp[10]
    telephone1 = tmp[11]
    w=db.push(modle,number1,VIN,engine,check1,run1,order1,company,address,name1,telephone1)
    print(w)
    if w:
        connfd.send(b'OK')

# 修改
def do_change(connfd,data):
    tmp = data.split(' ')
    id = tmp[1]
    company = tmp[2]
    r=db.change(company,id)
    print(r)
    if r:
        connfd.send(b'OK')

# 查询
def do_chat(connfd,data):
    tmp = data.split(' ')
    id = tmp[1]
    r=db.chat(id)
    print(r)
    msg=''
    for i in r[0]:
        msg+=str(i)
        msg+=' '
    if r:
        connfd.send(msg.encode())
    else:
        connfd.send('没有找到'.encode())

# 删除
def do_delete(connfd,data):
    id = data.split(' ')[1]
    db.delete(id)
    connfd.send(b'ok')

# 处理客户端各种请求
def request(connfd):
    db.create_cursor()
    while True:
        data = connfd.recv(1024).decode() # 接受请求
        print(data)
        if not data or data[0] == 'E':
            sys.exit() # 退出对应的子进程
        elif data.split(' ')[0] == 'R':
            do_push(connfd,data)
        elif data.split(' ')[0] == 'L':
            do_change(connfd,data)
        elif data.split(' ')[0] == 'C':
            do_chat(connfd,data)
        elif data.split(' ')[0] == 'H':
            do_delete(connfd,data)

# 搭建网络
def main():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    # 处理僵尸进场
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
    # 循环等待客户端链接
        print("Listen the port 8888")

        connfd,addr = s.accept()
        print("Connect from",addr)
        # 创建子进程
        p = Process(target=request,args=(connfd,))
        p.daemon = True
        p.start()

if __name__ == '__main__':
    main()











