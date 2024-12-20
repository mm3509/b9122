import doctest

###########################################################################
#
# TODO: Complete this section to import modules, until the next
# heading similar to this one
#
###########################################################################
import compound_interest

###########################################################################
#
# Your imports should end here.
#
###########################################################################


def check_value_with_rounding(value1, value2):
    return abs(value1 - value2) <= 0.02


def calculate_interest_differential(balance,
                                    baseline_rate,
                                    bonus_rate,
                                    transactions):
    """
    Calculate the compound interest paid monthly on the balance of a
    bank account, recursively.

    Args:
      balance: Current balance of the account at the start of the calculation.
      rate: Annual interest rate (as a decimal, e.g., 0.05 for 5%).
      transactions: A list of tuples representing transactions (day, amount).
          Positive amounts are deposits, negative are withdrawals.

    Returns:
      The interest rate to be paid at the end of the month.

    Note: Each doc-test has a comment at the start describing the case.

    >>> # Simple example.
    >>> i = calculate_interest_differential(1000, 0.02, 0.04, [])
    >>> check_value_with_rounding(3.23, i)
    True
    >>> # Simple example, constructed another way.
    >>> i = calculate_interest_differential(0, 0.02, 0.04, [(0, 1000)])
    >>> check_value_with_rounding(3.23, i)
    True
    >>> # Example with a withdrawal.
    >>> i = calculate_interest_differential(1000, 0.02, 0.04, [(29, -1)])
    >>> check_value_with_rounding(1.63, i)
    True
    >>> # Example with credits and withdrawals.
    >>> transactions = [(5, 500), (10, -200), (20, 100)]
    >>> i = calculate_interest_differential(1000, 0.02, 0.04, transactions)
    >>> check_value_with_rounding(2.14, i)
    True
    >>> # The interest rate has to compound daily.
    >>> i = calculate_interest_differential(10000, 0.02, 0.05, [])
    >>> check_value_with_rounding(40.18, i)
    True
    """

    ###########################################################################
    #
    # TODO: Complete the rest of this function, until the next heading
    # similar to this one
    #
    ###########################################################################
    rate = bonus_rate
    for _, amount in transactions:
        if amount < 0:
            rate = baseline_rate
            break

    return compound_interest.calculate_interest(balance, rate, transactions)

    ###########################################################################
    #
    # Your function should end here. You can write or edit code below
    # this point to help you solve the assignment, but it will not be
    # tested nor graded.
    #
    ###########################################################################


initial_balance = 1000
baseline_rate = 0.008
bonus_rate = 0.066

# Transactions: day 5 deposit 500, day 10 withdraw 200, day 20 deposit 100.
transactions = []
print(calculate_interest_differential(initial_balance, baseline_rate, bonus_rate, transactions))
