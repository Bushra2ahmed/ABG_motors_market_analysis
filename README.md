# 🚗 ABG Motors Market Entry Analysis

## 📌 Overview

This project analyzes customer purchase behavior to support **ABG Motors' market entry strategy**. A Logistic Regression model is trained using customer data from the Japanese market and then applied to Indian customer data to identify potential buyers. The project combines machine learning, business analytics, and data visualization to generate actionable insights for strategic decision-making.

---

## 🎯 Business Problem

ABG Motors plans to expand into the Indian automobile market. Before entering a new market, the company needs to identify customers who are most likely to purchase a vehicle.

This project answers questions such as:

* Which customer characteristics influence vehicle purchases?
* Can purchasing behavior learned from one market help predict another?
* Which Indian customers are potential buyers?
* How can machine learning support market expansion decisions?

---

## 📂 Datasets

The project uses two datasets:

* **Japanese Customer Dataset** – Used to train and evaluate the prediction model.
* **Indian Customer Dataset** – Used to predict potential customers for the Indian market.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook
* Power BI

---

## 📊 Machine Learning Workflow

1. Load Japanese and Indian datasets.
2. Clean and preprocess customer data.
3. Encode categorical variables.
4. Scale numerical features.
5. Train a Logistic Regression model.
6. Evaluate model performance using:

   * Classification Report
   * Confusion Matrix
7. Interpret model coefficients for business insights.
8. Predict purchasing potential for Indian customers.
9. Export prediction results for Power BI dashboard visualization.

---

## 📈 Features Used

* Customer Age
* Gender
* Annual Income
* Vehicle Age

**Target Variable**

* Purchase Decision

---

## 📊 Model Evaluation

The project evaluates the model using:

* Classification Report
* Precision
* Recall
* F1-Score
* Confusion Matrix

These metrics help measure how effectively the model predicts customer purchasing behavior.

---

## 📊 Business Insights

The analysis helps identify:

* High-value customer segments
* Factors influencing purchasing decisions
* Customer groups with higher purchase probability
* Opportunities for market expansion
* Data-driven recommendations for ABG Motors

---

## 📁 Repository Structure

```text
ABG_motors_market_analysis/
│
├── ABG_Market_Entry_Analysis_Updated.ipynb
├── market.pbix
├── JPN_Data.xlsx
|── IN_Data.xlsx
├── images/
├── README.md

```

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/Bushra2ahmed/ABG_motors_market_analysis.git
```

2. Install dependencies.

```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
```

3. Place the datasets in the project directory.

4. Open the notebook:

```
ABG_Market_Entry_Analysis_Updated.ipynb
```

5. Run all cells to reproduce the analysis and predictions.

---

## 🚀 Future Improvements

* Compare multiple machine learning algorithms.
* Perform hyperparameter tuning.
* Develop an interactive prediction application.
* Integrate real-time customer data.
* Deploy the model using Streamlit or Flask.

---



---

## ⭐ Acknowledgement

This project was developed for academic and learning purposes to demonstrate the practical application of machine learning and business analytics in solving real-world market entry problems.

