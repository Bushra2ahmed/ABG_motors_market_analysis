# DATA-ANLYSIS

## Iris Flower Species Classification

This repository includes a beginner-friendly machine learning example that uses
measurements of Iris flowers to classify each flower as one of three species:

- Setosa
- Versicolor
- Virginica

The example uses scikit-learn's built-in Iris dataset and trains a
`RandomForestClassifier` on sepal and petal measurements. It then evaluates the
model with held-out test data by printing accuracy, a classification report, and
a confusion matrix.

### Classification concepts shown

- **Features**: numeric inputs used for prediction, such as sepal length, sepal
  width, petal length, and petal width.
- **Labels/classes**: the target species the model learns to predict.
- **Training data**: examples used to teach the model patterns.
- **Test data**: examples kept separate to evaluate how well the model performs
  on unseen flowers.
- **Accuracy**: the percentage of test examples classified correctly.

### Setup

Install the required Python dependency:

```bash
pip install -r requirements.txt
```

### Run the model

```bash
python iris_classifier.py
```

The script will print the model accuracy, detailed per-species performance, a
confusion matrix, and an example prediction for a new Iris flower measurement.
