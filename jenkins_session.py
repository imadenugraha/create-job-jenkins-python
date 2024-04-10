from dotenv import load_dotenv
import jenkins
import os


def jenkins_session() -> jenkins.Jenkins:
    load_dotenv()

    user = os.getenv('JENKINS_USER')
    token = os.getenv('JENKINS_TOKEN')
    url = os.getenv('JENKINS_URL')

    return jenkins.Jenkins(url, username=user, password=token)
