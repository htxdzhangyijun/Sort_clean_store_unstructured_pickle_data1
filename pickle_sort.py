import pickle
import pandas as pd
from MyHTMLParser import MyHTMLParser
import numpy as np
from DBconnection import DBconnection
from MyHTMLParser import soupparser


#make SQL connection
connect1 = DBconnection("postgresql", "psycopg2", "postgres",
                        "postgres", "localhost", "5432", "local_dev", 50)
engine = connect1.DBengine()

#read pickle files
objects = []
with (open("fundamental_data.pkl", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break

#convert list file to pandas dataframe
df = pd.DataFrame(objects).T
df.columns = ['column1']
df = pd.DataFrame(df.column1.values.tolist())


def table_maker(pd_row):
    #read data from html-like file
    h = MyHTMLParser()
    h.feed(pd_row['data'])
    soup = soupparser()
    p = soup.handle_data(pd_row)
    dividendpershare = [h.type_dividendpershare, h.asofdate_dividendpershare, h.reporttype_dividendpershare,
                        h.period_dividendpershare, h.currency_dividendpershare, p.data_dividendpershare,
                        h.exdate_dividendpershare, h.recorddate_dividendpershare, h.paydate_dividendpershare,
                        h.declarationdate_dividendpershare]
    totalrevenue = [h.type_totalrevenue, h.asofdate_totalrevenue, h.reporttype_totalrevenue,
                    h.period_totalrevenue, h.currency_totalrevenue, p.data_totalrevenue,
                    h.exdate_totalrevenue, h.recorddate_totalrevenue, h.paydate_totalrevenue,
                    h.declarationdate_totalrevenue]
    dividend = [h.type_dividend, h.asofdate_dividend, h.reporttype_dividend,
                h.period_dividend, h.currency_dividend, p.data_dividend,
                h.exdate_dividend, h.recorddate_dividend, h.paydate_dividend,
                h.declarationdate_dividend]
    eps = [h.type_eps, h.asofdate_eps, h.reporttype_eps,
           h.period_eps, h.currency_eps, p.data_eps,
           h.exdate_eps, h.recorddate_eps, h.paydate_eps, h.declarationdate_eps]

    #sort data and make it into a dataframe
    names = ['type', 'asofdate', 'reporttype', 'period', 'currency','data',
             'exdate', 'recorddate', 'paydate', 'declarationdate']
    def make_dataframe(list1):
        dict1 = {names[i]: list1[i] for i in range(10)}
        dataframe1 = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in dict1.items()]))
        dataframe1 = dataframe1.fillna(method='ffill')
        return dataframe1

    dividendpershare_dataframe = make_dataframe(dividendpershare)
    totalrevenue_dataframe = make_dataframe(totalrevenue)
    dividend_dataframe = make_dataframe(dividend)
    eps_dataframe = make_dataframe(eps)

    table1 = pd.concat([dividendpershare_dataframe, totalrevenue_dataframe,
                        dividend_dataframe, eps_dataframe], axis = 0, ignore_index=True)

    reqId1 = [pd_row['reqId']] * len(table1['type'])
    table1['reqId'] = pd.Series(np.array(reqId1), index = table1.index)

    #format each column to put into sql
    table1['type'] = table1['type'].astype(str)
    table1['reporttype'] = table1['reporttype'].astype(str)
    table1['period'] = table1['period'].astype(str)
    table1['asofdate'] = pd.to_datetime(table1['asofdate'])
    table1['exdate'] = pd.to_datetime(table1['exdate'])
    table1['recorddate'] = pd.to_datetime(table1['recorddate'])
    table1['paydate'] = pd.to_datetime(table1['paydate'])
    table1['declarationdate'] = pd.to_datetime(table1['declarationdate'])

    #drop_duplicate line
    table1 = table1.drop_duplicates()

    return table1


#use for loop to concat dataframe
table = pd.DataFrame()
for i, row in df.iterrows():
    table = pd.concat([table, table_maker(row)], axis = 0, ignore_index=True)

#put the dataframe into a sql_table
table.to_sql('data_ib_equity_fundamental', engine, if_exists='replace',index=False)


#print(table_maker(df.iloc[1000]))
#print(table)

