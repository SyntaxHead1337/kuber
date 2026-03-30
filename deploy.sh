#!/bin/bash
# Deploy lokal auf k3s

# 1️⃣ Image in Deployment aktualisieren
kubectl set image deployment/flask-app flask-app=syntaxhead1337/kuber:latest

# 2️⃣ Warten, bis Rollout abgeschlossen ist
kubectl rollout status deployment/flask-app

# 3️⃣ Pods und Services anzeigen
echo "=== Pods ==="
kubectl get pods
echo "=== Services ==="
kubectl get svc
