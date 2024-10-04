import pytest
import pandas as pd
from mylyric.naming import Columns as cols
from mylyric.framework import sample_function



def test_calculate():
    assert sample_function() == 8


## This is a test to demonstrate fixtures.
## Where fixtures can be used to create entire dataframes. In this example product_demand_df is automatically 
## created as it gets called as a function argument here
def test_check_fixtures(product_demand_df):

    expect_df_data = {
        cols.P_ID: [1000, 1001, 1002, 1003, 2001, 2002, 2003, 2004],
        cols.L_ID: ["L1", "L2"] * 4,
        cols.DEMAND: [1.0, 2.0] * 4,
    }
    expect_df = pd.DataFrame(expect_df_data)
    # Note that product_demand_df here is the return of the product_demand_df() fixture in conftest.py !
    assert product_demand_df.equals(expect_df) == True

    