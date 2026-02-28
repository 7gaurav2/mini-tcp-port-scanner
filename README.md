# mini-tcp-port-scanner
# Mini TCP Port Scanner (Python)

## Description
This is a basic TCP connect port scanner built using Python's socket module.
The program scans a user-defined range of ports on a target host and identifies open ports.

This project was created to understand:
- TCP connections
- Port scanning fundamentals
- Python socket programming
- Exception handling in network applications

---

## How It Works

- Uses IPv4 (AF_INET)
- Uses TCP protocol (SOCK_STREAM)
- Attempts connection using connect_ex()
- If return value is 0 → Port is OPEN
- If return value is non-zero → Port is CLOSED

The scanner performs a full TCP connection attempt for each port.

---

## Features

- Custom target input (IP or hostname)
- Custom port range selection
- Timeout control
- Exception handling
- Summary of open ports

---

## Concepts Used

- TCP three-way handshake
- TCP connect scanning
- Socket programming in Python
- Basic network error handling

---

## Example

Input:
Target: 127.0.0.1  
Start Port: 1  
End Port: 100  

Output:
[OPEN] Port 80
Scan complete. 1 open port(s) found.

---

## Limitations

- Sequential scanning (not multithreaded)
- Basic TCP connect scan (not SYN scan)
- No advanced service detection

---

## Disclaimer

This tool is created for educational purposes only.
Use only on systems you own or have permission to test.
Unauthorized scanning may be illegal.

---

## Future Improvements

- Multithreading for faster scanning
- Banner grabbing
- Command-line argument support
- Logging results to file
