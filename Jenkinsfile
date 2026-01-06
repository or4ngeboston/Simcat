pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:latest-noble'
        }
    }

    parameters {
        choice(name: 'BROWSER', choices: ['chromium', 'firefox', 'webkit'], description: 'Browser to run tests on')
        string(name: 'ENV', defaultValue: 'testing', description: 'Environment to run tests against')
    }

    environment {
        PLAYWRIGHT_BROWSERS_PATH = '0' // Optional: if using pre-baked image
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'playwright install-deps'
            }
        }
        stage('Run Tests') {
            steps {
                sh "pytest --junitxml=results.xml --html=report.html --self-contained-html --browser=${params.BROWSER}"
            }
        }
    }

    post {
        always {
            junit 'results.xml'
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Playwright HTML Report'
            ])
            archiveArtifacts artifacts: 'results.xml, report.html', allowEmptyArchive: true
        }
    }
}
