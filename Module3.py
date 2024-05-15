def message_secret():
    message_code = [77, 97, 114, 116, 105, 110, 32, 116, 117, 32, 101, 115, 32, 117, 110, 32, 112, 101, 116, 105, 116,
                    32, 110, 111,
                    111, 98]
    message_decode = ''
    for x in message_code:
        message_decode += chr(x)
    return message_decode