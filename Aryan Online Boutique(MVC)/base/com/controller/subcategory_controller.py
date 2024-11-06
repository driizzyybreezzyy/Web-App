from flask import render_template, request, redirect

from base import app
from base.com.dao.category_dao import CategoryDAO
from base.com.dao.subcategory_dao import SubCategoryDAO
from base.com.vo.subcategory_vo import SubCategoryVO


@app.route('/load_subcategory')
def load_subcategory():
    category_dao = CategoryDAO()
    category_vo_list = category_dao.view_category()
    return render_template('addSubCategory.html',category_vo_list=category_vo_list)


@app.route('/add_subcategory', methods=['POST'])
def add_subcategory():
    subcategory_category_id = request.form.get('subcategory_category_id')
    subcategory_name = request.form.get('subcategory_name')
    subcategory_description = request.form.get('subcategory_description')
    subcategory_vo = SubCategoryVO()
    subcategory_dao = SubCategoryDAO()
    subcategory_vo.subcategory_name = subcategory_name
    subcategory_vo.subcategory_description = subcategory_description
    subcategory_vo.subcategory_category_id = subcategory_category_id
    subcategory_dao.insert_subcategory(subcategory_vo)
    return redirect('/view_subcategory')


@app.route('/view_subcategory')
def view_subcategory():
        subcategory_dao = SubCategoryDAO()
        subcategory_vo_list = subcategory_dao.view_subcategory()
        return render_template('viewSubCategory.html',subcategory_vo_list=subcategory_vo_list)


@app.route('/delete_subcategory')
def delete_subcategory():
    subcategory_id = request.args.get('subcategory_id')
    print('subcategory_id -- subcategory_delete', subcategory_id)
    subcategory_vo = SubCategoryVO()
    subcategory_vo.subcategory_id = subcategory_id
    subcategory_dao = SubCategoryDAO()
    subcategory_dao.delete_subcategory(subcategory_vo)
    return redirect('/view_subcategory')


@app.route('/edit_subcategory')
def edit_subcategory():
        subcategory_vo = SubCategoryVO()
        subcategory_dao = SubCategoryDAO()
        category_dao = CategoryDAO()
        subcategory_id = request.args.get('subcategory_id')
        subcategory_vo.subcategory_id = subcategory_id
        subcategory_vo_list = subcategory_dao.edit_subcategory(subcategory_vo)
        category_vo_list = category_dao.view_category()
        return render_template('editSubCategory.html',subcategory_vo_list=subcategory_vo_list,category_vo_list=category_vo_list)


@app.route('/update_subcategory')
def update_subcategory():
        subcategory_vo = SubCategoryVO()
        subcategory_dao = SubCategoryDAO()
        subcategory_id = request.args.get('subcategory_id')
        print("subcategory_id --->update subcategory", subcategory_id)
        subcategory_category_id = request.args.get('category_id')
        print("subcategory_category_id --->update subcategory",subcategory_category_id)
        subcategory_name = request.args.get('subcategory_name')
        subcategory_description = request.args.get('subcategory_description')
        subcategory_vo.subcategory_id = subcategory_id
        subcategory_vo.subcategory_name = subcategory_name
        subcategory_vo.subcategory_description = subcategory_description
        subcategory_vo.subcategory_category_id = subcategory_category_id
        subcategory_dao.update_subcategory(subcategory_vo)
        return redirect('/view_subcategory')