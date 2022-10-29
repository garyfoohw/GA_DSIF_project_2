# Buying a house and how to not get ripped off

![beach house](image/beachhouse.png)

## The market today

If you noticed in recent years, there's been an increase in online platforms whose job is to link buyers and sellers.  
These intermediary companies do not own any inventory, but only seek to be the middle-man and profit from the commisions.  
E-bay and Taobao are famous e-commerce platforms are great examples.  
Outside of e-commerce, we have Uber, AirBnB, which all do not hold any inventory themselves.

## Who we are, and why are we doing this

We are an intermediary company in the real-estate space.  
Our core business is to link up buyers and sellers of houses.  
This method of sales bypasses the traditional realtor (or real-estate agent), savings buyers and sellers on hefty consultancy fees.

While we provide a platform for buyers and sellers to connect, we do not dictate sale prices.  
To an inexperienced house buyer, it is difficult to know if the price of one house really warrant such a big difference from the market mean.  
How can we help buyers (and sellers) price the house more fairly in relation to the market mean?  
If we can equip our customers with confidence to price the property, we may seem more uptake in our platform.

## The problem and the approach
We aim to create a simplified framework, one that is easy for humans to deal with without a computer.  
The framework would comprise several major and minor features for buyers (and sellers) to look for when pricing thier house, relative to the market mean.

We first model the sale price of the market using multiple features (numerical, ordinal & categorial).  
Upon validating and confirming that the model is performing well,  
we dissect the model and look at the important features driving the prediction.

## Outcome
The model achieved a R2 score of 92.6%, with RMSE of aroudn 25000.
According to the model, the features that contribute significantly to the models can broken down into 2 main categories for practicality purpose:  
**Major features**:<br>
`Gr Liv Area`: Above ground living area square feet,<br>  `Overall Qual`: Rates the overall material and finish of the house (1-10),<br>`Year Built`: Original construction date<br>
**Minor features**:  <br>
`Total Bsmt SF`: Total square feet of basement area,<br> `Kitchen AbvGr`: Number of kitchens above ground level *(negative correlation)*,<br>`Utilities`: Type of utilities available (Elec, Elec+Gas, Elec+Gas+Water, Elec+Gas+Water+Sewage),<br>`BsmtFin SF 1`: Basement finished area of type 1 in square feet,<br> `Overall Cond`: Rates the overall condition of the house (1-10)<br>

## Recommndation and conclusion
The above 8 features are simple enough for a human to gauge the vaule of a house without running therough a computer program to obtain the valuation. This facilitates market pricing and boost economic transaction. Indirectly, our company will benefit from increased sales too.  

In conlcusion, we have presented a method to identify significant traits that affect house pricing, and we hope that this will aid buyers and sellers in their transactions in the future.
