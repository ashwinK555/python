student1 ={          #dictionaries are changeable
    "name": "Ashwin ",
    "address": "brt",
    "age":3,
    "marks": [12,23,2,22,33]
}
print(student1["marks"])

length = len(student1)
# print(length)

#changing values

student1["age"] = "ktm"
# print(student1)

#nested dic
student2 ={
  "name":"ashwin",
  "subjects":{
      "math":50,
      "sci":70,
      "com":80
  }
 }

# print(student2["subjects"]["math"])

#dictionaries methods
print(student1.keys())
student1.update({"location":"usa"})
print(student1)
print(student1.values())

# print(student1["names"]) #shows error (invalid key)
print(student1.get("names")) #no error