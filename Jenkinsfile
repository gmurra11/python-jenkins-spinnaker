pipeline {
   agent any

  environment {
    PROJECT = "gmura11"
    APP_NAME = "python_app"
    REGISTRY = "${PROJECT}/${APP_NAME}"
    IMAGE_TAG = "index.docker.io/${PROJECT}/${APP_NAME}:${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
    VERSION = "${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
    JENKINS_CRED = "${PROJECT}"
  }

  stages {
    stage('Test') {
      steps {
          sh """
            echo "yeeeeeeeeeeeeeeeeeee"
          """
        }
    }

    stage('Build and Push Image') {
        environment {
          registryCredential = 'dockerhub'
        }
        steps{
            script {
                def appimage = docker.build registry + ":$BUILD_NUMBER"
                docker.withRegistry( '', registryCredential ) {
                    appimage.push()
                    appimage.push('latest')
                }
            }
      }
    }
  }
}
