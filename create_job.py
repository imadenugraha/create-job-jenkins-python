from dotenv import load_dotenv
from jenkins_session import jenkins_session
import logging
import os


def create_job() -> bool:
    load_dotenv()

    server = jenkins_session()
    job_name = os.getenv('JOB_NAME')

    with open('./Jenkins_Job_Config/config.xml', 'r') as f:
        job_config = f.read()
        f.close()

    try:
        server.create_job(job_name, job_config)
        return True
    except Exception as e:
        logging.error(e)
        return False
