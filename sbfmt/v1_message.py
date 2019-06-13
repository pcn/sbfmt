#!/usr/bin/env python

import json
import importlib.resources
import jsonschema

def get_schema():
    """Load the appropriate schema"""
    with importlib.resources.path('sbfmt', 'formats') as fmt_path:
        with open(fmt_path.joinpath("v1_message.json")) as schema:
            return json.load(schema)


def write_message(version: int,
                  request: dict,
                  response: dict,
                  source: dict) -> dict:
    """Provided with the arguments for a message, turn them into a
    message and validate the message."""
    if version != 1:
        raise ValueError("The version for this message must be 1")
    message = {
        "version": version,
        "request": request,
        "response": response,
        "source": source
    }
    schema = get_schema()
    # Raises a ValidationError, no return required I guess
    jsonschema.validate(message, schema)
    return message
