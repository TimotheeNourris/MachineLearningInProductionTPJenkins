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
        stage('Deploy part') {
            steps {
                bat 'docker build -t Jenkinsdocker .'
                bat 'docker run -d -p 5000:5000 Jenkinsdocker'
            }
        }
        stage('Test part') {
            steps {       
                bat 'echo "test start"'
                bat 'python -m unittest'
            }
        }
       
    }
    triggers {
        githubPush()
    }
}
