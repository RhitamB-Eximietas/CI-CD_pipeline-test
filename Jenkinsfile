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
                robot --version
                node --version
                npm install newman
                '''
            }
        }
        stage('Test'){
            steps{
                sh '''
                robot ./Test1.robot
                '''
            }
        }
    }
}
