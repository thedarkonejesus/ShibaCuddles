# 🐕 ShibaCuddles - Network Scanner

> A lightweight, efficient network scanning tool written in Python. Discover active hosts and scan ports with ease.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP%208-brightgreen.svg)](https://pep8.org/)

---

## ✨ Features

- 🔍 **ICMP-based Device Discovery** - Quickly identify active hosts on your network
- 🔌 **TCP Port Scanning** - Scan ports 1-1024 by default, or customize your range
- ⚙️ **Highly Configurable** - Adjust port ranges, timeouts, and scan parameters
- 📊 **JSON Output Support** - Export results in structured JSON format
- 🔊 **Verbose Logging** - Detailed output for debugging and monitoring
- ✅ **Comprehensive Testing** - Includes unit tests for reliability
- 🚀 **Performance Optimized** - Efficient scanning with minimal resource usage

---

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Architecture](#architecture)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

```bash
# Clone the repository
git clone https://github.com/thedarkonejesus/ShibaCuddles.git
cd ShibaCuddles

# Install dependencies
pip install -r requirements.txt
```

---

## ⚡ Quick Start

```bash
# Scan a network subnet
python main.py 192.168.1.0/24

# Output will show discovered hosts and open ports
```

---

## 📖 Usage

### Basic Scanning

```bash
python main.py 192.168.1.0/24
```

### Advanced Options

```bash
# Scan specific ports only
python main.py 192.168.1.0/24 --ports 22,80,443,8080

# Save results to JSON file
python main.py 192.168.1.0/24 --output results.json

# Enable verbose output for detailed logs
python main.py 192.168.1.0/24 --verbose

# Combine multiple options
python main.py 192.168.1.0/24 --ports 22,80,443 --output scan_results.json --verbose

# Specify custom port range
python main.py 192.168.1.0/24 --ports 1:65535
```

### Command-Line Arguments

| Argument | Short | Description | Default |
|----------|-------|-------------|---------|
| `--ports` | `-p` | Comma-separated ports or range (e.g., 22,80,443 or 1:1024) | 1-1024 |
| `--output` | `-o` | Output file path (JSON format) | stdout |
| `--verbose` | `-v` | Enable verbose logging | False |
| `--timeout` | `-t` | Connection timeout in seconds | 5 |
| `--threads` | `-T` | Number of scanning threads | 4 |

---

## 🏗️ Architecture

```
ShibaCuddles/
├── README.md                 # Documentation
├── requirements.txt          # Python dependencies
├── main.py                   # Application entry point
├── src/
│   ├── __init__.py          # Package initialization
│   ├── device.py            # Device discovery module
│   ├── portscan.py          # Port scanning module
│   └── utils.py             # Utility functions
├── tests/
│   ├── __init__.py
│   ├── test_device.py       # Device discovery tests
│   └── test_portscan.py     # Port scanning tests
└── .gitignore               # Git ignore file
```

### Module Descriptions

- **device.py** - Handles ICMP-based device discovery on network subnets
- **portscan.py** - Implements TCP port scanning functionality
- **utils.py** - Common utilities including IP handling and result formatting
- **main.py** - CLI interface and orchestration logic

---

## ⚙️ Configuration

Configuration can be done via command-line arguments. For advanced configurations, edit the default settings in `src/utils.py`:

```python
DEFAULT_PORT_RANGE = (1, 1024)
DEFAULT_TIMEOUT = 5
DEFAULT_THREADS = 4
```

---

## 🧪 Testing

Run the test suite to ensure everything is working correctly:

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_device.py

# Run with verbose output
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ --cov=src
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository** on GitHub
2. **Create a feature branch** for your changes
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Write tests** for new functionality
4. **Commit your changes** with descriptive messages
   ```bash
   git commit -m "Add feature: description of changes"
   ```
5. **Push to your fork** and submit a **pull request**

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Write clear, descriptive commit messages
- Include unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors & Contributors

- **Lead Developer**: [thedarkonejesus](https://github.com/thedarkonejesus)
- **Contributors**: [View all contributors](https://github.com/thedarkonejesus/ShibaCuddles/graphs/contributors)

---

## 🐕 About the Name

*ShibaCuddles* combines the charm of Shiba Inu dogs with the friendly nature of this network scanning tool. Because every network deserves a cuddly, reliable scanner!

---

## ❓ FAQ

**Q: Is this tool for ethical purposes only?**  
A: Yes, this tool is designed for legitimate network administration and testing on networks you own or have permission to scan.

**Q: Can I scan the entire internet?**  
A: No, and you shouldn't. This tool is designed for local network scanning. Always get proper authorization before scanning any network.

**Q: How fast is the scanning?**  
A: Scanning speed depends on your network, the number of hosts, and thread count. Typical local subnets scan in seconds to minutes.

---

## 📞 Support

For issues, questions, or suggestions:
- Open an [issue](https://github.com/thedarkonejesus/ShibaCuddles/issues) on GitHub
- Check [existing issues](https://github.com/thedarkonejesus/ShibaCuddles/issues?q=is%3Aissue) for similar topics

---

**Last Updated**: June 2026  
**Status**: Active Development
