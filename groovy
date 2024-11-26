pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/DEVOPS-RA17.0437-8-Paulo.git'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/test_cadastro.py'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t flask_app .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
