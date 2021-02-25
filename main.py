import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    
    my_input = os.environ["INPUT_MYINPUT"]
    
    GITHUB_JOB = os.environ["GITHUB_JOB"]    
    print(GITHUB_JOB)    
    GITHUB_REF = os.environ["GITHUB_REF"]    
    print(GITHUB_REF)        
    GITHUB_REPOSITORY = os.environ["GITHUB_REPOSITORY"]    
    print(GITHUB_REPOSITORY)    
    GITHUB_REPOSITORY_OWNER = os.environ["GITHUB_REPOSITORY_OWNER"]
    print(GITHUB_REPOSITORY_OWNER)    
    GITHUB_RUN_ID = os.environ["GITHUB_RUN_ID"]     
    print(GITHUB_RUN_ID)
    GITHUB_RUN_NUMBER = os.environ["GITHUB_RUN_NUMBER"]     
    print(GITHUB_RUN_NUMBER)
    GITHUB_WORKFLOW = os.environ["GITHUB_WORKFLOW"]
    print(GITHUB_WORKFLOW)
    GITHUB_SERVER_URL = os.environ["GITHUB_SERVER_URL"]
    print(GITHUB_SERVER_URL)
    GITHUB_API_URL = os.environ["GITHUB_API_URL"]
    print(GITHUB_API_URL)
    GITHUB_ACTION = os.environ["GITHUB_ACTION"]
    print(GITHUB_ACTION)
    ACTIONS_RUNTIME_URL = os.environ["ACTIONS_RUNTIME_URL"]
    print(ACTIONS_RUNTIME_URL)
    ACTIONS_RUNTIME_TOKEN = os.environ["ACTIONS_RUNTIME_TOKEN"]
    print(ACTIONS_RUNTIME_TOKEN)
    
    GITHUB_TOKEN = os.environ["INPUT_GITHUB-TOKEN"]
    print(GITHUB_TOKEN)        
           
    url = "{url}/repos/{repo}/actions/runs".format(url=GITHUB_API_URL,repo=GITHUB_REPOSITORY)
    
    print(url)    
    
    r = requests.get(url, auth=('username','cfcf999d8c90445649ed10f1f0189d2a11975d04'))
    
    print(str(r))        
    print(str(r.text))    
                
    head = {'Authorization': 'Bearer ' + ACTIONS_RUNTIME_TOKEN}
           
    url = "{url}repos/{repo}/actions/runs".format(url=ACTIONS_RUNTIME_URL,repo=GITHUB_REPOSITORY)
    
    print(url)    
    
    r = requests.get(url, head)
    
    print(str(r))    
    
    print(str(r.text))    
    
    my_output = f"Hello {my_input}"       

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
