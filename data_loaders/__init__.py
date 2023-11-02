import pandas as pd


def load_offerings():
    return pd.read_csv("datasets/offerings.csv")


def load_reviews():
    return pd.read_csv("datasets/reviews.csv", nrows=1000)
