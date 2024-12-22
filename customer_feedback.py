def feedback(ratings):
    if not ratings:
        return 0.0
    positive_feedback = sum(1 for rating in ratings if rating >= 4)
    return round((positive_feedback / len(ratings)) * 100, 2)


ratings = [5, 4, 3, 5, 2, 4, 1, 5]

feedback_percent = feedback(ratings)

print(f"Positive Feedback: {feedback_percent}%")
