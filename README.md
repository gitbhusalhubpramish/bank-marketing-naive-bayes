# Bank-marketing with Naive-Bayes

In this project I have applied Gussian Naive-Bayes from scratch in [Bank-marketing](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset/) dataset in kaggle. This markdonw is just the overview of project and how I made this. I have given more detail in my [notes](https://github.com/gitbhusalhubpramish/ml-notes/tree/main/0.007%20navie-bayes) about Naive-Bayes.

<img src="visual.jpg" />

This is one of the probability distribution image of the algorithm. It is hard to visulize. Main thing here is the accuracy and tables rather than graph.

## Small intro to Naive-Bayes

Naive-Bayes is a Probability bashed supervised Meachine Learning algorithm. It uses Probabilities (Bayes theorem) to predict or classify any data. There are 2 types of Naive bayes - Categorical and Gussian. I have used both here. Categorial are used for catorigal data while gussian is used for numerical data.

## Feature

This project was made by me to understand Naive-bayes trom scratch so it has naive-bayes applied from scratch. But also:

- Naive-bayes from scratch.
- Gussian approch.
- Stats.
- Data Visulization

## Tech-Stack

This project python liberies used for datascience - visulizaion, calculation and datamanipulation. I've used:

- Numpy for calculation.
- matplotlib and streamlit for data visulization
- pandas for CSV and data manipulation.
- sk-learn for accuracy calculation and data split.

## Work-flow

The work flow of the project look like ths:

- **Fetch data:** Here it fetches the data from kaggle dataset.
- **Data Shepration:** Here the algorithm shaprate the data into 2(4) parts for training and testing with x and y each.
- **Calcuate $P(y|x)$ :** Here the model calculates $P(y|x)$ by calculate the variable required for this using log spacing naive bayes. It used catogral for catogral data and gussian for numeric data.
- **Calcuate $P(n|x)$ :** Here the model calculate $P(n|x)$ - probability of being no by calculating the variable required for this using loc spacing and naive bayes.
- **Visulization:** Well, This algorithm doesn't have any special thing to visulize though I ploted the likehood ($P(x|y)$ and $P(x|n)$).
- **Comparisn:** Here $P(n|x)$ and $P(y|x)$ are compared and returned which one is greater (*y mean yes and n mean no*).


