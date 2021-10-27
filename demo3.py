import requests
import json 
res=requests.get("https://merakilearn.org/api/courses" )
a=res.json()

course_list=(a["availableCourses"])
id_list=[]
slugs_list=[]
# pprint.pprint(len(course_list))
def first_api():
    with open("flight.json","w") as f:
        json.dump(a,f,indent=4)
        # course_list=(a["availableCourses"])
        course_index=0
        course=[]
        # id_list=[]
        while course_index<len(course_list):
            course_available=course_list[course_index]["name"]
            course.append(course_available)
            id_available=course_list[course_index]["id"]
            id_list.append(id_available)
            print(course_index+1,course_available,id_available)
            course_index+=1
first_api()

id_ = 0
def second_api():
    user=int(input("any number"))
    id_ = course_list[user-1]["id"]
    print(id_)
    data=requests.get("https://merakilearn.org/api/courses/"+str(id_)+"/exercises")
    fold=data.json()

    with open("flight2.json","w") as f1:
        json.dump(fold,f1,indent=4)

    # slugs_list=[]
    i=0
    while i<len(fold["data"]):
        print(i+1,fold["data"][i]["name"])
        print()
        if fold["data"][i]["childExercises"]==[]:
            a=fold["data"][i]["slug"]
            slugs_list.append(a)
        else:
            j=0
            while j<len(fold["data"][i]["childExercises"]):
                print("      ",j+1,fold["data"][i]["childExercises"][j]["name"])
                j+=1
        i+=1
    print(slugs_list)
    i=0
    while i<len(slugs_list):
        print(i+1,slugs_list[i])
        i+=1
second_api
slug_input=int(input("any number"))
def third_api():
    # slug_input=int(input("any number"))
    data2=requests.get("https://merakilearn.org/api/courses/"+str(id_)+"/exercise/getBySlug?slug="+slugs_list[slug_input])
    main_data=data2.json()
    


    with open("flight3.json","w") as f2:
        json.dump(main_data,f2,indent=4)

    with open("flight3.json","r") as f3:
        sign=json.load(f3)
        print(sign)
        print(sign["content"])
third_api()

while True:
    play=input("do u want to see again 1.up 2.next 3.pre 4.stop")
    if play=="up":
        first_api()
        print()
    elif play=="next":
        slug_input=slug_input+1
        third_api()
        print()
    elif play=="pre":
        slug_input=slug_input-1
        third_api()
        print()
    else:
        break
