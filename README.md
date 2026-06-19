# Production-Style Multi-Tier E-Commerce Platform on AWS

## Overview

This project demonstrates the design and implementation of a production-style multi-tier e-commerce platform on AWS using containerized microservices, event-driven architecture, security best practices, monitoring, and CI/CD automation.

The platform consists of multiple Flask-based microservices deployed on Amazon ECS Fargate behind an Application Load Balancer. The architecture integrates relational and NoSQL databases, object storage, asynchronous messaging, serverless processing, centralized monitoring, and AWS security services.

The primary objective of this project is to gain hands-on experience with AWS cloud architecture and modern DevOps practices rather than complex application development.

---

# Architecture

```text
Users
   │
   ▼
AWS WAF
   │
   ▼
Application Load Balancer
   │
   ▼
Amazon ECS Fargate
   ├── User Service
   ├── Product Service
   └── Order Service

Data Layer
   ├── Amazon RDS PostgreSQL
   ├── Amazon DynamoDB
   └── Amazon S3

Event Layer
   ├── Amazon SQS
   ├── AWS Lambda
   └── Amazon SNS

Security Layer
   ├── IAM Roles
   ├── AWS KMS
   ├── AWS Secrets Manager
   └── AWS CloudTrail

Observability
   ├── CloudWatch Logs
   ├── CloudWatch Metrics
   ├── CloudWatch Alarms
   └── CloudWatch Dashboard

CI/CD
   └── GitHub Actions → Amazon ECR → Amazon ECS
```

---

# Project Objectives

- Build a production-style AWS architecture
- Deploy containerized microservices using ECS Fargate
- Implement an event-driven architecture using SQS, Lambda, and SNS
- Integrate relational and NoSQL databases
- Apply AWS security best practices
- Implement centralized logging and monitoring
- Automate deployments using GitHub Actions
- Gain practical experience with AWS services commonly used in enterprise environments

---

# AWS Services Used

## Compute

- Amazon ECS Fargate
- AWS Lambda

## Containers

- Amazon ECR

## Networking

- Amazon VPC
- Public Subnets
- Private Subnets
- Internet Gateway
- NAT Gateway
- Route Tables
- Application Load Balancer

## Databases

- Amazon RDS PostgreSQL
- Amazon DynamoDB

## Storage

- Amazon S3

## Messaging

- Amazon SQS
- Amazon SNS

## Security

- IAM
- AWS KMS
- AWS Secrets Manager
- AWS CloudTrail
- AWS WAF

## Monitoring

- Amazon CloudWatch Logs
- Amazon CloudWatch Metrics
- Amazon CloudWatch Alarms
- Amazon CloudWatch Dashboard

## CI/CD

- GitHub Actions

---

# Microservices

## User Service

Provides user-related API endpoints.

Example Endpoint:

```http
GET /users
```

---

## Product Service

Provides product-related API endpoints.

Example Endpoint:

```http
GET /products
```

---

## Order Service

Provides order-related API endpoints.

Example Endpoint:

```http
GET /orders
```

---

# Infrastructure Design

## VPC Architecture

### Public Subnets

Used for:

- Application Load Balancer
- NAT Gateway

### Private Subnets

Used for:

- ECS Tasks
- RDS PostgreSQL

### Internet Gateway

Provides internet connectivity to public resources.

### NAT Gateway

Allows private resources to access the internet securely.

---

# Container Deployment

Each microservice is containerized using Docker.

### Container Workflow

```text
Source Code
    │
    ▼
Docker Build
    │
    ▼
Amazon ECR
    │
    ▼
Amazon ECS Fargate
```

---

# Data Layer

## Amazon RDS PostgreSQL

Used for:

- User data
- Order data
- Transactional workloads

### Benefits

- ACID compliance
- Structured schema
- Relational queries

---

## Amazon DynamoDB

Used for:

- Event storage
- Order event history
- High-performance NoSQL access

### Benefits

- Fully managed
- Low latency
- High scalability

---

## Amazon S3

Used for:

- Product images
- Static assets
- Log storage

### Features

- Versioning enabled
- Encryption enabled

---

# Event-Driven Architecture

Order processing is implemented using asynchronous AWS services.

## Flow

