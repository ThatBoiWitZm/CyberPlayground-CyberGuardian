def calculate_score(user_id):
    user_submissions = Submission.query.filter_by(user_id=user_id).all()
    score = 0

    for submission in user_submissions:
        score += submission.challenge.points

    return score
