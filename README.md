# HNG12_Stage0

A simple Flask API for the HNG12 Stage 0 task that returns:  
- Registered email address  
- Current datetime in ISO 8601 format  
- GitHub URL of the project  

# Technologies Used
Python (Flask)

# Setup Instructions

Clone the repository:
```
git clone https://github.com/PreciousEzeigbo/HNG12_Stage0
```
Install dependencies:
```
pip install -r requirements.txt
```
Run the API locally:
```
python app.py or python3 app.py
```
Access via ```http://127.0.0.1:5000/```

## API Endpoint Sample Response
### **GET /**  
Returns:  

```json{
    "email": "your-email@example.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/yourusername/your-repo"
}
```

# Useful Links
https://hng.tech/hire/python-developers
