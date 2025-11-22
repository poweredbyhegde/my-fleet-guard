# 🚛 FleetGuard: Real-Time Driver Anomaly Detection Pipeline

**FleetGuard** is an end-to-end MLOps project that processes real-time vehicle telemetry to detect dangerous driving behavior (anomalies) instantly.

Unlike traditional batch processing, this system uses a **streaming architecture** to ingest sensor data, retrieve windowed features from a **Feature Store** in milliseconds, and flag anomalies using an unsupervised machine learning model.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=yellow)
![Kafka](https://img.shields.io/badge/Redpanda-Kafka_API-red?logo=apachekafka)
![Feast](https://img.shields.io/badge/Feast-Feature_Store-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![AWS](https://img-shields.io/badge/AWS-EC2_Deployment-FF9900?logo=amazonaws)
![Streamlit](https://img.shields.io/badge/Streamlit-Real_Time_Dashboard-FF4B4B?logo=streamlit)

---

## 🏗️ Here is a demo of the application

https://github.com/user-attachments/assets/cd41a42f-821d-4af3-83dc-3a4ff43ce419


## 🏗️ System Architecture

The pipeline simulates a connected car fleet and processes data in real-time:

1.  **Data Ingestion:** **Redpanda (Kafka)** streams live telemetry (Speed, RPM, Throttle) from vehicles.
2.  **Feature Engineering:** **Feast** manages "windowed features" (e.g., *Average Speed over last 1 hour*) using **Redis** for low-latency online retrieval.
3.  **Machine Learning:** An **Isolation Forest** model (Unsupervised) detects anomalies based on historical driver patterns.
4.  **Inference:** A consumer service reads from Kafka, fetches features from Feast, and predicts anomalies in sub-second time.
5.  **Monitoring:** A **Streamlit** dashboard visualizes the live fleet status and alerts.

---

## 🚀 Key Features

* **Event-Driven Architecture:** Fully decoupled Producer and Consumer services using Kafka topics.
* **Feature Store Integration:** Ensures training-serving 



skew is eliminated by using Feast for both historical training data and online inference.
* **Unsupervised Learning:** Detects unknown failure modes without needing labeled "crash" data.
* **Cloud Native:** Fully containerized and deployed on **AWS EC2** with custom networking and security groups.

---

## 🛠️ How to Run Locally

### Prerequisites
* Docker & Docker Compose
* Python 3.11+ (in a virtual environment)

### 1. Start the Infrastructure
Spin up Redpanda (Kafka) and Redis using Docker Compose.
docker-compose up -d


### 2. Start the Simulation (The Truck)
Run the producer to generate synthetic sensor data.
python producer.py


### 3. Start the Processor 
Run the consumer to read data, fetch features, and make predictions.
python consumer.py

### 4. Launch the Dashboard
View the live telemetry and alerts.
streamlit run dashboard.py
