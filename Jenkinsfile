pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:latest-noble'  // Or pin to specific version: v1.47.0-noble
            // Optional: reuse the same container for faster runs if supported
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm  // Automatically checks out your repo
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest'  // Add flags like -v for verbose, or --headed for debugging (but CI is usually headless)
            }
        }
    }
    post {
        always {
            // Optional: Archive reports or artifacts
            junit 'test-results/*.xml'  // If you use pytest --junitxml
            archiveArtifacts artifacts: 'playwright-report/**', allowEmptyArchive: true
        }
    }
}