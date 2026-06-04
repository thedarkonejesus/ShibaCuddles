# ShibaCuddles - Advanced Network Scanner & Security Testing Suite

## 🎯 Quick Start

### CLI Mode
```bash
# Basic scan
python main.py 192.168.1.0/24

# Aggressive scan with service detection
python main.py 192.168.1.0/24 --aggressive -vv

# Export results
python main.py 192.168.1.0/24 --output results.json --format json
```

### GUI Mode
```bash
python gui_launcher.py
```

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip
- For WiFi features: aircrack-ng suite

### Setup
```bash
# Clone repository
git clone https://github.com/thedarkonejesus/ShibaCuddles.git
cd ShibaCuddles

# Install dependencies
pip install -r requirements.txt

# Install WiFi tools (Linux)
sudo apt-get install aircrack-ng  # Ubuntu/Debian
sudo dnf install aircrack-ng       # Fedora
brew install aircrack-ng           # macOS
```

## 🚀 Features

### Network Scanning
✅ **Device Discovery**
- ICMP ping sweep
- ARP scanning
- Hostname resolution
- MAC address detection

✅ **Port Scanning**
- TCP port scanning (1-65535)
- UDP port detection
- Banner grabbing
- Service version detection

✅ **Advanced Analysis**
- Service fingerprinting (20+ services)
- OS fingerprinting (TTL-based)
- Vulnerability detection
- Real-time statistics

### GUI Interface
✅ **User-Friendly Dashboard**
- Real-time scan progress
- Live results table
- Statistics visualization
- Comprehensive logging
- Multi-format export

### WiFi Security Testing
⚠️ **Deauthentication (Requires aircrack-ng)**
- Device deauthentication
- Broadcast deauth attacks
- Monitor mode control
- Network scanning
- Channel jamming analysis

⚠️ **Advanced Features**
- Rogue AP creation
- Traffic analysis
- Network interruption testing

## 📊 CLI Usage

### Basic Commands
```bash
# Default scan (ports 1-1024)
python main.py 192.168.1.0/24

# Specific ports
python main.py 192.168.1.0/24 --ports 22,80,443
python main.py 192.168.1.0/24 --ports 1-5000

# With threading
python main.py 192.168.1.0/24 --threads 20

# With services and OS detection
python main.py 192.168.1.0/24 --service-detection --os-detection

# Aggressive scan (all features)
python main.py 192.168.1.0/24 --aggressive

# Verbose output
python main.py 192.168.1.0/24 -vv

# Custom timeout
python main.py 192.168.1.0/24 --timeout 10
```

### Output Options
```bash
# JSON export (default)
python main.py 192.168.1.0/24 --output results.json

# CSV export
python main.py 192.168.1.0/24 --output results.csv --format csv

# XML export
python main.py 192.168.1.0/24 --output results.xml --format xml

# Text export
python main.py 192.168.1.0/24 --output results.txt --format txt
```

## 🖥️ GUI Features

### Scan Configuration
- Network target (CIDR notation)
- Custom port ranges
- Thread count (1-64)
- Connection timeout
- Toggle ping sweep
- Toggle service detection
- Toggle OS fingerprinting
- Aggressive mode

### Results Viewing
- Real-time results table
- IP address, status, ports, services, OS
- Statistics dashboard
- Live logging output
- Export to multiple formats

## ⚠️ WiFi Deauthentication (Advanced)

### Legal Warning
**Unauthorized wireless network interference is illegal in most jurisdictions.**

Only use this feature for:
- Testing your own networks
- Authorized penetration testing
- Educational purposes

### Usage
```python
from src.deauth import WiFiDeauthenticator

deauth = WiFiDeauthenticator()

# Enable monitor mode
deauth.enable_monitor_mode('wlan0')

# Deauth specific device
target = DeauthTarget(
    mac_address='AA:BB:CC:DD:EE:FF',
    gateway_mac='11:22:33:44:55:66',
    ssid='TestNetwork',
    channel=6,
    interface='wlan0mon'
)
deauth.deauthenticate_device(target)

# Disable monitor mode
deauth.disable_monitor_mode('wlan0mon')
```

## 🔍 Example Scans

### Small Office Network
```bash
python main.py 10.0.0.0/24 --threads 15 --ports 22,80,443,3306,5432
```

### Home Network Security Audit
```bash
python main.py 192.168.0.0/24 --aggressive --service-detection --os-detection
```

### Enterprise Network Assessment
```bash
python main.py 172.16.0.0/16 --threads 32 --ports 1-10000 --aggressive -vv
```

## 📊 Understanding Results

### JSON Output Format
```json
[
  {
    "ip": "192.168.1.1",
    "alive": true,
    "open_ports": [22, 80, 443],
    "services": {
      "22": {"name": "SSH", "version": "OpenSSH 8.2"},
      "80": {"name": "HTTP", "version": "Apache 2.4.29"}
    },
    "os_info": {"name": "Linux/Unix", "ttl": 64, "confidence": 95},
    "scan_time": 2.34
  }
]
```

## 🛠️ Troubleshooting

### Issue: Permission Denied (WiFi Features)
**Solution:**
```bash
sudo chmod +u+s /usr/bin/airmon-ng
sudo chmod +u+s /usr/bin/aireplay-ng
```

### Issue: PyQt6 Not Found
**Solution:**
```bash
pip install PyQt6 PyQt6-Charts
```

### Issue: Scan Timeout
**Solution:** Increase timeout value
```bash
python main.py 192.168.1.0/24 --timeout 15
```

### Issue: High False Negatives
**Solution:** Disable ping sweep
```bash
python main.py 192.168.1.0/24 --no-ping
```

## 📈 Performance Tips

1. **Threading**: Use more threads for larger networks
   ```bash
   python main.py 10.0.0.0/16 --threads 64
   ```

2. **Port Range**: Scan common ports first
   ```bash
   python main.py 192.168.1.0/24 --ports 22,80,443,3306,5432,8080
   ```

3. **Rate Limiting**: Reduce network load
   ```bash
   python main.py 192.168.1.0/24 --rate-limit 0.1
   ```

4. **Timeout**: Adjust based on network conditions
   ```bash
   python main.py 192.168.1.0/24 --timeout 3
   ```

## 🔐 Security Considerations

- Always get written permission before scanning networks
- Comply with local laws and regulations
- Don't use deauth features on networks you don't own
- Be mindful of DoS-like behavior
- Respect network resources

## 📝 Configuration File

Create `config.yaml` for default settings:
```yaml
scanning:
  threads: 20
  timeout: 5.0
  rate_limit: 0.0
  batch_size: 50

features:
  ping_sweep: true
  service_detection: false
  os_detection: false
  aggressive: false

output:
  format: json
  export_path: ./results/
```

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

**ShibaCuddles is provided as-is for educational and authorized security testing purposes only.**

Unauthorized access to computer systems is illegal. Users are responsible for ensuring they have proper authorization before using this tool on any network or system.

## 🐕 About

ShibaCuddles - "Because every network needs a cuddly scanner!"

Built for security professionals and network administrators to perform efficient, comprehensive network assessments.

---

For more information, visit: https://github.com/thedarkonejesus/ShibaCuddles
