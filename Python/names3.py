users = {
 'Students': [
     {'id': 1,'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'id': 2,'first_name' : 'John', 'last_name' : 'Rosales'},
     {'id': 3,'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'id': 4,'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'id': 1,'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'id': 2,'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
for keys in users:
    print(keys)
    for prop in users[keys]:
        print prop["id"],"-",prop["first_name"],prop["last_name"],"-",len(prop["first_name"])+len(prop["last_name"])
