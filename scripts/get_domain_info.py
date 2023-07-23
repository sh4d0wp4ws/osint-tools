import whois

def is_registered(target_domain):
    try:
        w = whois.whois(target_domain)
    except Exception:
        return False
    else:
        return bool(w.domain_name)
    
def whois_info(target_domain):
    w = whois.whois(target_domain)
    print("Domain Registrar:", w.registrar)
    print("Domain WHOIS Server:", w.whois_server)
    print("Domain Creation Date:", w.creation_date)
    print("Domain Expiration Date:", w.expiration_date)