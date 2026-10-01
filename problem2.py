
import json

student = {
    "name": "Shrabon",
    "age": 22,
    "department": "CST(Computer Science and Technology)",
}

student_json = json.dumps(student)

print(student_json)