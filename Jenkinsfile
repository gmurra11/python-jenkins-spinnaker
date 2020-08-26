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
          - name: jnlp
            workingDir: /tmp/jenkins
          - name: kaniko
            workingDir: /tmp/jenkins
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
                - key: .dockerconfigjson
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
      environment {
          PATH = "/busybox:/kaniko:$PATH"
      }
      steps {
        container(name: 'kaniko', shell: '/busybox/sh') {
            git 'https://github.com/jenkinsci/docker-jnlp-slave.git'
            git 'https://github.com/gmurra11/python-jenkins-spinnaker.git'
            sh """
            df -Ph
            ls -lrt /tmp/jenkins/workspace/my-app2_development
            ls -lrt /tmp/jenkins
            ls -lrt /tmp/jenkins/workspace
            /kaniko/executor --context `pwd` --verbosity debug --insecure --skip-tls-verify --cache=true --destination=gmurra11/python-ptds:${VERSION}
            cat /kaniko/Dockerfile
            """
        }
      }
    }
  }
}
