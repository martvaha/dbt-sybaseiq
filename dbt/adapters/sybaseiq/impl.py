from dbt.adapters.sql import SQLAdapter as adapter_cls

from dbt.adapters.sybaseiq import SybaseIQConnectionManager


class SybaseIQAdapter(adapter_cls):
    """
    Controls actual implmentation of adapter, and ability to override certain methods.
    """

    ConnectionManager = SybaseIQConnectionManager

    @classmethod
    def date_function(cls):
        """
        Returns canonical date func
        """
        return "now()"

    @classmethod
    def is_cancelable(cls):
        """
        Returns whether the adapter is cancelable
        """
        return False


# may require more build out to make more user friendly to confer with team and community.
