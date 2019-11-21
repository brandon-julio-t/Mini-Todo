from wtforms import Form, StringField, SubmitField, validators


class TodoForm(Form):
    todo_content = StringField(
        label='TODO',
        validators=[
            validators.InputRequired(),
            validators.DataRequired(
                message='TODO must be filled.')])
    submit = SubmitField(label='Submit')
