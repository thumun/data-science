## CS260 Lab 2: Modeling Climate Change

Name: Neha Thumu

Number of Late Days Using for this lab: 0

---

### Analysis

Part 2: Describe the patterns you see in the residuals. Based on these patterns, which model do you think is a better fit for this data?

I think the quadratic model is a better fit for this data. The residuals for
that model have less spikes and are all clustered. They are closer to the
zero line which means the true and predicted values are closer together. (If
the true and predicted values were the same then they would be zero) Which shows
that there's less outliers. Also shows that the raw and predicted data as being
closer together in value in comparison to the linear residual graph.

Part 3: Describe what you observe. Based on these visualizations, which model do you think is a better fit? How would you advise governments who are trying to make policy decisions based on this type of model fitting process?

Based on the visualizations, the linear model is a better fit. Because in the
quadratic model, the data points for the 2013-2020 data are all clustered above
the best fit curve. While in the linear model, the points are more evenly
distributed (above and below the line).  

I would advise governments to certainly take some action since the extent of
sea ice seems to be decreasing at a rapid rate.

Part 4: Describe the pattern you observe (in the polynomial models). Based on these preliminary visualizations, which model would you choose and why?

I would choose the 4th degree polynomial model. Because it is the one that
has the right shape and does not follow the data too rigidly (still room
for prediction of future). I was going to say the 3rd degree polynomial but
I feel like it does not fit the first part of the curve well (not high
enough - doesn't take into account some of the data). The 5th degree polynomial
and higher all fit to the data too much. The second and first degree
polynomials do not follow the data well (too simplified).

Looking at the elbow plot, which degree would you choose? Explain your answer.

I think I would stick with my answer before and choose the 4th degree.
One could argue that the 3rd degree is the start of the pattern (an asymptote
which signifies there is not much change after that polynomial for the
best fit). However, I think the 4th degree is slightly more in line with the
higher degree polynomials. Which shows that it is the best fit for the data.


---

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab
assignments in the future)

1. Approximately, how many hours did you take to complete this lab? (provide
  your answer as a single integer on the line below)

  14

2. How difficult did you find this lab? (1-5, with 5 being very difficult and 1
  being very easy)

  3

3. Describe the biggest challenge you faced on this lab:

  The first part of Part 4. For some reason I was very much confused by the
  directions but thanks to office hours figured it out!

---

### Coefficients for Part 4

~~~
deg_0_coef = [1.13010595]

deg_1_coef = [2.4464070947147207, -2.816353589568698]

deg_2_coef = [2.522610178119313, -3.27003073191282, 0.4743087284609393]

deg_3_coef = [1.2231425230496584, 10.649616212253513, -34.083679747347574, 23.590230897814727]

deg_4_coef = [0.8075214798200756, 17.32934850900337, -62.32907523274797, 66.75220156315058, -21.61184507602993]

deg_5_coef = [1.1537400009153576, 9.784042834672174, -14.963934203443742, -54.05134690879839, 111.9406595086277, -53.20467363235635]

deg_6_coef = [1.6031281515537332, -2.212955964351817, 87.09165569133722, -440.6384252637192, 832.5418657076268, -698.5859135919, 221.439066525518]

deg_7_coef = [1.0048620515132924, 17.4112052205856, -133.45588391947206, 713.2351017847259, -2320.831952624806, 3938.208550304347, -3249.3507974432723, 1036.2869129041017]

deg_8_coef = [0.8889729225247591, 21.927863684690806, -196.3956341264095, 1135.1023058754872, -3863.15628401735, 7177.078002707203, -7143.712758937181, 3524.932857125692, -654.5246542101304]

deg_9_coef = [6.455577860121968, -214.55025432038786, 3518.6484115354933, -28016.264919570815, 126197.74461140906, -343436.25785927917, 574211.0815161027, -575789.2765246094, 317309.99905972165, -73803.67907566673]

deg_10_coef = [5.571266255808752, -173.07147738443035, 2771.613686468927, -21023.423222254118, 87668.04317051847, -210606.67961073387, 280101.8712329003, -158297.13764038868, -49517.323077016044, 107648.64893355407, -38599.19918692205]
~~~
