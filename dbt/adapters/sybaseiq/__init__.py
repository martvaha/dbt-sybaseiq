from dbt.adapters.sybaseiq.connections import SybaseIQConnectionManager # noqa
from dbt.adapters.sybaseiq.connections import SybaseIQCredentials
from dbt.adapters.sybaseiq.impl import SybaseIQAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import sybaseiq


Plugin = AdapterPlugin(
    adapter=SybaseIQAdapter,
    credentials=SybaseIQCredentials,
    include_path=sybaseiq.PACKAGE_PATH
    )
