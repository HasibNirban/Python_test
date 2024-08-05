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
                    def testStatus = sh(script: 'pytest --cov=my_app --cov-report=html test/', returnStatus: true)

                    if (testStatus != 0) {
                        echo "Some Tests failed, but the artifacts will be synced."
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
                echo "::: Pipeline executed successfully :::"
         }
    }
}
}