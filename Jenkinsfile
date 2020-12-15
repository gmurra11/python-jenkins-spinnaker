pipeline {

  environment {
    REGISTRY = "index.docker.io"
    PROJECT = "gmurra11"
    IMAGE = "python-ptds"
    VERSION = "${env.BRANCH_NAME}.${env.BUILD_NUMBER}"
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
            image: gcr.io/kaniko-project/executor:debug-b04399eeac3da9533a8cfa1db7650b8899af5a8d
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
            /kaniko/executor --context `pwd` --verbosity debug --insecure --skip-tls-verify --cache=true --destination=${REGISTRY}/${PROJECT}/${IMAGE}:${VERSION}
            """
        }
      }
    }
  }
}
