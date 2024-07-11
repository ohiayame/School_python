import csv

with open("output.cvs", "w", encoding='utf-8') as f_hendler:
    
    writer = csv.writer(f_hendler)
    
    writer.writerow(['Name','Age','Email'])
    
    writer.writerows([['Alice', 30, 'alice@gjsgfk.com'], ['BOb', 25, 'BOb@gjsgfk.com']])