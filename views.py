from flask import render_template, request, flash, redirect, url_for

from app import app, db
from models.Todo import Todo
from models.TodoForm import TodoForm

# ------
# Create
# ------


@app.route('/create', methods=['get', 'post'])
def create():
    form = TodoForm(request.form)

    if request.method.lower() == 'post' and form.validate():
        todo = Todo(todo_content=form.todo_content.data)
        db.session.add(todo)
        db.session.commit()

        app.logger.info(f'Saved: {todo}')

        flash('TODO added.')
        return redirect(url_for('index'))

    return render_template('create_and_update.html',
                           action='create', form=form)


# ----
# Read
# ----


@app.route('/', methods=['get', 'post'])
def index():
    return render_template('index.html', todos=Todo.query.all())


# ------
# Update
# ------

@app.route('/<int:todo_id>/edit', methods=['get', 'post'])
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    form = TodoForm(request.form, todo)

    if request.method.lower() == 'post' and form.validate():
        app.logger.info(f'Before: {todo}')

        form.populate_obj(todo)
        db.session.commit()

        app.logger.info(f'After: {todo}')

        flash('Update success.')
        return redirect(url_for('index'))

    return render_template('create_and_update.html',
                           action=f'{todo_id}/edit', form=form)


# ------
# Delete
# ------


@app.route('/<int:todo_id>/delete', methods=['post'])
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()

    app.logger.info(f'Deleted: {todo}')

    flash('Delete success.')
    return redirect(url_for('index'))
