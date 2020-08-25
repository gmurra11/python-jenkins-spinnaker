pipeline {

  environment {
    PROJECT = "gmura11"
    APP_NAME = "python_app"
    IMAGE_TAG = "index.docker.io/${PROJECT}/${APP_NAME}:${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
    VERSION = "${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
    JENKINS_CRED = "${PROJECT}"
  }

  agent {
          docker { image 'node:14-alpine' }
      }

  stages {
    stage('Test') {
      steps {
        container('docker') {
          sh """
            echo "test"
          """
        }
      }
    }

    stage('Build and Push Image') {
      steps {
        container('docker') {
            sh """
              docker build . -t ${IMAGE_TAG}"
              docker push ${IMAGE_TAG}
            """
        }
      }
    }
  }
}
