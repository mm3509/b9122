import sys
import exercise_1_exchange


def convert_from_command_line(amount, src, dst, print):

    converted = exercise_1_exchange.convert(amount, src, dst)

    if print:
        print(f"{src} {amount:,.2f} = {dst} {converted:,.2f}")

    return converted


if '__main__' == __name__:
    args = sys.argv
    if 4 != len(args):
        err_msg = ("Usage: python exercise_7_debug.py "
                   "<amount> <source-currency> <destination-currency>")
        raise ValueError(err_msg)

    amount = float(args[1])
    src = args[2]
    dst = args[3]

    convert_from_command_line(amount, src, dst, print=True)
