from dns import resolver

def dns_enum(url):
    record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']

    domain = url
    res = dict()

    for records in record_types:
        try:
            try:
                answer = resolver.resolve(domain, records)
            except:
                pass
            try:
                ar = []
                for server in answer:
                    ar.append(server.to_text())
                res[records] = ar
            except:
                return None
        except resolver.NoAnswer:
            pass
        except resolver.NXDOMAIN:
            return None

    return res

