import dns.resolver
from dns.resolver import Resolver, NoAnswer, LifetimeTimeout

def dns_enum(target_domain):
    displayed_records = {}
    results = []
    record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
    resolver = dns.resolver.Resolver()
    for record_type in record_types:
        try:
            answers = resolver.resolve(target_domain, record_type)
        except NoAnswer:
            continue

        for rdata in answers:
            results.append(f"{record_type} records for {target_domain}\n {rdata}")
            process_string = "\n".join(results)
            # if record_type not in displayed_records:
            #     results.append(f"{record_type} records for {target_domain}\n {rdata}")
            #     displayed_records[record_type] = True

    print(process_string)
    # for i in results:
    #     print(i)