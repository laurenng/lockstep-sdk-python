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
class AppEnrollmentCustomFieldModel:
    """
    App enrollment and custom field merged into one
    """

    appEnrollmentId: str = None
    appId: str = None
    name: str = None
    appType: str = None
    groupKey: str = None
    customFieldDefinitionId: str = None
    customFieldLabel: str = None
    dataType: str = None
    sortOrder: int = None
    stringValue: str = None
    numericValue: float = None

