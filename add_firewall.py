import subprocess


def read_ips_from_file(filename):
    with open(filename, 'r') as file:
        ips = file.read().splitlines()
    return ips


def add_ips_to_firewall(rule_name, ips):
    for i in range(0, len(ips), 20):
        ip_chunk = ips[i:i + 20]
        ip_list = ",".join(ip_chunk)

        command = f"netsh advfirewall firewall add rule name=\"{rule_name}\" dir=out action=block protocol=any remoteip={ip_list}"
        subprocess.run(command, shell=True)
        print(f"Added IP range {ip_list} to Windows firewall outbound rule {rule_name}.")


if __name__ == "__main__":
    rule_name = input("Enter the rule name: ")
    filename = input("Enter the IP addresses file name: ")

    ips = read_ips_from_file(filename)

    if ips:
        add_ips_to_firewall(rule_name, ips)
    else:
        print("No IP addresses found in the file.")
