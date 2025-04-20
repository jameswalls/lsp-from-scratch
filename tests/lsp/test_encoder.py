from lsp_from_scratch.coders import encode_message, decode_message
import pytest


def test_encode_message():
    expected = b'Content-Length: 16\r\n\r\n{"testing":true}'
    encoding_example = { "testing": True }
    actual = encode_message(encoding_example)

    assert expected == actual, "\nexpected {},\nactual {}".format(expected, actual)

def test_decode_message():
    incoming_message = b"Content-Length: 15\r\n\r\n{\"method\":\"hi\"}"
    method, content = decode_message(incoming_message)
    content_length = len(content)

    assert content_length == 15, "\nexpected {},\nactual {}".format(15, content_length)
    assert method == "hi", "\nexpected {},\nactual {}".format("hi", method)
