pipeline {
    agent {
        docker {
            image 'python:3.10' // Use a Python Docker image
        }
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/your-repo/python-atm.git'
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    sh 'python3 atm.py 1234 balance'
                }
            }
        }
    }
}
