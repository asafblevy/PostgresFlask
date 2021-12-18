### Kubernetes and helm chart installation instructions ###
To get kubernetes to work you first have to install docker
Follow the installation instructions for your OS type on the following site:
https://docs.docker.com/engine/install/
Run the command "docker ps" to make sure docker is installed correctly

After installing the docker engine you would have to get a kubernetes environment to run the project on:
For this project I chose minikube, the project should work on any other kubernetes environment you choose to use.
To install minikube follow the instructions on this page:
https://minikube.sigs.k8s.io/docs/start/s
Make sure you can run kubectl commands to make sure the next steps work:
for example try running "kubectl get pods"

Now you would have to install helm, the package manager which will get the whole project set up.
Go to this page and follow the instructions:
https://helm.sh/docs/intro/install/
To make sure helm is installed run the command - "helm version" and make sure youre not getting any errors

To clone the project's repository use the following command:
git clone git@github.com:asafblevy/PostgresFlask.git

Build the application Image:
* If you're running the project on minikube you would first have to run the following command:
"eval $(minikube docker-env)" - after doing that minikube should recognize the image you build in the next step.
Run the following command: "docker build -t anzu-app ."

Now it's time to get the cluster running!
1. cd into the helm directory
2. Run the following command: "helm upgrade --install <name of your choice> ." , I chose anzu-postgres
3. The cluster should be running with all components
4. To check if the cluster is running run the command "kubectl get po" and make sure theres one pod called anzu-postgres-app... 
   another pod called anzu-postgres-init-job..., and a final pod called anzu-postgres-postgres...

To deploy a new version of the application:
1. Make the desired changes to the application in the app directory
2. Change directories to the main dir of the project
3. Run "docker build -t anzu-app ."
4. Go back into the helm directory
5. Run the following command: "helm upgrade --install <name of your choice> ."
6. The new environment should use the new image you just built.

