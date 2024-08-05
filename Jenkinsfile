pipeline {
    agent any
    environment {
        PATH = "/var/lib/jenkins/.local/bin:${env.PATH}"
    }
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install pytest pytest-cov'
            }
        }
        stage('Run tests with coverage') {
            steps {
                script {
                    // Run tests, capture the exit status, but don't stop the pipeline
                    def testStatus = sh(script: 'pytest --cov=my_app test/ || echo "Tests failed, but continuing to generate the report."', returnStatus: true)

                    // Generate the report regardless of the test results
                    sh 'pytest --cov=my_app --cov-report=html test/'

                    // If tests failed, store the status for use in the post section
                    if (testStatus != 0) {
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
        stage('Archive the HTML report') {
            always{
                steps {
                    archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline executed successfully (regardless of test results).'
        }
        failure {
            // Additional actions can be taken on failure, if needed
            echo 'Some tests failed, and the build is marked as FAILURE.'
        }
    }
}
