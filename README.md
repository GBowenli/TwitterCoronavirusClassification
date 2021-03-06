# TwitterCoronavirusClassification

Posiitve coronavirus datasets obtained from:  
Rabindra Lamsal, March 13, 2020, "Coronavirus (COVID-19) Tweets Dataset", IEEE Dataport, doi: https://dx.doi.org/10.21227/781w-ef42.

Negative coronavirus datasets obtained using:  
`Twitter API` and `tweepy`.

## Python Version
3.8.0

## Required Packages
1. numpy 1.21.4
2. pandas 1.3.5
3. sklearn 1.0.1
4. tensorflow 2.7.0
5. tweepy 4.4.0
6. nltk 3.6.5
7. joblib 1.1.0

## Scraping and Baseline Results
The datasets we collected is in folder `dataset`. The positive training dataset is in `dataset/pos`,
and the negative training dataset is in `dataset/neg`.  
The testing dataset is in `dataset/test`, where the dataset for general testing is in `dataset/test/general`,
and the dataset for comparison testing (i.e., the "omicron" dataset) is in `dataset/test/comparison`.  
The baseline results for each test is saved within the same folder as the testing dataset for the corresponding test.

***PLEASE NOTE:***  
Running the following file requires a significant period of time and computing resources!

**run** `twitter_scrape.py` to perform dataset collection again, which will OVERWRITE our saved datasets.

## Models

***PLEASE NOTE:***  
Running the following files requires a significant period of time and computing resources!

### Simple Models
**run** the following python files for validation results:
1. Logistic Regression - `logistic_regression.py`
2. SVM - `svm.py`
3. Multi-layer Perceptron classifier - `MLP.py`

**run** `simple_models_test.py` to perform testing again, which will OVERWRITE our saved results and models.

> The results of all the testing results for all the simple models are in `dataset/test/results`.

> The trained models are saved in `models`.

***Note:***  
To load the models we trained, run the following code and replace the name of the model to the desired one:

```python
from joblib import load
clf = load('./models/name_of_model.npy')
```

### Character-Level CNN
**run** `character_level_cnn.py` for testing results.

***Note:***  
Choose to run the `character_level_cnn.py` with CPU or GPU.  
Change the testing file location in `character_level_cnn.py` to switch between general and comparison test.
