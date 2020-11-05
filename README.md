# Project-2-for-EC-601
Feng Wang 
Project 2
1. retrieve tweets by account 
file name: Tweepy_file.py
This function retrieve tweets from specific tweet account.
The existing code returns the first newest 20 tweets from the user. 
You can uncomment code section 1 to retrive large quantity of tweets which requires longer time.
Max 3200 tweets.
The tweets are outputed into a JSON file in the form of dictionary. 
All information of the tweets are outputted in this case.
You can uncomment code section 2 to retrive a csv file containing selected information from the tweets.
The information includes tweet ID, Tweet creation date, and the content of the Tweet. 
Error case: The program is able to return error message: "The input contain unauthorized content, try another input"
This error message occurs when the input is invalid and if the account is private, or authoriztion keys of the user failed.
The program return error message: "Unexpected error", when an unexpected error occurs, such as tweeter fail to respond.
The output json file has name "tweet.json"
The output csv file has name @accountname_tweets.csv. For instance, @TheDailyShow_tweets.csv

2. retrieve tweets by time
file name: tweeter_time.py
function name: tweeter_time(screen_name)
The function take the tweeter account name as input.
After running the program, the 
This function retrieve tweets from this specific tweet account.
The the function prompt the user to input a date.
The prompt looks like this: >> Enter a date in the form (i.e. 2017,7,1)
Since the date requires a specific form, the function will keep prompting the user until the correct input is enter by the user.
After taking a date, the function will return all the tweets from this tweeter account from today to the inputted date.
If the entered date is too old, resulting in tweets amount exceeding tweety capacity.
The account will output: The date enter is too old, tweepy only able to retrieve 3200 tweets. The function will then terminate.
Error case: The program is able to return error message: "The input contain unauthorized content, try another input"
This error message occurs when the input is invalid and if the account is private, or authoriztion keys of the user failed.
The program return error message: "Unexpected error", when an unexpected error occurs, such as tweeter fail to respond.
The function is able to ouput the file in JSON file, excel and csv. 
You can comment out codes to generate your desired file type.
The output json file has name "tweet.json"
The output csv file has name @accountname_tweets.csv. For instance, @TheDailyShow_tweets.csv
The output excel file has name @accountname.excel. For instance, @TheDailyShow.excel

3. Search tweets by hashtags 
file_name: Tweepy_Hashtag.py
The function take the hashtag and number of tweets aim to retrieve from the hashtag as input.
The code will first check the inputted number of tweets.
If the number of tweets are larger than 2000, the system will exit, since the API will freeze if too many tweets are retieved.
The function will then check if a valid hashtag is inputted by the user. 
If the hashtag is not valid, the system will exit.
For other unexpected errors, the function and output a message telling the user why the file failed.
If the user is able to successful input correct number and tweeter hashtag, the function will return the file date and full text in a csv file. 
The output csv file has name @accountname_tweets.csv. For instance, @TheDailyShow_tweets.csv

4. sentence sentiments and Entity Level Sentiment
file_name: google.py
function_name: analyze_entity_sentiment(text_content)
The user needs to input the text content which they want to analyze into the function.
The function will then output Entity Level Sentiment with its's Representative name for the entity, Entity type, 
Salience score, Entity sentiment score, Entity sentiment magnitude. At the end of the output, the function will output overall sentiment score with its magnitude. 
For example:
In main: 
    # pass in the username of the account you want to download
    text_content = "Google, headquartered in Mountain."
    analyze_entity_sentiment(text_content)
output:
Representative name for the entity: Google
Entity type: OTHER
Salience score: 0.9005488753318787
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0

Representative name for the entity: Mountain
Entity type: LOCATION
Salience score: 0.09945113211870193
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0

Overall sentiment: 0.0, 0.0

Application:
The application can be tested with a pre generated file named #VOTE_tweets using the Tweepy_Hashtag.py function.
The goal of the application is to retrieve the most recent # of tweets by people under the hashtag #VOTE and understand people's general sentiment towards it.

Sub application 1:
file name:google2.py
This application mainly looks at the overall sentiment of tweets. 
The system takes a csv file as input. 
Note: the application runs on top of Tweepy_Hashtag.py, a self-generated file will not work with applcation, due to the column title requirement for the file.
The system then runs to extract the score and sentiment of the sentence into a cvs file named sentiment.csv. During extraction, the system will output running to let the user know that the file is running properly. 
The system then calculate the average sentiment score and magnituded of the collected tweets and generate outputs.
an example of output:
...
system running
system running
The overall average sentiment score is -0.14700000323355197, the average sentiment magnitude is 0.7190000089257955
the overall sentiment of the texts is relatively neutral
the text are over all emotional

Sub application 2:
file name:read_and_calculate
This application mainly looks at individual Entity Level Sentiment of tweets. 
The system takes a csv file as input. 
Note: the application runs on top of Tweepy_Hashtag.py, a self-generated file will not work with applcation, due to the column title requirement for the file.
The system then runs to extract the score and sentiment of individual Entity Level into a cvs file named sentiment_detail.csv. During extraction, the system will output running to let the user know that the file is running properly. 
The system then calculate the average sentiment score and magnituded of the collected for each entity level for the tweets and generate outputs.
an example of output:
....
file running
file running
file running
file running
file running
file running

For Entity Level OTHER,
the average sentiment score is -0.12780083143983145, the average sentiment magnitude is 0.34190871705652764
There are 252 neutral words for this keyword
the overall sentiment of the text relatively neutral
the text are over all emotional

For Entity Level CONSUMER_GOOD,
the average sentiment score is 0.10000000149011612, the average sentiment magnitude is 0.10000000149011612
There are 3 neutral words for this keyword
the overall sentiment of the text relatively neutral
the text are over all emotional

For Entity Level LOCATION,
the average sentiment score is 0.04285714030265808, the average sentiment magnitude is 0.18571428528853826
There are 10 neutral words for this keyword
the overall sentiment of the text relatively neutral
the text are over all emotional

For Entity Level PERSON,
the average sentiment score is 0.002173912104057229, the average sentiment magnitude is 0.33043478477908217
There are 50 neutral words for this keyword
the overall sentiment of the text relatively neutral
the text are over all emotional

For Entity Level EVENT,
the average sentiment score is -0.08571428841068632, the average sentiment magnitude is 0.2714285736992246
There are 11 neutral words for this keyword
the overall sentiment of the text relatively neutral
the text are over all emotional

For Entity Level ORGANIZATION,
the average sentiment score is -0.12857142809246266, the average sentiment magnitude is 0.20000000058540277
There are 14 neutral words for this keyword
the overall sentiment of the text relatively neutral
the text are over all emotional

For Entity Level WORK_OF_ART,
the average sentiment score is 0.13333334028720856, the average sentiment magnitude is 0.2666666756073634
There are 4 neutral words for this keyword
the overall sentiment of the text relatively neutral
the text are over all emotional




















