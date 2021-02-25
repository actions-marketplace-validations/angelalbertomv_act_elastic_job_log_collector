import os
import requests

from elasticsearch import Elasticsearch

def main():
          
    GITHUB_REF = os.environ["GITHUB_REF"]    
    print(GITHUB_REF)        
    GITHUB_REPOSITORY = os.environ["GITHUB_REPOSITORY"]    
    print(GITHUB_REPOSITORY)    
    GITHUB_RUN_ID = os.environ["GITHUB_RUN_ID"]     
    print(GITHUB_RUN_ID)
    GITHUB_API_URL = os.environ["GITHUB_API_URL"]
    print(GITHUB_API_URL)
    
    INPUT_JOB = os.environ["INPUT_JOB"]
    GITHUB_TOKEN = os.environ["INPUT_GITHUB-TOKEN"]
    ELASTIC_USER = os.environ["INPUT_ELASTIC-USER"]
    ELASTIC_PSW = os.environ["INPUT_ELASTIC-PSW"]
    ELASTIC_HOST = os.environ["INPUT_ELASTIC-HOST"]
    ELASTIC_PORT = os.environ["INPUT_ELASTIC-PORT"]
           
    url = "{url}/repos/{repo}/actions/runs/{run_id}/jobs".format(url=GITHUB_API_URL,repo=GITHUB_REPOSITORY,run_id=GITHUB_RUN_ID)    
    
    r = requests.get(url, auth=('username',GITHUB_TOKEN))
    
    doc = {}
    
    print(str(r))
   
    response = eval(str(r.text))
          
    for job in response['jobs']:
        if job['name'] == INPUT_JOB:
          doc['id'] = job['id']
          doc['name'] = job['name']
          doc['status'] = job['conclusion']
          doc['started_at'] = job['started_at']
          doc['completed_at'] = job['completed_at']
            
    es = Elasticsearch(
        [ELASTIC_HOST],
        http_auth=(ELASTIC_USER, ELASTIC_PSW),
        scheme="https",
        port=ELASTIC_PORT,
    )
    
    res = es.index(index="GITHUB-INDEX", id=doc['id'], body=doc)
    print(res['result'])
                
    my_output = f"Hello {my_input}"       

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
