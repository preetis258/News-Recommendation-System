
# News Recommender System

Link of the web application: https://news-recommender-system-ps.herokuapp.com/

News is the component of communication that keeps us up to date on current events, topics, and people in the globe. So creating a news recommender system to increase the engagement of active users on a news site using articles recommendations will not only beneficial for users but also for companies. News recommender systems (NRS) are being created to alleviate the problem of information overload and to propose news articles that may be of interest to news readers in order to assist them in finding the proper and relevant material.

This a popularity and content based hybrid news recommender system. A user has to select a category and subcategory based on which popularity scores are calculated and top 10 news articles are recommended. When an article is selected then using content based approach, 5 news articles are recommended.  

This project "News Recommender System" is created in Python using several Data Science libraries such as Pandas, Numpy, NLTK, Sci-kit Learn, etc. The Front-end is created using Streamlit library and is deployed on Heroku.

### Popularity based approach: 

 Opinion of users are considered for calculating this score. It is calculated using the number of times a news article is being read and the number of times a user has read a news article belonging to the selected category and subcategory.

 ### Content based approach:

 Bag of Words is used for feature vectorizing the news articles and cosine similarity is calculated. The top 5 news articles having maximum similarity are recommended.

 ## Datasets

 MIcrosoft News Dataset (MIND) dataset is used for performing this project. 
 - news.tsv: The information of news articles using which content based system is made
 - behaviour.tsv: The news articles click histories of users using which popularity scores are calculated. 

 Link to the dataset: https://msnews.github.io/
 