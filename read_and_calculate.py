from google.cloud import language_v1
from google.cloud.language import enums
from google.cloud.language import types
import csv
import pandas as pd

def analyze_entity_sentiment_detail():

    client = language_v1.LanguageServiceClient()

    # text_content = 'Grapes are good. Bananas are bad.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT
    encoding_type = enums.EncodingType.UTF8

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    unique = []
    df = pd.read_csv('#VOTE_tweets.csv')
    saved_column = df.text
    csvFile = open('sentiment_detail.csv', 'w')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["content", "entity","salience","sentiment_score","sentiment_magnitude"])
    for na in saved_column:
        #print(na)
        print("file running")
        language = "en"
        document = {"content": na, "type": type_, "language": language}
        response = client.analyze_entity_sentiment(document, encoding_type=encoding_type)
        # Loop through entitites returned from the API
        for entity in response.entities:
            cate = enums.Entity.Type(entity.type).name
            if cate not in unique:
                unique.append(cate)
            sentiment = entity.sentiment
            csvWriter.writerow([format(entity.name),format(enums.Entity.Type(entity.type).name),format(entity.salience),format(sentiment.score),format(sentiment.magnitude)])
    return unique


def calculate_entity(entity):
    # reference https://thispointer.com/python-read-csv-into-a-list-of-lists-or-tuples-or-dictionaries-import-csv-to-list/
    df = pd.read_csv('sentiment_detail.csv', delimiter=',')
    # User list comprehension to create a list of lists from Dataframe rows
    list_of_rows = [list(row) for row in df.values]
    # Print list of lists i.e. rows
    score = 0
    magnitude = 0
    index = 0
    neutral = 0
    #print(list_of_rows[1])
    for whole in list_of_rows:
        if whole[1] == entity:
            if whole[3] != 0:
                score = score + whole[3]
                magnitude = magnitude + whole[4]
                index = index + 1
            else:
                neutral = neutral + 1
    average_magnitude = magnitude / index
    average_score = score/index
    print(f"For Entity Level {entity},")
    print(f"the average sentiment score is {average_score}, the average sentiment magnitude is {average_magnitude}")
    print(f"There are {neutral} neutral words for this keyword")
    if average_score < 0.25 and average_score > -0.25:
        print("the overall sentiment of the text relatively neutral")
    elif average_score > 0.25:
        print("the overall sentiment of the text is positive ")
    else:
        print("the overall sentiment of the text is negative ")

    if average_magnitude < 0.25 and average_magnitude > 0.25:
        print("the texts are overall emotional ")
    else:
        print("the text are over all emotional")


if __name__ == '__main__':
    # pass in the username of th e account you want to download
    result = analyze_entity_sentiment_detail()
    print(result)
    for entity in result:
        print("    ")
        calculate_entity(entity)