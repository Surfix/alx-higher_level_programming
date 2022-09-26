!/usr/bin/python3
def multiple_returns(sentence):
    len_ = len(sentence)
    if len_ == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return len_, first_char
