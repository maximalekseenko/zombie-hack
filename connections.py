"""Module for handling connections.

Before using this module:
1. Set up settings in init.config
* `url` - url to the server. It can be a test one of a final one;
* `token` - personal token for  connecting ;

Those setting may be changed in run-time by adjusting them in `connections.settings` variable.

2. Run `connections.Init` to initialize this module.
"""



__is_initialized = False
"""Defines if this module was initialized correctly

Readonly.

It becomes `True` on successful run of `connections.Init` function.
"""



settings = {}
"""Settings for this module.

Initialized in `connections.Init`. Should not be used before initialization.
"""



def Init():
    """Function that initializes this module.

    Throws if file `init.config` is missing.
    """
    ...



__commands_attack:list[dict] = []
"""List of attack commands to be sent with next post request.

Add new commands with `connections.AddCommandAttack`
"""
def AddCommandAttack(blockId:str, target:dict):
    """Adds attack command to next post request.
    
    Arguments:
    * blockId -- Id of a base block to attack from;
    * target -- Target position, defined with `"x"` and `"y"` fields;

    Throws if this module is not initialized.
    """
    ...



__commands_build:list[dict] = []
"""List of attack commands to be sent with next post request.

Add new commands with `connections.AddCommandBuild`
"""
def AddCommandBuild(position:dict):
    """Adds build command to next post request.
    
    Arguments:
    * position -- Target position, defined with `"x"` and `"y"` fields;

    Throws if this module is not initialized.
    """
    ...
    


__commands_moveBase:list[dict] = []
"""List of attack commands to be sent with next post request.

Add new commands with `connections.AddCommandMoveBase`
"""
def AddCommandMoveBase(position:dict):
    """Adds moveBase command to next post request.
    
    Arguments:
    * position -- Target position, defined with `"x"` and `"y"` fields;

    Throws if this module is not initialized.
    """
    ...



def PostCommands() -> dict:
    """Post function, that sends commands to the server.

    Use AddCommandXXX functions to add commands, that will be sent with this function.

    All commands will be cleared after sending.
    
    Returns respond to this command.

    Throws if this module is not initialized.
    """
    ...



def PutQueue() -> dict:
    """Puts *us* into next round queue.
    
    Returns respond to this command.
    
    Throws if this module is not initialized.
    """
    ...



def GetWorldDynamic() -> dict:
    """Gets dynamic parts of the world.

    Returns respond to this command.
    
    Throws if this module is not initialized.
    """
    ...


def GetWorldStatic() -> dict:
    """Gets static parts of the world.
    
    Returns respond to this command.
    
    Throws if this module is not initialized.
    """
    ...


    
def GetRounds() -> dict:
    """Gets info about rounds.
    
    Returns respond to this command.
    
    Throws if this module is not initialized.
    """
    ...