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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "There are ", len(enron_data), "persons in the set"
print "Where each person has", len(enron_data[enron_data.keys()[0]]), "data points"
print "Keys: ", sorted(enron_data[enron_data.keys()[0]].keys())
print "Persons: ", sorted(enron_data.keys())

pois = 0
quantified_salary = 0
known_addresses = 0
unknown_total_payments = 0
unknown_poi_payments = 0
for p in enron_data:
    pois += enron_data[p]["poi"]
    if enron_data[p]["salary"] != "NaN":
        quantified_salary += 1
    if enron_data[p]["email_address"] != "NaN":
        known_addresses += 1
    if enron_data[p]["total_payments"] == "NaN":
        unknown_total_payments += 1
    if enron_data[p]["poi"] != 0 and enron_data[p]["total_payments"] == "NaN":
        unknown_poi_payments += 1

print "There are", quantified_salary, "people with quantified salary"
print "There are", known_addresses, "people with known addresses"
print "There are", unknown_total_payments, "with unknown total payment"
print "There are", unknown_total_payments / 146.0, "with unknown total payment"
print "There are", unknown_poi_payments / 18.0, "POI with unknown total payment"
print "There are", 10 / 28.0, "POI with unknown total payment"

print "There are", pois, "of interest"
print "James Prentice had stock value of", \
    enron_data["PRENTICE JAMES"]["total_stock_value"]

print "There are ", \
    enron_data["COLWELL WESLEY"]["from_this_person_to_poi"], "mails from Wesly Colwell"

print "Jeffery S Skiling stock value", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "CEO Jeffrey Skilling took home", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Chairman Kenneth Lay took home", enron_data["LAY KENNETH L"]["total_payments"]
print "CFO Andref Fastow took home", enron_data["FASTOW ANDREW S"]["total_payments"]

