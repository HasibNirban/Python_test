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
                    // Run tests but continue even if there are failures
                    sh 'pytest --cov=my_app --junitxml=results.xml test/ || echo "Tests failed, but continuing to generate the report."'
                }
            }
        }
        stage('Generate HTML report') {
            steps {
                // Generate the report even if tests have failed
                sh 'pytest --cov=my_app --cov-report=html --junitxml=results.xml test/'
            }
        }
        stage('Archive the HTML report and test results') {
            steps {
                archiveArtifacts artifacts: 'htmlcov/**, results.xml', allowEmptyArchive: true
            }
        }
    }
    post {
        always {
            echo 'Pipeline executed successfully'
        }
        failure {
            echo 'There were test failures.'
        }
    }
}
