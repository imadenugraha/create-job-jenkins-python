from jenkins_session import jenkins_session
import logging
import os

def create_job() -> bool:
    server = jenkins_session()

    job_name = os.getenv('JOB_NAME')

    with open('./Jenkins_Job_Config/config.xmlconfig.xml', 'r') as f:
        job_config = f.read()

    try:
        server.create_job(job_name, job_config)
        return True
    except Exception as e:
        logging.error(e)
        return False
