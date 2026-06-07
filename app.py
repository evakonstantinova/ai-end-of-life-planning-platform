# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
# Set the path to the Firebase service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "firebase-app-key.json"
from google.cloud import firestore
from logic import calculate_scaled_scores, generate_feedback


# Define the Flask app
app = Flask(__name__)
CORS(app)

# Define an API route to fetch personalized feedback
@app.route("/get-feedback")
def get_feedback():
    try:
        # Extract user ID and response ID from query parameters
        uid = request.args.get("uid")
        rid = request.args.get("rid", "response1")
        # Validate input
        if not uid or not rid:
            return jsonify({"error": "UID not provided"}), 400
        
        # Initialize Firestore client
        db = firestore.Client()

        # Reference the user's specific quiz response
        doc_ref = db.collection("users").document(uid).collection("quizResponses").document(rid)
        doc = doc_ref.get()

        # Check if the document exists
        if not doc.exists:
            return jsonify({"error": "Response not found"}), 404
        
        # Convert Firestore document to dictionary
        full_response = doc.to_dict()
        # Extract Q01 to Q29 raw scores
        user_response = {f"Q{str(i).zfill(2)}": int(full_response[f"Q{str(i).zfill(2)}"]) for i in range(1, 30) if f"Q{str(i).zfill(2)}" in full_response}

        # Calculate scaled scores and generate personalized feedback
        scores = calculate_scaled_scores(user_response)
        feedback = generate_feedback(scores)
 
        # Return the feedback and scores as JSON
        return jsonify({
            "feedback": feedback,
            "scores": scores
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

#  Run the app
if __name__ == "__main__":
    app.run(debug=True)