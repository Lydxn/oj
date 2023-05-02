from algogym import settings

import json
import socket
import struct


class JudgeClient:
    def __init__(self, address):
        self.address = address

    def __enter__(self):
        self.connect()
        return self

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(self.address)

        self.rfile = self.sock.makefile('rb')

    def submit(self, submission):
        self.send_data({
            'header': 'submit',
            'access-token': settings.JUDGE_ACCESS_TOKEN,
            'id': submission.id,
            'problem-code': submission.problem.code,
            'language': submission.language.code,
            'source': submission.source,
            'time-limit': submission.problem.time_limit,
            'memory-limit': submission.problem.memory_limit
        })

        while True:
            data = self.read_data()
            if data is None:
                raise socket.error('Failed to read data from judge server.\n')

            yield data

            if data['header'] == 'judging-end':
                break

    def read_data(self):
        packed_msglen = self.rfile.read(4)
        if not packed_msglen:
            return None

        msglen = struct.unpack('!I', packed_msglen)[0]

        data = self.rfile.read(msglen)
        if not data:
            return None

        return json.loads(data)

    def send_data(self, obj):
        data = json.dumps(obj).encode('utf-8')
        self.sock.sendall(struct.pack('!I', len(data)) + data)

    def __exit__(self, exc, value, traceback):
        self.sock.close()
