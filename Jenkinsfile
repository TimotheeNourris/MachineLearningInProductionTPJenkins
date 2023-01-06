pipeline {
    agent any 
    stages {
        stage('Build part') {
            steps {
                docker {
                    image 'Dockerimage'
                    // Run the container on the node specified at the
                    // top-level of the Pipeline, in the same workspace,
                    // rather than on a new node entirely:
                    reuseNode true
                }
                bat 'echo "build start"'
                bat 'echo "$HOME%"'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Test part') {
            steps {       
                bat 'python -m unittest'
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
