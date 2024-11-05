import json

def generate_report(scan_results, filename='vulnerability_report.json'):
    """
    Generate a JSON report of the scan results.

    :param scan_results: Dictionary containing scan results
    :param filename: Output file name
    """
    with open(filename, 'w') as file:
        json.dump(scan_results, file, indent=4)
    print(f"Report generated and saved as {filename}")

if __name__ == "__main__":
    sample_data = {
        '192.168.1.1': {
            'ports': {22: {'service': 'ssh', 'version': 'OpenSSH 7.4'}, 80: {'service': 'http', 'version': 'Apache 2.4.6'}},
            'vulnerabilities': ['CVE-2020-12345', 'CVE-2021-6789']
        }
    }
    generate_report(sample_data)
