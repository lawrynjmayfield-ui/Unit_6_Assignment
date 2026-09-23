# Unit 6 Assignment: AI-Driven Predictive Maintenance for Amazon EC2

## Project Overview
This project demonstrates a proof-of-concept predictive maintenance
workflow using AWS cloud services and machine learning. The solution
predicts potential high-CPU conditions on an Amazon EC2 instance before
CPU utilization reaches the defined 80% threshold.

## AWS Services
- Amazon EC2 – Test workload
- Amazon CloudWatch – CPU utilization monitoring
- Amazon SageMaker AI – Machine learning development and testing
- AWS Lambda – Automated decision and alert logic

## Machine Learning Model
A logistic regression classifier was trained using simulated CPU
utilization data.

Features:
- Previous CPU utilization
- Current CPU utilization
- Average CPU utilization
- CPU trend

Target:
- Normal CPU condition
- Upcoming high-CPU condition

## Model Results
- Accuracy: 97.00%
- Precision: 94.74%
- Recall: 90.00%
- F1 Score: 92.31%

## Validation Results

| Scenario | Current CPU | Risk Probability | Action |
|---|---:|---:|---|
| Normal | 28% | 0.00% | Continue Monitoring |
| Rising | 70% | 41.50% | Continue Monitoring |
| High Risk | 75% | 77.03% | Preventive Maintenance Alert |

## Repository Contents
- `predictive-maintenance-model.ipynb` – ML training and testing notebook
- `lambda_function.py` – AWS Lambda automation logic
- `vm_cpu_training_data.csv` – ML training dataset
- `validation_results.csv` – Test and validation results

## Implementation
1. Launch an Amazon EC2 test instance.
2. Monitor CPU utilization using Amazon CloudWatch.
3. Generate controlled CPU utilization to observe workload behavior.
4. Create and train the logistic regression model in SageMaker JupyterLab.
5. Evaluate the model using accuracy, precision, recall, and F1 score.
6. Test normal, rising, and high-risk CPU scenarios.
7. Pass prediction probabilities to AWS Lambda.
8. Lambda generates a preventive maintenance alert when predicted risk
   is 70% or greater.

## Proof-of-Concept Limitation
The lab implementation validates each component of the workflow but
does not implement a continuous production pipeline. Simulated historical
CPU data was used for model training, and SageMaker prediction results
were manually passed to Lambda as test events. A production implementation
could automatically ingest CloudWatch metrics and deploy the trained model
through a SageMaker inference endpoint.
