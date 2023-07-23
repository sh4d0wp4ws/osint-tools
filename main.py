import argparse
from scripts.dns_enum import dns_enum
from scripts.get_domain_info import is_registered, whois_info

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--domain', required=True, help='Target domain name resolution')
parser.add_argument('-w', '--whois', action='store_true', help='Target domain name Info')
parser.add_argument('-o', '--output', default='output.txt', help='Output text file')

args = parser.parse_args()

target_domain = args.domain
whois_enabled = args.whois

if __name__ == '__main__':
    print("Please wait a moment!")
    dns_enum(target_domain)
    if whois_enabled:
        print(target_domain, "is registered" if is_registered(target_domain) else "is not registered")
        whois_info(target_domain)