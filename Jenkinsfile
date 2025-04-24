pipeline {
    agent any

    environment {
        GIT_CREDENTIALS = credentials('github-token')
    }

    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/BhojanapuPavanKumar/python-atm.git', credentialsId: 'github-token'
            }
        }

        stage('Run ATM Script') {
            steps {
                script {
                    sh 'python3 atm.py'
                }
            }
        }
    }
}
