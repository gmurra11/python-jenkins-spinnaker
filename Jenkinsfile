pipeline {

  environment {
    REGISTRY = "index.docker.io"
    PROJECT = "gmurra11"
    IMAGE = "python-ptds"
    VERSION = "${env.BUILD_NUMBER}"
    BRANCH = "${env.BRANCH_NAME}"
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

    stage('Update k8s yamls') {
      steps {
        container('kaniko') {
          sh """
          sed -i.bak 's#version: jenkins-will-replace#version: ${VERSION}#' ./k8s/app/*.yaml;
          sed -i.bak 's#name: python-ptds-*#name: python-ptds-${BRANCH}' ./k8s/app/*.yaml;
          sed -i.bak 's#name: python-ptds-service-*#name: python-ptds-service-${BRANCH}' ./k8s/app/*.yaml;
        }
      }
    }

    stage('Build and Push Image') {
      steps {
        container('kaniko') {
            sh """
            /kaniko/executor --context `pwd` --verbosity debug --insecure --skip-tls-verify --cache=true --destination="${REGISTRY}/${PROJECT}/${IMAGE}:${BRANCH}.${VERSION}"
            """
        }
      }
    }
  }
}
