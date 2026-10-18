import socket
import time
import os
from datetime import datetime

# 1. TARGET INFRASTRUCTURE LOGISTICS
TARGET_HOST = "127.0.0.1"  # Localhost for testing (Change to AWS RDS Endpoint later)
TARGET_PORT = 5432         # The PostgreSQL Gate
LOG_FILE = "network_telemetry.log"

class Style:
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def audit_network_gate(host, port):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 2. INITIALIZE THE SOCKET PROBE
    probe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    probe.settimeout(2.0)  # 2-second SLA timeout limit
    
    try:
        start_time = time.time()
        # Attempt to knock on port 5432
        probe.connect((host, port))
        latency = (time.time() - start_time) * 1000
        
        log_entry = f"[{timestamp}] STATUS: ONLINE | Target: {host}:{port} | Latency: {latency:.2f}ms\n"
        print(Style.GREEN + log_entry.strip() + Style.RESET)
        return log_entry
        
        
    except socket.timeout:
        log_entry = f"[{timestamp}] STATUS: CRITICAL | Target: {host}:{port} | Error: Connection Timeout (SLA Breached)\n"
        print(Style.RED + log_entry.strip() + Style.RESET)
        return log_entry
        
    except socket.error as e:
        log_entry = f"[{timestamp}] STATUS: OFFLINE | Target: {host}:{port} | Error: Security Group/Firewall Blocked\n"
        print(Style.RED + log_entry.strip() + Style.RESET)
        return log_entry
        
    finally:
        probe.close()

def write_to_telemetry_log(filepath, data):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(data)

if __name__ == "__main__":
    print(Style.CYAN + f"=== INITIALIZING AUTOMATED PORT {TARGET_PORT} MONITORING INTERFACES ===" + Style.RESET)
    print(f"Logging active telemetry to: {os.path.abspath(LOG_FILE)}\n")
    
    # 3. CONTINUOUS LIVE MONITORING LOOP
    try:
        while True:
            log_payload = audit_network_gate(TARGET_HOST, TARGET_PORT)
            write_to_telemetry_log(LOG_FILE, log_payload)
            time.time()
            time.sleep(5)  # Rest the cycle for 5 seconds (Tachograph Compliance)
    except KeyboardInterrupt:
        print(Style.CYAN + "\n[ALERT] Monitoring loop manually terminated by Operator. Console out." + Style.RESET)
