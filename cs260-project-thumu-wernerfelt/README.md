## CS260 Project: Lab Notebook

Neha & Annie : 11-18-21 (1 hr)
- read in the data
- started setting up files

Neha: 11-20-21 (approx. 2-3 hours)
- working on an algorithm to convert continuous data to discrete

Annie: 11:24:21 (1.5 hr)
- implemented entropy on continuous data. Results indicate track_id is the best
feature so far, which shouldn't be the case, so we need to finish making the
data discrete.

Neha: 11-28-21 (1 hr)
- implemented ROC on continuous data. Did not quite work (was zero for each
of the feature values). I think the solution to the problem is to make the
data discrete.

Neha: 12-2-21 (1 hr)
- editing code (cont to discrete logic) 

Annie: 12-2-21 (2 hrs)
- debugged FeatureModel.py and found that it classifies everything as 1 no
matter what. I found a spot where there was a -1 instead of a 0 and this made
the ROC curve look correct.
- continued to discretize the data. We currently have a list of the new feature
values, and need to figure out how to insert that into the csv file

Neha: 12-3-21 (4 hr)
- fixed the continuous-to-discrete code
- worked on the powerpoint

Annie: 12/5/21 (2 hrs)
- made graphs for entropy and classification accuracy
- next step is using the new list of splits in the entropy code instead of
changing all the data  

Annie: 12/6/21 (3 hrs)
- made discrete data into a partition and replaced that dictionary with data
- there are still problems

Neha: 12/7/21 (4 hrs)
- fixing the discretizing data idea (changed from splits to kbins discretizer) --> now works :)
- working on Powerpoint

Annie: 12/7/21 (2 hrs)
- ordered the graphs
- made sure entropy code uses kbins discretizer code

Annie: 12/9/21 (30 min)
- comments

Neha: 12/9/21 (~30 min)
- comments

## References 

Sources
- Pham, Kyauk, and Park, “Predicting Song Popularity.” (2015)
- Sciandra and Spera, “A model based approach to Spotify data analysis: a Beta GLMM.” Journal of Applied Statistics (2020) 

Dataset information 
- User: tomigelo
- Dataset: Spotify Audio Features
- Desc: Audio features for 130k tracks collected from the official Spotify Web API
- Year: 2019
- Link: https://www.kaggle.com/tomigelo/spotify-audio-features

Helpful in understanding features
- About: Spotify Web API Info (where the user got their data from) 
- Link: https://developer.spotify.com/documentation/web-api/reference/#/

Outside method that we used (KBinsDiscretizer) 
- Library: sklearn
- Method: KBinsDiscretizer
- Link: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html

