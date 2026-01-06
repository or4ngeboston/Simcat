pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'  // Uses the Dockerfile you added
            args '--ipc=host'  // Optional: Improves browser performance in container
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
                // No need for 'playwright install' — browsers are pre-installed in the base image
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=results.xml --html=report.html --self-contained-html'  // Customize pytest flags as needed (e.g., add --browser if parameterized)
            }
        }

        stage('Publish Results') {
            steps {
                junit 'results.xml'  // Or '**/*.xml' if multiple files
                archiveArtifacts artifacts: 'results.xml, report.html', allowEmptyArchive: true
                // If using HTML Publisher plugin:
                // publishHTML(target: [allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: '.', reportFiles: 'report.html', reportName: 'Playwright Report'])
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