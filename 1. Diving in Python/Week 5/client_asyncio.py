import asyncio
import time

class ClientError(Exception):
    pass

class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.success_answer = 'ok\n\n'

    def _send_command(self, command_string):
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        server_answer = loop.run_until_complete(self._asyncio_client(command_string, loop))
        loop.close()
        return server_answer

    async def _asyncio_client(self, message, loop):
        reader, writer = await asyncio.open_connection(self.host, self.port, loop=loop)        
        writer.write(message.encode())        
        server_answer = await reader.read()        
        writer.close()
        return server_answer.decode()     
    
    def put(self, metric_name, metric_value, timestamp = str(int(time.time()))):
        command_string = f'put {metric_name} {metric_value} {timestamp}\n'
        server_answer = self._send_command(command_string)
        if server_answer != self.success_answer:
            raise ClientError(server_answer)

    def get(self, metric_name):
        result = {}
        command_string = f'get {metric_name}\n'
        server_answer = self._send_command(command_string)
        if server_answer[0:2] != self.success_answer[0:2]:
            raise ClientError

        server_answer = 'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'        
        for metrics in server_answer[3:].split('\n')[:-2]:
            metric = metrics.split()            
            if not result.get(metric[0]):
                result[metric[0]] = (int(metric[2]), float(metric[1]))

        return result


def main():
    client = Client('127.0.0.1', 8888, 15)
    
    client.put('palm.cpu', 0.5, timestamp=1150864247)
    client.put('palm.cpu', 2.0, timestamp=1150864248)
    client.put('palm.cpu', 0.5, timestamp=1150864248)

    client.put('eardrum.cpu', 3, timestamp=1150864250)
    client.put('eardrum.cpu', 4, timestamp=1150864251)
    client.put('eardrum.memory', 4200000)

    print(client.get('*'))

if __name__ == '__main__':
    main()






