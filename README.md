# Banking Microservices App

This project implements a simple banking application using microservices architecture. Each service is containerized using Docker and deployed via Docker Compose.

---

## Overview

### **Microservices**
1. **API Gateway**: Handles incoming requests and routes them to the appropriate service.
2. **Customer Service**: Manages customer information.
3. **Account Service**: Handles bank account details.
4. **Transaction Service**: Manages transactions between accounts.

### **Technology Stack**
- **Backend**: Python (Flask Framework)
- **Containerization**: Docker
- **Orchestration**: Docker Compose

---

## Prerequisites

Ensure the following are set up:

1. **AWS EC2 Instance**:
   - A Linux-based instance (e.g., Ubuntu 20.04 or Amazon Linux 2).
   - Security Group configured to allow incoming traffic on ports `5000-5003`.

2. **Installed Tools**:
   - **Docker**:
     ```bash
     sudo apt update
     sudo apt install docker.io -y
     sudo systemctl start docker
     sudo systemctl enable docker
     sudo usermod -aG docker $USER
     ```
   - **Docker Compose**:
     ```bash
     sudo curl -L "https://github.com/docker/compose/releases/download/v2.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
     sudo chmod +x /usr/local/bin/docker-compose
     ```

3. **Clone this Repository**:
   ```bash
   git clone https://github.com/<your-username>/banking-app.git
   cd banking-app



Here's a detailed version of the README.md with step-by-step instructions for deploying and accessing the application on an EC2 instance:

README.md
markdown
Copy code
# Banking Microservices App

This project implements a simple banking application using microservices architecture. Each service is containerized using Docker and deployed via Docker Compose.

---

## Overview

### **Microservices**
1. **API Gateway**: Handles incoming requests and routes them to the appropriate service.
2. **Customer Service**: Manages customer information.
3. **Account Service**: Handles bank account details.
4. **Transaction Service**: Manages transactions between accounts.

### **Technology Stack**
- **Backend**: Python (Flask Framework)
- **Containerization**: Docker
- **Orchestration**: Docker Compose

---

## Prerequisites

Ensure the following are set up:

1. **AWS EC2 Instance**:
   - A Linux-based instance (e.g., Ubuntu 20.04 or Amazon Linux 2).
   - Security Group configured to allow incoming traffic on ports `5000-5003`.

2. **Installed Tools**:
   - **Docker**:
     ```bash
     sudo apt update
     sudo apt install docker.io -y
     sudo systemctl start docker
     sudo systemctl enable docker
     sudo usermod -aG docker $USER
     ```
   - **Docker Compose**:
     ```bash
     sudo curl -L "https://github.com/docker/compose/releases/download/v2.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
     sudo chmod +x /usr/local/bin/docker-compose
     ```

3. **Clone this Repository**:
   ```bash
   git clone https://github.com/<your-username>/banking-app.git
   cd banking-app
Deployment Instructions
Follow these steps to deploy the application on the EC2 instance:
========================================================================================================================
Step 1: Start the Services
Navigate to the project directory:

bash
Copy code
cd banking-app
Build and start the services:

bash
Copy code
sudo docker-compose up --build -d
Verify that the containers are running:

bash
Copy code
sudo docker ps
Example Output:

bash
Copy code
CONTAINER ID   IMAGE                  COMMAND                  STATUS       PORTS
abc123         banking_app_gateway    "python app.py"         Up           0.0.0.0:5000->5000/tcp
def456         banking_app_customer   "python app.py"         Up           0.0.0.0:5001->5001/tcp
ghi789         banking_app_account    "python app.py"         Up           0.0.0.0:5002->5002/tcp
jkl012         banking_app_transaction "python app.py"        Up           0.0.0.0:5003->5003/tcp
