#!/usr/bin/env python3
"""
ShibaCuddles - Network Scanning Tool
Usage: python main.py [network]
Example: python main.py 192.168.1.0/24
"""

import sys
from shibacuddles.device import discover_devices
from shibacuddles.portscan import scan_ports

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [network]")
        return
        
    network = sys.argv[1]
    devices = discover_devices(network)
    
    print(f"Found {len(devices)} devices:")
    for dev in devices:
        open_ports = scan_ports(dev.ip, range(1, 1025))
        print(f"  {dev.ip}: {open_ports}")

if __name__ == "__main__":
    main()