from gaiasdk import sdk
import logging
import time

def CreateUser(args):
    logging.info("CreateUser has been started!")
    time.sleep(5)
    logging.info("CreateUser has been finished!")

def MigrateDB(args):
    logging.info("MigrateDB has been started!")
    time.sleep(5)
    logging.info("MigrateDB has been finished!")

def CreateNamespace(args):
    logging.info("CreateNamespace has been started!")
    time.sleep(5)
    logging.info("CreateNamespace has been finished!")

def CreateDeployment(args):
    logging.info("CreateDeployment has been started!")
    time.sleep(5)
    logging.info("CreateDeployment has been finished!")

def CreateService(args):
    logging.info("CreateService has been started!")
    time.sleep(5)
    logging.info("CreateService has been finished!")

def CreateIngress(args):
    logging.info("CreateIngress has been started!")
    time.sleep(5)
    logging.info("CreateIngress has been finished!")

def Cleanup(args):
    logging.info("Cleanup has been started!")
    time.sleep(5)
    logging.info("Cleanup has been finished!")

def Subdomainenumeretaion(args):
    logging.error(args)


def main():
    logging.basicConfig(level=logging.INFO)
    # variable = sdk.job(name, description, function, [dependencies, ...])
    # migratedb = sdk.Job("DB Migration", "Imports newest test data dump and migrates to newest version.", MigrateDB, ["Create DB User"])
    Subdomainenumeretaioncall = sdk.Job("testingggggggggggggs...........", Subdomainenumeretaion("gooooooooooooooooooog.go"))
    sdk.serve([Subdomainenumeretaioncall])
