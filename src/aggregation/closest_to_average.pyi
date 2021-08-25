__all__ = [
    'ClosestToAverage',
]
import crowdkit.aggregation.base_aggregator
import pandas.core.frame
import pandas.core.series
import typing


class ClosestToAverage(crowdkit.aggregation.base_aggregator.BaseAggregator):
    """Majority Vote - chooses the correct label for which more performers voted
    Attributes:
        outputs_ (DataFrame): Tasks' most likely true labels
            A pandas.Series indexed by `task` such that `labels.loc[task]`
            is the tasks's most likely true label.

        scores_ (DataFrame): Tasks' label probability distributions
            A pandas.DataFrame indexed by `task` such that `result.loc[task, label]`
            is the probability of `task`'s true label to be equal to `label`. Each
            probability is between 0 and 1, all task's probabilities should sum up to 1
    """

    def fit(
        self,
        data: pandas.core.frame.DataFrame,
        aggregated_embeddings: pandas.core.series.Series = None,
        true_embeddings: pandas.core.series.Series = None
    ) -> 'ClosestToAverage':
        """Args:
            data (DataFrame): Performers' outputs with their embeddings
                A pandas.DataFrame containing `task`, `performer`, `output` and `embedding` columns.
            aggregated_embeddings (Series): Tasks' embeddings
                A pandas.Series indexed by `task` and holding corresponding embeddings.
            true_embeddings (Series): Tasks' embeddings
                A pandas.Series indexed by `task` and holding corresponding embeddings.
        Returns:
            ClosestToAverage: self
        """
        ...

    def fit_predict_scores(
        self,
        data: pandas.core.frame.DataFrame,
        skills: pandas.core.series.Series = None
    ) -> pandas.core.frame.DataFrame:
        """Args:
            data (DataFrame): Performers' outputs with their embeddings
                A pandas.DataFrame containing `task`, `performer`, `output` and `embedding` columns.
            skills (Series): Performers' skills
                A pandas.Series index by performers and holding corresponding performer's skill
        Returns:
            DataFrame: Tasks' label probability distributions
                A pandas.DataFrame indexed by `task` such that `result.loc[task, label]`
                is the probability of `task`'s true label to be equal to `label`. Each
                probability is between 0 and 1, all task's probabilities should sum up to 1
        """
        ...

    def fit_predict(
        self,
        data: pandas.core.frame.DataFrame,
        skills: pandas.core.series.Series = None
    ) -> pandas.core.frame.DataFrame:
        """Args:
            data (DataFrame): Performers' outputs with their embeddings
                A pandas.DataFrame containing `task`, `performer`, `output` and `embedding` columns.
            skills (Series): Performers' skills
                A pandas.Series index by performers and holding corresponding performer's skill
        Returns:
            DataFrame: Tasks' most likely true labels
                A pandas.Series indexed by `task` such that `labels.loc[task]`
                is the tasks's most likely true label.
        """
        ...

    def __init__(self, distance: typing.Callable[[..., ...], float]) -> None:
        """Method generated by attrs for class ClosestToAverage.
        """
        ...

    outputs_: pandas.core.frame.DataFrame
    scores_: pandas.core.frame.DataFrame
    distance: typing.Callable[[..., ...], float]
