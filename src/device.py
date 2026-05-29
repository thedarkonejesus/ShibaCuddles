from scapy.all import sr1, IP, ICMP

class Device:
    def __init__(self, ip):
        self.ip = ip
    
    def __str__(self):
        return f"Device({self.ip})"

def discover_devices(network):
    devices = []
    for ip in network.hosts():
        pkt = IP(dst=str(ip))/ICMP()
        resp = sr1(pkt, timeout=2, verbose=0)
        if resp:
            devices.append(Device(str(ip)))
    return devices