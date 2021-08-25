__all__ = [
    'Annotation',
    'manage_docstring',
    'EMBEDDED_DATA',
    'DATA',
    'LABELED_DATA',
    'PAIRWISE_DATA',
    'SEGMENTATION_DATA',
    'LABEL_PRIORS',
    'LABEL_SCORES',
    'TASKS_EMBEDDINGS',
    'TASKS_LABELS',
    'TASKS_LABEL_PROBAS',
    'TASKS_LABEL_SCORES',
    'TASKS_TRUE_LABELS',
    'SEGMENTATIONS',
    'SEGMENTATION',
    'SEGMENTATION_ERRORS',
    'IMAGE_PIXEL_PROBAS',
    'TASKS_SEGMENTATIONS',
    'BIASES',
    'SKILLS',
    'ERRORS',
    'WEIGHTED_DATA',
    'WEIGHTS',
    'OPTIONAL_SCORES',
    'OPTIONAL_SKILLS',
    'OPTIONAL_PROBAS',
    'OPTIONAL_PRIORS',
    'OPTIONAL_LABELS',
    'OPTIONAL_ERRORS',
    'OPTIONAL_WEIGHTS',
]
import typing


class Annotation:
    def format_google_style_attribute(self, name: str) -> str: ...

    def format_google_style_return(self): ...

    def __init__(
        self,
        type: typing.Optional[typing.Type] = None,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None
    ) -> None:
        """Method generated by attrs for class Annotation.
        """
        ...

    type: typing.Optional[typing.Type]
    title: typing.Optional[str]
    description: typing.Optional[str]


def manage_docstring(obj): ...


EMBEDDED_DATA = ...

DATA = ...

LABELED_DATA = ...

PAIRWISE_DATA = ...

SEGMENTATION_DATA = ...

LABEL_PRIORS = ...

LABEL_SCORES = ...

TASKS_EMBEDDINGS = ...

TASKS_LABELS = ...

TASKS_LABEL_PROBAS = ...

TASKS_LABEL_SCORES = ...

TASKS_TRUE_LABELS = ...

SEGMENTATIONS = ...

SEGMENTATION = ...

SEGMENTATION_ERRORS = ...

IMAGE_PIXEL_PROBAS = ...

TASKS_SEGMENTATIONS = ...

BIASES = ...

SKILLS = ...

ERRORS = ...

WEIGHTED_DATA = ...

WEIGHTS = ...

OPTIONAL_SCORES = ...

OPTIONAL_SKILLS = ...

OPTIONAL_PROBAS = ...

OPTIONAL_PRIORS = ...

OPTIONAL_LABELS = ...

OPTIONAL_ERRORS = ...

OPTIONAL_WEIGHTS = ...
