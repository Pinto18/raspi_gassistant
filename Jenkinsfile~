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
	    sh '''
	        source env/bin/activate
	        python 'tests/*.py'
		deactivate
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
