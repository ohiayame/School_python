import csv

with open("output.cvs", "w", encoding='utf-8') as f:
    
    fields = ['Name','Age','Email']
    
    writer = csv.DictWriter(f, fieldnames=fields)
    
    writer.writeheader()
    
    writer.writerow({'Name': 'Alice', 'Age': 30, 'Email':'alice@gjsgfk.com'})
    writer.writerow({'Name': 'BOb', 'Age': 25, 'Email':'BOb@gjsgfk.com'})