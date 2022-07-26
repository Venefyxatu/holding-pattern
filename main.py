import random
from argparse import ArgumentParser
from enum import Enum, auto


class Turns(Enum):
    RIGHT = 'right'
    LEFT = 'left'


class Entries(Enum):
    DIRECT = auto()
    PARALLEL = auto()
    TEARDROP = auto()


def get_reciprocal(degrees):
    if degrees > 180:
        return degrees - 180
    else:
        return degrees + 180


def get_parallel_limits(holding_radial, turn):
    if turn == Turns.RIGHT:
        if holding_radial < 71:
            direct_radial = holding_radial + 290
        else:
            direct_radial = holding_radial - 70

        direct_reciprocal = get_reciprocal(direct_radial)
    else:
        if holding_radial < 291:
            direct_reciprocal = holding_radial + 70
        else:
            direct_reciprocal = holding_radial - 290

        direct_radial = get_reciprocal(direct_reciprocal)


    return direct_radial, direct_reciprocal


def is_clockwise_between(radial_a, radial_b, course):
    """Check whether a course falls clockwise between two radials
    Edges are always False"""

    reciprocal_course = get_reciprocal(course)

    if reciprocal_course == radial_a or reciprocal_course == radial_b:
        return False

    if radial_a < radial_b and reciprocal_course in range(radial_a, radial_b + 1):
        return True
    elif radial_a > radial_b and (reciprocal_course in range(radial_a, 360 + 1) or
                                  reciprocal_course in range(1, radial_b + 1)):
        return True
    else:
        return False


def get_entry(holding_radial, turn, direct_radial, direct_reciprocal, inbound_course):
    holding_reciprocal = get_reciprocal(holding_radial)

    if inbound_course == direct_radial or inbound_course == direct_reciprocal:
        return Entries.DIRECT
    elif inbound_course == holding_radial:
        return Entries.PARALLEL
    elif is_clockwise_between(direct_radial, direct_reciprocal, inbound_course):
        return Entries.DIRECT
    elif is_clockwise_between(direct_reciprocal, holding_reciprocal, inbound_course):
        if turn == Turns.RIGHT:
            return Entries.TEARDROP
        else:
            return Entries.PARALLEL
    elif is_clockwise_between(holding_reciprocal, direct_radial, inbound_course):
        if turn == Turns.RIGHT:
            return Entries.PARALLEL
        else:
            return Entries.TEARDROP
    else:
        raise ValueError(f'''Unhandled edge case: {holding_radial}, {turn.value}, {direct_radial}, '''
                         f'''{direct_reciprocal}, {inbound_course}''')


def quiz(args):
    for x in range(1, args.questions + 1):
        print(80 * '-')
        print(f'Question {x}')

        holding_radial = random.randint(1, 360)

        turn = random.choice([t for t in Turns])

        direct_radial, direct_reciprocal = get_parallel_limits(holding_radial, turn)

        inbound_course = random.randint(1, 360)

        correct_answer = get_entry(holding_radial, turn, direct_radial, direct_reciprocal, inbound_course)

        answer = None
        while answer not in [e.value for e in Entries]:
            print(80 * '-')
            print(f'''Choose entry method for holding on radial {holding_radial} with {turn.value} turn '''
                  f'''and arriving on course {inbound_course}.''')
            for entry in Entries:
                print(f'  {entry.value} {entry.name}')

            try:
                answer = int(input('Your answer? '))
            except ValueError:
                print(80 * '=')
                print(f'Please enter a value of {[e.value for e in Entries]}')
                print(80 * '=')

        if answer == correct_answer.value:
            print('That is correct')
        else:
            print(f'That should have been {correct_answer.value}. {correct_answer.name}')


def calc(args):
    direct_radial, direct_reciprocal = get_parallel_limits(args.holding_radial, args.turn)

    entry = get_entry(args.holding_radial, args.turn, direct_radial, direct_reciprocal, args.inbound)

    print(f'Use a {entry.name} entry')


def main():
    parser = ArgumentParser()

    subparsers = parser.add_subparsers()

    quiz_parser = subparsers.add_parser('quiz', help='Quiz mode')
    quiz_parser.add_argument('--questions', type=int, default=5, help='How many questions to ask')
    quiz_parser.set_defaults(func=quiz)

    calc_parser = subparsers.add_parser('calc', help='Calculator mode')
    calc_parser.add_argument('--inbound', type=int, required=True, help='Inbound course to the holding point')
    calc_parser.add_argument('--holding-radial', type=int, required=True, help='Hold radial as given by ATC or plate')
    calc_parser.add_argument('--turn', type=str, default=Turns.RIGHT.value, choices=[t.value for t in Turns],
                             help='Turn direction (defaults to right)')
    calc_parser.set_defaults(func=calc)

    args = parser.parse_args()
    if hasattr(args, 'turn'):
        args.turn = Turns[args.turn.upper()]
    args.func(args)


if __name__ == '__main__':
    main()
