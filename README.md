### machine_learning_project

### Software and account Requirement.
1. [Github Account](https://github.com/)

2. [Heroku Account](https://id.heroku.com/login)

3. [VS Code IDE](https://id.heroku.com/login)

4. [GIT cli](https://code.visualstudio.com/download)
 
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)
Creating conda enviroment
```
conda create -p venv python==3.7 -y
```
conda activate venv/
```
pip install -r requirements.txt

```
To Add files to git
```
git add.

OR
```
git add file_name
```

Note : To ignore file or folder from git we can write of file / folder in .gitignore file

To check git status 
```
git status
```
To check all version maintained by git
```
git log
```
To create version/commit all changes by git
```
git commit -m "message"         
```
To send version/changes to github
 ```
 git push origin main
 ```
 To check remote url
 ```
 git remote -v
 ```
 
 To setup CI/CD pipeline in heroku we need 3 information 

 1. HEROKU_EMAIL = shivanshsarathe2710@gmail.com
 2. HEROKU_API_KEY = 65e598f5-b217-41c6-bf5b-2b8e45bc1699
 3. HEROKU_APP_NAME = ml-regression-appp


 BUILD DOCKER IMAGE
 ```
 docker build -t <image_name>:<tagname> .
 ```
 > NOTE :Image name for docker must be lowercase

 To list docker image 
 ```
 docker images
 ```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>

```
To check running container in docker 
```
docker ps
```
To stop  docker container 
```
docker stop <container_id>
```

```
python setup.py isntall
```