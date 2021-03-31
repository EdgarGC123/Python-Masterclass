from urllib.parse import urlparse


def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return 'we got an error boiiis (get domain name)'

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return 'we got an error boiiis (get subdomain)'