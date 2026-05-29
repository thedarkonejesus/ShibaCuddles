"""
ShibaCuddles - Network Scanning Tool
Version 1.0
"""

__version__ = "1.0"
__author__ = "Your Name"

# Import core modules
from .device import discover_devices
from .portscan import scan_ports

__all__ = [
    "discover_devices",
    "scan_ports"
]