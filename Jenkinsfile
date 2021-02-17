pipeline {
  agent {
    docker {
      image 'phoenixloka/unstructured_data'
      args '--gpus all'
    }

  }
  stages {
    stage('testing') {
      steps {
        sh 'pip3 install pytest --user'
        sh 'pytest .'
      }
    }

  }
}