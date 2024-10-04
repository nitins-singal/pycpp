import pytest
import pandas as pd
from mylyric.naming import Columns as cols



@pytest.fixture(scope="session")
def product_demand_df():
    product_demand_data = {
        cols.P_ID: [1000, 1001, 1002, 1003, 2001, 2002, 2003, 2004],
        cols.L_ID: ["L1", "L2"] * 4,
        cols.DEMAND: [1.0, 2.0] * 4,
    }
    df = pd.DataFrame(product_demand_data)
    return df