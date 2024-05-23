# Fine-tune DistilBERT-base-uncased for Sentiment Analysis

## Dataset

The dataset used for this project is the Amazon Fine Food Reviews dataset, available [here](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews). Please download the dataset from the provided link.

## Problem Statement

The objective of this project is to perform sentiment analysis on Amazon Fine Food reviews using the DistilBERT model. Sentiment analysis aims to determine the sentiment expressed in a piece of text, which can be positive, negative, or neutral.

## Key Steps

- **Preprocessing:** Clean and preprocess the text data, including tasks such as removing stopwords, punctuation, and handling special characters.
- **EDA (Exploratory Data Analysis):** Explore the dataset to gain insights into the distribution of sentiment labels, the length of reviews, and any patterns present in the data.
- **NLP Tasks:** Perform Natural Language Processing (NLP) tasks such as tokenization, encoding, and preparing the data for training the model.
- **Training:** Fine-tune the DistilBERT-base-uncased model on the preprocessed data for sentiment analysis.
- **Model Evaluation:** Evaluate the performance of the trained model using appropriate evaluation metrics such as accuracy, precision, recall, and F1-score.

## Training

To access the training process and code, please refer to the provided notebooks file.

## Model Evaluation
```
Confusion Matrix:
[[ 230   21   21    8   29]
 [  65   47   56   26   20]
 [  31   28   59  140   55]
 [  15    5    9  174  340]
 [  13    0    6   75 2127]]
Accuracy: 0.7410
Precision: 0.7325
Recall: 0.7325
F1-score: 0.7325
```

## Output

Input: Maybe not worth it to buy
Result: The sentiment of the text is: Neutral review

##
API
POST: {host}/predict

```json
{
    "text": "Maybe not worth it"
}
```

## How to Deploy

### Requirements

- Docker
- Pytorch

### Deployment Steps

1. Build the Docker image:
```
docker-compose build
```

2. Run the Docker image:
```
docker-compose up
```

Api will be run in localhost:5000
Application will be run in localhost:8501