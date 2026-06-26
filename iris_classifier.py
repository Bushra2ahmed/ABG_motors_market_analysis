"""Train and evaluate an Iris flower species classifier.

This script demonstrates basic supervised classification with scikit-learn:
1. Load the built-in Iris dataset.
2. Split measurements into training and test data.
3. Train a machine learning model.
4. Evaluate accuracy and per-class performance.
5. Predict the species for a new sample measurement.
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


def main() -> None:
    """Run the complete Iris classification workflow."""
    # Load Iris measurements and species labels from scikit-learn.
    iris = load_iris()
    measurements = iris.data
    species = iris.target

    # Split data so the model is evaluated on flowers it did not see in training.
    x_train, x_test, y_train, y_test = train_test_split(
        measurements,
        species,
        test_size=0.2,
        random_state=42,
        stratify=species,
    )

    # Train a classifier. Random forests work well for small tabular datasets.
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)

    # Evaluate the trained model on held-out test data.
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)

    print("Iris Species Classification")
    print("===========================")
    print(f"Feature names: {', '.join(iris.feature_names)}")
    print(f"Species names: {', '.join(iris.target_names)}")
    print(f"Training samples: {len(x_train)}")
    print(f"Test samples: {len(x_test)}")
    print(f"Accuracy: {accuracy:.2%}\n")

    print("Classification report:")
    print(classification_report(y_test, predictions, target_names=iris.target_names))

    print("Confusion matrix:")
    print(confusion_matrix(y_test, predictions))

    # Example prediction for a new flower measurement:
    # [sepal length, sepal width, petal length, petal width]
    new_flower = [[5.1, 3.5, 1.4, 0.2]]
    predicted_class = model.predict(new_flower)[0]
    predicted_species = iris.target_names[predicted_class]
    print(f"\nNew flower measurements: {new_flower[0]}")
    print(f"Predicted species: {predicted_species}")


if __name__ == "__main__":
    main()
