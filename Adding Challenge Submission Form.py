from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired

# Form for submitting challenges
class ChallengeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    points = IntegerField('Points', validators=[DataRequired()])
    flag = StringField('Flag', validators=[DataRequired()])
    submit = SubmitField('Submit Challenge')

@app.route('/submit_challenge', methods=['GET', 'POST'])
@login_required
def submit_challenge():
    form = ChallengeForm()

    if form.validate_on_submit():
        challenge = Challenge(
            title=form.title.data,
            description=form.description.data,
            points=form.points.data,
            flag=form.flag.data
        )
        db.session.add(challenge)
        db.session.commit()
        flash('Challenge submitted successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('submit_challenge.html', form=form)

## Update 22/08/24
