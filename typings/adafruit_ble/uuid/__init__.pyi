"""
This type stub file was generated by pyright.
"""

import struct
import _bleio

"""

This module provides core Unique ID (UUID) classes.

"""
__version__ = ...
__repo__ = ...
class UUID:
    """Top level UUID"""
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __bytes__(self): # -> bytes:
        ...
    
    def pack_into(self, buffer, offset=...): # -> None:
        """Packs the UUID into the buffer at the given offset."""
        ...
    


class StandardUUID(UUID):
    """Standard 16-bit UUID defined by the Bluetooth SIG."""
    def __init__(self, uuid16) -> None:
        ...
    


class VendorUUID(UUID):
    """Vendor defined, 128-bit UUID."""
    def __init__(self, uuid128) -> None:
        ...
    

