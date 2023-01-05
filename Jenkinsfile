pipeline {
    agent any 
    stages {
        stage('Building') {
            steps {
                sh 'echo "build start"'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Testing') {
            steps {       
                bat 'python -m unittest'
            }
        }
        stage('Deploying') {
            steps {
                bat 'docker build -t JenkinsDocker .'
                bat 'docker run -d -p 5000:5000 JenkinsDocker'
            }
        }
    }
    triggers {
        githubPush()
    }
}
