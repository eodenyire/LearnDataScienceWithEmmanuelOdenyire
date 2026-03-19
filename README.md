Learn Data Science with Emmanuel Odenyire
====================================================

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

Welcome to the **Data Science Learning Journey** repository! This repository is designed to accompany our year-long exploration into the field of data science, providing a structured and comprehensive path for learners at all levels.

> 🚀 **New here?** Check out the [Quick Start Guide](QUICKSTART.md) to get started in 5 minutes!

Repository Overview
-------------------

This repository contains Jupyter Notebooks, datasets, and resources corresponding to each topic covered in our learning journey. The content is organized chronologically, with each month focusing on a specific theme in data science.

Table of Contents
-----------------

*   [Introduction](https://chatgpt.com/c/67be200c-b580-8005-b216-5b0f3f421173#introduction)
    
*   [Repository Structure](https://chatgpt.com/c/67be200c-b580-8005-b216-5b0f3f421173#repository-structure)
    
*   [Getting Started](https://chatgpt.com/c/67be200c-b580-8005-b216-5b0f3f421173#getting-started)
    
*   [Monthly Themes](https://chatgpt.com/c/67be200c-b580-8005-b216-5b0f3f421173#monthly-themes)
    
*   [Contributing](https://chatgpt.com/c/67be200c-b580-8005-b216-5b0f3f421173#contributing)
    
*   [License](https://chatgpt.com/c/67be200c-b580-8005-b216-5b0f3f421173#license)
    

Introduction
------------

Data science is a multidisciplinary field that combines statistics, computer science, and domain expertise to extract meaningful insights from data. This journey aims to equip you with the necessary skills and knowledge to excel in this dynamic field.

Repository Structure
--------------------

The repository is organized into directories for each month, reflecting the thematic focus of that period. Each directory contains:

*   **Jupyter Notebooks**: Interactive notebooks with explanations, code examples, and exercises.
    
*   **Datasets**: Relevant datasets used in the notebooks and exercises.
    
*   **Resources**: Additional reading materials, links, and references.
    

Example structure:

```
├── Month_01_Python_Basics
│   ├── README.md
│   ├── Day_01_Introduction_to_Data_Science_and_Python.ipynb
│   ├── Day_02_Setting_Up_Your_Python_Environment.ipynb
│   ├── Day_03_Variables_and_Data_Types.ipynb
│   ├── Day_04_Operators_and_Expressions.ipynb
│   └── Day_05_Control_Flow.ipynb
├── Month_02_Data_Analysis_with_Pandas_and_NumPy
│   ├── README.md
│   ├── Week_1_Introduction_to_NumPy.ipynb
│   ├── Week_2_Advanced_NumPy.ipynb
│   ├── Week_3_Pandas_Series_and_DataFrames.ipynb
│   ├── Week_4_Reading_and_Writing_Data.ipynb
│   └── Week_5_Data_Cleaning_and_Transformation.ipynb
│   ... (5 notebooks per month, Months 1–12)
├── datasets
│   ├── README.md
│   └── sample_sales.csv
├── resources
│   └── README.md
├── requirements.txt
├── verify_setup.py
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

Getting Started
---------------

To get the most out of this repository:

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/eodenyire/LearnDataScienceWithEmmanuelOdenyire.git
    cd LearnDataScienceWithEmmanuelOdenyire
    ```
    
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    
3.  **Verify Your Setup**:
    ```bash
    python verify_setup.py
    ```
    
4.  **Launch Jupyter Notebook**:
    ```bash
    jupyter notebook
    ```
    
5.  **Start Learning**: Navigate to `Month_01_Python_Basics` and open the first notebook!
    

Monthly Themes
--------------

Our learning journey is divided into the following monthly themes:

1.  **Month 1: Python Basics for Data Science**
    
    *   Introduction to Python programming
        
    *   Variables, data types, and operators
        
    *   Control flow, loops, and functions
        
    *   Data structures: lists, tuples, dictionaries, and sets
        
    *   String manipulation and error handling
        
2.  **Month 2: Data Analysis with Pandas & NumPy**
    
    *   Introduction to NumPy arrays and operations
        
    *   Advanced NumPy features
        
    *   Pandas Series and DataFrames
        
    *   Reading and writing data with Pandas
        
    *   Data cleaning and transformation techniques
        
3.  **Month 3: Data Visualization**
    
    *   Introduction to Matplotlib for basic plotting
        
    *   Advanced plotting techniques with Matplotlib
        
    *   Creating statistical plots with Seaborn
        
    *   Interactive visualizations with Plotly
        
    *   Combining Pandas and visualization libraries for data insights
        
4.  **Month 4: Statistics & Probability for Data Science**
    
    *   Descriptive statistics and data distributions
        
    *   Probability theory and distributions
        
    *   Inferential statistics and hypothesis testing
        
    *   Regression analysis
        
    *   Statistical modeling techniques
        
5.  **Month 5: Data Cleaning & Preprocessing Techniques**
    
    *   Handling missing data and duplicates
        
    *   Data type conversions and feature scaling
        
    *   Encoding categorical variables
        
    *   Handling imbalanced datasets
        
    *   Data augmentation techniques
        
6.  **Month 6: Exploratory Data Analysis (EDA) with Real-World Datasets**
    
    *   Understanding the EDA process
        
    *   Univariate and bivariate analysis
        
    *   Identifying patterns and anomalies
        
    *   Correlation analysis
        
    *   Case studies with real-world datasets
        
7.  **Month 7: Introduction to Machine Learning (Supervised & Unsupervised)**
    
    *   Overview of machine learning concepts
        
    *   Supervised learning algorithms: regression and classification
        
    *   Unsupervised learning algorithms: clustering and dimensionality reduction
        
    *   Model evaluation metrics
        
    *   Implementing machine learning models with scikit-learn
        
8.  **Month 8: Advanced Machine Learning Techniques & Feature Engineering**
    
    *   Ensemble methods: bagging and boosting
        
    *   Hyperparameter tuning and model optimization
        
    *   Feature selection and extraction
        
    *   Handling overfitting and underfitting
        
    *   Introduction to model interpretability
        
9.  **Month 9: Deep Learning with TensorFlow & PyTorch**
    
    *   Introduction to neural networks
        
    *   Building deep learning models with TensorFlow
        
    *   Implementing models with PyTorch
        
    *   Convolutional Neural Networks (CNNs)
        
    *   Recurrent Neural Networks (RNNs) and sequence modeling
        
10.  **Month 10: Natural Language Processing (NLP)**
    
    *   Text preprocessing techniques
        
    *   Tokenization and embedding methods
        
    *   Sentiment analysis and text classification
        
    *   Sequence-to-sequence models
        
    *   Introduction to transformers and BERT
        
11.  **Month 11: Time Series Analysis & Forecasting**
    
    *   Understanding time series data
        
    *   Time series decomposition
        
    *   Forecasting models: ARIMA, SARIMA, and Prophet
        
    *   Evaluating forecast accuracy
        
    *   Case studies in time series forecasting
        
12.  **Month 12: End-to-End Projects & Model Deployment**
    
    *   Building end-to-end data science projects
        
    *   Model deployment strategies
        
    *   Introduction to Flask, FastAPI, and Streamlit for web deployment
        
    *   Monitoring and maintaining deployed models
        
    *   Introduction to MLOps concepts
        

Contributing
------------

We welcome contributions to enhance this learning journey. If you have suggestions, improvements, or additional resources, please:

1.  Fork the repository.
    
2.  Create a new branch for your feature or improvement.
    
3.  Commit your changes with clear messages.
    
4.  Submit a pull request detailing your changes.
    

License
-------

This repository is licensed under the MIT License. You are free to use, modify, and distribute the content, provided proper attribution is given.

Embark on this journey with us and transform your data science skills. Happy learning!

---

## Phase-Based Curriculum Structure

The bootcamp is organized into **7 phases** spanning 12 months:

| Phase | Name | Duration | Focus | Directory |
|-------|------|----------|-------|-----------|
| Phase 0 | Foundations | 2 weeks | Setup, Git, Colab | [Phase_0_Foundations/](Phase_0_Foundations/) |
| Phase 1 | Python & Math | 2 months | Python, NumPy, Pandas, Statistics | [Phase_1_Python_Math/](Phase_1_Python_Math/) |
| Phase 2 | Data Analysis | 2 months | Visualization, Cleaning, EDA | [Phase_2_Data_Analysis/](Phase_2_Data_Analysis/) |
| Phase 3 | Machine Learning | 2 months | Supervised/Unsupervised ML | [Phase_3_ML/](Phase_3_ML/) |
| Phase 4 | Deep Learning | 2 months | CNNs, RNNs, Transformers | [Phase_4_DL/](Phase_4_DL/) |
| Phase 5 | Specialization | 2 months | DE / MLOps / NLP / CV tracks | [Phase_5_Specialization/](Phase_5_Specialization/) |
| Phase 6 | Capstone | 1 month | End-to-end project | [Phase_6_Capstone/](Phase_6_Capstone/) |

## Specialization Tracks (Phase 5)

| Track | Focus | Directory |
|-------|-------|-----------|
| Track 1 | Data Engineering | [Phase_5_Specialization/Track_1_Data_Engineering/](Phase_5_Specialization/Track_1_Data_Engineering/) |
| Track 2 | MLOps | [Phase_5_Specialization/Track_2_MLOps/](Phase_5_Specialization/Track_2_MLOps/) |
| Track 3 | NLP | [Phase_5_Specialization/Track_3_NLP/](Phase_5_Specialization/Track_3_NLP/) |
| Track 4 | Computer Vision | [Phase_5_Specialization/Track_4_Computer_Vision/](Phase_5_Specialization/Track_4_Computer_Vision/) |

## Weekly Learning Schedule

| Day | Activity |
|-----|----------|
| Monday | New concept notebook (1–2 hours) |
| Tuesday | Hands-on coding exercises |
| Wednesday | Dataset practice / mini-project |
| Thursday | Quiz or discussion participation |
| Friday | Assignment work or review |
| Weekend | Project continuation (optional) |

## Learning Resources

| Resource | Description | Link |
|----------|-------------|------|
| Assignments | Phase-based coding assignments | [assignments/](assignments/) |
| Quizzes | Conceptual quizzes for each phase | [quizzes/](quizzes/) |
| Projects | Detailed project guides | [projects/](projects/) |
| Discussions | Community discussion prompts | [discussions/](discussions/) |

## Updated Repository Structure

```
LearnDataScienceWithEmmanuelOdenyire/
├── Phase_0_Foundations/
│   ├── README.md
│   ├── Week_1_Setup_and_Mindset.ipynb
│   └── Week_2_Git_GitHub_Colab.ipynb
├── Phase_1_Python_Math/
│   └── README.md  (links to Month_01, Month_02, Month_04)
├── Phase_2_Data_Analysis/
│   └── README.md  (links to Month_03, Month_05, Month_06)
├── Phase_3_ML/
│   ├── README.md
│   ├── regression_from_scratch.ipynb
│   └── classification_pipeline.ipynb
├── Phase_4_DL/
│   ├── README.md
│   ├── image_classifier.ipynb
│   └── text_sentiment_model.ipynb
├── Phase_5_Specialization/
│   ├── README.md
│   ├── Track_1_Data_Engineering/
│   │   ├── README.md
│   │   ├── data_pipelines_with_kafka.ipynb
│   │   └── spark_data_processing.ipynb
│   ├── Track_2_MLOps/
│   │   ├── README.md
│   │   ├── docker_model_deployment.ipynb
│   │   └── mlflow_experiment_tracking.ipynb
│   ├── Track_3_NLP/
│   │   ├── README.md
│   │   ├── transformers_and_fine_tuning.ipynb
│   │   └── build_chatbot_qa_system.ipynb
│   └── Track_4_Computer_Vision/
│       ├── README.md
│       ├── object_detection.ipynb
│       └── transfer_learning.ipynb
├── Phase_6_Capstone/
│   ├── README.md
│   ├── capstone_project_template.ipynb
│   └── industry_simulation_guide.ipynb
├── Month_01_Python_Basics/
│   ├── Week_1_Functions_and_OOP.ipynb
│   ├── Week_2_Data_Structures.ipynb
│   ├── Week_3_File_Handling_and_Modules.ipynb
│   └── Week_4_Mini_Data_Analyzer_Project.ipynb
├── Month_08_Advanced_Machine_Learning/
│   ├── feature_engineering_masterclass.ipynb
│   ├── ensemble_methods_from_scratch.ipynb
│   └── cross_validation_strategies.ipynb
├── assignments/
│   ├── README.md
│   ├── Phase_0_Assignment_Data_Science_Journey_Plan.md
│   ├── Phase_1_Assignment_Mini_Data_Analyzer.md
│   ├── Phase_2_Assignment_Netflix_Dataset_Analysis.md
│   ├── Phase_3_CAT_House_Price_Prediction.md
│   ├── Phase_4_Assignment_Image_Text_Classifier.md
│   ├── Phase_5_Assignment_Specialization_Project.md
│   └── Phase_6_Final_Capstone_Project.md
├── quizzes/
│   ├── README.md
│   └── Phase_0 through Phase_5 quizzes
├── projects/
│   ├── README.md
│   └── Project_01 through Project_06
├── discussions/
│   ├── README.md
│   └── Discussion_01 through Discussion_06
├── datasets/
├── resources/
├── requirements.txt
├── verify_setup.py
└── README.md
```
