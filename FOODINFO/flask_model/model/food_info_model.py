
# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class FoodInfo(db.Model):
    """ 
    table name : foodInfo 
    table info
    : 기본정보 불러오기
    """
    __tablename__ = 'food_info'

    prd_lst_report_no = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=False)

    prd_lst_nm = db.Column(db.String(20, 'utf8mb4_general_ci'))
    businessitem_nm = db.Column(db.String(20, 'utf8mb4_general_ci'))
    product_gb = db.Column(db.String(20, 'utf8mb4_general_ci'))
    company = db.Column(db.String(20, 'utf8mb4_general_ci'))

    def __init__(self, prd_lst_nm, businessitem_nm, product_gb,company):
        self.prd_lst_nm = prd_lst_nm
        self.businessitem_nm = businessitem_nm
        self.product_gb = product_gb
        self.company = company



class HazardousIngredient(db.Model):
    """
    table name : foodInfo
    table info
    : 기본정보 불러오기
    """
    __tablename__ = 'hazardous_ingredient'

    seq_hazardous_ingredient = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)

    seq_ingredient = db.Column(db.Integer())
    ingredient_name = db.Column(db.String(20, 'utf8mb4_general_ci'))
    seq_segment = db.Column(db.Integer())
    explanation = db.Column(db.String(1000, 'utf8mb4_general_ci'))
    news_link = db.Column(db.String(1000, 'utf8mb4_general_ci'))

    def __init__(self, seq_ingredient, ingredient_name, seq_segment,explanation,news_link):
        self.seq_ingredient = seq_ingredient
        self.ingredient_name = ingredient_name
        self.seq_segment = seq_segment
        self.explanation = explanation
        self.news_link = news_link

class Segment(db.Model):
    """
    table name : foodInfo
    table info
    : 기본정보 불러오기
    """
    __tablename__ = 'segment'

    seq_segment = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)

    segment_name = db.Column(db.String(20, 'utf8mb4_general_ci'))


    def __init__(self, segment_name):
        self.segment_name = segment_name



