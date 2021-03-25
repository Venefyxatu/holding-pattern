import pytest

from main import get_reciprocal
from main import get_parallel_limits
from main import get_entry
from main import is_clockwise_between
from main import Entries
from main import Turns


@pytest.mark.parametrize('degrees, reciprocal', [(180, 360), (179, 359), (1, 181), (360, 180), (359, 179), (90, 270)])
def test_reciprocal(degrees, reciprocal):
    assert get_reciprocal(degrees) == reciprocal


@pytest.mark.parametrize('holding_radial, turn, direct_radial, direct_reciprocal',
                         [
                             (90, Turns.RIGHT, 20, 200),
                             (45, Turns.RIGHT, 335, 155),
                             (127, Turns.RIGHT, 57, 237),
                             (251, Turns.RIGHT, 181, 1),
                             (249, Turns.RIGHT, 179, 359),
                             (359, Turns.RIGHT, 289, 109),
                             (1, Turns.RIGHT, 291, 111),
                             (10, Turns.RIGHT, 300, 120),
                             (1, Turns.LEFT, 251, 71)
                         ])
def test_get_parallel_limits(holding_radial, turn, direct_radial, direct_reciprocal):
    assert get_parallel_limits(holding_radial, turn) == (direct_radial, direct_reciprocal)


@pytest.mark.parametrize('holding_radial, turn, direct_radial, direct_reciprocal, inbound_course, entry_type',
                         [
                             (90, Turns.RIGHT, 20, 200, 19, Entries.DIRECT),
                             (90, Turns.RIGHT, 20, 200, 20, Entries.DIRECT),
                             (90, Turns.RIGHT, 20, 200, 21, Entries.TEARDROP),
                             (90, Turns.RIGHT, 20, 200, 199, Entries.PARALLEL),
                             (90, Turns.RIGHT, 20, 200, 200, Entries.DIRECT),
                             (90, Turns.RIGHT, 20, 200, 201, Entries.DIRECT),
                             (90, Turns.RIGHT, 20, 200, 89, Entries.TEARDROP),
                             (90, Turns.RIGHT, 20, 200, 90, Entries.PARALLEL),
                             (90, Turns.RIGHT, 20, 200, 91, Entries.PARALLEL),

                             (45, Turns.RIGHT, 335, 155, 334, Entries.DIRECT),
                             (45, Turns.RIGHT, 335, 155, 335, Entries.DIRECT),
                             (45, Turns.RIGHT, 335, 155, 336, Entries.TEARDROP),
                             (45, Turns.RIGHT, 335, 155, 154, Entries.PARALLEL),
                             (45, Turns.RIGHT, 335, 155, 155, Entries.DIRECT),
                             (45, Turns.RIGHT, 335, 155, 156, Entries.DIRECT),
                             (45, Turns.RIGHT, 335, 155, 44, Entries.TEARDROP),
                             (45, Turns.RIGHT, 335, 155, 45, Entries.PARALLEL),
                             (45, Turns.RIGHT, 335, 155, 46, Entries.PARALLEL),

                             (127, Turns.RIGHT, 57, 237, 56, Entries.DIRECT),
                             (127, Turns.RIGHT, 57, 237, 57, Entries.DIRECT),
                             (127, Turns.RIGHT, 57, 237, 58, Entries.TEARDROP),
                             (127, Turns.RIGHT, 57, 237, 236, Entries.PARALLEL),
                             (127, Turns.RIGHT, 57, 237, 237, Entries.DIRECT),
                             (127, Turns.RIGHT, 57, 237, 238, Entries.DIRECT),
                             (127, Turns.RIGHT, 57, 237, 126, Entries.TEARDROP),
                             (127, Turns.RIGHT, 57, 237, 127, Entries.PARALLEL),
                             (127, Turns.RIGHT, 57, 237, 128, Entries.PARALLEL),

                             (251, Turns.RIGHT, 181, 1, 180, Entries.DIRECT),
                             (251, Turns.RIGHT, 181, 1, 181, Entries.DIRECT),
                             (251, Turns.RIGHT, 181, 1, 182, Entries.TEARDROP),
                             (251, Turns.RIGHT, 181, 1, 360, Entries.PARALLEL),
                             (251, Turns.RIGHT, 181, 1, 1, Entries.DIRECT),
                             (251, Turns.RIGHT, 181, 1, 2, Entries.DIRECT),
                             (251, Turns.RIGHT, 181, 1, 250, Entries.TEARDROP),
                             (251, Turns.RIGHT, 181, 1, 251, Entries.PARALLEL),
                             (251, Turns.RIGHT, 181, 1, 252, Entries.PARALLEL),

                             (249, Turns.RIGHT, 179, 359, 178, Entries.DIRECT),
                             (249, Turns.RIGHT, 179, 359, 179, Entries.DIRECT),
                             (249, Turns.RIGHT, 179, 359, 180, Entries.TEARDROP),
                             (249, Turns.RIGHT, 179, 359, 358, Entries.PARALLEL),
                             (249, Turns.RIGHT, 179, 359, 359, Entries.DIRECT),
                             (249, Turns.RIGHT, 179, 359, 360, Entries.DIRECT),
                             (249, Turns.RIGHT, 179, 359, 248, Entries.TEARDROP),
                             (249, Turns.RIGHT, 179, 359, 249, Entries.PARALLEL),
                             (249, Turns.RIGHT, 179, 359, 250, Entries.PARALLEL),

                             (359, Turns.RIGHT, 289, 109, 288, Entries.DIRECT),
                             (359, Turns.RIGHT, 289, 109, 289, Entries.DIRECT),
                             (359, Turns.RIGHT, 289, 109, 290, Entries.TEARDROP),
                             (359, Turns.RIGHT, 289, 109, 108, Entries.PARALLEL),
                             (359, Turns.RIGHT, 289, 109, 109, Entries.DIRECT),
                             (359, Turns.RIGHT, 289, 109, 110, Entries.DIRECT),
                             (359, Turns.RIGHT, 289, 109, 358, Entries.TEARDROP),
                             (359, Turns.RIGHT, 289, 109, 359, Entries.PARALLEL),
                             (359, Turns.RIGHT, 289, 109, 360, Entries.PARALLEL),

                             (1, Turns.RIGHT, 291, 111, 290, Entries.DIRECT),
                             (1, Turns.RIGHT, 291, 111, 291, Entries.DIRECT),
                             (1, Turns.RIGHT, 291, 111, 292, Entries.TEARDROP),
                             (1, Turns.RIGHT, 291, 111, 110, Entries.PARALLEL),
                             (1, Turns.RIGHT, 291, 111, 111, Entries.DIRECT),
                             (1, Turns.RIGHT, 291, 111, 112, Entries.DIRECT),
                             (1, Turns.RIGHT, 291, 111, 360, Entries.TEARDROP),
                             (1, Turns.RIGHT, 291, 111, 1, Entries.PARALLEL),
                             (1, Turns.RIGHT, 291, 111, 2, Entries.PARALLEL),

                             (1, Turns.LEFT, 251, 71, 250, Entries.DIRECT),
                             (1, Turns.LEFT, 251, 71, 251, Entries.DIRECT),
                             (1, Turns.LEFT, 251, 71, 252, Entries.PARALLEL),
                             (1, Turns.LEFT, 251, 71, 70, Entries.TEARDROP),
                             (1, Turns.LEFT, 251, 71, 71, Entries.DIRECT),
                             (1, Turns.LEFT, 251, 71, 72, Entries.DIRECT),
                             (1, Turns.LEFT, 251, 71, 360, Entries.PARALLEL),
                             (1, Turns.LEFT, 251, 71, 1, Entries.PARALLEL),
                             (1, Turns.LEFT, 251, 71, 2, Entries.TEARDROP),
                          ])