```text
Order Service
     │
     ▼
Amazon SQS
     │
     ▼
AWS Lambda
     │
     ▼
Amazon SNS
     │
     ▼
Email Notification
```

---

## Benefits

- Decoupled architecture
- Improved scalability
- Increased reliability
- Asynchronous processing

---

# Security Implementation

## IAM Roles

Used for:

- ECS Task Execution
- ECS Application Access

Principle applied:

- Least Privilege Access

---

## AWS KMS

Used for encryption of:

- S3 objects
- Secrets Manager secrets

---

## AWS Secrets Manager

Used for secure storage of:

- Database credentials
- Application secrets

---

## AWS CloudTrail

Used for:

- API activity auditing
- Governance
- Compliance tracking

---

## AWS WAF

Protects the Application Load Balancer using:

- AWS Managed Rule Sets
- IP Reputation Lists
- Rate Limiting Rules

---

# Monitoring and Observability

## CloudWatch Logs

Log groups created for:

```text
/ecs/user-service
/ecs/product-service
/ecs/order-service
/lambda/process-order-events
```

---

## CloudWatch Metrics

Monitored resources:

- ECS Services
- RDS
- Lambda
- SQS
- DynamoDB

---

## CloudWatch Alarms

Configured alarms:

- High RDS CPU Usage
- Lambda Errors
- SQS Queue Backlog

---

## CloudWatch Dashboard

Provides centralized visibility into:

- ECS Services
- RDS
- Lambda
- SQS
- DynamoDB

---

# CI/CD Pipeline

GitHub Actions automates the deployment process.

## Pipeline Flow

```text
Developer Push
      │
      ▼
GitHub Actions
      │
      ▼
Build Docker Image
      │
      ▼
Push Image to Amazon ECR
      │
      ▼
Deploy to Amazon ECS
```

---

# ECS Deployment

## ECS Cluster

- ECS Fargate
- Multi-service deployment

## ECS Services

- User Service
- Product Service
- Order Service

## Load Balancing

Application Load Balancer routes traffic using path-based routing.

### Routing Rules

```text
/users     → User Service
/products  → Product Service
/orders    → Order Service
```

---

# Auto Scaling

Configured using ECS Service Auto Scaling.

### CPU Scaling Policy

```text
Target CPU Utilization: 70%
```

### Memory Scaling Policy

```text
Target Memory Utilization: 80%
```

### Scaling Limits

```text
Minimum Tasks: 1
Maximum Tasks: 3
```

---

# Security Best Practices Implemented

- Private ECS deployment
- Private RDS deployment
- Secrets stored in Secrets Manager
- Encryption using KMS
- WAF protection
- CloudTrail auditing
- IAM role-based access
- Security Group isolation

---

# Cost Optimization Considerations

The following choices were made to reduce operational cost while maintaining architectural realism:

- ECS Fargate instead of EKS
- Standard SQS instead of FIFO
- Single NAT Gateway
- Minimal ECS task count
- DynamoDB on-demand capacity
- RDS db.t3.micro instance
- CloudWatch log retention configured

---

# Future Improvements

- CloudFront integration
- Route 53 custom domain
- HTTPS using ACM certificates
- Blue/Green deployments
- Infrastructure as Code using Terraform
- Multi-AZ RDS deployment
- AWS X-Ray tracing
- Centralized security monitoring

---

# Skills Demonstrated

- AWS Architecture Design
- ECS Fargate
- Docker
- CI/CD Automation
- Application Load Balancer
- Event-Driven Architecture
- Serverless Computing
- RDS PostgreSQL
- DynamoDB
- S3
- CloudWatch Monitoring
- IAM Security
- KMS Encryption
- Secrets Management
- CloudTrail Auditing
- AWS WAF
- GitHub Actions

---

# Resume Summary

Built a production-style multi-tier e-commerce platform on AWS using ECS Fargate microservices integrated with RDS PostgreSQL, DynamoDB, and S3. Implemented event-driven order processing using SQS, Lambda, and SNS. Automated container deployments through GitHub Actions and Amazon ECR. Secured workloads using IAM roles, AWS KMS, Secrets Manager, CloudTrail, and AWS WAF. Implemented centralized monitoring, alerting, and auto scaling using Amazon CloudWatch and ECS Service Auto Scaling.
