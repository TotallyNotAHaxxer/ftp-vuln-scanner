import socket 
import time

print(" EX ==> FreeFloat Ftp Server (version 1.00) ")
time.sleep(1)
print(" If you want to scan defualt servers just press enter ")


A = str(input(" Server ==> "))
B = str(input(" IPA to scan on ===> "))

class TCP_Scan(object):
    def __init__(self):
        socket.setdefaulttimeout(2)
        self.connection = socket.socket()
        self.vulnerbailities = [
            "FreeFloat Ftp Server (version 1.00)",
            "3Com 3CDaemon FTP Server Version 2.0",
            "Ability Server 2.34",
            "Sami FTP Server 2.0.2"
        ]
    
    def scan(self, IP=f"{B}"):
        self.connection.connect((IP, 21))
        answer = self.connection.recv(1024)
        for vul in self.vulnerbailities:
            if vul in answer:
                print(f"[!] {vul} is vulnerable")
            else:
                print("FTP Server is not vulnerable")

if __name__ == "__main__":
    TCP_Scan().scan()
    print("Scanned the following")
    print(self.vulnerbailities)
