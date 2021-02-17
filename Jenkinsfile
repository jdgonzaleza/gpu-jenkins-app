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
        sh 'pip install pytest'
        sh 'pytest .'
      }
    }

  }
}