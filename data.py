
# data.py

# Group questions into knowledge topics
question_topics = {
    "Talking Support": list(range(1, 5)),
    "Hands-On Support": list(range(5, 9)),
    "Experience": list(range(9, 14)),
    "Practical Knowledge": list(range(14, 21)),
    "Community Support 1": list(range(21, 26)),
    "Community Support 2": list(range(26, 30)),
    "Community (Overall)": list(range(21, 30)),        
    "Death Literacy Index (Overall)": list(range(1, 30))  
}

# Thresholds for scaled mean comparison per topic
feedback_thresholds = {
    "Talking Support": (4.24, 6.68),
    "Hands-On Support": (3.35, 5.89),
    "Experience": (4.75, 7.05),
    "Practical Knowledge": (2.50, 5.08),
    "Community Support 1": (2.91, 5.39),
    "Community Support 2": (3.88, 6.24),
    "Community (Overall)": (3.50, 5.70),
    "Death Literacy Index (Overall)": (3.86, 5.80)
}
