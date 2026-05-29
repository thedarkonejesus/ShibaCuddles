#!/usr/bin/env python3
"""
ShibaCuddles - Network Scanning Tool
Usage: python main.py [network] [options]
Example: python main.py 192.168.1.0/24 --ports 1-1024 --output results.json
"""

import argparse
import json
from src import discover_devices, scan_ports

def parse_args():
    parser = argparse.ArgumentParser(description="Network scanner for ShibaCuddles")
    parser.add_argument("network", help="Target network (CIDR notation)")
    parser.add_argument("--ports", "-p", type=str, default="1-1024",
                       help="Port range (default: 1-1024)")
    parser.add_argument("--output", "-o", type=str,
                       help="Output file (JSON format)")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Verbose output")
    return parser.parse_args()

def format_ports(port_range):
    """Convert port range string to list of integers."""
    if "-" in port_range:
        start, end = map(int, port_range.split("-"))
        return list(range(start, end + 1))
    return [int(p) for p in port_range.split(",")]

def main():
    args = parse_args()
    ports = format_ports(args.ports)
    
    if args.verbose:
        print(f"Scanning {args.network} for ports {args.ports}")
        
    devices = discover_devices(args.network)
    results = []
    
    for dev in devices:
        open_ports = scan_ports(dev.ip, ports)
        device_data = {
            "ip": dev.ip,
            "open_ports": sorted(open_ports)
        }
        results.append(device_data)
        
        if args.verbose:
            print(f"Found {len(open_ports)} open ports on {dev.ip}")
    
    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {args.output}")
    else:
        print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
