import argparse
import pyshark

def capture_packets(interface, packet_count, save_path):
    try:
        capture = pyshark.LiveCapture(interface=interface)
        capture.sniff(packet_count=packet_count)
        capture.dump(save_path)
        print(f"Captured {len(capture)} packets.")
    except Exception as e:
        print(f"Error capturing packets: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Packet Capture")
    parser.add_argument("interface", type=str, help="Network interface to capture packets from")
    parser.add_argument("packet_count", type=int, help="Number of packets to capture")
    parser.add_argument("save_path", type=str, help="Path to save captured packets")

    args = parser.parse_args()
    capture_packets(args.interface, args.packet_count, args.save_path)
