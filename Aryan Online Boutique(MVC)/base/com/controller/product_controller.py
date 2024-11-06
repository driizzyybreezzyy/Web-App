from flask import render_template, request, jsonify, redirect
from werkzeug.utils import secure_filename

from base import app
from base.com.dao.category_dao import CategoryDAO
from base.com.dao.product_dao import ProductDAO
from base.com.dao.subcategory_dao import SubCategoryDAO
from base.com.vo.product_vo import ProductVO
from base.com.vo.subcategory_vo import SubCategoryVO
import os


@app.route('/load_product')
def load_product():
    try:
        category_dao = CategoryDAO()
        category_vo_list = category_dao.view_category()
        return render_template('addProductCategory.html',
                               category_vo_list=category_vo_list)
    except Exception as ex:
        print("Something went Wrong", ex)
        return render_template('viewError.html', ex=ex)


@app.route('/ajax_subcategory_product')
def ajax_subcategory_product():
    subcategory_category_id = request.args.get('category_id')
    subcategory_vo = SubCategoryVO()
    subcategory_dao = SubCategoryDAO()
    subcategory_vo.subcategory_category_id = subcategory_category_id
    subcategory_vo_list = subcategory_dao.view_ajax_subcategory_product(
        subcategory_vo)
    response_message = [i.as_dict() for i in subcategory_vo_list]
    print("response_message={}".format(response_message))
    return jsonify(response_message)


@app.route('/add_product', methods=['POST'])
def add_product():
    product_category_id = request.form.get('category_id')
    print("product_category_id.........", product_category_id)

    product_subcategory_id = request.form.get('subcategory_id', 1)
    print("product_subcategory_id", product_subcategory_id)

    product_name = request.form.get('product_name')
    product_description = request.form.get('product_description')
    product_price = request.form.get('product_price')
    product_quantity = request.form.get('product_quantity')

    product_image = request.files.get('productImage')
    product_image_name = secure_filename(product_image.filename)

    product_image_path = 'base/static/images/'
    product_image_file = product_image_path + product_image_name
    product_image.save(product_image_file)

    product_vo = ProductVO()
    product_dao = ProductDAO()

    product_vo.product_category_id = product_category_id
    product_vo.product_subcategory_id = product_subcategory_id
    product_vo.product_name = product_name
    product_vo.product_description = product_description
    product_vo.product_price = product_price
    product_vo.product_quantity = product_quantity

    product_vo.product_image_name = product_image_name
    product_vo.product_image_path = product_image_path.replace("base",
                                                                    "/..")

    product_dao.insert_product(product_vo)
    return redirect('/view_product')


@app.route('/view_product')
def view_product():
    product_dao = ProductDAO()
    product_vo_list = product_dao.view_product()
    return render_template('viewProductCategory.html',product_vo_list=product_vo_list)


@app.route('/delete_product_category')
def delete_product_category():
    product_id = request.args.get('product_id')
    print('>>>>>>>product_id', product_id)
    product_dao = ProductDAO()
    product_vo = ProductVO()
    product_vo.product_id = product_id

    file = product_id
    location = 'base/static/images/'
    path = os.path.join(location, file)
    os.remove(path)
    print("file and path both are remove")
    product_dao.delete_product(product_vo)
    return redirect('/view_product')