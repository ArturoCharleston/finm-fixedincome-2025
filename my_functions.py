from scipy.optimize import fsolve
import pandas as pd
import datetime

def pv(rate, cashflows, maturities,freq=1):
    price = sum([cfi/(1+rate/freq)**(maturities[i]*freq) for i, cfi in enumerate(cashflows)])
    return price

def compound_rate(intrate,compound_input,compound_output):
    
#    outrate = intrate[['maturity']]
    
    if compound_input is None:
        outrate = compound_output * (np.exp(intrate/compound_output) - 1)
    elif compound_output is None:
        outrate = compound_input * np.log(1 + intrate/compound_input)
    else:
        outrate = ((1 + intrate/compound_input) ** (compound_input/compound_output) - 1) * compound_output

    return outrate

def get_coupon_dates(quote_date,maturity_date):

    if isinstance(quote_date,str):
        quote_date = datetime.datetime.strptime(quote_date,'%Y-%m-%d')
        
    if isinstance(maturity_date,str):
        maturity_date = datetime.datetime.strptime(maturity_date,'%Y-%m-%d')
    
    # divide by 180 just to be safe
    temp = pd.date_range(end=maturity_date, periods=np.ceil((maturity_date-quote_date).days/180), freq=pd.DateOffset(months=6))
    # filter out if one date too many
    temp = pd.DataFrame(data=temp[temp > quote_date])

    out = temp[0]
    return out
    
def calc_cashflows(quote_data, coupon_payments = 2, face_value = 100):
    CF = pd.DataFrame(data=0, index=quote_data.index, columns=quote_data['maturity date'].unique())

    for i in quote_data.index:
        coupon_dates = get_coupon_dates(quote_data.loc[i, 'quote date'], quote_data.loc[i, 'maturity date'])

        if coupon_dates is not None:
            CF.loc[i, coupon_dates] = quote_data.loc[i, 'cpn rate'] / coupon_payments # It is assuming semi-annual coupon rate payments

        CF.loc[i, quote_data.loc[i, 'maturity date']] += face_value # On bond's maturity (final payment), add 100 to the cash flows. This assumes that the bond has a face value (par value) of 100. 

    CF = CF.fillna(0).sort_index(axis=1)
    CF.drop(columns=CF.columns[CF.sum() == 0], inplace=True)
    
    return CF
