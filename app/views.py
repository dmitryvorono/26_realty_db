from app import app, db, models
from flask import render_template
from flask import request
from datetime import datetime
from sqlalchemy import or_
from config import ads_per_page
from config import count_years_new_settlement


@app.route('/', methods=['GET', 'POST'], defaults={'page': 1})
@app.route('/<int:page>', methods=['GET', 'POST'])
def ads_list(page):
    city = request.args.get('oblast_district', default='', type=str)
    is_new_building_only = request.args.get('new_building',
                                            default=False, type=bool)
    min_price = request.args.get('min_price', default=0, type=int)
    max_price = request.args.get('max_price', default=0, type=int)
    ads = db.session.query(models.Advertisement)
    request_args = {}
    if city:
        ads = ads.filter(models.Advertisement.settlement == city)
        request_args['oblast_district'] = city
    if min_price:
        ads = ads.filter(models.Advertisement.price >= min_price)
        request_args['min_price'] = min_price
    if max_price:
        ads = ads.filter(models.Advertisement.price <= max_price)
        request_args['max_price'] = max_price
    if is_new_building_only:
        now = datetime.now()
        ads = ads.filter(or_(models.Advertisement.under_construction.is_(True),
                             models.Advertisement.construction_year >= now.year - count_years_new_settlement))
        request_args['new_building'] = is_new_building_only
    paginate_ads = ads.paginate(page, ads_per_page, False)
    return render_template('ads_list.html',
                           ads=paginate_ads.items,
                           pagination=paginate_ads,
                           request_args=request_args)
