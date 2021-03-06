from app import db, models
import argparse
import os
import json


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def create_parser():
    parser = argparse.ArgumentParser(description='Json loader')
    parser.add_argument('path', help='Path to file with data')
    return parser


def create_new_advertisement(properties_list):
    new_advertisement = models.Advertisement()
    new_advertisement.identifier = properties_list['id']
    new_advertisement.premise_area = properties_list['premise_area']
    new_advertisement.rooms_number = properties_list['rooms_number']
    new_advertisement.construction_year = properties_list['construction_year']
    new_advertisement.address = properties_list['address']
    new_advertisement.has_balcony = properties_list['has_balcony']
    new_advertisement.living_area = properties_list['living_area']
    new_advertisement.oblast_district = properties_list['oblast_district']
    new_advertisement.price = properties_list['price']
    new_advertisement.description = properties_list['description']
    new_advertisement.under_construction = properties_list['under_construction']
    new_advertisement.settlement = properties_list['settlement']
    new_advertisement.active = True
    return new_advertisement

    
def update_advertisement_to_db(ads):
    if ads is None:
        return
    load_advertisement_to_db(ads)
    mark_notactive_advertisement(ads)


def load_advertisement_to_db(ads):
    for ad in ads:
        advertisement_query = db.session.query(models.Advertisement).filter(models.Advertisement.identifier == ad['identifier'])
        if advertisement_query.count() > 0:
            advertisement_query.update(ad)
        else:
            new_advertisement = create_new_advertisement(ad)
            db.session.add(new_advertisement)
    db.session.commit()


def mark_notactive_advertisement(ads):
    id_ads = [ad['identifier'] for ad in ads]
    advertisement_query = db.session.query(models.Advertisement)
    advertisement_query = advertisement_query.filter(models.Advertisement.identifier.notin_(id_ads))
    advertisement_query = advertisement_query.filter(models.Advertisement.active == True)
    for advertisement in advertisement_query.all():
        advertisement.active = False
    db.session.commit()


def main():
    parser = create_parser()
    args = parser.parse_args()
    ads = load_json_data(args.path)
    for ad in ads:
        ad['identifier'] = ad.pop('id')
    update_advertisement_to_db(ads)


if __name__ == '__main__':
    main()
    