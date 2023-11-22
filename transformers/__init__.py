import pandas as pd
import ast


def transform_data(**kwargs):
    addresses = get_addresses(**kwargs)
    authors = get_authors(**kwargs)
    locations = get_locations(authors)
    hotels = get_hotels(**kwargs, addresses=addresses)
    ratings = get_ratings(**kwargs)
    reviews = get_reviews(**kwargs, ratings=ratings, authors=authors)

    # Merge authors and locations
    merged_authors = pd.merge(authors, locations, left_on='location',
                              right_on='name', how='left')
    authors = merged_authors.rename(
        columns={'id_x': 'id', 'id_y': 'location_id'})
    authors = authors.loc[:, ['id', 'username', 'num_reviews', 'location_id']]
    return {
        'location': locations,
        'address': addresses,
        'hotel': hotels,
        'author': authors,
        'ratings': ratings,
        'review': reviews
    }


def get_addresses(**kwargs):
    offerings = kwargs["offerings"]
    addresses = offerings.loc[:, ['address']]
    addresses['address'] = addresses['address'].apply(ast.literal_eval)
    addresses = pd.json_normalize(addresses['address'])
    addresses['street_address'] = addresses.loc[:, ['street-address']]
    addresses['postal_code'] = addresses.loc[:, ['postal-code']]
    addresses = addresses.drop(columns=['street-address', 'postal-code'])
    addresses['id'] = addresses.index
    return addresses


def get_hotels(addresses, **kwargs):
    offerings = kwargs["offerings"]
    hotel_offerings = offerings[offerings['type'] == 'hotel']
    hotels = hotel_offerings.loc[:, ['id', 'hotel_class', 'name', 'url']]
    hotels['address_id'] = addresses.index
    hotels = hotels.rename(columns={'hotel_class': 'stars'})
    return hotels


def get_authors(**kwargs):
    reviews = kwargs["reviews"]
    authors = reviews.loc[:, ['author']]
    authors['author'] = authors['author'].apply(ast.literal_eval)
    authors = pd.json_normalize(authors['author'])
    authors = authors.loc[:, ['username', 'num_reviews', 'id', 'location']]
    authors = authors.drop_duplicates(subset=['id'])
    authors['num_reviews'] = authors['num_reviews'].fillna(0)
    authors = authors.dropna(subset=['id'])
    return authors


def get_ratings(**kwargs):
    reviews = kwargs["reviews"]
    ratings = reviews.loc[:, ['ratings']]
    ratings['ratings'] = ratings['ratings'].apply(ast.literal_eval)
    ratings = pd.json_normalize(ratings['ratings'])
    ratings['id'] = ratings.index
    ratings = ratings.loc[:, ['id', 'service', 'cleanliness',
                              'overall', 'value', 'location', 'sleep_quality', 'rooms']]

    return ratings


def get_locations(authors):
    author_locations = authors['location'].unique()
    locations = pd.DataFrame({
        'name': author_locations
    })
    locations['id'] = locations.index

    return locations


def get_reviews(ratings, authors, **kwargs):
    reviews = kwargs["reviews"]
    reviews = reviews.loc[:, ['id', 'text', 'date', 'offering_id']]
    reviews = reviews.rename(columns={'offering_id': 'hotel_id'})

    reviews['rating_id'] = ratings['id']
    reviews['author_id'] = authors['id']

    return reviews
