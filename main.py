import pandas as pd
import plotly.express as px

df = pd. \
    read_csv('voting.csv', header=0). \
    fillna(
    value={'Year': -1, 'Presidential Candidate': "Votes Not Cast", 'Party': "No Political Party",
           'Electoral Votes': 0}). \
    groupby(['Year', 'Party']). \
    agg({'Electoral Votes': ['sum'], 'Presidential Candidate': ', '.join}). \
    reset_index(). \
    set_axis(["Year", "Party", "Electoral Votes", "Presidential Candidates"], axis=1)
df = df[df.Party.duplicated(keep=False)]

colormap = {
    'Democratic': 'blue',
    'Republican': 'red'
}
graph = px.line(df,
                x='Year',
                y='Electoral Votes',
                color='Party',
                hover_name='Party',
                hover_data=['Presidential Candidates'],
                color_discrete_map=colormap)
graph.write_html('index.html')
