pipeline {
    agent any

    stages {
        stage('Source Checkout') {
            steps {
                echo 'Verifying checked-out repository files...'
                sh 'ls -la'
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Creating Python virtual environment and installing requirements...'
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Automated Validation Tests') {
            steps {
                echo 'Running automated unit tests...'
                sh '''
                . venv/bin/activate
                python3 -m unittest discover -s . -v
                '''
            }
        }
        stage('Deployment Packaging') {
            steps {
                echo 'Packaging runnable artifact into deploy_artifact directory...'
                sh '''
                rm -rf deploy_artifact
                mkdir -p deploy_artifact
                cp delivery_metrics.py requirements.txt deploy_artifact/
                tar -czf delivery-metrics-artifact.tar.gz -C deploy_artifact .
                ls -lh deploy_artifact delivery-metrics-artifact.tar.gz
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'delivery-metrics-artifact.tar.gz', allowEmptyArchive: true
        }
        success {
            echo 'PIPELINE SUCCESS: Application validated and packaged!'
        }
        failure {
            echo 'PIPELINE FAILED: Validation failed. Deployment artifact blocked.'
        }
    }
}