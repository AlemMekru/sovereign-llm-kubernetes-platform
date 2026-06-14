# Sovereign LLM Kubernetes Platform

🚧 **Work in Progress**

A production-grade Kubernetes platform for deploying private LLM and RAG workloads with Kubernetes, Docker, Helm, FastAPI, vLLM, CI/CD, Prometheus, Grafana, autoscaling, and secure secret management.

## Architecture

![Architecture](assets/Architecture.PNG)

## Project Structure

```text
sovereign-llm-kubernetes-platform/
├── assets/
│   └── Architecture.png            # System architecture diagram
├── .github/
│   └── workflows/                  # CI/CD pipelines
├── apps/
│   ├── api/
│   │   ├── main.py                 # FastAPI application
│   │   ├── requirements.txt        # Python dependencies
│   │   └── Dockerfile              # Container definition
│   ├── rag-service/                # Retrieval-Augmented Generation service
│   └── web/                        # Frontend application
├── infra/
│   ├── k8s/                        # Kubernetes manifests
│   ├── helm/                       # Helm charts
│   └── monitoring/                 # Prometheus & Grafana configuration
├── docs/
│   └── architecture.md             # Architecture notes and decisions
├── README.md
├── LICENSE
└── .gitignore
```

## Core Components

- **FastAPI Gateway** — API entry point for private LLM and RAG requests
- **RAG Service** — document retrieval and context generation
- **Vector Database** — semantic search over embedded documents
- **vLLM Inference Server** — private open-source LLM serving
- **Kubernetes** — container orchestration and deployment
- **Helm** — repeatable Kubernetes deployment packaging
- **Prometheus & Grafana** — monitoring, metrics, and dashboards
- **GitHub Actions** — automated CI/CD pipeline
- **Secrets Management** — secure configuration for API keys and environment variables

## Current Status

✅ Project architecture defined
✅ Repository structure created
✅ FastAPI service skeleton created
✅ Docker configuration added
✅ Kubernetes deployment manifest added
✅ Kubernetes service manifest added
🔄 Helm chart in development
🔄 Monitoring stack in development
🔄 CI/CD pipeline in development

## Roadmap

- [ ] Deploy FastAPI service to Kubernetes
- [ ] Configure Ingress
- [ ] Add Horizontal Pod Autoscaler
- [ ] Deploy Prometheus/Grafana
- [ ] Add GitHub Actions CI/CD
- [ ] Deploy vLLM inference service
- [ ] Add RAG document ingestion pipeline
- [ ] Add architecture screenshots
- [ ] Add local Minikube deployment guide

## Purpose

This project demonstrates practical AI infrastructure and MLOps skills by combining Kubernetes, LLM serving, RAG architecture, CI/CD, observability, and secure deployment patterns.

## Portfolio Focus

This repository is designed to showcase experience with:

- AI infrastructure
- Kubernetes deployment
- MLOps engineering
- Cloud-native application design
- Private LLM serving
- Enterprise RAG systems
- Production-style observability

## Developer

```text
Alem Mekru 
MSc. in Artificial Intelligence
```