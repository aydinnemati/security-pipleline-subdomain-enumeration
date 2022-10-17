from gaiasdk import sdk
import logging
import time
import subprocess

# pwd = "/data/tmp/python/subs"
target_url = "aasaam.com"

def sub_domains_enumeration(args):
    puut = subprocess.getoutput("pwd")
    f = open("/home/a/gaia/resaults/AAs-puutingout.txt", "a")
    f.write(puut)
    f.close()
    logging.info(puut)
    logging.info(target_url)


def main():
    logging.basicConfig(level=logging.INFO)
    # variable = sdk.job(name, description, function, [dependencies, ...])
    sub_domains_enumeration_call = sdk.Job("MY TEST JOB NAME IS SUNDOMAINS ENUMERATION", "desciriptions are useless", sub_domains_enumeration)
    sdk.serve([sub_domains_enumeration_call])



