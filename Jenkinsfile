pipeline {
    agent any
    environment {
        PATH = "/var/lib/jenkins/.local/bin:${env.PATH}"
    }
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install pytest pytest-cov pytest-html pytest-metadata'
            }
        }
        stage('Run tests with coverage') {
            steps {
                script {
                    // Run tests, capture the exit status, but don't stop the pipeline
                    def testStatus = sh(script: 'pytest --cov=my_app --cov-report=html --html=full_report.html --self-contained-html', returnStatus: true)
                    // Generate the coverage report regardless of the test results
                    sh 'pytest --cov=my_app --cov-report=html test/'

                    // If tests failed, generate a report for only failed tests
                    if (testStatus != 0) {
                        sh 'pytest --last-failed --html=failed_tests_report.html --self-contained-html --tb=short'
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
                archiveArtifacts artifacts: 'full_report.html', allowEmptyArchive: true
                archiveArtifacts artifacts: 'failed_tests_report.html', allowEmptyArchive: true
                echo "::: Pipeline executed successfully :::"
         }
    }
}
}