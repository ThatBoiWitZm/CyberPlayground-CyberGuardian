from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user

@app.route('/dashboard')
@login_required
def dashboard():
    challenges = Challenge.query.all()
    submissions = Submission.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', challenges=challenges, submissions=submissions)

## Update 22/08/24
