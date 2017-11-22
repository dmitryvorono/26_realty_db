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


def load_advertisement_to_db(ads):
    if ads is None:
        return
    for ad in ads:
        advertisement_query = db.session.query(models.Advertisement).filter(models.Advertisement.id == ad['id'])
        if advertisement_query.count() > 0:
            advertisement_query.update(ad)
        else:
            new_advertisement = models.Advertisement(**ad)
            db.session.add(new_advertisement)
    db.session.commit()


def main():
    parser = create_parser()
    args = parser.parse_args()
    ads = load_json_data(args.path)
    load_advertisement_to_db(ads)


if __name__ == '__main__':
    main()
    