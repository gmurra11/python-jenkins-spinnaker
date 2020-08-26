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
            workingDir: /tmp/jenkins
            image: gcr.io/kaniko-project/executor:debug
            imagePullPolicy: Always
            command:
            - /busybox/cat
            tty: true
            volumeMounts:
              - name: jenkins-docker-cfg
                mountPath: /kaniko/.docker
          restartPolicy: Never
          volumes:
          - name: jenkins-docker-cfg
            projected:
              sources:
              - secret:
                  name: regcred
                  items:
                    - key: .dockerconfigjson
                      path: config.json
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
        container('kaniko') {
            sh """
            /kaniko/executor --context `pwd` --verbosity debug --insecure --skip-tls-verify --cache=true --destination=index.docker.io/gmurra11/python-ptds:${VERSION}
            """
        }
      }
    }
  }
}
