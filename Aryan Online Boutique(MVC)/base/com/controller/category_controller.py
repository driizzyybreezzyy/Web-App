from flask import render_template, redirect, request

from base import app
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.category_vo import CategoryVO


@app.route('/')
def load_home_page():
    return render_template('home.html')


@app.route('/load_category')
def load_category():
    return render_template('addCategory.html')


@app.route('/insert_category', methods=['POST'])
def insert_category():
    try:
        category_name = request.form.get('category_name')
        category_description = request.form.get('category_description')

        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_vo.category_name = category_name
        category_vo.category_description = category_description
        category_dao.insert_category(category_vo)
        return redirect('/view_category')

    except Exception as ex:
        print("Something want to wrong", ex)
        return render_template('viewError.html', ex=ex)


@app.route('/view_category')
def view_category():
    try:
        category_dao = CategoryDAO()
        category_vo_list = category_dao.view_category()
        return render_template('viewCategory.html',
                               category_vo_list=category_vo_list)
    except Exception as ex:
        print("Something want to wrong", ex)
        return render_template('viewError.html', ex=ex)


@app.route('/delete_category')
def delete_category():
    category_id = request.args.get('category_id')
    category_vo = CategoryVO()
    category_vo.category_id = category_id
    category_dao = CategoryDAO()
    category_dao.delete_category(category_vo)
    return redirect('/view_category')


@app.route('/edit_category')
def edit_category():
    try:
        category_vo = CategoryVO()
        category_dao = CategoryDAO()
        category_id = request.args.get('category_id')
        category_vo.category_id = category_id
        category_vo_list = category_dao.edit_category(category_vo)
        return render_template('editCategory.html',
                               category_vo_list=category_vo_list)
    except Exception as ex:
        print("Something went to wrong", ex)
        return render_template('viewError.html', ex=ex)


@app.route('/update_category')
def update_category():
    try:
        category_id = request.args.get('category_id')
        category_name = request.args.get('category_name')
        category_description = request.args.get('category_description')

        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_vo.category_id = category_id
        category_vo.category_name = category_name
        category_vo.category_description = category_description

        category_dao.update_category(category_vo)
        return redirect('/view_category')
    except Exception as ex:
        print("Something went to wrong", ex)
        return render_template('viewError.html', ex=ex)
