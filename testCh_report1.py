import subprocess 

def run_newman(collection_path,environment_path):
    json_report_path = 'Reports\\JSON\\report.json'
    html_report_path = 'Reports\\HTML\\report.html'
    command = [
        'C:\\Users\\RHITAM BHATTACHARYA\\AppData\\Roaming\\npm\\newman.cmd',
        'run', collection_path,
        '-e', environment_path,
        '--reporters', 'json,htmlextra', 
        '--reporter-json-export', json_report_path,
        '--reporter-htmlextra-export', html_report_path,
    ]
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
    return result.stdout, result.stderr, result.returncode      
if __name__ == '__main__':
    run_newman('API\FakeRESTApi.Web V1.postman_collection.json', 'API\FakeRestAPI.postman_environment.json')