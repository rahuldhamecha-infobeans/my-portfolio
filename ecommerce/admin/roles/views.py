from ecommerce import app
from ecommerce.database import db
from flask import Blueprint,render_template,redirect,flash,url_for
from flask_login import login_required
from ecommerce.admin.roles.forms import RoleForm
from ecommerce.database.models.Role import Role

roles_blueprint = Blueprint('roles',__name__)
@roles_blueprint.route('/')
@login_required
def index():
	roles = Role.query.all()
	return render_template('admin/roles/index.html',**locals())


@roles_blueprint.route('/create',methods=['GET','POST'])
@login_required
def create():
	form = RoleForm()
	if form.validate_on_submit():
		role = Role(name=form.name.data)

		db.session.add(role)
		db.session.commit()
		flash('Roles Successfully Created.','success')
		return redirect(url_for('roles.index'))

	return render_template('admin/roles/create.html',form=form)


@roles_blueprint.route('/update/<int:id>',methods=['GET','POST'])
@login_required
def update(id):
	role = Role.query.get(id)
	form = RoleForm(role_id=id)
	if form.validate_on_submit():
		role = Role.query.get(form.role_id.data)
		if role:
			role.name = form.name.data
			db.session.commit()
			flash('Roles Successfully Updated.','success')
			return redirect(url_for('roles.index'))

	return render_template('admin/roles/create.html',form=form,role=role)


@roles_blueprint.route('/delete/<int:id>',methods=['GET'])
@login_required
def delete(id):
	role = Role.query.get(id)
	if role:
		db.session.delete(role)
		db.session.commit()
		flash('Roles Successfully Delete.','success')
		return redirect(url_for('roles.index'))

	flash('Role No Found.', 'error')
	return redirect(url_for('roles.index'))



app.register_blueprint(roles_blueprint,url_prefix='/admin/roles')