<!-- manual -->

## Instructions

Jill is developing a client/server program. Her server script launches without a problem, but she receives the following error message when she launches the client’s script:

```python
Traceback (most recent call last):
  File "/Users/jill/pythonfiles/client.py", line 15, in <module>
    server.connect(ADDRESS) # Connect it to a host
ConnectionRefusedError: [Errno 61] Connection refused
```

Here are the code segments in her server and client scripts that are responsible for setting up the connection:

```python
"""
File: server.py
"""
from socket import *
from codecs import decode
HOST = "localhost"
PORT = 6000
ADDRESS = (HOST, PORT)
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
"""
File: client.py
"""
from socket import *
from codecs import decode
HOST = "localhost"
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
server = socket(AF_INET, SOCK_STREAM) # Create a socket
server.connect(ADDRESS) # Connect it to a host
```

Determine why the error occurs in Jill’s program and correct it.

## Your Tasks
