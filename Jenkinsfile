pipeline {

agent {
        docker { image 'node:14-alpine' }
    }

  environment {
    PROJECT = "gmura11"
    APP_NAME = "python_app"
    IMAGE_TAG = "index.docker.io/${PROJECT}/${APP_NAME}:${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
    VERSION = "${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
    JENKINS_CRED = "${PROJECT}"
  }

  stages {
    stage('Test') {
      steps {
          sh """
            echo "test"
          """
        }
    }

    stage('Build and Push Image') {
      steps {
            sh """
              echo "test"
            """
        }
    }
  }
}
