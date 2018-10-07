import socket
import time

class ClientError(Exception):
    pass

class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.success_answer = 'ok\n\n'        
    
    def put(self, metric_name, metric_value, timestamp = str(int(time.time()))):
        command_string = f'put {metric_name} {metric_value} {timestamp}\n'
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            sock.sendall(command_string.encode())
            server_answer = sock.recv(1024).decode()
        if server_answer != self.success_answer:
            raise ClientError(server_answer)
        

    def get(self, metric_name):
        result = {}
        command_string = f'get {metric_name}\n'
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            sock.sendall(command_string.encode())
            server_answer = sock.recv(1024).decode()
        if server_answer[0:2] != self.success_answer[0:2]:
            raise ClientError
        
        # server_answer = 'ok\npalm.cpu 10.5 1\npalm.cpu 0.5 2\neardrum.cpu 15.3 3\n\n'        
        for metrics in server_answer[3:].split('\n')[:-2]:            
            metric = metrics.split()            
            if not result.get(metric[0]):
                result[metric[0]] = []            
            result[metric[0]].append((int(metric[2]), float(metric[1])))        
        return result

def _main():
    client = Client('127.0.0.1', 8888, 15)
    
    # client.put('palm.cpu', 0.5, timestamp=1150864247)
    # client.put('palm.cpu', 2.0, timestamp=1150864248)
    # client.put('palm.cpu', 0.5, timestamp=1150864248)

    # client.put('eardrum.cpu', 3, timestamp=1150864250)
    # client.put('eardrum.cpu', 4, timestamp=1150864251)
    # client.put('eardrum.memory', 4200000)

    print(client.get('*'))

if __name__ == '__main__':
    _main()






