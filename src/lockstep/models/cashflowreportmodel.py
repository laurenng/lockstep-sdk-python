#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @version    2022.4
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class CashflowReportModel:
    """
    Represents the cashflow report based on a timeframe
    """

    timeframe: int = None
    paymentsCollected: float = None
    paymentsCollectedCount: int = None
    invoicesBilled: float = None
    invoicesBilledCount: int = None

