"""
dict 客户端

功能: 发起请求,接收结果
"""

from socket import *
import sys

# 服务器地址
ADDR = ('127.0.0.1',8898)
s = socket()
s.connect(ADDR)

# 增加
def do_push():
    while True:
        modle=input('modle:')
        number1=input('number:')
        VIN=input('VIN:')
        engine=input('engine:')
        check1=input('check1:')
        run1=input('run1:')
        order1=input('order1:')
        company=input('company:')
        address=input('address:')
        name1=input('name:')
        telephone1=input('telephone1:')
        msg = "R %s %s %s %s %s %s %s %s %s %s %s"%(modle,number1,VIN,engine,check1,run1,order1,company,address,
                                                       name1,telephone1)
        s.send(msg.encode()) # 发送请求
        data = s.recv(128).decode() # 反馈
        if data == 'OK':
            print("增加成功")
        else:
            print("增加失败")
        return

# 修改 规定修改company
def do_change():
    while True:
        id=int(input('id:'))
        company = input('company:')
        msg = "L %d %s"%(id,company)
        s.send(msg.encode())  # 发请求
        data = s.recv(128).decode() # 得到反馈
        if data == 'OK':
            print("修改成功")
        else:
            print("修改失败")

#查询
def do_chat():
    while True:
        id = int(input('id:'))
        msg = "C  %d"%(id)
        s.send(msg.encode())
        data = s.recv(1024).decode()
        print(data)

#删除
def do_delet():
    while True:
        id = int(input('id:'))
        msg = "H %d"%(id)
        s.send(msg.encode())
        data = s.recv(1024).decode()
        print(data)

#退出

# 搭建网络
def main():
    while True:
        print("""
        ================== Welcome =============
          1.增加    2.修改    3.查询  4.删除  5.退出
        ========================================
        """)
        cmd = input("选项(1,2,3,4,5):")
        if cmd == '1':
            do_push()
        elif cmd == '2':
            do_change()
        elif cmd == '3':
            do_chat()
        elif cmd == '4':
            do_delet()
        elif cmd == '5':
            s.send(b'E')
            sys.exit("谢谢使用")
        else:
            print("请输入正确命令语句")

if __name__ == '__main__':
    main()







