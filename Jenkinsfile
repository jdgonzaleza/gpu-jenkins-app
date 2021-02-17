pipeline {
  agent {
    docker {
      image 'phoenixloka/unstructured_data'
      args '--gpu all'
    }

  }
  stages {
    stage('testing') {
      steps {
        sh 'pytest .'
      }
    }

  }
}