import os
import subprocess
import tempfile

def run_tests():
    print("Running tests...")

    capture_file = tempfile.NamedTemporaryFile(delete=False).name + '.pcap'

    try:
        subprocess.run(["python", "packet_capture.py", "Wi-Fi", "10", capture_file])
        process = subprocess.Popen(["python", "analyzer.py", capture_file], stdout=subprocess.PIPE)
        output, _ = process.communicate()

        with open("test_results.txt", "w") as results_file:
            results_file.write(output.decode())
    except Exception as e:
        print(f"Error during testing: {e}")
    finally:
        if os.path.exists(capture_file):
            os.remove(capture_file)

    print("Tests completed successfully")

if __name__ == "__main__":
    run_tests()
