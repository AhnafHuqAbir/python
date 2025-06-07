import socket

def port_scanner(target, start_port, end_port):
    print(f"🎯 Target: {target}")
    print(f"🔍 Scanning from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout set to 1 second
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"yes Port {port} is OPEN")
        else:
            print(f"oh no this:-(n Port {port} is CLOSED")

        sock.close()

# User input
target_ip = input("🌐 Enter the IP address to scan (e.g., 127.0.0.1): ")
start = int(input("🔢 Start port number: "))
end = int(input("🔢 End port number: "))

port_scanner(target_ip, start, end)
