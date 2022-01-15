## CS260 Lab 5: Naive Bayes

Name 1: Neha Thumu

Name 2 (optional):

Number of Late Days Using for this lab:

---

### Analysis

#### Part 2

1. In this lab we will be considering sex as a protected attribute, and seeing if we can predict sex from the remaining attributes. First, compute the fractions of males and females in the *training* data.

(approximately)
Males: 0.677
Females: 0.323

2. Given these ratios, if an algorithm to predict sex randomly flipped a coin for every *test* example, what confusion matrix would result? What overall classification accuracy would result?

Confusion Matrix:

                        Predicted
              M                   F
          M   # males / 2      # females / 2
True
          F   # females / 2    #  males / 2

Accuracy = (# males + # females)/2*(# males + # females) = 0.5

3. What if an algorithm always predicted the majority class? What would the confusion matrix look like in this scenario? What overall classification accuracy would result?

Confusion Matrix:

                      Predicted

              M                   F
          M   # males             0
True
          F   # females           0

Accuracy = (# males)/(# males + # females) = 0.67

#### Part 4

1. Just temporarily, remove the LaPlace counts from your code and run your method again. What error do you obtain? What does this error actually mean about the data?

The error is math domain error. Since the function is attempting to take the
log(0) which is undefined.  
This error means that there is an example(s) that doesn't have a feature value
for one of the labels/the feature value was not present in the examples.

2. When trying to predict sex from the other attributes, what accuracy do you obtain? Is this higher or lower than you would expect with one of the naive strategies from Part 2?

The accuracy is 0.8188435099069955. The accuracy is higher than both of the
predicted accuracies in Part 2.

3. Re-run your method with the `corrected` train/test data. What accuracy do you obtain now? Explain the difference between the two datasets and why this accuracy change makes sense.

The new accuracy is 0.7770589028170912.
This accuracy is lower since there's a gender neutral term for the relationship
feature (partner).
In the previous data set, it is more likely for someone with a husband to be
female. And more likely for someone with a wife to be male. As such, this
feature previously affected the probability.
But since it simply says partner (or nothing if there's no partner - like
before), there is less of an impact on the probability for determining the
person's sex.

4. What (if anything) is concerning about being able to predict such a protected attribute
from the other attributes (especially using an algorithm like Naive Bayes that does not explicitly account for feature interactions)?  If the actual "label" were "hired" or "not hired" for a job, and you
were responsible for making this decision, how would you deal with data where features were
redundantly encoded?

It is pretty concerning (and a creepy) to be able to predict something like sex
based on the attributes in this data. Of course, some of them probably are
a bit of a guess (like age) but it's I feel like it's definitely possible to
see the connection between salary, job, and education and an individual's sex.
It could lead to a misinterpretation of data or a skewing of results since a
person's sex shouldn't have an influence on a study (especially a study
regarding work or education or something else along those lines).

For the hiring scenario, it would be best to ignore the features that are most
directly connected to the protected attributes (in order to ensure that
these attributes are not influencing the hiring process). Or to assign an
emphasis to certain features (not treating all the features with the same
weight). In other words, not using Naive Bayes but a different algorithm.  


---

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab
assignments in the future)

1. Approximately, how many hours did you take to complete this lab? (provide
  your answer as a single integer on the line below)

  17

2. How difficult did you find this lab? (1-5, with 5 being very difficult and 1
  being very easy)

  3

3. Describe the biggest challenge you faced on this lab:

  Splitting the data
