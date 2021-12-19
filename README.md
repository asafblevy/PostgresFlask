### Anzu Helm Chart ###

**Building the app image**
* If you're running the project on minikube you would first have to run the following command:
`eval $(minikube docker-env)` - after doing that minikube should recognize the image you build in the next step.
Run the following command: `docker build -t anzu-app:<app_version> .`

```shell
# needed if running on minikube
eval $(minikube docker-env)

docker build -t anzu-app .
```

**Installing or upgrading the Helm chart**

```shell
cd helm/
helm upgrade --install anzu --values  .
```

> Note: To check if the cluster is running run the command `kubectl get po` and make sure theres one pod called `anzu-app...`
   another pod called `anzu-init-job...`, and a final pod called `anzu-postgres...`

**Accessing the application**

To access the app through the ingress add the following record to the hosts file:

```shell
<host_ip> test.anzu
```

**Deploying a new version of the app**
1. Make the desired changes to the application in the app directory
2. Change directories to the main dir of the project
3. In the Dockerfile, update the `version` label and then run `docker build -t anzu-app:<app_version> .`
4. Go back into the `helm/` directory
5. Update the `app.image.tag` value in the `values.yaml` file
6. Run the following command: `helm upgrade --install --wait anzu .`
7. The pod should now be using the newly built image

