pipeline{
    agent any
    triggers {
        pollSCM '*/1 * * * *'
    }
    tools{
        nodejs '22.1.0'
    }
    stages{
        stage('Build'){
            steps{
                sh '''
                python3 --version
                node --version
                npm install newman
                '''
            }
        }
        stage('Test'){
            steps{
                sh '''
                newman run "API\\FakeRESTApi.Web V1.postman_collection.json" -e "API\\FakeRestAPI.postman_environment.json" --reporters cli,htmlextra --reporter-htmlextra-export "Reports\\HTML\\report.html"
                '''
            }
        }
    }
}
