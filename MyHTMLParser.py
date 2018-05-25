from html.parser import HTMLParser
from bs4 import BeautifulSoup

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.type_dividendpershare = []
        self.asofdate_dividendpershare = []
        self.reporttype_dividendpershare = []
        self.period_dividendpershare = []
        self.currency_dividendpershare = []
        self.exdate_dividendpershare = []
        self.recorddate_dividendpershare = []
        self.paydate_dividendpershare = []
        self.declarationdate_dividendpershare = []

        self.type_totalrevenue = []
        self.asofdate_totalrevenue = []
        self.reporttype_totalrevenue = []
        self.period_totalrevenue = []
        self.currency_totalrevenue = []
        self.exdate_totalrevenue = []
        self.recorddate_totalrevenue = []
        self.paydate_totalrevenue = []
        self.declarationdate_totalrevenue = []

        self.type_dividend = []
        self.asofdate_dividend = []
        self.reporttype_dividend = []
        self.period_dividend = []
        self.currency_dividend = []
        self.exdate_dividend = []
        self.recorddate_dividend = []
        self.paydate_dividend = []
        self.declarationdate_dividend = []

        self.type_eps = []
        self.asofdate_eps = []
        self.reporttype_eps = []
        self.period_eps = []
        self.currency_eps = []
        self.exdate_eps = []
        self.recorddate_eps = []
        self.paydate_eps = []
        self.declarationdate_eps = []


    def handle_starttag(self, tag, attrs):
        if tag == 'dividendpershare':
            self.type_dividendpershare.append(tag)
            for name, value in attrs:

                if name == 'asofdate':
                    self.asofdate_dividendpershare.append(value)
                if name == 'reporttype':
                    self.reporttype_dividendpershare.append(value)
                if name == 'period':
                    self.period_dividendpershare.append(value)
                if name == 'exdate':
                    self.exdate_dividendpershare.append(value)
                if name == 'recorddate':
                    self.recorddate_dividendpershare.append(value)
                if name == 'paydate':
                    self.paydate_dividendpershare.append(value)
                if name == 'declarationdate':
                    self.declarationdate_dividendpershare.append(value)

        if tag == 'dividendpershares':
            for name, value in attrs:
                if name == 'currency':
                    self.currency_dividendpershare.append(value)
        #if tag == 'financialsummary':
            #print('1111111111')

        if tag == 'totalrevenue':
            self.type_totalrevenue.append(tag)
            for name, value in attrs:
                if name == 'asofdate':
                    self.asofdate_totalrevenue.append(value)
                if name == 'reporttype':
                    self.reporttype_totalrevenue.append(value)
                if name == 'period':
                    self.period_totalrevenue.append(value)
                if name == 'exdate':
                    self.exdate_totalrevenue.append(value)
                if name == 'recorddate':
                    self.recorddate_totalrevenue.append(value)
                if name == 'paydate':
                    self.paydate_totalrevenue.append(value)
                if name == 'declarationdate':
                    self.declarationdate_totalrevenue.append(value)
        if tag == 'totalrevenues':
            for name, value in attrs:
                if name == 'currency':
                    self.currency_totalrevenue.append(value)

        if tag == 'dividend':
            self.type_dividend.append(tag)
            for name, value in attrs:
                #print(name, value)
                if name == 'asofdate':
                    self.asofdate_dividend.append(value)
                if name == 'reporttype':
                    self.reporttype_dividend.append(value)
                if name == 'period':
                    self.period_dividend.append(value)
                if name == 'exdate':
                    self.exdate_dividend.append(value)
                if name == 'recorddate':
                    self.recorddate_dividend.append(value)
                if name == 'paydate':
                    self.paydate_dividend.append(value)
                if name == 'declarationdate':
                    self.declarationdate_dividend.append(value)
        if tag == 'dividends':
            for name, value in attrs:
                if name == 'currency':
                    self.currency_dividend.append(value)

        if tag == 'eps':
            self.type_eps.append(tag)
            for name, value in attrs:
                if name == 'asofdate':
                    self.asofdate_eps.append(value)
                if name == 'reporttype':
                    self.reporttype_eps.append(value)
                if name == 'period':
                    self.period_eps.append(value)
                if name == 'exdate':
                    self.exdate_eps.append(value)
                if name == 'recorddate':
                    self.recorddate_eps.append(value)
                if name == 'paydate':
                    self.paydate_eps.append(value)
                if name == 'declarationdate':
                    self.declarationdate_eps.append(value)
        if tag == 'epss':
            for name, value in attrs:
                if name == 'currency':
                    self.currency_eps.append(value)

class soupparser:
    def __init__(self):
        self.data_dividendpershare = []
        self.data_totalrevenue = []
        self.data_dividend = []
        self.data_eps = []

    def handle_data(self, pd_row):
        soup = BeautifulSoup(pd_row['data'], "html.parser")
        for d in soup.findAll('dividendpershare', {}):
            for text in d.stripped_strings:
                self.data_dividendpershare.append(text)
        for d1 in soup.findAll('totalrevenue', {}):
            for text in d1.stripped_strings:
                self.data_totalrevenue.append(text)
        for d2 in soup.findAll('dividend', {}):
            for text in d2.stripped_strings:
                self.data_dividend.append(text)
        for d3 in soup.findAll('eps', {}):
            for text in d3.stripped_strings:
                self.data_eps.append(text)

        return self


