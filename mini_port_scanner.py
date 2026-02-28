import socket

def scan_port(target_host, port_number, timeout_seconds=1):
    """
    Try to connect to a specific port on the target host.
    Returns True if the port is open, False otherwise.
    """
    try:
        # Create a new TCP socket
        scanner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner_socket.settimeout(timeout_seconds)

        # Attempt to connect — returns 0 if successful
        connection_result = scanner_socket.connect_ex((target_host, port_number))
        scanner_socket.close()

        return connection_result == 0  # 0 means port is open

    except socket.gaierror:
        print(f"Error: Could not resolve hostname '{target_host}'")
        return False
    except socket.error as error:
        print(f"Socket error: {error}")
        return False


def run_port_scanner():
    """
    Main function to take user input and scan a range of ports.
    """
    print("=" * 40)
    print("        Mini TCP Port Scanner")
    print("=" * 40)

    target_host  = input("Enter target IP or hostname: ").strip()
    start_port   = int(input("Enter start port: ").strip())
    end_port     = int(input("Enter end port:   ").strip())

    print(f"\nScanning {target_host} from port {start_port} to {end_port}...\n")

    open_ports = []

    for port_number in range(start_port, end_port + 1):
        if scan_port(target_host, port_number):
            print(f"  [OPEN]   Port {port_number}")
            open_ports.append(port_number)
        else:
            print(f"  [CLOSED] Port {port_number}")

    print("\n" + "=" * 40)
    print(f"Scan complete. {len(open_ports)} open port(s) found.")
    print("=" * 40)

if __name__ == "__main__":
    run_port_scanner()

