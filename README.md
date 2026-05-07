# Course-Final-Project-Report

##Team Members
Sophia Doumazios, sdoumazi@stevens.edu (ID: 20015171),
Arlette Martinez Lima, amarti10@stevens.edu (ID: 20015104),
Ahmed Elshaar, aelshaar@stevens.edu (ID: 20011169)

## Project Description
This project analyzes chemical properties of wine samples and predicts wine classification using machine learning. The system uses a dataset of chemical attributes such as alcohol content, malic acid, and color intensity to train a classification model. Users can input new wine characteristics and receive a predicted class. The project also includes statistical summaries and data visualizations.

##Libraries Used
-pandas
-numpy
-matplotlib
-scikit-learn
-statistics
-pytest

##File and Module Structure

```text
Course-Final-Project-Report/
│
├── dataAnalysis.ipynb
├── README.md
│
├── data/
│   └── wine.csv
│
├── models/
│   ├── __init__.py
│   ├── wine_sample.py
│   └── wine_dataset.py
│
├── utils/
│   ├── __init__.py
│   ├── data_loader.py
│   └── visualization.py
│
└── tests/
    └── test_wine.py
```

## How to Run
Step 1. Install dependencies
pip install pandas numpy matplotlib scikit-learn pytest
Step 2. Download the project
Download the repository as a ZIP from GitHub
Extract the folder
Step 3. Open the project
Open the extracted folder in Visual Studio Code (or any Python IDE)
Step 4. Launch Jupyter Notebook
Run the following in terminal:
python -m notebook
(or: jupyter notebook if installed directly)
Step 5. Run the program
Open main.ipynb (recommended) or dataAnalysis.ipynb
Run all cells in order from top to bottom


## Contributions
Sophia Doumazios: Data analysis, notebook
Arlette Martinez Lima: Classes and data handling, notebook
Ahmed Elshaar: Visualization, testing notebook
