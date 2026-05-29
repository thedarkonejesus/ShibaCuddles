#!/usr/bin/env python3
"""
Unit tests for port scanning functionality.
"""

import unittest
from unittest.mock import patch, MagicMock
import socket
from src.portscan import scan_ports, is_port_open

class TestIsPortOpen(unittest.TestCase):
    @patch('socket.socket')
    def test_port_open(self, mock_socket_class):
        mock_socket = MagicMock()
        mock_socket.connect_ex.return_value = 0  # Connection successful
        mock_socket_class.return_value = mock_socket
        
        result = is_port_open("192.168.1.1", 80)
        
        self.assertTrue(result)
        mock_socket.connect_ex.assert_called_once_with(("192.168.1.1", 80))
        
    @patch('socket.socket')
    def test_port_closed(self, mock_socket_class):
        mock_socket = MagicMock()
        mock_socket.connect_ex.return_value = 1  # Connection failed
        mock_socket_class.return_value = mock_socket
        
        result = is_port_open("192.168.1.1", 80)
        
        self.assertFalse(result)
        
    @patch('socket.socket')
    def test_port_exception(self, mock_socket_class):
        mock_socket = MagicMock()
        mock_socket.connect_ex.side_effect = socket.error
        mock_socket_class.return_value = mock_socket
        
        result = is_port_open("192.168.1.1", 80)
        
        self.assertFalse(result)

class TestScanPorts(unittest.TestCase):
    @patch('src.portscan.is_port_open')
    def test_scan_ports_success(self, mock_is_port_open):
        mock_is_port_open.side_effect = [True, False, True, False, True]
        
        ports = [22, 80, 443, 3306, 8080]
        result = scan_ports("192.168.1.1", ports)
        
        self.assertEqual(result, [22, 443, 8080])
        
    @patch('src.portscan.is_port_open')
    def test_scan_ports_empty(self, mock_is_port_open):
        mock_is_port_open.return_value = False
        
        result = scan_ports("192.168.1.1", [22, 80, 443])
        
        self.assertEqual(result, [])
        
    @patch('src.portscan.is_port_open')
    def test_scan_ports_all_open(self, mock_is_port_open):
        mock_is_port_open.return_value = True
        
        result = scan_ports("192.168.1.1", [22, 80, 443])
        
        self.assertEqual(result, [22, 80, 443])

if __name__ == '__main__':
    unittest.main()