# Create Job Jenkins Python

This is a simple script in purpose to create Jenkins Job using Python-Jenkins.

## How To Use
1. Get config.xml from existing Job in Jenkins using curl
```shell
$ curl -X GET https://example.com/job/test/config.xml -u username:API_TOKEN -o Jenkins_Job_Config/config.xml
```

2. Clone this script
```shell
$ git clone https://github.com/imadenugraha/create-job-jenkins-python.git
```

3. Copy .env.example and give it name .env
```shell
$ cp .env.example .env
```

4. Install script dependencies using poetry install
```shell
$ poetry install --no-root
```

5. Insert your credential and job name into the .env. Here is the example
```text
JENKINS_USER=user
JENKINS_TOKEN=askjdnasfajskaeasfn
JENKINS_URL=https://myjenkins.com
```

6. You can run this script using poetry run. Here is the example
```shell
$ poetry run python3 main.py /myApp/Staging
```
