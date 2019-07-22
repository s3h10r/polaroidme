# --- all polaroidme-plugins (generators, filters) must implement this
name = "example"
description = "a template you can use to roll your own plugins"
kwargs = { 'arg1' : 'val1', 'arg2' : 'val2', } # plugin specific arguments (if any)
args = None
author = "optional author and copyright infos"
version = "0.2.0"

def perform_operation(**kwargs):
    """
    this is the interface/wrapper around the functionality of the plugin.
    """
    #call the plugin-specific function(s) here
    if not kwargs :
        #use default values if no args given
        return _bla()
    else:
        return _bla(**kwargs)

# --- END all polaroidme-plugins (generators, filters) must implement this

def _bla(arg1=None, arg2 = None):
    return ("Hello from Plugin dummy1. arg1=%s, arg2=%s " % (arg1,arg2))
