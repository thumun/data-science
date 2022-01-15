## CS260 Lab 8: Statistics

Name: Neha Thumu

Number of Late Days Using for this lab: 0

---

### Analysis

1. For Part 1, include both your p-values below. What is the probabilistic *interpretation* of the p-value in this coin toss situation? Given this interpretation, do you reject the null hypothesis (fair coin) or fail to reject?

CLT p-value: 0.0017451186995289033
Random trials p-value: 0.00216

The probabilistic interpretation of the p-value in this coin toss situation is the probability under the null hypothesis of observing the number of heads that’s more extreme than the average/mean. (And since it’s 2-sided, this would be both extremes - greater than or equal to 54/80 and less than or equal to 26/80.

In this case, the p-value is much lower than 0.05 which means that I reject the null hypothesis.

2. For Part 2, include both your p-values below. Do you reject the null hypothesis (genomes from Population 1 and Population 2 are roughly the same size) or fail to reject?

CLT p-value: 0.0019026420082769626
Permutation testing p-value: 0.00354

The p-values are much lower than 0.05 which means I reject the null hypothesis.
The genomes from Population 1 and Population 2 are not roughly the same size.

3. For Part 2, you may have noticed that your p-values were not as close as in Part 1. What assumption of the CLT might be violated with this dataset?

The assumption that might be violated is that we don't have a clear null distribution.
And don't know the true mean and variance of the null distribution. As such, the
CLT is more of a guess-timate.

4. (Optional) If you did Part 3, write up your procedure and results here (what were you trying to test, how you went about it, what you found, etc).

---

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab
assignments in the future)

1. Approximately, how many hours did you take to complete this lab? (provide
  your answer as a single integer on the line below)
  12

2. How difficult did you find this lab? (1-5, with 5 being very difficult and 1
  being very easy)
  3

3. Describe the biggest challenge you faced on this lab:
  honestly this was a pretty straightforward lab
  only challenge was trying to see if my numbers are right but code-wise was
  simple
