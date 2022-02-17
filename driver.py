from joblib import load

review = input("Enter the review to be examined:")


def make_predictions(review):
    text = [review]
    clf = load('finalized_model.joblib')
    predictions = clf.predict(text)
    if predictions == 0:
        print("Negative review")
    elif predictions == 1:
        print("Neutral review")
    else:
        print("Positive review")


make_predictions(review)
