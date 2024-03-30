pipeline {
    agent any

    environment {
        MY_IMAGE = 'rabia/mlops-a01:final'
    }

    stages {
        stage('Build Image') {
            steps {
                script {
                    sh "docker build -t $MY_IMAGE ."
                }
            }
        }

        stage('Login and Push Image') {
            environment {
                CREDENTIALS = credentials('dockerhub-credentials')
            }
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'REGISTRY_USERNAME', passwordVariable: 'REGISTRY_PASSWORD')]) {
                        sh "echo $REGISTRY_PASSWORD | docker login -u $REGISTRY_USERNAME --password-stdin"

                        sh "docker push $MY_IMAGE"
                    }
                }
            }
        }
    }

    post {
        always {
            sh 'docker system prune -af'
        }
        success {
            echo 'Success'
            mail to: "rabiakewan402@gmail.com", subject: "Success CI: Project name -> ${env.JOB_NAME}", body: "<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> Build URL: ${env.BUILD_URL}", contentType: 'text/html'
        }
        failure {
            echo 'Failed'
            mail to: "rabiakewan402@gmail.com", subject: "ERROR CI: Project name -> ${env.JOB_NAME}", body: "<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> Build URL: ${env.BUILD_URL}", contentType: 'text/html'
        }
    }
}
