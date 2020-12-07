
# QA-Practical-Project

# Brief
The brief provided to us for this project sets the following out as its overall objective: To create a service-orientated architecture application, which must be composed of at least 4 services that works together. The services must be deployed by using docker to containerized the services and using docker swarm as a orchestration tool to deploy it out to the cluster. 


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



![ Architecture](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/artchi.png)

I must create 4 services which communicates as one service. My application is a random dnd character generator. 

•	Service 1 sends a ‘get’ request to service 2 (weapon) and 3 (element power).

•	Service 4 combines service 2 and 3 then generates a random name and sends them over to service 1.

## All  relevant images of the project can be found in the documents in the repo, this includes:

### ERD diagram

![Erd](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/erd.png)


### Project tracking 

![Trello](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/trello.png)

### Risk assessment

![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/risk.png)

### Testing 
This is my first testing for service 1:
![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/pytest%20cov%20ser1.png)
This is the the 2nd version
![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/pytest%20cov%20ser1%20ver2.png)
![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/pytest%20cov%20ser2.png)
![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/pytest%20cov%20ser3.png)
![](https://github.com/PhillipHage202/practical-project/blob/main/doc%20for%20pro/pytest%20cov%20ser4%20ver2.png)

### Front-End Design

![Home Page](https://github.com/PhillipHage202/QA-Fundemental-Project/blob/main/Documents/home%202.png)

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



	


### Author

Phillip Hau
