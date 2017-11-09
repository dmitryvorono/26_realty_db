import config
from flask import Flask, render_template
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db_create import Advertisement
from flask import request
from datetime import datetime
from sqlalchemy import or_


app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')


@app.route('/')
def ads_list():
    city = request.args.get('oblast_district', default='', type=str)
    is_new_building_only = request.args.get('new_building',
                                            default=False, type=bool)
    min_price = request.args.get('min_price', default=0, type=int)
    max_price = request.args.get('max_price', default=0, type=int)
    engine = create_engine(config.sqlalchemy_database_url, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    ads = session.query(Advertisement)
    if city:
        ads = ads.filter(Advertisement.settlement == city)
    if min_price:
        ads = ads.filter(Advertisement.price >= min_price)
    if max_price:
        ads = ads.filter(Advertisement.price <= max_price)
    if is_new_building_only:
        now = datetime.now()
        ads = ads.filter(or_(Advertisement.under_construction.is_(True),
                             Advertisement.construction_year >= now.year - 3))
    return render_template('ads_list.html', ads=ads)


if __name__ == "__main__":
    app.run()
