import socket

def nslookup(url):
    try:
        ip_addresses = socket.getaddrinfo(url, None, socket.AF_UNSPEC, socket.SOCK_DGRAM)
        ipv4_addresses = []
        ipv6_addresses = []
        for address in ip_addresses:
            if address[0] == socket.AF_INET:
                ipv4_addresses.append(address[4][0])
            elif address[0] == socket.AF_INET6:
                ipv6_addresses.append(address[4][0])
        # print(f"{url} has the following IPv4 addresses: {ipv4_addresses}")
        # print(f"{url} has the following IPv6 addresses: {ipv6_addresses}")
        res = dict()
        res['ipv4'] = ipv4_addresses
        res['ipv6'] = ipv6_addresses
        return res
    except socket.gaierror:
        return None
