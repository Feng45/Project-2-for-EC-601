from google.cloud import language_v1
from google.cloud.language_v1 import enums
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
# set GOOGLE_APPLICATION_CREDENTIALS= C:\Users\feng2\Desktop\Fall_2020\Project-2-for-EC-601\GOOGLE_KEY.JSON
# reference https://cloud.google.com/natural-language/docs/sentiment-tutorial
# reference https://cloud.google.com/natural-language/docs/analyzing-entity-sentiment
def analyze_entity_sentiment(text_content):
    """
    Analyzing Entity Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'Grapes are good. Bananas are bad.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_entity_sentiment(document, encoding_type=encoding_type)
    # Loop through entitites returned from the API
    for entity in response.entities:
        print(u"Representative name for the entity: {}".format(entity.name))
        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
        # Get the salience score associated with the entity in the [0, 1.0] range
        print(u"Salience score: {}".format(entity.salience))
        # Get the aggregate sentiment expressed for this entity in the provided document.
        sentiment = entity.sentiment
        print(u"Entity sentiment score: {}".format(sentiment.score))
        print(u"Entity sentiment magnitude: {}".format(sentiment.magnitude))
        print(u"      ")

    # overall sentiment score
    document = types.Document(content=text_content, type=enums.Document.Type.PLAIN_TEXT)
    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    print('Overall sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))


if __name__ == '__main__':
    # pass in the username of th e account you want to download
    text_content = "Google, headquartered in Mountain."
    analyze_entity_sentiment(text_content)

