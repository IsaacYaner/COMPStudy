import zlib
import time

from rsa import sign

def bytewise(message, encoding='utf-8'):
    message = bytes(str(message), encoding) if type(message) != bytes else message
    return message

def hash(message, encoding='utf-8'):
    message = bytewise(message, encoding)
    value = zlib.crc32(message) & 0xffffffff
    return f"{value:#0{10}x}"

def feature(message, stamp=None, encoding='utf-8'):
    if stamp is None:
        stamp = time.time()
    stamp = bytewise(stamp)
    message = bytewise(message, encoding)
    message += stamp
    return hash(message, encoding)

def encode(message, stamp=None, feat=None, encoding='utf-8'):
    if feat is None:
        feat = feature(message, stamp, encoding)
    feat = bytewise(feat)
    return feat+bytewise(message)
    
def decode(message):
    return message[10:], message[:10]