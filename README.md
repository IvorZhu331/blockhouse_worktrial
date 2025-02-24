# 📊 Trade Order API (FastAPI + Docker + AWS EC2 + CI/CD)

A **FastAPI** backend for managing trade orders, containerized using **Docker**, deployed on an **AWS EC2 instance**, and integrated with **GitHub Actions** for **CI/CD**.

---

## 🚀 Features

- ✅ **Create, Retrieve, and Delete** Trade Orders
- ✅ **Dockerized** for Easy Deployment
- ✅ **CI/CD Pipeline** with **GitHub Actions**
- ✅ **Deployed on AWS EC2**
- ✅ **SQLite** for Simplicity
- ✅ **Swagger/OpenAPI** Documentation

---

## 📁 Project Structure

```
project/ │ 
    ├── app/ │ 
      ├── main.py           # FastAPI entry point │ 
      ├── database.py       # SQLite database connection │ 
      ├── models.py         # Pydantic models │ 
      └── routers/ │ 
          └── orders.py     # API endpoints
    ├── test/ │ 
        └── test_orders.py  # Unit tests for API │ 
    ├── Dockerfile          # Docker container setup 
    ├── requirements.txt    # Python dependencies 
    ├── .github/ │ 
        └── workflows/ │ 
            └── ci-cd.yml   # GitHub Actions CI/CD pipeline └── README.md # Project documentation
```

---

## 🧑‍💻 API Documentation

**Swagger UI:**  
Visit → `http://54.163.82.225:8000/docs`  

**Available Endpoints:**

| Method   | Endpoint          | Description                      |
|----------|-------------------|----------------------------------|
| `POST`   | `/orders/`         | Create a new trade order        |
| `GET`    | `/orders/`         | List all trade orders           |
| `DELETE` | `/orders/{id}`     | Delete a trade order by ID      |

---

## 🐳 Local Setup with Docker

### **1. Clone the Repository**

```bash
git clone https://github.com/IvorZhu331/blockhouse_worktrial.git
cd blockhouse
```

### **2. Build the Docker Image**
```bash
docker build -t trade_order_api .
```

### **3.Run the Docker Container**
```bash
docker run -d -p 8000:8000 trade_order_api
```

### **4. Access the API**
Visit → `http://54.163.82.225:8000/docs`

---

## ✅ Running Tests
Run the following command to execute unit tests:

```bash
pytest test/
```





