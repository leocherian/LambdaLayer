import pandas as pd

def lambdaHandler(event, context):
    print("Pandas version: ",pd.__version__)