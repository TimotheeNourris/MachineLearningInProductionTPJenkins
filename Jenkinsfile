pipeline {
    agent any 
    stages {
        stage('Build part') {
            steps {
                bat 'echo "build start"'
                bat 'echo "$HOME%"'
                bat 'pip3 install -r requirements.txt'
                bat 'python --version'
            }
        }

        stage('Test part') {
            steps {       
                bat 'echo "test start"'
                bat 'python -m unittest'
            }
        }
        
        stage('Deploy part') {
            steps {
                bat 'docker build -t jenkinsdocker .'
                bat 'docker run -d -p 5000:5000 jenkinsdocker'
            }
        }       
    }
    triggers {
        githubPush()
    }
}
