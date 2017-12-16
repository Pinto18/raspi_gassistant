#!usr/bin/envy/groovy

pipeline
{
   agent any

   stages
   {
      stage('Build')
      {
         steps
	 {
	    echo '========== Building =========='
	 }
      }
      stage('Test')
      {
         steps
	 {
	    echo '========== Testing =========='
	    echo "${pwd()}"
	    bat '''
	         python 'tests/*.py'
	        '''
            junit 'test-report/*.xml'
	 }
      }
      stage('Deploy')
      {
         steps
	 {
	    echo '========== Deploying =========='
	 }
      }
   }
}
