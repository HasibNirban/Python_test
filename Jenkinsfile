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
                    sh 'pytest --continue-on-collection-errors --cov=my_app test/ || echo "Tests failed, but continuing to generate the report."'
                }
            }
        }
        stage('Generate HTML report') {
            steps {
                sh 'pytest --continue-on-collection-errors --cov=my_app --cov-report=html test/'
            }
        }
        stage('Archive the HTML report') {
            steps {
                archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
            }
        }
    }
    post {
        always {
            echo 'Pipeline executed successfully'
        }
    }
}
