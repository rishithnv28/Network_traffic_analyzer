# Network Traffic Analyzer

## Observation
This application captures and analyzes network packets to detect suspicious activity or potential threats using Python and Pyshark.

Check out the Python installation:

Verify that Python is added to the PATH by enabling python --version in the Command Prompt.

Run the setup script:

Run setup.bat to install dependencies and set up the environment.

Run the test:

In order to create the test scenarios and run_tests.py to make sure everything works as expected.

## features
- **Packet Capture**: Captures network packets for analysis.
- **Suspicious Activity Detection**: Detects possible SYN scans and DNS tunnels.
- **Automatic Analysis**: Analyzes captured packets for immediate threat detection.
- **IP Blocking**: Manages a database of tagged IPs to prevent malicious traffic.

## lay
1. Cloning a repository:
    ```Sh
    git clone https://github.com/yourname/web_traffic_analyzer.git
    cd web_drive_analyzer
    ```

2. Run `setup.bat` with the necessary installation:
    ```Sh
    system.bat
    ```

### Survey
### Packet capture
Use the following command to capture packets from the specified network interface.
```Sh
python packet_capture.py <connection> <packet_count> <save_method>

interface: The network interface from which to receive packets (e.g., 'eth0', 'Wi-Fi').

packet_count: Number of packets to capture.

save_path: Path to save captured packets.

Packet analysis

Run the analyzer and examine the captured packets for suspicious activity:

python analyzer.py <file_get>

capture_file: The path to the captured packet file.

For example

Capture the packets:

python packet_capture.py 1 100 captured_packets.pcap

Examine the packets:

Python Analyzer.py captured_packets.pcap

Examine

Run run_tests.py to create the basic test environment:

python run_tests .