pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:v1.57.0-noble'
            args '--workdir /workspace --ipc=host'  // Fixes path bug + better for browsers
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm  // Explicit if needed
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
                // Browsers are pre-installed in this image
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=results.xml --html=report.html --self-contained-html'  // Adjust command to your needs
            }
        }

        stage('Publish Results') {
            steps {
                junit 'results.xml'
                archiveArtifacts artifacts: 'results.xml, report.html', allowEmptyArchive: true
                // Add publishHTML if you use it
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Tests passed!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}