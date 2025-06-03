from fastapi import FASTAPI

app = FASTAPI() 

#endpoint
strudents = {
    
     1 : {
          "name" : "Abhinay",
          "age" : 20,      
     }  
}

@app.get("/")
def index():
    return {"message": "Welcome"}

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return authenticate_user(form_data)

@app.get("/get-student/{student_id}")
def get_student(student_id: int, username: str = Depends(verify_token)):
    if student_id in students:
        return students[student_id]
    else:
        return {"error": "Student not found"}


 
 
 