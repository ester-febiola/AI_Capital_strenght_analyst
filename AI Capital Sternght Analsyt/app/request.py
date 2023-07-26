import requests

url = 'http://127.0.0.1:5000/api'

r = requests.post(url, json={ 
                                'debt_to_equity_ratio':               1.00,
                                'debt_to_asset_ratio':                0.44,
                                'accounts_receivable_turnover':       0.19,
                                'Inventory_turnover':                 0.17,
                                'return_on_assets':                   0.20,
                                'interest_coverage_ratio':            0.00,
                                'accounts_payable_turnover':          0.05,
                                'Gross_profit_margin':                0.82,
                                'debt_to_equity_ratio_cat':           2.00,
                                'debt_to_asset_ratio_cat':            2.00,
                                'accounts_receivable_turnover_cat':   2.00,
                                'Inventory_turnover_cat':             1.00,
                                'return_on_assets_cat':               1.00,
                                'interest_coverage_ratio_cat':        2.00,
                                'Accounts_payable_turnover_cat':      2.00,
                                'Market_conditions':                  2.00,
                                'Gross_profit_margin_cat':            2.00,
                                'cash_flow_operation_cat':            1.00,
                                'cash_flow_financing_cat':            1.00,
                                'cash_flow_invest_cat':               1.00,
                                'cash_flow':                          1.00
                              })
print(r.json())