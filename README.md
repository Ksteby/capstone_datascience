# 🚀 SpaceX Falcon 9 First Stage Landing Prediction: End-to-End ML Pipeline

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-green.svg)
![Plotly/Dash](https://img.shields.io/badge/Plotly_Dash-Interactive%20Dataviz-informational.svg)

## Executive Summary
SpaceX has revolutionized the aerospace industry by making space travel affordable. Their secret? Reusing the first stage of the Falcon 9 rocket, which saves upwards of $100 million per launch. 

The objective of this project is to build an end-to-end Data Science and Machine Learning pipeline to **predict whether the Falcon 9 first stage will successfully land**. This predictive model could be used by a competing aerospace company to accurately estimate launch costs and bid against SpaceX.

##  Project Architecture & MLOps Pipeline
This repository is structured as a sequential Data Engineering and Machine Learning pipeline, demonstrating a clear, industrial approach to data:

### Phase 1: Data Collection
* `01_data_collection_api.ipynb`: Extracting raw launch data via the official SpaceX REST API.
* `02_data_collection_webscraping.ipynb`: Scraping historical Falcon 9 launch records from Wikipedia using BeautifulSoup to enrich the dataset.

### Phase 2: Data Wrangling & Exploratory Data Analysis (EDA)
* `03_data_wrangling.ipynb`: Cleaning the raw data, handling missing values, and formatting features.
* `04_eda_sql_analysis.ipynb`: Performing deep data exploration using SQL queries to extract key launch metrics.
* `05_eda_dataviz_matplotlib.ipynb`: Visualizing payload mass, launch sites, and flight trajectories using Matplotlib and Seaborn to identify correlations.
* `06_launch_site_location_folium.ipynb`: Interactive geospatial analysis of launch sites and landing success clusters using Folium maps.

### Phase 3: Machine Learning Modeling
* `07_machine_learning_prediction.ipynb`: 
  * Feature engineering and data standardization.
  * Training multiple classification algorithms (Logistic Regression, SVM, Decision Tree, KNN).
  * Hyperparameter tuning using `GridSearchCV`.
  * Model evaluation using accuracy scores and confusion matrices.

### Phase 4: Interactive Dashboarding
* `Spacex_dash_app.py`: A fully interactive web application built with Plotly Dash, allowing end-users to dynamically filter launch success rates by site and payload mass.

##  Key Results & Model Performance
After extensive hyperparameter tuning, both the **Support Vector Machine (SVM)** and **Logistic Regression** models achieved the highest performance on the test data:
* **Accuracy:** 89%
* The models successfully identified that lower payload masses and specific launch sites (like CCAFS SLC 40) heavily influence the probability of a successful booster landing.

##  How to Run the Project
1. Clone the repository: `git clone https://github.com/Ksteby/capstone_datascience.git`
2. Install the required dependencies: `pip install pandas numpy scikit-learn dash plotly folium beautifulsoup4`
3. To view the analysis, open the Jupyter Notebooks in sequence (from 01 to 07).
4. To launch the interactive dashboard, run: `python Spacex_dash_app.py`

---

##  About the Author
**Steby KEMO TOUOHOU**
*Software Engineer | Data Scientist | ML Engineer*

 *Currently pursuing a Master in Data Science for Societal Challenges at Université de Tours (France).*
** Open to Work:** I am actively seeking a 12-month work-study program (*Alternance*) in Data Science, Machine Learning, or MLOps starting in September 2026. 

* 🔗 **LinkedIn:** [https://www.linkedin.com/in/steby-kemo-a7161b33a/] 
*  **Email:** kemosteby@gmail.com
