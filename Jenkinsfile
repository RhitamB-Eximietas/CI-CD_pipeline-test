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
                python ./testCh_report1.py
                '''
            }
        }
    }
}
