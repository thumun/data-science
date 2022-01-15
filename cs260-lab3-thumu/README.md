## CS260 Lab 3: Gradient Descent

Name 1: Neha Thumu

Name 2 (optional):

Number of Late Days Using for this lab: 1

---

### Analysis

Part 2: Comment on how close your results are (for `w`) to the provided models from Lab 2.

For sea ice::
The weights from this lab:
w = [ 1.90503823e+02, -9.22444614e-02]

From lab 2:
deg_1_coef = [190.5038227644984, -0.09224446142042844]


For regression train::
The weights from this lab:
w = [ 2.44640709, -2.81635359]

From lab 2:
deg_1_coef = [2.4464070947147207, -2.816353589568698]


As you can see, the results are exactly the same for both of the datasets
(the weights from this lab are rounded however).


Part 4:

a) Include the optimal weights from both your analytic solution and your SGD solution. Comment on any differences between the two models.

Analytical:
[[2.09068873e-14]
[6.51280605e-01]
[4.65062749e-01]
[3.43692235e-01]
[5.77068966e-03]
[4.27271975e-01]]

SGD:
[[0.00228857]
[0.65146888]
[0.46595808]
[0.34565975]
[0.00885319]
[0.42510867]]

The analytic solution for the first value is much lower than the one in the SGD solution (by several degrees of magnitude). The rest of the values are pretty
similar in value.


b) For each model, what was the most important feature? Which features were essentially not important? Do these results make sense to you? Does it matter that we normalized the features first?

For both analytical and SGD the most important feature is 0.651 (since that was
the largest/had the most impact). The least significant for analytical was
2.09068873e-14 and for SGD it was 0.00228857.
They make sense (except the least significant - but that was the least significant and some magnitudes off) since analytical and SGD had similar answers.

Yes, it matters because if not they won't be comparable. Since the magnitude of the coefficients would vary. 

---

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab
assignments in the future)

1. Approximately, how many hours did you take to complete this lab? (provide
  your answer as a single integer on the line below)

    20(?)

2. How difficult did you find this lab? (1-5, with 5 being very difficult and 1
  being very easy)
  5

3. Describe the biggest challenge you faced on this lab:
  I think the shape of matricies is what gave me the most trouble in this lab.
  Since it calculated the values even though the shapes were off (being vectors instead of matricies), it was difficult to find and correct the errors. I
  also didn't realize that this was the problem until late last night.
