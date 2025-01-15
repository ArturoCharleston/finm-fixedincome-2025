### Theory

#### Week 0
- Yield Curve 
1. Relationship between a Bond Yield (Y-axis) and its Maturity (x-axis).  
2. The yield curve gives us an idea, at certain point in time (it is not a time series; it is a snapshot at a moment in time) of how bonds are being priced. It says, if you buy a bond TODAY that matures in 6 months, 1 year, 2 years, etc, that is the pricing (yield). 
3. Yield surface is the time series version when you overlap the different snapshots of daily yield curves
4. Yield Curve at 30 years (e.g) is not the 'expected FED Fund rates' because FED only affect short term. However, short term FED affect a lot of longer term rates in levels. 


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

#### Week 1

- The yield to maturity (YTM) is the rate of return that equates the present value (PV) of all future bond cash flows to the bond's current price. 
- Price of a bond $P = \sum_{i=1}^{N} \frac{C}{(1 + Y)^i} + \frac{F}{(1 + Y)^N}$, where P = Bond price, C = Coupon payment ($F*c/f$), F is the face value of the bond, N is the number of periods ($T*f$) where T is the time to maturity and $f$ is the payment frequency, Y: Yield per period (YTM/f). 
- The YTM equation does not have a closed-form analytical solution, so we use non linear solvers to find the YTM. 

- Solver functions: 
1. pv_wrapper: Calculate the difference between the actual bond price (P) and the price calculated using the price_bond function for a given y (YTM). Then simply find the root
2. 

Price vs Dirty Price
1. 

Spot Discount Rates
1. Bootstrapping
- a) You need to filter some data
- b) You need to have a square system to drop them. You want to end with the same amount of columns and same amount of rows
- c) You drop rows from the cashflows, and you will only drop columns if they are zero only
- d) You want to have one face value payment per maturity, for bootstrap and OLS
You need to remove duplicates, you get rid of negative maturities
2. OLS
- a) Overidentified system, you don't need a square system
3. Nielson-Siegel
- a) You do not get rid of the duplicates
- b) Curvature, Slope, and Shape

Spot Curve
- 