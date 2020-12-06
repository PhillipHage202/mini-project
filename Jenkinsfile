pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh "bash ./scripts/setup.sh"
            }
        }
        stage('Test') {
            steps {
                sh "bash ./scripts/test.sh"
            }
        }
        stage('Build') {
            steps {
                sh "bash ./scripts/build.sh"
            }
        }
        stage('Deploy') {
            steps {
                sh "bash ./scripts/deploy.sh"
            }
        }
    }
}