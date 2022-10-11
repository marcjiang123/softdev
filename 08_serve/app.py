# TNPG: PPP
# SoftDev
# October 2022

from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello_world():
    return "TNPG: PPP (Marc Jiang, Thomas Zhang, Kevin Liu) <br> SoftDev <br> October 2022 <br><br>" + choose() + "<br><br>" + printList()

def hellow_world2():
    return occupation

import random as rng

occupation = open("occupations.csv").read() #reading the csv file into a string

occupation = occupation.split("\n") #split each new line 
occupation.pop(0) #delete the heading
occupation.pop(len(occupation)-1) #delete the extra empty line
total = occupation.pop(len(occupation)-1) #delete the total of the values and store value

#create dictionary
jobs = {}
for x in occupation:
    job = x.rsplit(",", 1)
    jobs[job[0]] = job[1]
    
vals = list(jobs.values())
#convert the values into floats
for x in range(0, len(vals)):
    vals[x] = float(vals[x])

def choose():
    sort_jobs = {}
    sort_jobs = jobs


    #identify the total of all the values         
    sum = total.split(",")
    sum = float(sum[1])
    #generate a random number from 1 to the total
    random = round(rng.uniform(1,sum),1)
    
    #continue to subtract from largest to smallest values from the rand val until <= 0
    #key of the last value to be subtracted is the outputed occupation!
    ret_val = ""
    for key in sort_jobs:
        random = random - float(sort_jobs[key])
        if random <= 0 :
            return key
    return ret_val

keyList = jobs.keys()

def printList():
    s = ""
    for i in keyList:
        s = s + i + "<br>"
    return s

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()