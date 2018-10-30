# LS_Regressor
Least square linear regression is implemented using the normal equaiton :<br />
                                                **_W=(X^T  X)^(-1) X^T y_**
                                                 
 `Poly_fit` function takes the polynomial features Xtr, output Ytr, and polynomial degree M.
 And it returns polynomial coefficients W in a (d+1) vector, where d is the number of features. 
 
 `Predict` function evaluates the polynomial given the weights W , the features X, and the polynomial degree M. :<br />
                                                            **_y(x)=W^T X_**
                         

# CCPP Dataset
The LS regressor is applied to the [CCPP dataset](https://archive.ics.uci.edu/ml/datasets/combined+cycle+power+plant).
In part1, univariate polynomial regression is applied to find the best polynomial degree for fitting the input feature Exhaust Vaccum (V) with 
the output energy (E).
In part2, multivariate linear regression is applied to find the best subset of the four features. In part3,  multivariate polynomial regression
is applied by using all the features to find the best polynomial degree.
