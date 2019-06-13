#!/usr/bin/env python

# Loads jsonschema files, uses them to list modules that will be
# created. The jsonschema files will be provided from the provided module_path

import importlib
import posixpath
import os

import json
import jsonschema

import sbfmt


MODS = dict()

def get_schema(version: str = "v1_module") -> str:
    """Load the appropriate schema"""
    with importlib.resources.path('sbfmt', 'formats') as fmt_path:
        with open(fmt_path.joinpath(version)) as schema:
            return json.load(schema)

def load_modules(module_name: str, module_path: str) -> dict:
    """Load every file that starts with "module_" that is within
    the module_name/module_path
    """
    importlib.import_module(module_name)
    with importlib.resources.path(module_name, module_path) as mpath:
        for fname in os.listdir(mpath):
            if fname.startswith('module_') and fname.endswith('.json'):
                # XXX: wrap this in some retrying or something
                import_module(mpath, fname)

def import_module(mpath: str, fname: str) -> dict:
    """Loads a module's json file"""
    with open(fname) as schema:
        schema = get_schema()
        loadit = json.load(mpath.joinpath(schema))
        jsonschema.validate(loadit, schema)
        # XXX I think at this point the goal is to turn a configuration
        # into a thing that can be loaded into this:
        # http://errbot.io/en/latest/errbot.botplugin.html#errbot.botplugin.Command
        # Or this:
        # http://errbot.io/en/latest/_modules/errbot/botplugin.html#BotPluginBase.create_dynamic_plugin
        
    
