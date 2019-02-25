import socket
import sys
from threading import Thread

def getc_data(con,address):
    maxsize = 4096
    input_data = con.recv(maxsize)

    siz = sys.getsizeof(input_data)
    if siz >= maxsize:
        print(" messgae is out off size",siz)
    input_msg = input_data.decode("utf8")

    print(input_msg)

def start_server():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serversocket.bind(("127.0.1.1", 12345))
        
    except socket.error as msg:
        print('Bind failed. Error : ' + str(sys.exc_info()))
        sys.exit()

    serversocket.listen(1)
    while True:
        (con, address) = serversocket.accept()
        #print("connetcion enable to this ip",address)
        try:

            Thread(target=getc_data,args=(con,address)).start()

        except:
            print("Terible error!")
            import traceback
            traceback.print_exc()
    serversocket.close()

start_server() 
        




