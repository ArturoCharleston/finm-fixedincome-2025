# Theory

## Week 0
- Yield Curve 
1. Relationship between a Bond Yield (Y-axis) and its Maturity (x-axis).  
2. The yield curve gives us an idea, at certain point in time (it is not a time series; it is a snapshot at a moment in time) of how bonds are being priced. It says, if you buy a bond TODAY that matures in 6 months, 1 year, 2 years, etc, that is the pricing (yield). 
3. Yield surface is the time series version when you overlap the different snapshots of daily yield curves
4. Yield Curve at 30 years (e.g) is not the 'expected FED Fund rates' because FED only affect short term. However, short term FED affect a lot of longer term rates in levels. 
5. A Yield is a price. It is an alternative way to quote the price, it serves as a benchmark. Prefered way of viewing yield. By definition, it is just an alternative way to quote a price. 
6. Yield Curve is not certain of how much are we getting, it is an annualized rate not across the x year, but in addition we are not sure that we can reinvest at the same interest rate. It assumes that the coupons are reinvested at the same rate. 
7. The yield is NOT a return, it is only a return if three things happens. 1) It is annualized, 2) You can reinvest the coupons at the same rate, 3) You hold it to maturity. If any of these do not happen, then it is not the return. Its connection to return is a little bit tenuous. 
8. I know the yield for each instrument as of today because I know their prices as of today, and I know what their final payoff will be. 
9. Why do we prefer the yield instead of the price? There is a time preference. The yield is factoring in how soon it matures, it is normalizing for that. It is also normalizing for different coupon rates. Prices change dramatically for their different coupons and different maturities. Yield to maturity is a simple way to normalize it. 
10. We do not have one issue that matures in certain date, they have several maturing at similar maturities. At any given point you do not have some perfect timing, so you need to make decisions to generate the yield curve. 
11. YTM is an alternate way to quote a price. For a zero-coupon bond held to maturity, it is the annualized return. Beyond that, it is not that helpful. It is not a discount rate. You cannot use Yield-To-Maturity to price a different security, the yield to maturity only prices itself. 
12. Yield Curve is usually upward slopping. However, now it is downward slopping (inverted yield curve).

Fixed income products
1. Bills: Less than a year, interest paid a maturity (it is sell at a discount)
2. Treasury Bonds: More than 10 years, 20 or 30 years, paid interest every 6 months
3. Treasury Notes: 2,3,5,7,10 years, paid interest every 6 months

Yield-To-Maturity
1. It is a concept of price. A way to evaluate a bond. 
2. Internal Rate of Return, Is the discount rate for that particular bond, it is not given, it is found given the cashflows and price. 
3. What is the rate that will make this price a reality given these cash flows?
4. If you have the cashflows, and yield-to-maturity, you can get the price
5. Yield-to-Maturity (X-axis) vs Price (y-axis) it has a NEGATIVE and non linear relationship

## Week 1

- The yield to maturity (YTM) is the rate of return that equates the present value (PV) of all future bond cash flows to the bond's current price. 
- Price of a bond $P = \sum_{i=1}^{N} \frac{C}{(1 + Y)^i} + \frac{F}{(1 + Y)^N}$, where P = Bond price, C = Coupon payment ($F*c/f$), F is the face value of the bond, N is the number of periods ($T*f$) where T is the time to maturity and $f$ is the payment frequency, Y: Yield per period (YTM/f). 
- The YTM equation does not have a closed-form analytical solution, so we use non linear solvers to find the YTM. 

- Solver functions: 
1. pv_wrapper: Calculate the difference between the actual bond price (P) and the price calculated using the price_bond function for a given y (YTM). Then simply find the root
2. 

Cashflow Matrix
- Each row is a treasury
- Each column is a date
- It is lower diagonal when filtered. The very top only pays once, then it is all zeros, the second one pays twice, then all zeros, the very bottom one pays out all the way. 
- The columns will be linear independent, so it will be invertible. 
- When it is invertible, in fixed income they call it bootstrapping the curve


Spot Discount Curve
- It is also called the zero-curve. 
- 

Spot Discount Rates Methods
1. Bootstrapping
- a) You need to filter some data
- b) You need to have a square system to drop them. You want to end with the same amount of columns and same amount of rows
- c) You drop rows from the cashflows, and you will only drop columns if they are zero only
- d) You want to have one face value payment per maturity, for bootstrap and OLS
- e) It is when you have a exactly identified linear system of equations. Unique solutions, square matrix. If not, then we use OLS. 
You need to remove duplicates, you get rid of negative maturities
2. OLS
- a) Overidentified system, you don't need a square system. It works when you have more data than what you need. 
- b) You solve $p = Cz + e$. It is a linear projection
- c) You can use Weighted Least Squares if you are interested in putting more attention to some of those. Least Squares pay equal attention to every observation.  
3. Nielson-Siegel
- a) We need a model that avoids: Missing data problem, overfitting in-sample
- b) This model controls for: Level, Slope, and Curvature
- c) Downside: If I give the wrong structure, then I'm going to get a very precise measure of a biased thing.
- d) Idea: First create discount rates, then convert into discount factors, then use those to price everything, and these will be modelled priced, and then I will compare them to the actual market prices, and take the sum of the squared errors. Then, use gradient descendent, that is, improve it to minimize that error. It uses numerical methods, you need to optimize step by step and it depends on your initial conditions 
- e) You need to have reasonable parameters for the level, slope and curvature. 

