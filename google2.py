from google.cloud import language_v1
from google.cloud.language import enums
from google.cloud.language import types
import csv
import pandas as pd
# set GOOGLE_APPLICATION_CREDENTIALS= json file here

def analyze_overal_entity_sentiment(file):

    client = language_v1.LanguageServiceClient()

    # text_content = 'Grapes are good. Bananas are bad.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    df = pd.read_csv(file)
    saved_column = df.text
    csvFile = open('sentiment.csv', 'w')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["sentiment_score", "sentiment_magnitude"])
    for na in saved_column:
        #print(na)
        language = "en"
        document = {"content": na, "type": type_, "language": language}
        #keyword = []
        # Available values: NONE, UTF8, UTF16, UTF32
        encoding_type = enums.EncodingType.UTF8
        # Use csv Writer
        document = types.Document(content=na, type=enums.Document.Type.PLAIN_TEXT)
        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        #print('Overall sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
        print("system running")
        csvWriter.writerow([format(sentiment.score), format(sentiment.magnitude)])


def calculate_overal_entity_sentiment():
# reference https://stackoverflow.com/questions/35107815/sum-of-a-column-in-python-for-csv-file
    df = pd.read_csv('sentiment.csv', delimiter=',')
    score = df['sentiment_score'].sum()
    magnitude = df['sentiment_magnitude'].sum()
    index = 0
    for value in df.sentiment_score:
        index += 1
    ave_score = score/index
    ave_magnitude = magnitude/index
    print(f"The overall average sentiment score is {ave_score}, the average sentiment magnitude is {ave_magnitude}")
    if ave_score < 0.25 and ave_score > -0.25:
        print("the overall sentiment of the keyword is negative")
    else:
        print("the overall sentiment of the keyword is very negative")
    if ave_magnitude < 0.25 and ave_magnitude > 0.25:
        print("the text is not emotional ")
    else:
        print("the text is emotional")


if __name__ == '__main__':
    # pass in the username of th e account you want to download
    file = '#VOTE_tweets.csv'
    analyze_overal_entity_sentiment(file)
    calculate_overal_entity_sentiment()