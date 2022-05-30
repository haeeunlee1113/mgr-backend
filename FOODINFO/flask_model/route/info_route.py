import sys

from flask import Blueprint, jsonify
from flask import request
from sqlalchemy import engine, create_engine

from FOODINFO.flask_model.model import food_info_model as food_info
from FOODINFO.flask_model.model.food_info_model import HazardousIngredient, Segment
from sqlalchemy.orm import sessionmaker

info_route = Blueprint('info_route',__name__)
engine = create_engine(
    '**',
    echo=True
)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

#이름만 불러오는 api 입니다.
@info_route.route('/select/food-list',methods=['GET'])
def select_data():
    select_data = food_info.FoodInfo.query.all()
    print(select_data)
    if len(select_data) == 0: 
        return "data does not exist" 
    else:
        food_list=[]
        for food in select_data:
            data = dict(prdLstReportNo = food.prd_lst_report_no, prdLstNm = food.prd_lst_nm,businessItemNm=food.businessitem_nm,productGb=food.product_gb,company=food.company )
            food_list.append(data)
    return jsonify(food_list)



@info_route.route('/select/food-segment',methods=['GET'])
def select_segment():
    ingredient = request.args.get('ingredient', type=str, default='').replace("\n","")

    segments = session.query(HazardousIngredient,Segment).\
            filter(HazardousIngredient.seq_segment == Segment.seq_segment).\
            filter(food_info.HazardousIngredient.ingredient_name.like(ingredient))\
            .all()
    print(segments)

    if len(segments) == 0:
        return "data does not exist"
    else:
        segment_list=[]
        for segment in segments:
            data = dict(seq_segment = segment[0].seq_segment , ingredient_name = segment[0].ingredient_name, explanation = segment[0].explanation, news_link = segment[0].news_link, segment_name = segment[1].segment_name)
            segment_list.append(data)
    return jsonify(segment_list)

'''
@info_route.route('/insert',methods=['POST']) 
def insert_data(): 
    packet = request.get_json() 
    try: 
        data = food_info.FoodInfo(name = packet.get('name'), 
                              info = packet.get('info'), 
                              ingredient = packet.get('ingredient')
        
        select_data = food_info.FoodInfo.query.filter_by(name=packet.get('name')).all() 
        
        if len(select_info) > 0: 
            return "data already exists" 
        food_info.db.session.add(data) 
        food_info.db.session.commit() 
        food_info.db.session.remove() 
        return "success" 
    except Exception as e: 
        return "fail"
    
@info_route.route('/update/<target>',methods=['POST']) 
def update_data(target): 
    select_info = food_info.FoodInfo.query.filter_by(name=target).all() 
    if len(select_info) == 0: 
        return "data does not exist" 
    else: 
        name = food_info.FoodInfo.query.filter_by(name=target).first() 
        food_info.db.session.commit() 
        food_info.db.session.remove() 
        return "updated" 
    
'''

    
    


