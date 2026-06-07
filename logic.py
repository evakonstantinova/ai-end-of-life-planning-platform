
# logic.py
from data import question_topics, feedback_thresholds
from feedback import feedback_recommendations

def calculate_scaled_scores(user_response):
    topic_scores = {}
    for topic, q_range in question_topics.items():
        scores = [user_response[f"Q{str(q).zfill(2)}"] for q in q_range]
        raw_mean = sum(scores) / len(scores)
        scaled_mean = round((raw_mean / 5) * 10, 2)
        topic_scores[topic] = scaled_mean
    return topic_scores

def generate_feedback(topic_scores):
    feedback = []
    for topic, scaled_mean in topic_scores.items():
        low, high = feedback_thresholds[topic]
        level = "low" if scaled_mean < low else "high" if scaled_mean > high else "similar"
        message = feedback_recommendations[topic][level]
        feedback.append(f"{topic}: {message}")
    return feedback
