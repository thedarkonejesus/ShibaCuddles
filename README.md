# ShibaCuddles - Network Scanner

A lightweight network scanning tool written in Python. ShibaCuddles performs device discovery and port scanning to identify active hosts and open ports on a network.

## Features

- ICMP-based device discovery
- TCP port scanning (1-1024 by default)
- Configurable port ranges
- JSON output support
- Verbose mode for detailed output
- Test suite with unit tests

## Installation

```bash
git clone https://github.com/yourusername/shibacuddles.git
cd shibacuddles
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python main.py 192.168.1.0/24
```

Advanced options:
```bash
# Scan specific ports
python main.py 192.168.1.0/24 --ports 22,80,443

# Save results to JSON
python main.py 192.168.1.0/24 --output results.json

# Verbose mode
python main.py 192.168.1.0/24 --verbose
```

## Architecture

```
shibacuddles/
├── README.md          # This file
├── requirements.txt   # Dependencies
├── main.py            # Entry point
├── src/               # Source code
│   ├── __init__.py    # Package init
│   ├── device.py      # Device discovery
│   ├── portscan.py    # Port scanning
│   └── utils.py       # Utilities
└── tests/             # Unit tests
    ├── test_device.py
    └── test_portscan.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Write tests for new functionality
4. Submit a pull request

## License

MIT License - see LICENSE file for details

## Authors

- Your Name (author)
- [Contributors](https://github.com/yourusername/shibacuddles/graphs/contributors)

---

*ShibaCuddles - Because every network needs a cuddly scanner!*
