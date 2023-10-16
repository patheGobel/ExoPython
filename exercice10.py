"""Exercise 10: Access the nested key increment from the following dictionary
Given:

emp_dict = {
    "company": {
        "employee": {
            "name": "Jess",
            "payable": {
                "salary": 9000,
                "increment": 12
            }
        }
    }
}"""

def accessTheNestedKeyIncrementFromTheFollowingDictionary(dic):
    dic["company"]["employee"]["payable"]["increment"]=dic["company"]["employee"]["payable"]["increment"]+1
    return dic

emp_dict = {
    "company": {
        "employee": {
            "name": "Jess",
            "payable": {
                "salary": 9000,
                "increment": 12
            }
        }
    }
}

print(f"{accessTheNestedKeyIncrementFromTheFollowingDictionary(emp_dict)}")