pipeline {
    agent any

    parameters {
        string(name: 'PIN', defaultValue: '', description: 'ATM PIN (Leave empty to run default CI/CD flow)')
        choice(name: 'ACTION', choices: ['none', 'balance', 'withdraw', 'deposit'], description: 'Action to perform (choose "none" for CI/CD mode)')
        string(name: 'AMOUNT', defaultValue: '0', description: 'Amount (only for deposit)')
        string(name: 'WITHDRAW', defaultValue: '0', description: 'Amount (only for withdraw)')
    }

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
                    if (params.PIN?.trim() && params.ACTION != 'none') {
                        // Manual mode: run with provided params
                        def command = "python3 atm.py ${params.PIN} ${params.ACTION}"
                        
                        // Add amount for deposit or withdraw if provided
                        if (params.ACTION == 'withdraw' && params.WITHDRAW?.trim()) {
                            command -= " ${params.WITHDRAW}"
                        } else if (params.ACTION == 'deposit' && params.AMOUNT?.trim()) {
                            command += " ${params.AMOUNT}"
                        }

                        sh command
                    } else {
                        // Default CI/CD mode: fixed steps
                        sh 'python3 atm.py 1234 balance'
                        sh 'python3 atm.py 1234 withdraw 5000'
                        sh 'python3 atm.py 1234 deposit 10000'
                    }
                }
            }
        }
    }
}
