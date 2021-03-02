import os
import requests
import json

from elasticsearch import Elasticsearch

def main():
    
    #Execution context variables
    GITHUB_REF = os.environ["GITHUB_REF"]          
    GITHUB_REPOSITORY = os.environ["GITHUB_REPOSITORY"]        
    GITHUB_RUN_ID = os.environ["GITHUB_RUN_ID"]         
    GITHUB_API_URL = os.environ["GITHUB_API_URL"]
    
    #User provided variables
    INPUT_JOB = os.environ.get("INPUT_JOB")
    GITHUB_TOKEN = os.environ.get("INPUT_GITHUB-TOKEN")
    ELASTIC_USER = os.environ.get("INPUT_ELASTIC-USER")
    ELASTIC_PSW = os.environ.get("INPUT_ELASTIC-PSW")
    ELASTIC_HOST = os.environ.get("INPUT_ELASTIC-HOST")
    ELASTIC_PORT = os.environ.get("INPUT_ELASTIC-PORT")                    
          
    assert INPUT_JOB != None and 
           GITHUB_TOKEN != None and 
           ELASTIC_USER != None and 
           ELASTIC_PSW != None and 
           ELASTIC_HOST != None and
           ELASTIC_PORT != None 
           
    url = "{url}/repos/{repo}/actions/runs/{run_id}/jobs".format(url=GITHUB_API_URL,repo=GITHUB_REPOSITORY,run_id=GITHUB_RUN_ID)    
    
    r = requests.get(url, auth=('username',GITHUB_TOKEN))
    
    doc = {}
    
    print(str(r))
   
    response = json.loads(r.text)
          
    es = Elasticsearch(
        [ELASTIC_HOST],
        http_auth=(ELASTIC_USER, ELASTIC_PSW),
        scheme="https",
        port=ELASTIC_PORT,
    )
          
    for job in response['jobs']:
        res = es.index(index="github", id=doc['id'], body=job)
        print("Job " + str(job['name']) + " inserted with result: " + str(res['result']))           
                
    my_output = f"Process completed!"       

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
