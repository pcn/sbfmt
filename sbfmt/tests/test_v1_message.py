from sbfmt import v1_message


def test_v1_message_write_message():
    """Validate that the function returns the appropriate schema"""
    request = {"a": "b", "c": "d"}
    source = {
        "user": "pcn",
        "channel": "ops-blah",
        "return_to_user": False}
    print(v1_message.write_message(1, request, {}, source))
    assert v1_message.write_message(1, request, {}, source) == {
        "version": 1,
        "request": request,
        "response": {},
        "source": source
    }
