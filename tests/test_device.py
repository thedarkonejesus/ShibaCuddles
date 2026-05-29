#!/usr/bin/env python3
"""
Unit tests for device discovery functionality.
"""

import unittest
from unittest.mock import patch, MagicMock
from scapy.all import IP, ICMP, sr1
from src.device import Device, discover_devices

class TestDevice(unittest.TestCase):
    def setUp(self):
        self.device = Device("192.168.1.1")

    def test_device_creation(self):
        self.assertEqual(self.device.ip, "192.168.1.1")
        self.assertEqual(str(self.device), "Device(192.168.1.1)")

class TestDiscoverDevices(unittest.TestCase):
    @patch('src.device.sr1')
    def test_discover_devices_single_response(self, mock_sr1):
        mock_response = MagicMock()
        mock_response.summary.return_value = "ICMP reply"
        mock_sr1.return_value = mock_response
        
        network = "192.168.1.0/30"  # Only 4 IPs
        devices = discover_devices(network)
        
        self.assertEqual(len(devices), 4)
        for device in devices:
            self.assertIsInstance(device, Device)
            self.assertTrue(device.ip.startswith("192.168.1."))

    @patch('src.device.sr1')
    def test_discover_devices_no_responses(self, mock_sr1):
        mock_sr1.return_value = None
        
        network = "192.168.1.0/30"
        devices = discover_devices(network)
        
        self.assertEqual(len(devices), 0)

    @patch('src.device.sr1')
    def test_discover_devices_mixed_responses(self, mock_sr1):
        mock_responses = [MagicMock(), None, MagicMock(), None]
        for i, resp in enumerate(mock_responses):
            if resp:
                resp.summary.return_value = "ICMP reply"
            mock_sr1.side_effect = lambda *args, **kwargs: mock_responses[i]
        
        network = "192.168.1.0/30"
        devices = discover_devices(network)
        
        self.assertEqual(len(devices), 2)
        self.assertTrue(all(d.ip in ["192.168.1.1", "192.168.1.3"] 
                          for d in devices))

if __name__ == '__main__':
    unittest.main()