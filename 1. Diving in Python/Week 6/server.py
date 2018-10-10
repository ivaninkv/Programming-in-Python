import json
import asyncio


ALLOWED_COMMAND = ('put', 'get', 'storage')
SUCCESS_ANSWER = 'ok\n\n'
WRONG_COMMAND_ANSWER = 'error\nwrong command\n\n'
STORAGE = {}

def storage_handler():
    return str(STORAGE)

def put_handler(recv_data):        
    try:
        metric, value, timestamp = recv_data.split()[1:]
        if metric not in STORAGE.keys():
            STORAGE[metric] = []            
        
        l = STORAGE.get(metric)
        updated = False
        for element in l:
            if element[0] == int(timestamp):
                element[1] = float(value)
                updated = True
        if not updated:
            STORAGE[metric].append([int(timestamp), float(value)])

        return SUCCESS_ANSWER
    except Exception as e:
        print(e)        
        return WRONG_COMMAND_ANSWER    


def get_handler(recv_data):
    command_list = recv_data.split()
    if len(command_list) != 2:
        return WRONG_COMMAND_ANSWER

    key = command_list[1]    
    answer = 'ok\n'
    for k, value in STORAGE.items():
        if k == key or key == '*':
            for val in value:
                answer += f'{k} {val[1]} {val[0]}\n'
    answer += '\n'
    return answer    


def parse_request(recv_data):
    if len(recv_data) > 4 and (recv_data[:3] in ALLOWED_COMMAND or recv_data[:7] in ALLOWED_COMMAND): 
        if recv_data[:3] == ALLOWED_COMMAND[0]:
            return put_handler(recv_data)
        elif recv_data[:3] == ALLOWED_COMMAND[1]:
            return get_handler(recv_data)
        elif recv_data[:7] == ALLOWED_COMMAND[2]:
            return storage_handler()
        else:
            return WRONG_COMMAND_ANSWER
    else:    
        return WRONG_COMMAND_ANSWER


async def handle_echo(reader, writer):
    recv_data = await reader.read(1024)
    client_answer = parse_request(recv_data.decode())

    print(f'Received {recv_data} from {writer.get_extra_info("peername")}')
    print(f'Send to client {client_answer.encode()}')
    
    writer.write(client_answer.encode())
    await writer.drain()
    
    writer.close()


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = parse_request(data.decode())
        self.transport.write(resp.encode())


def run_server(host, port):        
    
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()    
    
    ''' old version
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_echo, host, port, loop=loop)    
    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
    '''


def _main():
    run_server('127.0.0.1', 8888)

if __name__ == '__main__':
    _main()