- When you have a perfect system, it is better bootstrapped and then OLS, and finally Nelson-Siegel. However, as you increase the "bad" data, that is, when you don't have a diagonal matrix, Nelson-Siegel is way better than the Bootstrap and OLS substantially. However, Nelson-Siegel has strong assumptions about the world. 

Problems Spot Discount Rates
- You can have periods where nothing mature, and thus you don't have a cash flow. You cannot estimate it with Bootstrapping as you will have several columns that are equal, so it is not invertible. 
- It is not easy to solve, in OLS you simply drop a column, but here it doesnt make sense because it is a bad assumption because we KNOW that they pay at certain dates, even if we don't have anything maturing at certain dates. 
- With OLS you get zig zagging, with discount rates up and down with peaks instead of being a decreasing line. 
- The 10 year gap is very problematic. 
- If a treasury is issued on a really weird date, then I'm going to have coupons on all these weird dates, and it will be the only security with coupons on those dates. So you filter those. If this treasury pays on a date, and its the only thing that pays on that date, remove it. 
- Could we use lasso? No, we can't use lasso because it will remove maturity dates, and that is not reasonable. For some of the dates, the discount factor is zero. That does not make sense. 

Spot Curve = Discount Curve (Discount factor) vs Yield Curve (YTM)
1. Yield-To-Maturity depends on the particular issue/security/bond you are referring to. Spot Curve does NOT depend on which issue you are talking about. Does not depend on j.
2. The spot rate as of today, says, there is a cash flow in 5 years, the spot curve as a discount rate that price a cashflow. It doesn't care where does this cash flow comes from, it can be a dividend, a coupon, etc. As long as it is a guaranteed cash flow and we know when is it arriving.
3. A yield handles any cash flow attached to a certain security, and a discount rate handles any cash flow that arrives on a given date. 
4. Yield To maturity gets the discount wring is because it tries to apply the same discount rate at different periods in time. I've got a 10 year treasury, why am I discounting the 1st coupon the same was as the 7th coupon? That makes no sense. If we could look at securities where they only paid one time, then it is exactly what a discount rate is. 
5. If we were in an scenario where we have 0 coupon bonds, chart the yield, and their yield would be exactly a discount rate. 

Discount factors vs discount rates
1. Discount factor is 1/discount rate. It remains constant regardless of compounding. 
2. The discount rate can vary depending on compounding, while discount rate would remain the same. 
3. The discount factors says, for any cashflow in the future, how much will it be worth it? That is, for 1 dollar today, it will be worth 65 cents in 30 years. It is less than 1. It is the present value of $1 to be received at a future time. $DF(t) = 1/(1+r_t)^t$, where $r_t$ is the periodic discount rate (per unit of time). 
4. The discount rates is the rate of return used to discount future cash flows. $r_t = (1/DF(t))^{1/t} - 1. 

Modelling the spot curve = discount curve
1. Filter to eliminate: maturities that are too short or long, quotes that do not have a quoted positive yield, tips. 
2. Filter dates to eliminate: dates where no bond is maturing (identification), dates that are not benchmark treasury dates (liquidity).
- $\boldsymbol{p}$: $n\times 1$ vector of the price for each issue
- $\boldsymbol{z}$: $k\times 1$ vector of the discounts for each cash-flow time
- $\boldsymbol{C}$: $n\times k$ matrix of the cashflow for each issue (row) and each time (column)
- $\boldsymbol{p} = \boldsymbol{C}\boldsymbol{z}$
When you have an exact square matrix with these dimensions, the same number of treasuries, and the same number of maturities, you can use linear algebra to solve for Z.

Dirty Price vs Clean Price
- Dirty price accounts for the accrued interest, so the prices differ because you know it will pay a coupon soon. They don't match just the exact date after it paid the coupon
- Clean Price should not even exist, the price is just a price convention, but the real price is the dirty price. It is used for reasons of communication, derivatives, etc. 
- Clean price is the actual transacted price that we call the dirty price, minus the amount of coupon that has proportionally happened over time. 
- The true is the dirty price, that is actually transacted, but in our dashboards we put the clean price, just as a pricing convention. In Bloomberg you will have the Clean Price, but you have data to add the accrued interest and calculate the dirty price. The market quote will always be the clean price

