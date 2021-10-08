import sys

from flask import Blueprint, jsonify

from FOODINFO.flask_model.model import food_info_model as food_info

info_route = Blueprint('info_route',__name__) 


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


#@info_route.route('/select_all',methods=['GET'])
# def select_all_data(): 
#     select_user = my_user.MyUser.query.all() 
#     if len(select_user) == 0: 
#         return "user does not exists" 
#     else: 
#         user_list = [] 
#         for user in select_user: 
#             data = dict(id = user.id , name = user.user_name, created_at = user.created_at, udpated_at = user.udpated_at) 
#             user_list.append(data) 
#             
#    return jsonify(user_list) 

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

    
    


