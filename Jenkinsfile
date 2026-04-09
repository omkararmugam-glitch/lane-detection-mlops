pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/omkararmugam-glitch/lane-detection-mlops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t lane-detection-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 8000:8000 lane-detection-app'
            }
        }
    }
}
