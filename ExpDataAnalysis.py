import pandas as pd

google = pd.read_csv('job_skills.csv')

print('-------------- dataset info  --------------------')
print(google.info())
print('-------------- dataset dimensions  --------------------')
print(google.shape)


