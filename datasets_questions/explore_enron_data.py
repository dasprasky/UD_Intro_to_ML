#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print("Number of persons: ", len(enron_data))
print("Number of features for each person: ", len(enron_data.values()[0]))
def known_email(person):

poi_count = 0
max=0
person=''
for person in enron_data:
    if enron_data[person]['poi']==1:
        poi_count += 1
    if enron_data[person]["total_payments"] > max and enron_data[person]["total_payments"] != 'NaN':
        if person == "SKILLING JEFFREY K" or person == "LAY KENNETH L" or person == "FASTOW ANDREW S":
            max = enron_data[person]["total_payments"]
            person_max = person
            known_email(person)

print("POI Count", poi_count)
print "Most Money Take Home By", person_max, " total value: ", max

poi_names=[]
with open("../final_project/poi_names.txt", 'r') as poi:
    for name in poi.readlines()[2:]:
        poi_names.append(name)
print "Actual POI Count", len(poi_names)
print "Total Value of Stock Belonging to James Prentice", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Number of email messages do we have from Wesley Colwell to persons of interest", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Stock Options Exercised by Jeffrey K Skilling", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
