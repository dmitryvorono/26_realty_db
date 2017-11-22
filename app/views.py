from app import app, db, models
from flask import render_template
from flask import request
from datetime import datetime
from sqlalchemy import or_


@app.route('/')
def ads_list():
    city = request.args.get('oblast_district', default='', type=str)
    is_new_building_only = request.args.get('new_building',
                                            default=False, type=bool)
    min_price = request.args.get('min_price', default=0, type=int)
    max_price = request.args.get('max_price', default=0, type=int)
    ads = db.session.query(models.Advertisement)
    if city:
        ads = ads.filter(models.Advertisement.settlement == city)
    if min_price:
        ads = ads.filter(models.Advertisement.price >= min_price)
    if max_price:
        ads = ads.filter(models.Advertisement.price <= max_price)
    if is_new_building_only:
        now = datetime.now()
        ads = ads.filter(or_(models.Advertisement.under_construction.is_(True),
                             models.Advertisement.construction_year >= now.year - 3))
    return render_template('ads_list.html', ads=ads)
