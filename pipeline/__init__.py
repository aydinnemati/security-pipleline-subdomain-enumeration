from gaiasdk import sdk
import logging
import time
import os


target_url = "aasaam.com"

def sub_domains_enumeration(args):
    logging.info("output is ---------------->>>>", os.system("pwd"))
    logging.info(target_url)


def main():
    logging.basicConfig(level=logging.INFO)
    # variable = sdk.job(name, description, function, [dependencies, ...])
    sub_domains_enumeration_call = sdk.Job("MY TEST JOB NAME IS SUNDOMAINS ENUMERATION", "desciriptions are useless", sub_domains_enumeration)
    sdk.serve([sub_domains_enumeration_call])
