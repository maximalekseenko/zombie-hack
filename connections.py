"""Module for handling connections.

Before using this module:
1. Set up settings in `.env`
* `url` - url to the server. It can be a test one of a final one;
* `token` - personal token for connecting;

Those setting may be changed in run-time by adjusting them in `connections.settings` variable.

2. Run `connections.Init` to initialize this module.
"""



import os
import requests as r
from dotenv import load_dotenv



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
    load_dotenv()
    URL=os.getenv("URL")
    TOKEN=os.getenv("TOKEN")
    settings['url'] = URL
    settings['token'] = TOKEN
    __is_initialized = True




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

    # Asserts.
    assert __is_initialized, "Using uninitialized module 'connections'"

    # Adding command.
    __commands_attack.append({"blockId":blockId, "target":target})



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

    # Asserts.
    assert __is_initialized, "Using uninitialized module 'connections'"

    # Adding command.
    __commands_build.append({"position":position})


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

    # Asserts.
    assert __is_initialized, "Using uninitialized module 'connections'"

    # Adding command.
    __commands_moveBase.append({"position":position})


def PostCommands() -> dict:
    """Post function, that sends commands to the server.

    Use AddCommandXXX functions to add commands, that will be sent with this function.

    All commands will be cleared after sending.

    Returns respond to this command with next structure on success:
    * `acceptedCommands` -- List of accepted commands;
    * `errors` -- list of errors happened during command execution.

    Throws if this module is not initialized.
    """

    # Asserts.
    assert __is_initialized, "Using uninitialized module 'connections'"

    ret = r.post(
        url=f"{settings["url"]}/play/zombidef/command",

        headers={
            "X-Auth-Token":settings["token"]
        },

        data={
            "attack":__commands_attack,
            "build":__commands_build,
            "moveBase":__commands_moveBase
        }
    )

    return ret


def PutIntoQueue() -> dict:
    """Puts *us* into next round queue.

    Returns respond to this command with next structure on success:
    * `startsInSec` -- Number of time until start.

    Throws if this module is not initialized.
    """

    ret = r.put(
        url=f"{settings["url"]}/play/zombidef/participate",

        headers={
            "X-Auth-Token":settings["token"]
        }
    )
    return ret


def GetWorldDynamic() -> dict:
    """Gets dynamic parts of the world.

    Returns respond to this command with next structure on success:
    * TODO

    Throws if this module is not initialized.
    """
    ret = r.get(
        url=f"{settings["url"]}/play/zombidef/units",

        headers={
            "X-Auth-Token":settings["token"]
        }
    )
    return ret


def GetWorldStatic() -> dict:
    """Gets static parts of the world.

    Returns respond to this command with next structure on success:
    * TODO

    Throws if this module is not initialized.
    """
    ret = r.get(
        url=f"{settings["url"]}/play/zombidef/world",

        headers={
            "X-Auth-Token":settings["token"]
        }
    )
    return ret



def GetRounds() -> dict:
    """Gets info about rounds.

    Returns respond to this command with next structure on success:
    * TODO

    Throws if this module is not initialized.
    """
    ...
