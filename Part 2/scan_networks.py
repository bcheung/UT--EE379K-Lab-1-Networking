#!/usr/bin/env python3
import subprocess

def main():
    # r - read file
    with open('zmap_output.txt', 'r', newline=None) as file:
        with open("failed_ip.txt", "a") as failed_ip:
            with open("successful_ip.txt", "a") as successful_ip:
                ip = file.readline()

                num_ip = 0
                num_successful = 0
                num_failed = 0
                while ip:
                    ip = ip.rstrip()
                    print(ip)
                    num_ip += 1
                    out = subprocess.run(['./whois_scan.sh', ip], stdout=subprocess.PIPE)
                    result = out.stdout.decode("utf-8").rstrip()
                    print(result)
                    if (result == "failed"):
                        failed_ip.write("{}\n".format(ip))
                        num_failed += 1
                    else:
                        successful_ip.write("{}\n".format(ip))
                        num_successful += 1
                    ip = file.readline()
                    print()
                print("Total: {}, Successful: {}, Failed: {}".format(num_ip, num_successful, num_failed))


if __name__ == "__main__":
    main()