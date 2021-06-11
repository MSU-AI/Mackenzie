import csv
import json

def create_dict(filename):
    """
    Given a json filename try to open it, else create it. Returns its dictionary
    representation.
    """
    # If there is already a json file, open and save it to master dictionary
    try:
        with open(filename) as file:
            master = json.load(file)
    # If there isn't a json file, create the master dictionary and save it to a json file
    except:
        # Open each csv file individually
        password = csv.reader(open('password.csv', encoding="utf-8"))
        conference = csv.reader(open('conference.csv', encoding="utf-8"))
        security = csv.reader(open('security.csv', encoding="utf-8"))
        network = csv.reader(open('network.csv', encoding="utf-8"))
        hardware = csv.reader(open('hardware.csv', encoding="utf-8"))
        
        files = [password, conference, security, network, hardware]  # Store files pointers
        filenames = ["password", "conference", "security", "network", "hardware"]  # Store filenames
        
        # Backbone structure of master dictionary
        master = {"intents":{"password":[], "conference":[], "security":[], "network":[], "hardware":[]}}
        
        # Iterate over each file and its index (i)
        for i, reader in enumerate(files):
            next(reader)  # Skip header
            
            # Iterate over each row
            for row in reader:
                # Handle specific hardware case
                if i == 4: 
                    temp = {'tag':row[0],'queries':row[1:3],"w_answer":row[3],"m_answer":row[4],"w_source":row[5],"m_source":row[6]}
                # All other cases
                else:
                    temp = {'tag':row[0],'queries':row[1:3],"answer":row[3],"source":row[4]}
                
                # Append to list of respective category
                master["intents"][filenames[i]].append(temp)
        
        # Ultimately, use the dictionary to create a json file of it
        with open(filename, 'w') as outfile:
            json.dump(master, outfile, indent=4)
    
    # Return the dictionary
    return master
