# Preface

We're really happy that you're considering to join us! Here's a challenge that will help us understand your skills and serve as a starting discussion point for the interview.

We're not expecting that everything will be done perfectly as we value your time. You're encouraged to point out possible improvements during the interview though!

Have fun!

## The challenge

Pleo runs most of its infrastructure in Kubernetes. It's a bunch of microservices talking to each other and performing various tasks like verifying card transactions, moving money around, paying invoices ...

We would like to see that you both:
- Know how to create a small microservice
- Know how to wire it together with other services running in Kubernetes

We're providing you with a small service (Antaeus) written in Kotlin that's used to charge a monthly subscription to our customers. The trick is, this service needs to call an external payment provider to make a charge and this is where you come in.

You're expected to create a small payment microservice that Antaeus can call to pay the invoices. You can use the language of your choice. Your service should randomly succeed/fail to pay the invoice.

On top of that, we would like to see Kubernetes scripts for deploying both Antaeus and your service into the cluster. This is how we will test that the solution works.

## Instructions

Start by forking this repository. :)

1. Build and test Antaeus to make sure you know how the API works. We're providing a `docker-compose.yml` file that should help you run the app locally.
2. Create your own service that Antaeus will use to pay the invoices. Use the `PAYMENT_PROVIDER_ENDPOINT` env variable to point Antaeus to your service.
3. Your service will be called if you invoke `/rest/v1/invoices/pay` call on Antaeus. You can probably figure out which call returns the current status invoices by looking at the code ;)
4. Kubernetes: Provide deployment scripts for both Antaeus and your service. Don't forget about Service resources so we can call Antaeus from outside the cluster and check the results.
    - Bonus points if your scripts use liveness/readiness probes.
5. **Discussion bonus points:** Use the README file to discuss how this setup could be improved for production environments. We're especially interested in:
    1. How would a new deployment look like for these services? What kind of tools would you use?
    2. If a developers needs to push updates to just one of the services, how can we grant that permission without allowing the same developer to deploy any other services running in K8s?
    3. How do we prevent other services running in the cluster to talk to your service. Only Antaeus should be able to do it.

## How to run

If you want to run Antaeus locally, we've prepared a docker compose file that should help you do it. Just run:
```
docker-compose up
```
and the app should build and start running (after a few minutes when gradle does its job)

## How we'll test the solution

1. We will use your scripts to deploy both services to our Kubernetes cluster.
2. Run the pay endpoint on Antaeus to try and pay the invoices using your service.
3. Fetch all the invoices from Antaeus and confirm that roughly 50% (remember, your app should randomly fail on some of the invoices) of them will have status "PAID".

## Solution

Deploy services
```shell
kubectl apply -k kubernetes
```

To hit the Antaeus endpoint you need the cluster's node ip & node port
```shell
curl <NodeIP>:<NodePort>/rest/health
```

### Discussion
* How would a new deployment look like for these services? What kind of tools
  would you use?
    * Separate services into their own repositories
    * Use [Semantic Versioning](https://semver.org/) to tag images, it's easier
      to rollback if you know which version is running
    * Use
      [ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
      to route traffic into the cluster instead of NodePort
    * Use
      [volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
      to persist data in a pod, otherwise data will be lost on a pod restart
    * Configure [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
    * Consider using a GitOps tool, such as [Flux](https://fluxcd.io/), to
      automate infrastructure provisioning & application deployment
* If a developers needs to push updates to just one of the services, how can we
  grant that permission without allowing the same developer to deploy any other
  services running in K8s?
    * [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) can
      be used to regulate access, however developers SHOULD NOT deploy manually
      instead deployments should be carried out by CI/CD pipelines
* How do we prevent other services running in the cluster to talk to your
  service. Only Antaeus should be able to do it.
    * [Network
      Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
      can be used to control traffic flow

### Other comments
- The `payInvoices` method in `AntaeusRest.kt` makes an early exist whenever a
  payment fails resulting in unhandled payments, is that intended?
- The `Currency` enum class in `Currency.kt` does not properly serialize the
  values
