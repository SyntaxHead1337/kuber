#!/bin/bash
# Deploy lokal auf k3s mit Rollout, PVC Check und Logs

DEPLOYMENT_NAME="flask-app"
CONTAINER_NAME="flask-app"
IMAGE="syntaxhead1337/kuber:latest"

echo "===1. Update Image im Deployment ==="
kubectl set image deployment/$DEPLOYMENT_NAME $CONTAINER_NAME=$IMAGE

echo "===2. Warten auf Rollout ==="
kubectl rollout status deployment/$DEPLOYMENT_NAME

echo "===3. Prüfen, ob MariaDB PVC existiert ==="
kubectl get pvc mariadb-pvc || echo "⚠️ PVC mariadb-pvc nicht gefunden!"

echo "===4. Pods und Services anzeigen ==="
kubectl get pods
kubectl get svc

echo "===5. Optional: DB Init testen ==="
kubectl exec -it $(kubectl get pod -l app=flask-app -o jsonpath="{.items[0].metadata.name}") -- python -c "
import requests
r = __import__('requests').get('http://localhost:5000/api/init')
print(r.text)"

echo "✅ Deployment abgeschlossen. Teste: curl http://localhost:30007/api/get"
