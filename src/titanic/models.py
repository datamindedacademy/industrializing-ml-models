import numpy as np
from sklearn.base import BaseEstimator
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import PrecisionRecallDisplay, balanced_accuracy_score


def fit_random_forest(
    features: np.ndarray, target: np.ndarray, *, plot_roc: bool = False
) -> tuple[RandomForestClassifier, float]:
    classifier = RandomForestClassifier(n_estimators=100)
    classifier = classifier.fit(features, target)

    predicted = classifier.predict(features)
    accuracy = balanced_accuracy_score(target, predicted)

    if plot_roc:
        plot_classifier_roc_curve(classifier, features, target)

    return classifier, accuracy


def plot_classifier_roc_curve(
    classifier: BaseEstimator, features: np.ndarray, target: np.ndarray
) -> None:
    display = PrecisionRecallDisplay.from_estimator(
        classifier, features, target, name="RandomForest"
    )
    _ = display.ax_.set_title("Precision-Recall curve")
