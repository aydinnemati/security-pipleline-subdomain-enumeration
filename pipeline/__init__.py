from gaiasdk import sdk
import logging
import time

# def CreateUser(args):
#     logging.info("CreateUser has been started!")
#     time.sleep(5)
#     logging.info("CreateUser has been finished!")

def sub_domains_enumeration(args):
    logging.info(args)


def main():
    logging.basicConfig(level=logging.INFO)
    # variable = sdk.job(name, description, function, [dependencies, ...])
    # migratedb = sdk.Job("DB Migration", "Imports newest test data dump and migrates to newest version.", MigrateDB, ["Create DB User"])
    sub_domains_enumeration_call = sdk.Job("MY TEST JOB NAME IS SUNDOMAINS ENUMERATION", "desciriptions are useless", sub_domains_enumeration("gooooooooooooooooooog.go"))
    sdk.serve([sub_domains_enumeration_call])
