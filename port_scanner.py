import socket 
import pyfiglet
import time
start_time = round(time.time())
banner = pyfiglet.figlet_format("Port Scanner")
print(banner)
ip = input("Enter IP Address: ")
target = socket.gethostbyname(ip)
print(f"Scanning Target: {target}")
start_port = int(input("Enter Starting port: "))
end_port = int(input("Enter Ending port: "))
print(f"Start Time is {start_time}")
print("Scanning ports...\n")

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f" [+] GREAT. Port is {port} is OPEN...")
    else:
        print(f" [-] OOP'S Port is {port} is CLOSED...")
    s.close()
end_time = time.time()
print(f"End Time is {end_time}")
print(f"Total Time taken is{round(end_time - start_time)} seconds")