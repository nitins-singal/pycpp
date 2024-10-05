import pytest
import pandas as pd
from mylyric.naming import Columns as cols
from mylyric.framework import sample_function



def test_calculate():
    assert sample_function() == 8


## This is a test to demonstrate fixtures.
## Where fixtures can be used to create entire dataframes. In this example product_demand_df and bom_df
## are automatically  created as they gets called as a function arguments here
def test_check_fixtures(product_demand_df, bom_df):

    expect_df_data = {
        cols.PRODUCT_ID: [1000, 1001, 1002, 1003, 2001, 2002, 2003, 2004],
        cols.LOCATION_ID: ["L1", "L2"] * 4,
        cols.DEMAND: [1.0, 2.0] * 4,
    }
    expect_product_demand_df = pd.DataFrame(expect_df_data)
    # Note that product_demand_df here is the return of the product_demand_df() fixture in conftest.py !
    assert product_demand_df.equals(expect_product_demand_df) == True

    expect_bom_df_data = {
        cols.BOM_ID: [1] * 4,
        cols.BOM_LOCATION_ID: ["L1"] * 4,
        cols.BOM_COMPONENT_ID: [101, 102, 103, 104],
        cols.BOM_PRODUCT_ID: [1000] * 4
    }
    expect_bom_df = pd.DataFrame(expect_bom_df_data)
    assert bom_df.equals(expect_bom_df) == True


    