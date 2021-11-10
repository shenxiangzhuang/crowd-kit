# fit_predict_scores
`crowdkit.aggregation.embeddings.closest_to_average.ClosestToAverage.fit_predict_scores`

```
fit_predict_scores(
    self,
    data: DataFrame,
    skills: Series = None
)
```

## Parameters Description

| Parameters | Type | Description |
| :----------| :----| :-----------|
`data`|**DataFrame**|<p>Performers&#x27; outputs with their embeddings A pandas.DataFrame containing `task`, `performer`, `output` and `embedding` columns.</p>
`skills`|**Series**|<p>Performers&#x27; skills A pandas.Series index by performers and holding corresponding performer&#x27;s skill</p>

* **Returns:**

  Tasks' label probability distributions
A pandas.DataFrame indexed by `task` such that `result.loc[task, label]`
is the probability of `task`'s true label to be equal to `label`. Each
probability is between 0 and 1, all task's probabilities should sum up to 1

* **Return type:**

  DataFrame