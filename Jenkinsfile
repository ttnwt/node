pipeline {
    agent any 
    stages {
        stage('version') { 
            steps {
                sh 'python3 --version'
            }
        }
	stage("hello") {
            steps {
                sh 'groovy node.groovy'
            }
        }
    }
}
