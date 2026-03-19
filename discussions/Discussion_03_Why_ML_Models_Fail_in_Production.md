# Discussion 03: Why ML Models Fail in Production

## Context
Studies show that 87% of ML models never make it to production, and many that do fail within months. Understanding why is crucial for building robust ML systems.

## Common Failure Modes
- **Data drift**: Input data distribution changes over time
- **Concept drift**: The relationship between features and target changes
- **Training-serving skew**: Data preprocessing differs between training and deployment
- **Feedback loops**: Model predictions influence future training data

## Discussion Prompts

### Part A: Case Study Analysis (200+ words)
Read about one of these real ML failures:
1. Amazon's biased hiring algorithm (2018)
2. Google Photos misclassifying people (2015)
3. IBM Watson for Oncology errors (2018)

Summarize: What failed? What were the consequences? What should have been done differently?

### Part B: Prevention Strategies (150+ words)
For a house price prediction model deployed at a real estate company:
- Identify 3 specific ways it could fail within 2 years
- Propose monitoring strategies to detect each failure mode
- Suggest retraining strategies

### Part C: Technical vs. Organizational Failure
Are most ML failures technical problems or organizational/process problems? Defend your position with examples (150+ words).

---

## Recommended Reading
- [Sculley et al. "Hidden Technical Debt in Machine Learning Systems" (2015)](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)
- [Google's ML Production Guide](https://developers.google.com/machine-learning/crash-course/production-ml-systems)
