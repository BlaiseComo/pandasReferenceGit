import pandas as pd

ad_clicks = pd.read_csv('page_visits.csv')

print(ad_clicks) 


ad_clicks_utm = ad_clicks.groupby('utm_source').user_id.count().reset_index()

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()


print(ad_clicks)

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id').reset_index()

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])


print(clicks_pivot)

ad_clicks_huh = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

ad_clicks_huh = ad_clicks_huh.pivot(columns='is_click', index='experimental_group', values='user_id').reset_index()

ad_clicks_huh['percentage'] = ad_clicks_huh[True] / (ad_clicks_huh[True] + ad_clicks_huh[False])


print(ad_clicks_huh)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_clicks_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
b_clicks_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

a_clicks_day_pivot = a_clicks_day.pivot(columns='is_click', index='day', values='user_id')
b_clicks_day_pivot = b_clicks_day.pivot(columns='is_click', index='day', values='user_id')

a_clicks_day_pivot['percentage'] = a_clicks_day_pivot[True] / (a_clicks_day_pivot[True] + a_clicks_day_pivot[False])
b_clicks_day_pivot['percentage'] = b_clicks_day_pivot[True] / (b_clicks_day_pivot[True] + b_clicks_day_pivot[False])


print(a_clicks_day_pivot)
print(b_clicks_day_pivot)

