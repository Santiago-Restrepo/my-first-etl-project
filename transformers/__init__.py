import pandas as pd
import pdb
import ast


def transform_data(**kwargs):

    # Initial data
    offerings = kwargs["offerings"]
    reviews = kwargs["reviews"]

    # Transforming
    addresses = offerings.loc[:, ['address']]
    addresses['address'] = addresses['address'].apply(ast.literal_eval)
    addresses = pd.json_normalize(addresses['address'])
    addresses['street_address'] = addresses.loc[:, ['street-address']]
    addresses.drop('street-address', axis=1, inplace=True)

    pdb.set_trace()
    print("transforming data")
