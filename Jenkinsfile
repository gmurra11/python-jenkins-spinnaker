pipeline {

  environment {
    APP_NAME = "python_app"
    FE_SVC_NAME = "${APP_NAME}"
    CLUSTER = "jenkins-cd"
    CLUSTER_ZONE = "europe-west2-a"
    IMAGE_TAG = "docker.io/${PROJECT}/${APP_NAME}:${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
    VERSION = "${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
    JENKINS_CRED = "${PROJECT}"
  }

  agent {
    kubernetes {
      label 'python_app'
      defaultContainer 'jnlp'
      yaml """
apiVersion: v1
kind: Pod
metadata:
labels:
  component: ci
spec:
  # Use service account that can deploy to all namespaces
  serviceAccountName: cd-jenkins
  containers:
  - name: gcloud
    image: gcr.io/cloud-builders/gcloud
    command:
    - cat
    tty: true
  - name: kubectl
    image: docker.io/cloud-builders/kubectl
    command:
    - cat
    tty: true
"""
}
  }
  stages {
    stage('Test') {
      steps {
        container('kubectl') {
          sh """
            echo "test"
          """
        }
      }
    }
    stage('Build and push image with Container Builder') {
      steps {
        container('gcloud') {
          sh("sed -i.bak 's#1.0#${VERSION}#' ./templates/form.html")
          sh "PYTHONUNBUFFERED=1 gcloud builds submit -t ${IMAGE_TAG} ."
        }
      }
    }
    }
  }
}
