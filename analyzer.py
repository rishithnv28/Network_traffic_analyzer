import pyshark
from utils import suspicious_packet

def analyze_packets(capture_file):
    try:
        capture = pyshark.FileCapture(capture_file)
        results = []
        for packet in capture:
            result = suspicious_packet(packet)
            if result:
                results.append(result)
        return results
    except Exception as e:
        print(f"Error analyzing packets: {e}")
        return []

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Network Traffic Analyzer")
    parser.add_argument("capture_file", type=str, help="Path to the captured packet file")

    args = parser.parse_args()
    results = analyze_packets(args.capture_file)

    if results:
        print("Suspicious Activities Detected:")
        for result in results:
            print(result)
    else:
        print("No suspicious activities found.")
