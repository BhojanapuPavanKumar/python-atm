pipeline {
    agent any

    parameters {
        string(name: 'PIN', defaultValue: '', description: 'ATM PIN (Leave empty to run default CI/CD flow)')
        choice(name: 'ACTION', choices: ['none', 'balance', 'withdraw', 'deposit'], description: 'Action to perform (choose "none" for CI/CD mode)')
        string(name: 'AMOUNT', defaultValue: '0', description: 'Amount (for deposit or withdraw)')
    }

    stages {
        stage('Check Python3 Location') {
            steps {
                sh 'which python3'
            }
        }

        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/BhojanapuPavanKumar/python-atm.git'
            }
        }

        stage('Run ATM Script') {
            steps {
                script {
                    def pythonCmd = '/usr/bin/python3' // Replace with output of 'which python3' on your system

                    if (params.PIN?.trim() && params.ACTION != 'none') {
                        def amount = params.AMOUNT?.trim()

                        if (params.ACTION in ['withdraw', 'deposit'] && (!amount.isInteger() || amount.toInteger() <= 0)) {
                            error("Invalid amount provided for ${params.ACTION}. Please enter a positive number.")
                        }

                        def command = "${pythonCmd} atm.py ${params.PIN} ${params.ACTION}"
                        if (params.ACTION in ['withdraw', 'deposit']) {
                            command += " ${amount}"
                        }

                        echo "Executing: ${command}"
                        sh command
                    } else {
                        echo "Running default CI/CD pipeline steps"
                        sh "${pythonCmd} atm.py 1234 balance"
                        sh "${pythonCmd} atm.py 1234 withdraw 5000"
                        sh "${pythonCmd} atm.py 1234 deposit 10000"
                    }
                }
            }
        }
    }
}
