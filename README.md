
# QA-Practical-Project

# Brief
The brief provided to us for this project sets the following out as its overall objective: To create a service-orientated architecture application, which must be composed of at least 4 services that works together. 


In addition to what has been set out in the brief, I am also required to include the following:
•	An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.

•	This could also provide a record of any issues or risks that you faced creating your project.

•	An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be 

•	built through a CI server and deployed to a cloud-based virtual machine.

•	If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application

•	The project must follow the Service-oriented architecture that has been asked for.

•	The project must be deployed using containerisation and an orchestration tool.

•	As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.

•	The project must make use of a reverse proxy to make your application accessible to the user.


### Architecture

My application is a random dnd character generator. which has 4 services.

•	At its core Service 1 renders Jinja2 templates and sends a ‘get’ request to service 2 and 3 which generates random objects (weapon and element)

•	Service 4 combines service 2 and 3 based on pre-defined results then generates a random name and 'post' them over to service 1.

![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/artchi.png)

### Project tracking 

![Trello](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/trello.png)

### ERD diagram

![Erd](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/erd.png)

### VSC
The use of VSC was important as it manages the codes repository and it can push up changes to the main branch which contains the entire application which is saved into one place and is easily accessible it can also track any code that gets pushed in.

### Docker

Docker was used in this project as it a useful tool. It can create images using a Dockerfile, containerize application and run it with a single command, this is called docker-compose. Docker swarm was also used which is a orchestration tool that creates networks between the manager nodes and worker nodes to share the workload and act as an backup. This is important for rolling updates utilsing volumes as makes additional replicas for the update to run without interfering the user experience.

![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/docker.png)

### CI Pipeline
![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/ci%20pipeline.png)
Pictured above is the continuous integration pipeline with the associated frameworks and services related to them. This pipeline allows for rapid and simple development-to-deployment by automating the integration process, i.e. I can produce code on my local machine and push it to GitHub, which will automatically push the new code to Jenkins via a webhook to be automatically installed on the cloud VM. From there, tests are automatically run and reports are produced. A testing environment for the app is also run in debugger mode, allowing for dynamic testing.

### Jenkins

This process is handled by a Jenkins 'pipeline' job with distinct build stages. The design of this type of job means that if a previous build stage fails, the job will fail altogether and provide you with detailed information as to where this occurred. The more modular you make this system, the easier it is to pinpoint where your code is failing. As pictured below, the four build stages are:

'Checkout SCM' (pull code from Git respository)
'Build' (would be more accurately named 'Installation' as Python doesn't require building, in the strictest sense)
'Test' (run pytest, produce coverage report)
'Run' (start the flask-app service on the local VM, belonging to systemctl)  

![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/Jenkin%20pic.png.png)

Once the app is considered stable, it is then pushed to a separate VM for deployment. This service is run using the Python-based HTTP web server Gunicorn, which is designed around the concept of 'workers' who split the CPU resources of the VM equally. When users connect to the server, a worker is assigned to that connection with their dedicated resources, allowing the server to run faster for each user.

### Risk assessment

![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/risk.png)

### Testing 
### This is my first testing for service 1:
![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/pytest%20cov%20ser1.png)
### This is the the 2nd version of service 1:
![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/pytest%20cov%20ser1%20ver2.png) 
### Service 2:
![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/pytest%20cov%20ser2.png) 
### Service 3
![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/pytest%20cov%20ser3.png)
### Service 4:
![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/pytest%20cov%20ser4%20ver2.png)

### Front-End Design

![Home Page](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/home.png)

![Add Workout](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/demo%201.png)
![Add Session](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/demo%202.png)



### Known Issues

•	An error while trying to configure ansible

![View Page](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/error.png)
![View Page](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/error%202.png)




### Future Improvements

There are several improvements I would like to implement:


•	Try to fix the issue with ansible then the ci/cd pipeline will be completed

•	Add an image when the random character is generated 

•	HTML styling for better looks

•	Implement Nexus




	


### Author

Phillip Hau
