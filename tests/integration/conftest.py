import pytest
import pandas as pd
from mylyric.naming import Columns as cols


@pytest.fixture(scope="session")
def product_demand_df():
    product_demand_data = {
        cols.PRODUCT_ID: [1000, 1001, 1002, 1003, 2001, 2002, 2003, 2004],
        cols.LOCATION_ID: ["L1", "L2"] * 4,
        cols.DEMAND: [1.0, 2.0] * 4,
    }
    df = pd.DataFrame(product_demand_data)
    return df

@pytest.fixture(scope="session")
def bom_df():
    bom_info_data = {
        cols.BOM_ID: [1] * 4,
        cols.BOM_LOCATION_ID: ["L1"] * 4,
        cols.BOM_COMPONENT_ID: [101, 102, 103, 104],
        cols.BOM_PRODUCT_ID: [1000] * 4
    }
    df = pd.DataFrame(bom_info_data)
    return df
