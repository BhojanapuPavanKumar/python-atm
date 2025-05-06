pipeline {
    agent {
        docker {
            image 'python:3.10' // Use an official Python image
        }
    }

    parameters {
        string(name: 'PIN', defaultValue: '', description: 'ATM PIN (Leave empty to run default CI/CD flow)')
        choice(name: 'ACTION', choices: ['none', 'balance', 'withdraw', 'deposit'], description: 'Action to perform (choose "none" for CI/CD mode)')
        string(name: 'AMOUNT', defaultValue: '0', description: 'Amount (for deposit or withdraw)')
    }

    environment {
        GIT_CREDENTIALS = credentials('github-token') // GitHub personal access token (PAT)
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/BhojanapuPavanKumar/python-atm.git', credentialsId: 'github-token'
            }
        }

        stage('Run ATM Script') {
            steps {
                script {
                    if (params.PIN?.trim() && params.ACTION != 'none') {
                        def amount = params.AMOUNT?.trim()

                        if (params.ACTION in ['withdraw', 'deposit'] && (!amount.isInteger() || amount.toInteger() <= 0)) {
                            error("Invalid amount provided for ${params.ACTION}. Please enter a positive number.")
                        }

                        def command = "python atm.py ${params.PIN} ${params.ACTION}"
                        if (params.ACTION in ['withdraw', 'deposit']) {
                            command += " ${amount}"
                        }

                        echo "Executing: ${command}"
                        sh command
                    } else {
                        echo "Running default CI/CD pipeline steps"
                        sh 'python atm.py 1234 balance'
                        sh 'python atm.py 1234 withdraw 5000'
                        sh 'python atm.py 1234 deposit 10000'
                    }
                }
            }
        }
    }
}
