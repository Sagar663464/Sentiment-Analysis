# Sentiment Analysis using Twitter data

This repo is all about sentiment analysis of tweets. I've used TextBlob's naive bayes classifier model for classification. The dataset is too large to upload in GitHub with over 6 million records and 290 MB. It has a jupyter notebook `main.ipynb` with which you can learn about the processes that are needed to be done. Firstly I've taken models from sklearn, and it's accuracy were very low. So I have to move onto some other models. Also while vectorizing a new text from user input, it was giving me vecctors with 3 to 4 features while the trained data had 1000 features. I encountered few problems in this part, so I had to move onto other models. I chosed TextBlob's Naive Bayes classifier model, which worked pretty well.


## Dataset description

The dataset was downloaded from kaggle with 6 features and 6 million samples. The features are `Target`, `UserID`, `DateTime`, `Flag`, `Username`, `Tweet`. Target
had 2 unique valuee(0 - Negative and 1 - Positive). Only needed features were taken for analysis, as the model would experience difficulty in learning the data. 

## Steps for running

 - Clone the repo and open in an IDE.
 - Create a virtual environment and activate it.
   
   ```
   python -m venv sentenv
   sentenv\Scripts\activate
   
   ```
- Install the requires python libraries.

  ```
  pip install requirements.txt
  ```
- Run the `app.py` file in localhost.
  ```
  python app.py
  ```
   It would most likely run in localhost (http://127.0.0.1:5000/)

- Enter the text you wish and press Submit.
- It would display the polarity of texts entered.

## Screenshots
![Screenshot 2023-10-15 114402](https://github.com/Sagar663464/Sentiment-Analysis/assets/65543059/9e9feddc-a193-4aa3-95b6-09296dac89d4)

![Screenshot 2023-10-15 120041](https://github.com/Sagar663464/Sentiment-Analysis/assets/65543059/3181169b-32db-4818-8c0d-12dddea2f1dd)

![Screenshot 2023-10-17 112449](https://github.com/Sagar663464/Sentiment-Analysis/assets/65543059/70a68028-5e70-4846-a4d5-1c2ccf36a5db)


