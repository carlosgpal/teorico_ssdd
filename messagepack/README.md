# PREVIOUS INSTALLATIONS
>   pip install msgpack

# USAGE
> ./msgpack_example.py

# CASUAL EXECUTION
Data before packing:
 {'identifier': 0, 'randomvalue': 37, 'timestamp': 1670328851.37362} 

Data after packing:
 b'\x83\xaaidentifier\x00\xabrandomvalue%\xa9timestamp\xcbA\xd8\xe3\xcc\x84\xd7\xe9d' 

Data after unpacking:
 {'identifier': 0, 'randomvalue': 37, 'timestamp': 1670328851.37362} 




Data before packing:
 {'identifier': 1, 'randomvalue': 40, 'timestamp': 1670328854.3775797} 

Data after packing:
 b'\x83\xaaidentifier\x01\xabrandomvalue(\xa9timestamp\xcbA\xd8\xe3\xcc\x85\x98*D' 

Data after unpacking:
 {'identifier': 1, 'randomvalue': 40, 'timestamp': 1670328854.3775797} 




Data before packing:
 {'identifier': 2, 'randomvalue': 21, 'timestamp': 1670328857.3815832} 

Data after packing:
 b'\x83\xaaidentifier\x02\xabrandomvalue\x15\xa9timestamp\xcbA\xd8\xe3\xcc\x86Xk\xdc' 

Data after unpacking:
 {'identifier': 2, 'randomvalue': 21, 'timestamp': 1670328857.3815832} 
 
 ...