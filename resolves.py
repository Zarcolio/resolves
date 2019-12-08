#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys

for strInput in sys.stdin:
    strInput = strInput.strip()
    try:
        result = socket.gethostbyname_ex(strInput)
        #if result:
        sys.stdout.write(strInput + "\n")
    except socket.gaierror:
        sys.stdout.write("")