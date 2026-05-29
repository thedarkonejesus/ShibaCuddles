#!/usr/bin/env python3
"""
ShibaCuddles - Utility functions
"""

import json
import socket
from ipaddress import IPv4Network
from typing import List, Dict, Any

def validate_ip(ip: str) -> bool:
    """Validate IPv4 address format."""
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def validate_network(network: str) -> bool:
    """Validate CIDR notation."""
    try:
        IPv4Network(network)
        return True
    except ValueError:
        return False

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file."""
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_results(results: List[Dict], output_path: str) -> None:
    """Save scan results to JSON file."""
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

def format_ports(port_range: str) -> List[int]:
    """Convert port range string to list of integers."""
    if "-" in port_range:
        start, end = map(int, port_range.split("-"))
        return list(range(start, end + 1))
    return [int(p) for p in port_range.split(",")]

def get_hostname(ip: str) -> str:
    """Resolve hostname for IP address."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "unknown"

def is_port_open(ip: str, port: int) -> bool:
    """Check if specific port is open."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

__all__ = [
    "validate_ip",
    "validate_network",
    "load_config",
    "save_results",
    "format_ports",
    "get_hostname",
    "is_port_open"
]