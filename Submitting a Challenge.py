@app.route('/submit_flag/<int:challenge_id>', methods=['POST'])
@login_required
def submit_flag(challenge_id):
    challenge = Challenge.query.get_or_404(challenge_id)
    user_flag = request.form.get('flag')

    if user_flag == challenge.flag:
        submission = Submission(user_id=current_user.id, challenge_id=challenge_id)
        db.session.add(submission)
        db.session.commit()
        flash('Flag submitted successfully!', 'success')
    else:
        flash('Incorrect flag. Try again.', 'danger')

    return redirect(url_for('dashboard'))

## Update 22/08/24
