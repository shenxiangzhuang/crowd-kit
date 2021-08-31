# Crowd-Kit: Computational Quality Control for Crowdsourcing

[![GitHub Tests][github_tests_badge]][github_tests_link]
[![Codecov][codecov_badge]][codecov_link]

[github_tests_badge]: https://github.com/Toloka/crowdlib/workflows/Tests/badge.svg?branch=main
[github_tests_link]: https://github.com/Toloka/crowdlib/actions?query=workflow:Tests
[codecov_badge]: https://codecov.io/gh/Toloka/crowd-kit/branch/main/graph/badge.svg
[codecov_link]: https://codecov.io/gh/Toloka/crowd-kit

**Crowd-Kit** is a powerful Python library that implements commonly-used aggregation methods for crowdsourced annotation and offers the relevant metrics and datasets. We strive to implement functionality that simplifies working with crowdsourced data.

Currently, Crowd-Kit contains:

* implementations of commonly-used aggregation methods for categorical, pairwise, textual, and segmentation responses
* metrics of uncertainty, consistency, and agreement with aggregate
* loaders for popular crowdsourced datasets

*The library is currently in a heavy development state, and interfaces are subject to change.*

## Installing

Installing Crowd-Kit is as easy as `pip install crowd-kit`

## Getting Started

This example shows how to use Crowd-Kit for categorical aggregation using the classical Dawid-Skene algorithm.

First, let us do all the necessary imports.

````python
from crowdkit.aggregation import DawidSkene
from crowdkit.datasets import load_dataset

import pandas as pd
````

Then, you need to read your annotations into Pandas DataFrame with columns `task`, `performer`, `label`. Alternatively, you can download an example dataset.

````python
df = pd.read_csv('results.csv')  # should contain columns: task, performer, label
# df, ground_truth = load_dataset('relevance-2')  # or download an example dataset
````

Then you can aggregate the performer responses as easily as in scikit-learn:

````python
aggregated_labels = DawidSkene(n_iter=100).fit_predict(df)
````

## Implemented Aggregation Methods

### Categorical Responses

|Method|Status|
|-|:-:|
|Majority Vote|✅|
|[Dawid-Skene](https://doi.org/10.2307/2346806)|✅|
|Gold Majority Vote|✅|
|[M-MSR](https://proceedings.neurips.cc/paper/2020/hash/f86890095c957e9b949d11d15f0d0cd5-Abstract.html)|✅|
|Wawa|✅|
|Zero-Based Skill|✅|
|[GLAD](https://papers.nips.cc/paper/3644-whose-vote-should-count-more-optimal-integration-of-labels-from-labelers-of-unknown-expertise.pdf)|🟡|
|BCC|🟡|

### Textual Responses

|Method|Status|
|-|:-:|
|[RASA](https://doi.org/10.18653/v1/D19-5904)|✅|
|[HRRASA](https://doi.org/10.1145/3397271.3401239)|✅|
|[ROVER](https://ieeexplore.ieee.org/document/659110)|✅|

### Image Segmentation

|Method|Status|
|-|:-:|
|Segmentation MV|✅|
|Segmentation RASA|✅|
|Segmentation EM|✅|

### Pairwise Comparisons

|Method|Status|
|-|:-:|
|[Bradley-Terry](https://doi.org/10.2307/2334029)|✅|
|Noisy Bradley-Terry|✅|

## Questions and Bug Reports

For reporting bugs please use the [Toloka/bugreport](https://github.com/Toloka/crowdlib/issues) page.

## License

© YANDEX LLC, 2020-2021. Licensed under the Apache License, Version 2.0. See LICENSE file for more details.
