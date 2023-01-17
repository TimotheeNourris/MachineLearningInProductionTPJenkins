pipeline {
    agent any 
    stages {
        stage('Build part') {
            steps {
                bat 'echo "build start"'
                bat 'echo "$HOME%"'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Test part') {
            steps {       
                python -m unittest
            }
        }
        stage('Deploy part') {
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
