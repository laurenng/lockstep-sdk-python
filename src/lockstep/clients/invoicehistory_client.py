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

from lockstep.lockstep_response import LockstepResponse

class InvoiceHistoryClient:

    def __init__(self, client):
        self.client = client

    def retrieve_invoice_history(self, id: str) -> LockstepResponse:
        """
        Retrieves the history of the Invoice specified by this unique
        identifier.

        An Invoice represents a bill sent from one company to another.
        The Lockstep Platform tracks changes to each Invoice so that you
        can observe the changes over time. You can view the
        InvoiceHistory list to monitor and observe the changes of this
        Invoice and track the dates when changes occurred.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this invoice; NOT
            the customer's ERP key
        """
        path = f"/api/v1/InvoiceHistory/{id}"
        return self.client.send_request("GET", path, None, {"id": id})

    def query_invoice_history(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        """
        Queries Invoice History for this account using the specified
        filtering, sorting, and pagination rules requested.

        An Invoice represents a bill sent from one company to another.
        The Lockstep Platform tracks changes to each Invoice so that you
        can observe the changes over time. You can view the
        InvoiceHistory list to monitor and observe the changes of this
        Invoice and track the dates when changes occurred.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. No collections are currently available
            for querying but may be available in the future.
        order : str
            The sort order for this query. See See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageSize : int
            The page size for results (default 200). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = f"/api/v1/InvoiceHistory/query"
        return self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber})
