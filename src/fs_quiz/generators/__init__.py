"""Domain generator modules. Each module registers its topics on import."""
from fs_quiz.generators import boundary_law  # noqa: F401
from fs_quiz.generators import survey_computations  # noqa: F401

__all__ = ["boundary_law", "survey_computations"]
