import logging

def MyAwesomeJob(args):
    logging.info("This output will be streamed back to gaia and will be displayed in the pipeline logs.")
    # Just raise an exception to tell Gaia if a job failed.
    # raise Exception("Oh no, this job failed!")

def main():
    logging.basicConfig(level=logging.INFO)