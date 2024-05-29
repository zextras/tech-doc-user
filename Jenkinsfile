pipeline {
  agent {
    node {
      label 'python3-agent-v1'
    }
  }
  options {
    buildDiscarder(logRotator(numToKeepStr: '10'))
    timeout(time: 60, unit: 'MINUTES')
  }
  environment {
    SPHINX_DIR = '.'
    BUILD_DIR = 'build'
    SOURCE_DIR = 'source'
    WORKSPACE = pwd()
    PROJECT = "ztd-sphinx"
    DESTINATION = ""
    PRODUCTION_BRANCH = "master"
    STAGING_BRANCH = "pre_release"
    PRODUCTION_BUCKET_NAME = "docs.zextras.com"
    STAGING_BUCKET_NAME = "zextrasdoc"
    DEVEL_BRANCH = "devel"
    DEVEL_BUCKET_NAME = "zextrasdoc-devel"
    PRODUCTION_CREDENTIALS = "docs.zextras.com-s3-key"
    STAGING_CREDENTIALS = "doc-zextras-area51-s3-key"
    REGION = 'eu-west-1'
  }

  stages {
    stage('Build doc static') {
      when {
        anyOf {
          branch 'master'
          branch 'pre_release'
          branch 'devel'
        }
      }
      steps {
        sh '''
python3 -m venv .
source bin/activate
pip3 install -r requirements.txt
./build.sh
'''

        stash name: 'build_done', includes: 'build/**'
      }
    }

    

    stage('Upload to DEVEL') {
      when {
        branch 'devel'
      }
      steps {
        unstash "build_done"
        withAWS(region: REGION, credentials: STAGING_CREDENTIALS) {
          s3Delete(bucket: DEVEL_BUCKET_NAME,
            path: 'user-guides/')
          s3Upload(bucket: DEVEL_BUCKET_NAME,
            includePathPattern: '**',
            workingDir: 'build'
          )
        }
        script {
          DESTINATION = "$DEVEL_BUCKET_NAME"
        }
      }
    }
    
    stage('Upload to STAGING') {
      when {
        branch 'pre_release'
      }
      steps {
        unstash "build_done"
        withAWS(region: REGION, credentials: STAGING_CREDENTIALS) {
          s3Delete(bucket: STAGING_BUCKET_NAME,
            path: 'user-guides/')
          s3Upload(bucket: STAGING_BUCKET_NAME,
            includePathPattern: '**',
            workingDir: 'build'
          )
        }
        script {
          DESTINATION = "$STAGING_BUCKET_NAME"
        }
      }
    }
    stage('Upload to PRODUCTION') {
      when {
        branch 'master'
      }
      steps {
        unstash "build_done"
        withAWS(region: REGION, credentials: PRODUCTION_CREDENTIALS) {
          s3Delete(bucket: PRODUCTION_BUCKET_NAME,
            path: 'user-guides/')
          s3Upload(bucket: PRODUCTION_BUCKET_NAME,
            includePathPattern: '**',
            workingDir: 'build'
          )
        }
        script {
          DESTINATION = "$PRODUCTION_BUCKET_NAME"
        }
      }
    }
  }
}
