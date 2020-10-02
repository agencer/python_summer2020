############################################################################################
####								  PYTHON PROJECT									####
####								Alper Sukru Gencer 									####
############################################################################################


##	GOALs:
##	
##	
## 	Preprocessing the tweets to prepare it for the sentiment analysis.

from bs4 import BeautifulSoup
import re 
import tweepy
import sys # add directory to system PATH
import os
import io
import csv
import pandas as pd 
import numpy as np
import datetime
import nltk
from os import getcwd

os.chdir('C:/Users/alper/OneDrive/Belgeler/GitHub/python_summer2020/Summer_Project/')

##	
##
##
##	It worked. Now start from the here:
data_ExecOrders = pd.read_csv("gencer_exeorder.csv",  engine='python') 
data_ExecOrders.head()
data_ExecOrders 
data_TrumpTweets = pd.read_csv("gencer_TrumpTweets_2.csv", sep = ",", engine='python')
data_TrumpTweets.head()
for col in data_TrumpTweets.columns:
	print(col)								##	Looks great!

##
##
##
##	Now let's get our training data to predict the sentiment:
nltk.download('twitter_samples')
nltk.download('stopwords')
filePath = f"{getcwd()}/../tmp2/"

##	Let's run this py file which will give me precreated process_tweet() and build_freq functions:
os.chdir("G:/My Drive/_WashU_courses/2020_Fall/Methods/NLP/nltk_data/labs/")
run utf-8''utils.py

import numpy as np
import pandas as pd
from nltk.corpus import twitter_samples

##	Now let's train the data:

## First, let's select the set of positive and negative tweets
all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

test_pos = all_positive_tweets[4000:]
train_pos = all_positive_tweets[:4000]
test_neg = all_negative_tweets[4000:]
train_neg = all_negative_tweets[:4000]

train_x = train_pos + train_neg 
test_x = test_pos + test_neg

## Create the numpy array of positive labels and negative labels.

## Combine positive and negative labels
train_y = np.append(np.ones((len(train_pos), 1)), np.zeros((len(train_neg), 1)), axis=0)
test_y = np.append(np.ones((len(test_pos), 1)), np.zeros((len(test_neg), 1)), axis=0)

## Print the shape train and test sets
print("train_y.shape = " + str(train_y.shape))
print("test_y.shape = " + str(test_y.shape))

# create frequency dictionary
freqs = build_freqs(train_x, train_y)

# check the output
print("type(freqs) = " + str(type(freqs)))
print("len(freqs) = " + str(len(freqs.keys())))

##
##
## Testing the preprocess function below:
print('This is an example of a positive tweet: \n\n', train_x[0])
print('\nThis is an example of the processed version of the tweet: \n\n', process_tweet(train_x[0]))


##
##
##	Let's write out logistic function:

##	A- Sigmoid Function:

def sigmoid(z): 
    '''
    Input:
        z: is the input (can be a scalar or an array)
    Output:
        h: the sigmoid of z
    '''
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    # calculate the sigmoid of z
    h = 1 / (1 + np.exp(-z))
    ### END CODE HERE ###
    return h

def gradientDescent(x, y, theta, alpha, num_iters):
    '''
    Input:
        x: matrix of features which is (m,n+1)
        y: corresponding labels of the input matrix x, dimensions (m,1)
        theta: weight vector of dimension (n+1,1)
        alpha: learning rate
        num_iters: number of iterations you want to train your model for
    Output:
        J: the final cost
        theta: your final weight vector
    Hint: you might want to print the cost to make sure that it is going down.
    '''
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    # get 'm', the number of rows in matrix x
    m = x.shape[0]
    
    for i in range(0, num_iters):
        
        # get z, the dot product of x and theta
        z = np.dot(x, theta)
        
        # get the sigmoid of z
        h = sigmoid(z)
        
        # calculate the cost function
        J = -1./m *(np.dot(y.transpose(), np.log(h)) + np.dot((1-y).transpose(), np.log(1-h)))
        if i % 25 == 0:
	        print("Iteration no: ", i, ". Cost is: " + str(J))
        # update the weights theta
        theta = theta - (alpha/m) * np.dot(x.transpose(), (h-y))
        
    ### END CODE HERE ###
    J = float(J)
    return J, theta

# X input is 10 x 3 with ones for the bias terms
tmp_X = np.append(np.ones((10, 1)), np.random.rand(10, 2) * 2000, axis=1)
# Y Labels are 10 x 1
tmp_Y = (np.random.rand(10, 1) > 0.35).astype(float)

# Apply gradient descent
tmp_J, tmp_theta = gradientDescent(tmp_X, tmp_Y, np.zeros((3, 1)), 1e-8, 700)
print(f"The cost after training is {tmp_J:.8f}.")
print(f"The resulting vector of weights is {[round(t, 8) for t in np.squeeze(tmp_theta)]}")


##
##
## Feature Extracter
def extract_features(tweet, freqs):
    '''
    Input: 
        tweet: a list of words for one tweet
        freqs: a dictionary corresponding to the frequencies of each tuple (word, label)
    Output: 
        x: a feature vector of dimension (1,3)
    '''
    # process_tweet tokenizes, stems, and removes stopwords
    word_l = process_tweet(tweet)
    
    # 3 elements in the form of a 1 x 3 vector
    x = np.zeros((1, 3)) 
    
    #bias term is set to 1
    x[0,0] = 1 
    
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    
    # loop through each word in the list of words
    for word in word_l:
        
        # increment the word count for the positive label 1
        x[0,1] += freqs.get((word, 1.0), 0)
        
        # increment the word count for the negative label 0
        x[0,2] += freqs.get((word, 0.0), 0)
        
    ### END CODE HERE ###
    assert(x.shape == (1, 3))
    return x


## test on training data
tmp1 = extract_features(train_x[0], freqs)
print(tmp1)

# check for when the words are not in the freqs dictionary
tmp2 = extract_features('blorb bleeeeb bloooob', freqs)
print(tmp2)


# collect the features 'x' and stack them into a matrix 'X'
X = np.zeros((len(train_x), 3))
for i in range(len(train_x)):
    X[i, :]= extract_features(train_x[i], freqs)

# training labels corresponding to X
Y = train_y

# Apply gradient descent 
J, theta = gradientDescent(X, Y, np.zeros((3, 1)), 1e-9, 1500)
print(f"The cost after training is {J:.8f}.")
print(f"The resulting vector of weights is {[round(t, 8) for t in np.squeeze(theta)]}")

##
##
##	Testing the logistic regression:

def predict_tweet(tweet, freqs, theta):
    '''
    Input: 
        tweet: a string
        freqs: a dictionary corresponding to the frequencies of each tuple (word, label)
        theta: (3,1) vector of weights
    Output: 
        y_pred: the probability of a tweet being positive or negative
    '''
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    
    # extract the features of the tweet and store it into x
    x = extract_features(tweet, freqs)
    
    # make the prediction using x and theta
    y_pred = sigmoid(np.dot(x, theta))
    
    ### END CODE HERE ###
    
    return y_pred


##
##
##	Let's try with Trump tweets:

len(data_TrumpTweets["text"])
sentiment = []
sentiment_bin = []

for tweet in data_TrumpTweets["text"]:
	sentiment.append(predict_tweet(tweet, freqs, theta))
	sentiment_bin.append(predict_tweet(tweet, freqs, theta)>=0.5)
data_TrumpTweets["sentiment"] = sentiment
data_TrumpTweets["sentiment_bin"] = sentiment_bin

data_TrumpTweets.head()

##
##
##	Let's save this: