## CS260 Lab 6: Information Theory

Name: Neha Thumu

Number of Late Days Using for this lab: 0

---

### Analysis

For Part 2, was the feature selected by information gain ever different from the feature selected by classification accuracy? Explain your results for each of the 4 datasets.

Tennis:
best feature (entropy): Outlook
best feature (classification accuracy): Outlook

Movie:
best feature (entropy): Director
best feature (classification accuracy): Director

Heart:
best feature (entropy): thal
best feature (classification accuracy): thal

Diabetes
best feature (entropy): plas<=127.5
best feature (classification accuracy): plas<=143.5

The feature selected by information gain was different from the feature selected
by classification accuracy in the case of the diabetes training set.

For the movie, heart, and tennis data set, they have feature values that are
discrete. So the best feature from entropy and from classification accuracy
are the same.

For diabetes, the best feature differs since the feature values of the features
are continuous. So there's a large number of feature values. And as such it is
more difficult to predict using classification accuracy since there is more
possibilities/variety.

---

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab
assignments in the future)

1. Approximately, how many hours did you take to complete this lab? (provide
  your answer as a single integer on the line below)

  17

2. How difficult did you find this lab? (1-5, with 5 being very difficult and 1
  being very easy)

  4

3. Describe the biggest challenge you faced on this lab:

  Calculating the entropies (a lot of loops)
