# Data Analysis

And finally, now that we have regular, easily grokkable information - how can we do useful things with it? What tools do we have at our disposal to easily make sense of the data we have accumulated?

## THEME: Sports Statistics

🏟️ 🚴 🤺 👟 🏅 🏅

Now that we are familiar with **gathering** data from disparate sources, let's put our newest skills to use **wrangling** these data sources into one, easily grokkable data structure. When dealing with complex and exhaustive data sources, it is no longer enough to just use dicts and lists - their builtin functionalities are simply not enough. 

## Tform HTML to Dict

We will begin our exploration of data by leveraging the **[pandas](https://pandas.pydata.org/pandas-docs/stable/10min.html)** python library, which allows us to store data into a specialized dict called the **DataFrame**. We will explore some of the useful operations we can run on a dataframe in this unit.

To start:

### 1. Pull in data from online

Create a new python file that will use **bs4, requests** to gather data from **[this](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights)** (light) datasource on MLB players and their characteristics.

### 2. Tform the HTML into python dict

Write a small loop that will ingest the table (in HTML) containing player data and transform it into a simple dict with the following fields: `Name, Team, Position, Height, Weight, Age`. 

The dict should be in the following format:

```python
d = {
  'Name': ['Player A', 'Player B', ..., 'Player N'
  'Team': ['Player A\'s Team', 'Player B\'s Team', ..., 'Player N\'s Team',
  ...
  'Age': ['A\'s age', ..., 'N\'s age',
}
```

### 3. Import Pandas into PyCharm

You should import it as follows:

```python
import pandas as pd
```

Then, create a pandas **DataFrame** object:

```
df = pd.DataFrame(d)
```

Explore this object a bit - how can you view it? What can you do with it? In particular, run the following commands on your object:

1. `df.dtypes` - what does this give you?
2. `df.head()`, `df.tail()`, `df.tail(3)`
3. `df.index`, `df.columns`, `df.values`,
4. `df.describe`
5. `df.T`
6. `df.sort_index(axis=1, ascending=False)`
7. `df.sort_values(by='Age')`

### 3. Selecting stuff from DataFrames

Continuing our exploration, let's see how we can grab swaths of data for manipulation or analysis...
(print out results of all these items and ensure they are what you expect)

1. Select by column name: `df['Name']`
2. Or, `df.loc[:,['Name', 'Position']]`
3. If you know a row to select: `df.iloc[3]`

### 4. Now, for the fun part...

Using the dataframe only, answer the following questions:

1. Let's calculate the BMI of all our players. Using the DataFrame, create a new **Series** (panda concept, look it up!) that stores player BMIs. Concat this Series back to original dataframe
2. Let's define BMI > 24 to be overweight. How many players in our dataset are overweight...?
3. Look for and track age distribution for players (ie: how many are 25? 26? etc)


### 5 Additional Practice!

* [Pandas exercises](https://www.machinelearningplus.com/python/101-pandas-exercises-python/)
* [Pandas puzzles](https://github.com/ajcr/100-pandas-puzzles/blob/master/100-pandas-puzzles.ipynb) / [Pandas solutions](https://github.com/ajcr/100-pandas-puzzles/blob/master/100-pandas-puzzles-with-solutions.ipynb)
* [Loan Prediction Problem](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-learn-data-science-python-scratch-2/)
* [Kaggle: free datasets for analysis](https://www.kaggle.com/)
* [24 other data exercises w/python](https://www.analyticsvidhya.com/blog/2018/05/24-ultimate-data-science-projects-to-boost-your-knowledge-and-skills/)
