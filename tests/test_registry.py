"""Registry tests: every expected topic registered and discoverable."""
from fs_quiz import registry
from fs_quiz import engine  # noqa: F401  (imports register generator modules)


EXPECTED_SURVEY_COMPUTATIONS_TOPICS = [
    "angular-misclosure",
    "area-coordinates",
    "bowditch",
    "error-propagation",
    "forward",
    "horizontal-curve",
    "inverse",
    "level-notes",
    "stadia",
    "traverse-misclosure",
    "vertical-curve",
    "volumes",
]


def test_survey_computations_topics_registered():
    assert registry.list_topics("survey-computations") == EXPECTED_SURVEY_COMPUTATIONS_TOPICS


def test_get_generator_round_trip():
    for topic in EXPECTED_SURVEY_COMPUTATIONS_TOPICS:
        fn = registry.get_generator("survey-computations", topic)
        assert callable(fn)
        assert fn._fs_domain == "survey-computations"
        assert fn._fs_topic == topic


def test_unknown_generator_raises():
    try:
        registry.get_generator("survey-computations", "nope")
    except KeyError:
        pass
    else:
        raise AssertionError("expected KeyError")
