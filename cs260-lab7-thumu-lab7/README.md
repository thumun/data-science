## CS260 Lab 7: Visualization

Name 1: Neha Thumu

Name 2 (optional):

Number of Late Days Using for this lab: 1

---

### Analysis

1. For the iris flower dataset, what genealogical relationships can we infer from the PCA plot?
  The cluster of Iris Versicolour and the Iris Virginica are separate from the cluster of Iris Setosa.
  We can infer this to mean that Iris Versicolour and the Iris Virginica are more genealogically related than Iris Setotsa.

2. For the human dataset, what fraction of the variance is explained by the first PC?  By the second? (Hint: see PCA documentation)

    PC1: 0.05109354   ~5.1%
    PC2: 0.02377386   ~2.4%

    Got from the pca.explained_variance_ratio_


3. For the human dataset, what genealogical relationships can we infer from PC1 and PC2?

  There seems to be four main clusters. The East Asian cluster, the African cluster, the South Asian and the European cluster. From the chart, the African cluster seems to be a bit distanced while the East Asian cluster seems to be distancing itself as well (with increased samples and features I infer it will distance itself more - like the chart we looked at in class).
  The South Asian cluster is visible and is located between the European cluster and the
  East Asian cluster.
  The American super population is not existent as a cluster. Rather it's scattered around.
  Seems to be overlaying with the South Asian cluster and between the
  European and African clusters.

  Genealogically, I think the African super population is not as related to the East Asian, South Asian, and European super populations. But may have a greater genealogical relation with the American super population (not sure how to interpret that part of the chart).

  The East Asian population has a bit of genealogical relation with the South Asian and American population but is mostly isolated.

  The European, South Asian, and American populations seemed to be the most genealogically related. Due to how close they are/how much they're overlapping.


4. (*Optional*) Plot PC3 and PC4 on a separate plot. What genealogical relationships can we infer from these PCs?

---

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab
assignments in the future)

1. Approximately, how many hours did you take to complete this lab? (provide
  your answer as a single integer on the line below)

  10

2. How difficult did you find this lab? (1-5, with 5 being very difficult and 1
  being very easy)

  3

3. Describe the biggest challenge you faced on this lab:

  running the data
