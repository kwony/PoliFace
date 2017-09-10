# Data Model

## Example

'''shell
entity_name, entity_data_type
'''

## Politician

'''shell
name,  models.CharField(max_length=200)
party,  models.CharField(max_length=200)
job, models.CharField(max_length=200)
namu_link, models.CharField(max_length=1000)
count, models.IntegerField()
age, models.IntegerField()
political_preference,  models.CharField(max_length=200)
shot_history,  models.TextField()
'''

## User

'''shell
living_area, models.CharField(max_length=200)
political_preference, models.CharField(max_length=200)
job, models.CharField(max_length=200)
age, models.IntegerField()
'''
