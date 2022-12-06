# PREVIOUS INSTALLATIONS
>   pip install protobuf==3.20.*

# USAGE
> protoc -I . --python_out=. structure.proto
> ./protocolbuffers_example.py

# CASUAL EXECUTION
Data before packing:
 randomvalue: 24
timestamp: 1670330752.0
 

Data after packing:
 b'\x10\x18\x1ds\x1e\xc7N' 

Data after unpacking:
 randomvalue: 24
timestamp: 1670330752.0
 




Data before packing:
 identifier: 1
randomvalue: 35
timestamp: 1670330752.0
 

Data after packing:
 b'\x08\x01\x10#\x1ds\x1e\xc7N' 

Data after unpacking:
 identifier: 1
randomvalue: 35
timestamp: 1670330752.0
 




Data before packing:
 identifier: 2
randomvalue: 24
timestamp: 1670330752.0
 

Data after packing:
 b'\x08\x02\x10\x18\x1ds\x1e\xc7N' 

Data after unpacking:
 identifier: 2
randomvalue: 24
timestamp: 1670330752.0

...