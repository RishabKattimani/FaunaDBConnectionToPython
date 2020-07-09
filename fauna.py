
#-------------------------------------------------------------------------------------------------------
# Imports
import re
import json
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
 #---------------------------------------------------------------------------------------------------
 # Variables & Setup
client = FaunaClient(secret="YOUR_SECRET_HERE")
c = client.query(
    q.paginate(
    q.match(q.index('YOUR_INDEX_HERE')))
 )
list1=[c['data']]
string = str(list1)
pattern = '\d+'
result = re.findall(pattern, string)
index = (len(result))
#--------------------------------------------------------------------------------------------------------

for j in range(0, index, 1):
  # print(result[j])

  i = result[j]
  c = client.query(q.get(q.ref(q.collection('YOUR_COLLECTION_HERE'), i)))

  list2=[c['data']]
  # print (list2)

# -----------------------------------------------------------------------------------

# for i in range(len(list)):
  print("UserName:",list2[0].get("UserName"))
  print("Email:",list2[0].get("EmailID"))
  print("Password:",list2[0].get("Password"))
  print("Phonenum:",list2[0].get("PhoneNo"))
  print("City:",list2[0].get("City"))
  print("Country:",list2[0].get("Country"))
  print('--------------------------------------------------------')

#------------------------------------------------------------------------------------------

client.query(
   q.create(
     q.collection("COLLECTION_NAME"),
     {"data": {"UserName": " NewUser", "EmailID": "newuser@hotmail.com", "Password": "user123", "City": "Raliegh", "Country": "USA"}}
   ))
# Above just creates the new collection with data
