import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    
    my_input = os.environ["INPUT_MYINPUT"]
    
    GITHUB_JOB = os.environ["GITHUB_JOB"]
    
    print(GITHUB_JOB)
    
    GITHUB_REF = os.environ["GITHUB_REF"]
    
    print(GITHUB_REF)
        
    GITHUB_REPOSITORY = os.environ["GITHUB_REPOSITORY"]    
    GITHUB_REPOSITORY_OWNER = os.environ["GITHUB_REPOSITORY_OWNER"]
    GITHUB_RUN_ID = os.environ["GITHUB_RUN_ID"]     
    print(GITHUB_RUN_ID)
    GITHUB_RUN_NUMBER = os.environ["GITHUB_RUN_NUMBER"]     

    GITHUB_WORKFLOW = os.environ["GITHUB_WORKFLOW"]
    
    print(GITHUB_WORKFLOW)

    GITHUB_SERVER_URL = os.environ["GITHUB_SERVER_URL"]
    
    print(GITHUB_SERVER_URL)
    
    GITHUB_API_URL = os.environ["GITHUB_API_URL"]
    
    print(GITHUB_API_URL)
    GITHUB_ACTION = os.environ["GITHUB_ACTION"]

    ACTIONS_RUNTIME_URL = os.environ["ACTIONS_RUNTIME_URL"]
    print(ACTIONS_RUNTIME_URL)
    ACTIONS_RUNTIME_TOKEN = os.environ["ACTIONS_RUNTIME_TOKEN"]
    print(ACTIONS_RUNTIME_TOKEN)
    
    url = "{url}/repos/{owner}/{repo}/actions/runs/{run_id}".format(url=ACTIONS_RUNTIME_URL,owner=GITHUB_REPOSITORY_OWNER,repo=GITHUB_REPOSITORY,run_id=GITHUB_RUN_ID)
    
    r = requests.get(url)
    
    print(str(r))
    
    url = "{url}/repos/{owner}/{repo}/actions/runs/{run_id}".format(url=GITHUB_SERVER_URL,owner=GITHUB_REPOSITORY_OWNER,repo=GITHUB_REPOSITORY,run_id=GITHUB_RUN_ID)
    
    r = requests.get(url)
    
    print(str(r))

    my_output = f"Hello {my_input}"       

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
