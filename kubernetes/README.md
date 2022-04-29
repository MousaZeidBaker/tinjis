# Kubernetes

## Prerequisites

- Kubernetes cluster
- kubectl command-line tool configured to communicate with the cluster

## Useful commands

Apply Kubernetes manifests
```shell
kubectl apply -k .
```

Get Node IP
```shell
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}'
```

Get Service NodePort
```shell
kubectl get svc -o jsonpath='{.items[*].spec.ports[*].nodePort}'
```