def test_get_entry(holding_radial, turn, direct_radial, direct_reciprocal, inbound_course, entry_type):
    assert get_entry(holding_radial, turn, direct_radial, direct_reciprocal, inbound_course) == entry_type


@pytest.mark.parametrize('radial_a, radial_b, course, result',
                         [
                             (20, 200, 199, False),
                             (20, 200, 200, False),
                             (20, 200, 201, True),
                             (20, 200, 19, True),
                             (20, 200, 20, False),
                             (20, 200, 21, False),

                             (200, 270, 19, False),
                             (200, 270, 20, False),
                             (200, 270, 21, True),
                             (200, 270, 89, True),
                             (200, 270, 90, False),
                             (200, 270, 91, False),

                             (270, 20, 89, False),
                             (270, 20, 90, False),
                             (270, 20, 91, True),
                             (270, 20, 199, True),
                             (270, 20, 200, False),
                             (270, 20, 201, False),


                             (300, 120, 119, False),
                             (300, 120, 120, False),
                             (300, 120, 121, True),
                             (300, 120, 299, True),
                             (300, 120, 300, False),
                             (300, 120, 301, False),

                             (120, 190, 299, False),
                             (120, 190, 300, False),
                             (120, 190, 301, True),
                             (120, 190, 9, True),
                             (120, 190, 10, False),
                             (120, 190, 11, False),

                             (190, 300, 9, False),
                             (190, 300, 10, False),
                             (190, 300, 11, True),
                             (190, 300, 119, True),
                             (190, 300, 120, False),
                             (190, 300, 121, False),

                             (181, 1, 180, True),

                             (251, 71, 250, True),
                             (251, 71, 251, False),
                             (251, 71, 252, False),
                         ])
def test_is_clockwise_between(radial_a, radial_b, course, result):
    assert is_clockwise_between(radial_a, radial_b, course) is result
