#----Definition-----
#Ans:Dict is a datastructure in python used to store multiple data in ke value pair(ky:value).
# Ordered ,mutable
#Index by key, not position
# Key must be unique
#value can be any data-type
#Used in fast lookup


# creation 
# stu_profile={"aman":'noida',"rohit":"meerut"}
# print(type(stu_profile))
# print(stu_profile)

# stu_marks=dict([('aman',400),('shivam',80)])
# print(stu_marks)


# stu_profile={"Aman":"JAIPUR","Rohit":"BHOPAL","Arvind":"Patna","Pradeep ":"Bihar"}
# stu_profile['aman']="dubai"
# print(stu_profile)

#inbult method

# stu_marks={'aman':80,'shivam':90,'rohan':40,'abhi':56}
# v=stu_marks.values()
# k=stu_marks.keys()
# i=stu_marks.items()
# res=stu_marks.get('amit',"not found")

# print(v)
# print("--------------------------------")
# print(k)
# print("--------------------------------")
# print(i)
# print("--------------------------------")
# print(res)

# update method
# stu_marks={'aman':80,'shivam':90,'rohan':40,'abhi':56}
# new_marks={"kamal":65,"ram":55,"raghav":44}
# stu_marks.update(new_marks)
# print(stu_marks)

# profile={'aman':{'address':["noida","delhi","mumbai"]}}
# print(profile)


profile={
    'aman':
    {'address':["noida","delhi","mumbai"],
      'hobbies':["travling","cooking","reading"],
      'password':{"insta":674657,"fb":7678458},
      },

    'Rohit':
    {'address':["noida","delhi","mumbai"],
      'hobbies':["travling","cooking","reading"],
      'password':{"insta":674657,"fb":7678458},
      }

      }
print(profile)

res=profile["aman"]["password"]["insta"]
print(res)