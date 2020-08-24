pipeline {

  environment {
    APP_NAME = "python_app"
    IMAGE_TAG = "index.docker.io/${PROJECT}/${APP_NAME}:${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
    VERSION = "${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
    JENKINS_CRED = "${PROJECT}"
  }

  agent {
    kubernetes {
      label 'python_app'
      yaml """
        kind: Pod
        metadata:
          name: jenkins-agent
        spec:
          containers:
          - name: kaniko
            image: gcr.io/kaniko-project/executor:debug
            imagePullPolicy: Always
            command:
            - /busybox/cat
            tty: true
            volumeMounts:
              - name: docker-registry-config
                mountPath: /kaniko/.docker
          restartPolicy: Never
          volumes:
            - name: docker-registry-config
              configMap:
              items:
                - key: my-docker
                  path: docker-registry-config
          """
          }
  }

  stages {
    stage('Test') {
      steps {
        container('kaniko') {
          sh """
            echo "test"
          """
        }
      }
    }

    stage('Build and Push Image') {
      steps {
        git 'https://github.com/jenkinsci/docker-jnlp-slave.git'
        container('kaniko') {
            sh "`pwd`"
            sh "ls -lrt"
            sh '/kaniko/executor --dockerfile ./Dockerfile -c `pwd` --insecure --skip-tls-verify --cache=true --destination=index.docker.io/gmurra11/python-ptds:${VERSION}'
        }
      }
    }
  }
}
