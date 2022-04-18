import zlib
import time

from rsa import sign

# Convert message into bytes form
def bytewise(message, encoding='utf-8'):
    message = bytes(str(message), encoding) if type(message) != bytes else message
    return message

# Return crc32 encoded message
def hash(message, encoding='utf-8'):
    # Convert message into bytes format
    message = bytewise(message, encoding)
    # Encode using crc32
    value = zlib.crc32(message) & 0xffffffff
    # Restrict format into 0x{10 digits}
    return f"{value:#0{10}x}"

# Return unique feature code for the message using current timestamp
#   By hashing message+stamp
def feature(message, stamp=None, encoding='utf-8'):
    if stamp is None:
        stamp = time.time()
    stamp = bytewise(stamp)
    message = bytewise(message, encoding)
    message += stamp
    return hash(message, encoding)

# Encode message by attaching feature code
def encode(message, stamp=None, feat=None, encoding='utf-8'):
    if feat is None:
        feat = feature(message, stamp, encoding)
    feat = bytewise(feat)
    return feat+bytewise(message)
    
# Decode by detaching feature code
def decode(message):
    return message[10:], message[:10]