# Fine-tune DistilBERT-base-uncased for Sentiment Analysis

## Dataset

The dataset used for this project is the Amazon Fine Food Reviews dataset, available [here](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews). Please download the dataset from the provided link.

## Problem Statement

The objective of this project is to perform sentiment analysis on Amazon Fine Food reviews using the DistilBERT model. Sentiment analysis aims to determine the sentiment expressed in a piece of text, which can be positive, negative, or neutral.

Columns:
1. Id: The unique identifier for each review entry.
1. ProductId: The unique identifier for the product being reviewed.
1. UserId: The unique identifier for the user who wrote the review.
1. ProfileName: The name or profile of the user who wrote the review.
1. HelpfulnessNumerator: The number of users who found the review helpful.
1. HelpfulnessDenominator: The total number of users who voted on whether the review was helpful or not.
1. Score: The rating given by the user for the product, ranging from 1 to 5.
1. Time: The timestamp indicating when the review was posted, in Unix time format (seconds since January 1, 1970).
1. Summary: A brief summary or headline for the review.
1. Text: The main body of the review, containing the detailed feedback or description provided by the user about the product.

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