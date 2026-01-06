pipeline {
    agent any  // Runs on Windows host, no buggy Docker agent

    stages {
        stage('Build Image') {
            steps {
                bat 'docker build -t simcat-test -f Dockerfile .'  // Builds your custom image with deps installed
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                docker run --rm --ipc=host ^
                -v "%WORKSPACE%":/workspace ^
                -w /workspace ^
                simcat-test ^
                pytest --junitxml=results.xml --html=report.html --self-contained-html
                '''
                // Customize pytest flags (e.g., add --browser ${params.BROWSER} if parameterized)
            }
        }

        stage('Publish Results') {
            steps {
                junit 'results.xml'  // Or '**/*.xml' for multiple reports
                archiveArtifacts artifacts: 'results.xml, report.html', allowEmptyArchive: true
                // If using HTML Publisher: publishHTML(target: [reportName: 'Playwright Report', reportDir: '.', reportFiles: 'report.html'])
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