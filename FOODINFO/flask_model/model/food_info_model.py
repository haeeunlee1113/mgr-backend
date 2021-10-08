
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





