# Phase 2 Quiz: Data Analysis

**Instructions**: 25 questions. Open book.

---

## Section A: Visualization (Multiple Choice, 1 point each)

**1.** Which plot type is best for showing distribution of a continuous variable?
- a) Bar chart
- b) Scatter plot
- c) Histogram / KDE plot
- d) Pie chart

**2.** What does a correlation heatmap show?
- a) Time series trends
- b) Pairwise linear relationships between numerical features
- c) Categorical feature distributions
- d) Missing value patterns

**3.** When should you use a log scale on an axis?
- a) When values are normally distributed
- b) When data spans several orders of magnitude
- c) When there are negative values
- d) When comparing categorical data

---

## Section B: Data Cleaning (3 points each)

**4.** List 4 strategies for handling missing values. When is each appropriate?

**5.** What is the IQR method for detecting outliers? Write the formula.

**6.** Explain the difference between data normalization and standardization.

**7.** You have a date column stored as a string (`"January 5, 2022"`). How would you convert it to a `datetime` type in Pandas?

---

## Section C: EDA (3 points each)

**8.** What is the difference between univariate, bivariate, and multivariate analysis?

**9.** You're analyzing a dataset and find that `income` is highly right-skewed. What transformations would you consider and why?

**10.** Describe a complete EDA workflow for a new dataset you've never seen before (at least 6 steps).

---

## Section D: Practical Code (5 points each)

**11.** Write code to: load a CSV, identify columns with >30% missing values, drop those columns, and plot a heatmap of the remaining missing values.

**12.** Given a DataFrame with `date`, `product`, `revenue` columns, write code to plot monthly revenue trends for each product on the same chart.

---

*Total: 25 points*
