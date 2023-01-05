pipeline {
    agent any 
    stages {
        stage('Building') {
            steps {
                bat 'echo "build start"'
                bat 'echo "$HOME%"'
                sh 'echo $PATH; pip3 install -r requirements.txt'
                //bat 'pip install -r requirements.txt'
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
