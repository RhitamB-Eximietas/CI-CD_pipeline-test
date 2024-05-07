import subprocess

def run_newman(collection_path , environment_path):
    json_report_path = 'POC_Robot_Newman\\JSON\\report.json'
    html_report_path = 'POC_Robot_Newman\\HTML\\report.html'
    command = [
        'C:\\Users\\RHITAM BHATTACHARYA\\AppData\\Roaming\\npm\\newman.cmd',
        'run', collection_path,
        '-e', environment_path,
        '--reporters', 'cli,htmlextra,json', 
        '--reporter-json-export', json_report_path, 
        '--reporter-htmlextra-export', html_report_path  
    ]
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
    return result.stdout, result.stderr, result.returncode


