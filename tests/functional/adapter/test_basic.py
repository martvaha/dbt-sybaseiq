import pytest

from dbt.tests.adapter.basic.test_base import BaseSimpleMaterializations
from dbt.tests.adapter.basic.test_singular_tests import BaseSingularTests
from dbt.tests.adapter.basic.test_singular_tests_ephemeral import (
    BaseSingularTestsEphemeral,
)
from dbt.tests.adapter.basic.test_empty import BaseEmpty
from dbt.tests.adapter.basic.test_ephemeral import BaseEphemeral
from dbt.tests.adapter.basic.test_incremental import BaseIncremental
from dbt.tests.adapter.basic.test_generic_tests import BaseGenericTests
from dbt.tests.adapter.basic.test_snapshot_check_cols import BaseSnapshotCheckCols
from dbt.tests.adapter.basic.test_snapshot_timestamp import BaseSnapshotTimestamp
from dbt.tests.adapter.basic.test_adapter_methods import BaseAdapterMethod


class TestSimpleMaterializationsSybaseIQ(BaseSimpleMaterializations):
    pass


# class TestSingularTestsSybaseIQ(BaseSingularTests):
#     pass


# class TestSingularTestsEphemeralSybaseIQ(BaseSingularTestsEphemeral):
#     pass


# class TestEmptySybaseIQ(BaseEmpty):
#     pass


# class TestEphemeralSybaseIQ(BaseEphemeral):
#     pass


# class TestIncrementalSybaseIQ(BaseIncremental):
#     pass


# class TestGenericTestsSybaseIQ(BaseGenericTests):
#     pass


# class TestSnapshotCheckColsSybaseIQ(BaseSnapshotCheckCols):
#     pass


# class TestSnapshotTimestampSybaseIQ(BaseSnapshotTimestamp):
#     pass


# class TestBaseAdapterMethodSybaseIQ(BaseAdapterMethod):
#     pass
