# Discussion 06: Bias in Data

## Introduction
Data is never neutral. It reflects the world it was collected in, including its inequalities, assumptions, and blind spots. Understanding data bias is critical for building fair, reliable models.

## Types of Data Bias
| Bias Type | Description | Example |
|-----------|-------------|---------|
| Selection bias | Sample doesn't represent population | Surveying only smartphone users |
| Confirmation bias | Only collecting data that confirms beliefs | A/B test stopped early at positive result |
| Historical bias | Past discrimination encoded in data | Resume screening on historically biased hiring |
| Measurement bias | Inconsistent or inaccurate data collection | Self-reported income data |
| Aggregation bias | Averaging over groups erases subgroup differences | Heart disease models ignoring gender differences |

## Discussion Prompts

### Part A: Identify Bias in a Real Dataset (200+ words)
Pick a dataset you've used (Titanic, Netflix, Housing, etc.) and identify:
1. What selection biases might exist?
2. What groups might be underrepresented?
3. How could these biases affect a model trained on this data?
4. What would you do to mitigate these biases?

### Part B: Case Study – Healthcare AI (150+ words)
A hospital trains an AI model to predict patient deterioration. The training data comes from 10 years of hospital records. However, patients from lower-income areas received less monitoring, so their records have fewer data points about early warning signs.

- Identify the bias in this scenario
- Explain how it could affect the model's predictions
- Propose at least 2 concrete mitigation strategies

### Part C: Debiasing Techniques (100+ words)
Research one of these debiasing approaches and explain how it works:
1. **Reweighting**: Adjusting sample weights to balance representation
2. **Adversarial debiasing**: Training models to be invariant to protected attributes
3. **Fairness constraints**: Adding fairness as a regularization term

---

## Tools to Explore
- [Fairlearn (Microsoft)](https://fairlearn.org/)
- [AI Fairness 360 (IBM)](https://aif360.mybluemix.net/)
- [What-If Tool (Google)](https://pair-code.github.io/what-if-tool/)
