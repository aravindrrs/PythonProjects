from yahoofinancials import YahooFinancials as yf 
import pandas as pd
import json 
yahootech = yf (['SQ'])
cashflowjason= yahootech.get_financial_stmts('annual','cash')
cashflow = cashflowjason.get('cashflowStatementHistory'or {}).get('SQ')
print (type(cashflow))
print (cashflow)
# cashflowTable = pd.DataFrame.from_dict(cashflow)
# print (cashflowTable)