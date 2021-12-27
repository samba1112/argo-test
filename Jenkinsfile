pipeline {
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git url: 'https://github.com/samba1112/argo-test.git', branch:'main'
      }
    }
    stage('Building image') {
      steps{
        script {
          sh 'docker build -t samba1112/argotest:${BUILD_NUMBER} .'
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
         withCredentials([string(credentialsId: 'docker-hub', variable: 'password')]) {
          sh "docker login -u samba1112 -p ${password}"
          }
         sh 'docker push samba1112/argotest:${BUILD_NUMBER}'
          }
        }
      }
    stage('Helm value replace'){
        agent { docker { image 'samba1112/libconf'} }
        steps{
            script{
                sh'''
                git clone https://github.com/samba1112/argo-test.git
                cd argo-test/charts/example-chart/
                value=$(perl -MYAML -le 'print YAML::LoadFile(shift)->{image}{tag}' values.yaml)
                sed -i "s/tag: $value/tag: ${BUILD_NUMBER}/g" values.yaml
                git config user.email "sambasiva@gmail.com"
                git config user.name "samba1112"
                git add .
                git commit -m "push to git"
                git push https://ghp_CaMAyo2RW81@github.com/samba1112/argo-test.git'''
                dir ('argo-test') {
                      deleteDir()
                     }
            }
        }
    }
  }
   }
