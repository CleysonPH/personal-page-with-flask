from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from personal_page import app, db
from personal_page.models import User, Course
from personal_page.forms import LoginForm, CourseForm, UpdateUserForm


@app.route('/')
def home():
    data_user = User.query.all()[0]

    return render_template('home.html', data=data_user)


@app.route('/courses/')
def courses():
    courses = Course.query.all()

    return render_template('courses.html', courses=courses)


@app.route('/courses/add', methods=['GET', 'POST'])
@login_required
def add_course():
    form = CourseForm()
    if form.validate_on_submit():
        course = Course(
            title=form.title.data,
            image=form.image_link.data,
            description=form.description.data,
            certification_link=form.certification_link.data
        )

        db.session.add(course)
        db.session.commit()

        flash('Course added in the database')

        return redirect(url_for('add_course'))
    return render_template('add_course.html', form=form)


@app.route('/courses/edit/<int:id>')
@login_required
def edit_course(id):
    flash('To Implement')
    return redirect(url_for('courses'))


@app.route('/courses/delete/<int:id>')
@login_required
def delete_course(id):
    course = Course.query.get(id)
    db.session.delete(course)
    db.session.commit()

    flash('Course deleted with success!')

    return redirect(url_for('courses'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user.check_password(form.password.data) and user is not None:
            print(user)
            login_user(user)
            flash('Logged in Successfully!')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('home')

            return redirect(next)
    return render_template('login.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))


@app.route('/account/', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateUserForm()

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.image = form.image_link.data
        current_user.description = form.description.data
        db.session.commit()
        flash('User Account Updated!')

        return redirect('account')
    form.username.data = current_user.username
    form.email.data = current_user.email
    form.image_link.data = current_user.image
    form.description.data = current_user.description

    return render_template('account.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)