Level, Slope, Curvature
- PCA is good a discomposing the yields into 3 factors: Level, Slope, Curvature which explain almost 99% of the variation

### Week 1 HW review

Yield Curve vs Spot Curve
- Main difference: Yield Curve any given point is pricing a particular treasury. The Spot curve is pricing for ANY cashflow in time. 
- They are related, but there is not reason to say that they are related by construction
- Can you use YTM as a discount rate? No, only if you are referring to that particular security. Or is we have no coupon treasuries

- STRIPS are zero coupon bonds, but these are not issued by the treasury. However, there is a strip programs. The treasury keeps track of those, but they do not issue them 
- Why we don't use STRIPS? Because there is not enough liquidity on those. That is a derivative product. 

Spot curve
- It is extremely important. It is as important as the risk free rate in portfolio. 
- When you construct this, the more liquid instruments are more important and should be put more attention, instead of focussing on everything. You need to filter/ or to use Weighted Least Squares, the idea is to put more weight to those observations that you trust the most. In Nelson-Siegel, you can do weighted curve fitting.
- OLS Method doesnt assign any particular structure, it DOES NOT need to be a curve, it can have values scattered all around. So firms DO NOT really use OLS because it has problems.
- OLS is "non parametric", in the sense that you let the data speak. While Nelson-Siegel is "parametric" in the sense that you are making some assumptions about how the world behave. Nelson-Siegal requires good initial conditions, otherwise it does not converge. 

- OLS you need to remove columns where nothing mature, but also need to remove to remove ANY security that paid on that date. Otherwise, your error will absorb this and the mean of the errors won't be zero. Note that we do not include an intercept, so it does not capture the mean. 
- If you have 3 securities maturing the same day, you need to remove 2 of those to keep only one. 

Bootstrapping
- First filter is not subjective. Remove dates without maturities
- Second filter is more subjective, what securities do you remove?

- Expected Inflation: Take the yield curve without TIPS, and take the yield curve with TIPS only, then take the spread, and this should be the inflation expectation at a certain point in time about the inflation estimates at some year. 

- The current Yield Curve does not have significant variation. Its range is .50 bps, while in other dates it was closely to 5bps. 


## Week 2

Risk factors: In equities, it is the market factor. However, in fixed income, it is the interest rate LEVEL.
Yields and discount rates are very interrelated. They do not change 1 by 1 but change similarly. However this is not by construction.

- Why we don't calculate sensitivity using a linear regression/linear factor decomposition? Because we have some economic theory behind about their behavior, why should we waste so much statistical power if we already have some idea of its behavior? You have a lot of mathematical information, so why leaving it to the data to speak and waste statistical power. 

- Your 2 year treasury, will be a one year treasury one year from now. And these relations are important and provide us information. 

- Sensitivity: 
$\frac{dP}{P} \approx -D\times dr + \frac{1}{2}C\times (dr)^2$

where dr is a small change in the level of the spot curve, D is the duration (negative relationship with price and included as -D to make it positive), and C is the Convexity. 

- Duration
1. Refers to the sensitivity of a bond (or other fixed-income product) to the **level of interest rates**.
2. Rather than measure sensitivity to the 3-month, 1-year, or 10-year rate, measure sensitivity to a parallel shift in all these rates, all else equal.
3. $D \equiv -\frac{1}{P}\frac{dP}{dr}$
4. Duration is a **percentage** change in the price, (via the $1/P$ term).
5. We denote the parallel shift in the spot curve with $dr$
6. The negative in the definition is so that the resulting duration will be a positive number. ($dP/dr$ is a negative number!)
7. Treasuries with higher time to maturity are more sensitive to interest rate risk (change) because they have more time in the market. So it is more sensitive to interest rates. 
8. Duration is the weighted average of the cashflow maturities (in a bond)
9. Is the sensitivity of price to time.
10. Duration is a time-varying metric, with a predictable path. 
11. Coupons lower duration because you are getting paid part of the value of the treasury before. The relation depends on how high/low is the coupon. When coupon is low, then duration is very similar to time to maturity. When it is high, they differ significantly, and duration would be significantly lower. 
12. Prices on a 30 year treasury are way more volatile than in a 1 year treasury and this is because of duration. 


- Convexity
1. Is not as interesting as duration. The action is in duration
2. Is the second derivative of the price with respect to rates. Now we are not adding a minus, as in duration. 
3. For a zero coupon bond, it is (T-t)^2, time to maturity squared

### Homework Week 2

- Duration is presented in years (divide by 365.25)
- Modified duration is Duration/(1+YTM/n), where n is the number of periods that pay a coupon.