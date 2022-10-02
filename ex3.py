import pytz
import snscrape.modules
import datetime as dt
from datetime import timezone
import pandas as pd




def exercise_3():

    keyword = "Bitcoin"

    datenow = dt.datetime.now(pytz.timezone('UTC'))
    time_delta = dt.timedelta(minutes=380)
    search_date =  datenow-time_delta
    pd_dataframe = pd.DataFrame(columns=['author', 'lang', 'internal_id', 'hashtags', 'content'])


    for i, _post in enumerate(snscrape.modules.twitter.TwitterSearchScraper('(about:{}) since_time:{}'.format(keyword, int(search_date.timestamp()))).get_items()):
        
        if i < 10:
            post = _post.__dict__
            tr_post = dict()
            tr_post["internal_id"] = post["id"]
            tr_post["content"] = post["content"]
            tr_post["hashtags"] = post["hashtags"] if post["hashtags"] else []
            tr_post["author"] = post["user"].displayname
            tr_post["lang"] = post["lang"]

            pd_dataframe = pd_dataframe.append(tr_post, ignore_index=True)
        else:
            break


    # Get unique Hastags from the df 
    exploded = pd_dataframe["hashtags"].explode().unique() 
    cleaned = [x.lower() for x in exploded if str(x) != 'nan']
    unique = set(cleaned)

    print('Unique hastags are {}'.format(unique))



if __name__ == "__main__":
    exercise_3()