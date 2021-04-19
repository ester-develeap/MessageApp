pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                sh "docker build -t msgapp ."
            }
        }
        stage('Test') {
            steps {
                sh "docker run --rm --entrypoint=pytest msgapp"
            }
        }
        stage('Deploy') {
            steps {
                sh "docker run --rm -d msgapp"
            }
        }
    }
}
