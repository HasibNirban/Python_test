pipeline{
    agent any
    environment {
        PATH = "/var/lib/jenkins/.local/bin:${env.PATH}"
    }
    stages{
        stage('Install dependecies'){
            steps{
                sh 'pip install pytest pytest-cov'
            }
        }
        stage('Run tests with coverage'){
            steps{
                 script {
                    try {
                        sh 'pytest --cov=my_app test/'
                    } catch (Exception e) {
                        echo "Tests failed, but continuing to generate the report."
                    }
                }   
            }
        }
        stage('Generate HTML report'){
            steps{
                sh 'pytest --cov=my_app --cov-report=html test/'
            }
        }
        stage('Archive the html report'){
            steps{
                archiveArtifacts artifacts: 'htmlcov/**' ,allowEmptyArchive: true
            }
        }
    }
    post{
        always{
            echo 'Pipelien executed successfully'
        }
    }
}
