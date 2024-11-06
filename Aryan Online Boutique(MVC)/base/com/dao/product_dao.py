from base import db
from base.com.vo.category_vo import CategoryVO
from base.com.vo.subcategory_vo import SubCategoryVO
from base.com.vo.product_vo import ProductVO

class ProductDAO:

    def insert_product(self, product_vo):
        db.session.add(product_vo)
        db.session.commit()

    def view_product(self):
        product_vo_list = db.session.query(CategoryVO,SubCategoryVO,ProductVO)\
            .filter(CategoryVO.category_id == ProductVO.product_category_id)\
            .filter(SubCategoryVO.subcategory_id == ProductVO.product_subcategory_id)\
            .all()
        return product_vo_list


    def delete_product(self,product_vo):
        product_vo_list = ProductVO.query.get(product_vo.product_id)
        db.session.delete(product_vo_list)
        db.session.commit()

    def get_product_by_id(self,product_id):
        return ProductVO.query.get(product_id)