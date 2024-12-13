The Epilepsy Detection project aims to create an automated system for identifying epileptic seizures from EEG recordings. This tool could potentially assist medical professionals in diagnosing and monitoring epilepsy more efficiently.

EEG Data: 

Collected from multiple epilpetic and non-epileptic subjects using 19 electrodes on the scalp. Signals 10 seconds long are used as input.

Pre-Processing:  

Denoising and smoothing EEG data. Signals can be separated into 5 bands (alpha, beta, delta, theta and gamma) or used as is. 

Feature Extraction:

Extracting 4 features (the Hjorth parameters and Entropy). The Hjorth parameters are time domain parameters - activity, mobility and complexity - first identified and defined by Bo Hjorth in 1970.

Machine Learning Model: 

Implements a model for classifying EEG signals as epileptic or non-epileptic. 6 models (supervised and unsupervised) are considered - K-Means, KNN, Logistic Regression, Naive Bayes, Random Forest and SVM. 

Evaluation: 

Provides methods for assessing the model's performance in terms of precision and accuracy.

The programs are run in the following order:
1. WaveletDenoising.m
2. ExtractFeatures.m
3. BandSeparation.m (if required)
4. Any of the .py files in the folder 'Classifiers' to calculate accuracy of one classifier at a time
5. OR EpilepsyDetection.ipynb to compare the accuracy of classifiers  



