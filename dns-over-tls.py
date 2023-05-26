#!/usr/bin/env python

"""
dnspython3==1.12.0
mock==1.3.0
pbr==1.8.1
six==1.10.0
"""

import dns.message
import dns.query
import mock
import ssl
import socket


q = dns.message.Message()

orig_socket = socket.socket
orig_connect = dns.query._connect

(_, destination, _) = dns.query._destination_and_source(None, '185.60.217.53', 443, None, 0)


def our_socket(family, type, proto):
    s = orig_socket(family, type, proto)
    orig_connect(s, destination)
    return ssl.wrap_socket(s)


def our_connect(s, destination):
    pass

with mock.patch('socket.socket') as socket, mock.patch('dns.query._connect') as connect:
    socket.configure_mock(side_effect=our_socket)
    connect.configure_mock(side_effect=our_connect)
    r = dns.query.tcp(q, 'ruangguru.com', port=443)

print(r.to_text())