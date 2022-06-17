
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#reading the datasets
df_history=pd.read_csv('PC-behaviour-data.csv')
df_content=pd.read_csv('PC-news-data.csv')
st.header("News Recommendation System")

### category input
st.markdown("### Select a category")
input_category=st.selectbox("",df_content.category.unique())
input_df=df_content[df_content.category==input_category].reset_index(drop=True)
input_history_df=df_history[df_history.category==input_category].reset_index(drop=True)

# subcategory input
st.markdown("### Select a subcategory")
input_subcategory = st.selectbox("",input_df.subcategory.unique())
input_df_final=input_df[input_df.subcategory==input_subcategory].reset_index(drop=True)
input_history_df_final=input_history_df[input_history_df.subcategory==input_subcategory].reset_index(drop=True)

# threshold setting
threshold_li=[]
for i in input_history_df_final.history.unique():
    val=input_history_df_final[input_history_df_final.history==i].user_id.value_counts().iloc[0]
    threshold_li.append(val)
threshold_val=np.round(np.mean(threshold_li))
df_counts=input_history_df_final.groupby(['history','user_id']).user_id.count().to_frame().rename({'user_id':'counts'},axis=1)
df_counts=df_counts[df_counts<threshold_val].reset_index()
df_counts.counts.fillna(threshold_val,inplace=True)
user_id_count_sum = np.sum(df_counts.counts)
df_counts['user_score']=df_counts['counts']/user_id_count_sum
news_score_dict=df_counts.history.value_counts(normalize=True).to_dict()
df_counts['news_score']=df_counts.history.map(news_score_dict)
df_counts['score']=df_counts['user_score']*df_counts['news_score']
recs=df_counts.groupby(['history']).score.mean().to_frame().sort_values('score',ascending=False)
rec_news_id=recs.iloc[:10].index.tolist()

## recommendations
news_recommended=df_content[df_content.news_id.isin(rec_news_id)]
if st.button("Recommend"):
    st.markdown("#### Select a news index from below")
    for idx, i in enumerate(news_recommended.title):
        st.markdown(f'{idx + 1}: {i}')
sel_idx = st.selectbox('Select the news index',[i for i in range(1,news_recommended.shape[0])])
sel_news = news_recommended.iloc[sel_idx - 1]
st.markdown(f"#### Title: {sel_news.title}")
st.markdown(sel_news.abstract)

#### Content based recommendation
# Bag of words
bow=CountVectorizer(max_features=5000)
vectors=bow.fit_transform(input_df_final['tags'])
similarity=cosine_similarity(vectors)
c_input=sel_news.news_id

def recommend(newd_id_c):
    news_index = input_df_final[input_df_final.news_id == newd_id_c].index[0]
    distance = similarity[news_index]
    news_list = sorted(list(enumerate(distance)), reverse=True,key=lambda x:x[1])[1:6]
    for idx,i in enumerate(news_list):
        st.markdown(f"#### {idx+1}. Title: {input_df_final.iloc[i[0]].title}")
        st.markdown(f"{input_df_final.iloc[i[0]].abstract}")

if st.button("Recommend similar content"):
    recommend(c_input)





