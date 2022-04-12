# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:07:19 2022

@author: shiva
"""

import PyPDF2 as reader
import textract
import re
import string
import pandas as pd
import matplotlib.pyplot as plt


pdf = open('1.pdf','rb')     #open pdf

pdfReader = reader.PdfFileReader(pdf)          #read file
 
num_pages = pdfReader.numPages   #total nuumber of pages

count = 0           # Initialize a count for the number of pages


text = ""            # Initialize a text empty etring variable


while count < num_pages:          # Extract text from every page on the file
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

    
text = text.lower()

# Remove numbers
text = re.sub(r'\d+','',text) #removenumbers

text = text.translate(str.maketrans('','',string.punctuation)) #remove puctuation

 #Create dictionary with industrial and system engineering key terms by area
terms = {'Quality/Six Sigma':['black belt','capability analysis','control charts','doe','dmaic','fishbone',
                              'gage r&r', 'green belt','ishikawa','iso','kaizen','kpi','lean','metrics',
                              'pdsa','performance improvement','process improvement','quality',
                              'quality circles','quality tools','root cause','six sigma',
                              'stability analysis','statistical analysis','tqm'],
        'Operations management':['automation','bottleneck','constraints','cycle time','efficiency','fmea',
                                 'machinery','maintenance','manufacture','line balancing','oee','operations',
                                 'operations research','optimization','overall equipment effectiveness',
                                 'pfmea','process','process mapping','production','resources','safety',
                                 'stoppage','value stream mapping','utilization','python'],
        'Supply chain':['abc analysis','apics','customer','customs','delivery','distribution','eoq','epq',
                        'fleet','forecast','inventory','logistic','materials','outsourcing','procurement',
                        'reorder point','rout','safety stock','scheduling','shipping','stock','suppliers',
                        'third party logistics','transport','transportation','traffic','supply chain',
                        'vendor','warehouse','wip','work in progress'],
        'Project management':['administration','agile','budget','cost','direction','feasibility analysis',
                              'finance','kanban','leader','leadership','management','milestones','planning',
                              'pmi','pmp','problem','project','risk','schedule','scrum','stakeholders',"project"],
        'Data analytics':['analytics','api','aws','big data','busines intelligence','clustering','code',
                          'coding','data','database','data mining','data science','deep learning','hadoop',
                          'hypothesis test','iot','internet','machine learning','modeling','nosql','nlp',
                          'predictive','programming','python','r','sql','tableau','text mining',
                          'visualuzation'],
        
        'Healthcare':['adverse events','care','clinic','cphq','ergonomics','healthcare',
                      'health care','health','hospital','human factors','medical','near misses',
                      'patient','reporting system'],
        "Education and Training":["administration","assisted","awarded","classroom","coach","course","discipline","education","training","interactive","networking","mentor","tutoring","training"],
        
          "Law Enforcement":["clerk","copyrightlaw","joint venture","legal recearch","trial law","will preparation"],
          
          "Tourism and Hospitality":["budgeting","catering","flexibility","customer service","greeting","maintenance","marketing","positivity","server","travel","tourism","transportation"],
          
          "Marketing and Business":["account management","agile","analytical","analyzing data","branding","automation","budget management","business plans","business strategy","business system","client relationships","coding","counseling","data analysis","data management","six sigma","supply chain management"] }


quality = 0
operations = 0
supplychain = 0
project = 0
data = 0
healthcare = 0
education= 0
law = 0
tourism = 0
marketing = 0
finance = 0
architecture = 0



scores = []

# Obtain the scores for each area
for area in terms.keys():

    if area == 'Quality/Six Sigma':
        for word in terms[area]:
            if word in text:
                quality +=1
        scores.append(quality)
        
    elif area == 'Operations management':
        for word in terms[area]:
            if word in text:
                operations +=1
        scores.append(operations)

    elif area == 'Supply chain':
        for word in terms[area]:
            if word in text:
                supplychain +=1
        scores.append(supplychain)

    elif area == 'Project management':
        for word in terms[area]:
            if word in text:
                project +=1
        scores.append(project)

    elif area == 'Data analytics':
        for word in terms[area]:
            if word in text:
                data +=1
        scores.append(data)
        
    elif area == "Education and Training":
        for word in terms[area]:
            if word in text:
                education +=1
                scores.append(education)
                
    elif area == "Law enforcement":
        for word in terms[area]:
            if word in text:
                law +=1
                scores.append(law)
                
    elif area == "Tourism and Hospitality":
         for word in terms[area]:
             if word in text:
                 tourism +=1
                 scores.append(tourism)
                 
    elif area == "Marketing and Business":
        for word in terms[area]:
            if word in text:
                marketing+=1
                scores.append(marketing)
                
    else:
        for word in terms[area]:
            if word in text:
                healthcare +=1
        scores.append(healthcare)

        # Create a data frame with the scores summary
summary = pd.DataFrame(scores,index=terms.keys(),columns=['score']).sort_values(by='score',ascending=False)
summary

# Create pie chart visualization
pie = plt.figure(figsize=(11,11))
plt.pie(summary['score'], labels=summary.index, explode = None, autopct='%1.0f%%',shadow=True,startangle=90)
plt.title('Job Recommendation\n\n')
plt.axis('equal')
plt.show()

# Save pie chart as a .png file
pie.savefig('resume_screening_results.png')
