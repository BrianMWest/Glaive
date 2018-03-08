import pickle
import re
import struct
import sys

in_pipe = None
out_pipe = None

_params = {}


def init():
    global in_pipe, out_pipe, _params

    in_pipe = sys.stdin
    out_pipe = sys.stdout

    sys.stdin = None
    sys.stdout = sys.stderr

    for arg in sys.argv[1:]:
        key_values = arg.split('=')
        _params[key_values[0]] = '='.join(key_values[1:])


def close():
    sys.stdin = in_pipe
    sys.stdout = out_pipe

    in_pipe = None
    out_pipe = None


def params():
    return _params


def send(packet, port=0):
    if in_pipe is None or out_pipe is None:
        return 0

    out_pipe.write(struct.pack('<B', port))
    packet_bytes = pickle.dumps(packet)
    out_pipe.write(struct.pack('<I', len(packet_bytes)))
    out_pipe.write(packet_bytes)
    out_pipe.flush()

    return 5 + len(packet_bytes)


def get():
    if in_pipe is None or out_pipe is None:
        return None

    port = struct.unpack('<B', in_pipe.read(1))[0]
    packet_length = struct.unpack('<I', in_pipe.read(4))[0]
    return (port, pickle.loads(in_pipe.read(packet_length)))


def stream():
    while in_pipe is not None and out_pipe is not None and not in_pipe.closed:
        yield get()
